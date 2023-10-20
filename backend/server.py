from http import HTTPStatus
from subprocess import CompletedProcess, run
import sys
from tempfile import NamedTemporaryFile 

from flask import Flask, jsonify, request
from flask_cors import CORS

sys.path.append("src")

from config import LEADING_SPACES, PATHS, TIMEOUT
from dataframe import DataFrame
from main import main

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse():
    raw_code : str = request.get_json()
    if timeout(raw_code):
        desc : str = "Your program ran for more than {} second{}".format(
            TIMEOUT, "" if TIMEOUT == 1 else "s"
        )
        return desc, HTTPStatus.BAD_REQUEST
    
    sanity_check : CompletedProcess = sanity(raw_code)
    if sanity_check.returncode:
        desc : list[str] = [
            "Your program could not be run.",
            "There is likely a syntax error in the code",
            "More info here :",
            sanity_check.stderr
        ]
        return "\n".join(desc), HTTPStatus.BAD_REQUEST

    wrap_program(raw_code)
    dataframes : list[DataFrame] = main()
    return jsonify([ d.to_dict() for d in dataframes ])

def timeout(raw_code : str):
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
        commands  : list[str] = ["dash", PATHS.timeout, t.name, str(TIMEOUT)]
        timeout   : CompletedProcess = run(commands)
        timed_out : bool = bool(timeout.returncode)
    return timed_out

def temp_print(data : str, file : NamedTemporaryFile):
    print(data, file=file, end="", flush=True)
    file.seek(0)

def sanity(raw_code : str):
    """Check the given program can be run without errors.
    Return a CompletedProcess storing the status of the sanity check."""
    with NamedTemporaryFile(mode="w") as t:
        temp_print(raw_code, t)
        commands : list[str] = ["dash", PATHS.sanity, t.name]
        check    : CompletedProcess = run(
            commands,
            capture_output=True, text=True
        )
    return check 

def wrap_program(raw_code : str):
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(PATHS.program, "w") as f:
        for c in code:
            print(c, file=f)
