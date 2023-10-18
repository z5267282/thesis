from http import HTTPStatus
from subprocess import CompletedProcess, run
import sys
from tempfile import NamedTemporaryFile 

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

sys.path.append("src")

from config import LEADING_SPACES, PATHS, TIMEOUT
from dataframe import DataFrame
from main import main

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse():
    raw_code : str = request.get_json()
    check_timeout(raw_code)

    wrap_program(raw_code)
    dataframes : list[DataFrame] = main()
    return jsonify([ d.to_dict() for d in dataframes ])

def check_timeout(raw_code : str):
    timed_out : bool = False
    with NamedTemporaryFile(mode="w") as t:
        t.write(raw_code)
        t.seek(0)
        commands : list[str] = ["dash", PATHS.timeout, t.name, str(TIMEOUT)]
        timeout : CompletedProcess = run(commands)
        if timeout.returncode:
            timed_out = True
    if timed_out:
        print("i timed out in python")
        raise ProgramTimeOutError()

class ProgramTimeOutError(HTTPException):
    code        : int = HTTPStatus.REQUEST_TIMEOUT.value
    description : str = "User program ran for more than {} second{}".format(
        TIMEOUT, "" if TIMEOUT == 1 else "s"
    )

@app.errorhandler(ProgramTimeOutError)
def handle_timeout(e : ProgramTimeOutError):
    return e.description, e.code

def wrap_program(raw_code : str):
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(PATHS.program, "w") as f:
        for c in code:
            print(c, file=f)
