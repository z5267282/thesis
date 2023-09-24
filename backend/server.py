import sys
from typing import Any, Callable

from flask import Flask, jsonify, request
from flask_cors import CORS

sys.path.append("src")

from cfg import LEADING_SPACES, PROGRAM_PATH
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
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(os.path.join(*PROGRAM_PATH), "w") as f:
        for c in code:
            print(c, file=f)
