import sys
from typing import Any, Callable

from flask import Flask, jsonify, request
from flask_cors import CORS

sys.path.append("src")

from cfg import LEADING_SPACES, PROGRAM
from dataframe import DataFrame
from main import main

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse():
    raw_code   : str = request.get_json()
    program    : Callable = wrap_program(raw_code)
    dataframes : list[DataFrame] = main(program)
    return jsonify([ d.to_dict() for d in dataframes ])

def wrap_program(raw_code : str):
    """From raw source code, return a wrapped Python function object"""
    code_lines : list[str] = [f"def {PROGRAM}():"] + indent(raw_code)
    code       : str = "\n".join(code_lines)
    namespace  : dict[str, Any] = {}
    exec(code, namespace)
    return namespace[PROGRAM]

def indent(raw_code : str):
    return [
        "{}{}".format(" " * LEADING_SPACES, raw) for raw in raw_code.split("\n")
    ]
