from http import HTTPStatus
from json import dump
import os
from subprocess import CompletedProcess, run
import sys
from tempfile import NamedTemporaryFile 
from typing import Literal

from flask import Flask, jsonify, request, Response
from flask_cors import CORS

sys.path.append("src")

from config import GENERATE_TEST, LEADING_SPACES, PATHS, TIMEOUT
from dataframe import DataFrame
from main import main

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse() -> Response | tuple[str, Literal[HTTPStatus.BAD_REQUEST]]:
    raw_code : str = request.get_json()
    errors   : tuple[str, int] | None = program_errors(raw_code)
    if errors is not None:
        return errors

    wrap_program(raw_code)
    dataframes : list[DataFrame] = main()
    as_dicts   : list[dict] = DataFrame.to_dicts(dataframes)
    write_dataframes(as_dicts)
    return jsonify(as_dicts)

def program_errors(
    raw_code : str
) -> tuple[str, Literal[HTTPStatus.BAD_REQUEST]] | None:
    """Check the given raw code for any errors.
    Return None if there were no errors.
    Otherwise return a tuple of error desciprtion and status code."""
    if timeout(raw_code):
        return gen_timeout_response()
    
    sane : CompletedProcess = sanity(raw_code)
    if sane.returncode:
        return gen_insane_response(sane)
    
    return None

def timeout(raw_code : str) -> bool:
    """Write the given program to a temporary file and time its execution.
    Return whether the program timed out."""
    with NamedTemporaryFile(mode="w") as t:
        signal_wrapped : str = f"""from signal import SIGTERM, signal
import sys
signal(
    SIGTERM, lambda signum, frame: sys.exit(1)
)
{raw_code}"""
        temp_print(signal_wrapped, t)
        commands  : list[str] = ["sh", PATHS.timeout, t.name, str(TIMEOUT)]
        timeout   : CompletedProcess = run(commands)
        timed_out : bool = bool(timeout.returncode)
    return timed_out

def temp_print(data : str, file : NamedTemporaryFile) -> None:
    print(data, file=file, end="", flush=True)
    file.seek(0)

def gen_timeout_response() -> tuple[str, Literal[HTTPStatus.BAD_REQUEST]]:
    desc : str = "Your program ran for more than {} second{}".format(
        TIMEOUT, "" if TIMEOUT == 1 else "s"
    )
    return desc, HTTPStatus.BAD_REQUEST

def sanity(raw_code : str) -> CompletedProcess:
    """Check the given program can be run without errors.
    Return a CompletedProcess storing the status of the sanity check."""
    with NamedTemporaryFile(mode="w") as t:
        temp_print(raw_code, t)
        commands : list[str] = ["sh", str(PATHS.sanity), t.name]
        sanity   : CompletedProcess = run(
            commands,
            capture_output=True, text=True
        )
    return sanity 

def gen_insane_response(
    insane : CompletedProcess
) -> tuple[str, Literal[HTTPStatus.BAD_REQUEST]]:
    desc : list[str] = [
        "Your program could not be run.",
        "There is likely a syntax error in the code",
        "More info here :",
        insane.stderr
    ]
    return "\n".join(desc), HTTPStatus.BAD_REQUEST

def wrap_program(raw_code : str) -> None:
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(PATHS.program, "w") as f:
        for c in code:
            print(c, file=f)

def write_dataframes(dataframe_dicts : list[dict]) -> None:
    """Write a list of DataFrame-converted dictionaries to
    PATHS.generated_frame. and prepare them as python files.
    Only write when locally hosted and per GENERATE_TEST in the config."""
    if os.getenv("REACT_APP_HOST") == "LOCAL" and GENERATE_TEST:
        with open(PATHS.generated_frame, "w") as f:
            dump(dataframe_dicts, f, indent=LEADING_SPACES)
        
        run(["sh", PATHS.to_python])
