from concurrent.futures import Future, ProcessPoolExecutor
import os
import sys

from werkzeug.exceptions import HTTPException

from flask import Flask, jsonify, request
from flask_cors import CORS

sys.path.append("src")

from cfg import LEADING_SPACES, PROGRAM_PATH, TIMEOUT
from dataframe import DataFrame
from main import main

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse():
    raw_code : str = request.get_json()
    wrap_program(raw_code)
    dataframes : None | list[DataFrame] = run_timed_program()
    if dataframes is None:
        raise ProgramTimeoutError()

    return jsonify([ d.to_dict() for d in dataframes ])

class ProgramTimeoutError(HTTPException):
    code        : int = 400
    description : str = "User uploaded program took too long to run"

def run_timed_program():
    """Run the user program for TIMEOUT seconds and return the corresponding
    list of DataFrames.
    Return None if the program timed out."""
    dataframes : None | list[DataFrame] = None
    with ProcessPoolExecutor(max_workers=1) as pool:
        future : Future = pool.submit(main)
        try:
            dataframes = future.result(timeout=TIMEOUT) 
        except TimeoutError:
            pass
    
    return dataframes

@app.errorhandler(ProgramTimeoutError)
def handle_timeout(e : ProgramTimeoutError):
    return e.description, e.code

def wrap_program(raw_code : str):
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(os.path.join(*PROGRAM_PATH), "w") as f:
        for c in code:
            print(c, file=f)
