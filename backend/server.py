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
        desc : str = "User program ran for more than {} second{}".format(
            TIMEOUT, "" if TIMEOUT == 1 else "s"
        )
        return desc, HTTPStatus.REQUEST_TIMEOUT.value

    wrap_program(raw_code)
    dataframes : list[DataFrame] = main()
    return jsonify([ d.to_dict() for d in dataframes ])

def timeout(raw_code : str):
    """Write the given program to a temporary file and time its execution.
    Return whether the program timed out."""
    with NamedTemporaryFile(mode="w") as t:
        t.write(raw_code)
        t.seek(0)
        commands  : list[str] = ["dash", PATHS.timeout, t.name, str(TIMEOUT)]
        timeout   : CompletedProcess = run(commands)
    #     timed_out : bool = bool(timeout.returncode)
    # return timed_out

    return True

def wrap_program(raw_code : str):
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(PATHS.program, "w") as f:
        for c in code:
            print(c, file=f)
