import os
import subprocess
import sys
from tempfile import TemporaryFile

from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

sys.path.append("src")

from config import LEADING_SPACES, PATHS
from dataframe import DataFrame
from main import main

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse():
    raw_code : str = request.get_json()
    wrap_program(raw_code)
    dataframes : list[DataFrame] = main()
    return jsonify([ d.to_dict() for d in dataframes ])

def check_timeout(raw_code : str):
    with TemporaryFile() as t:
        t.write(raw_code)
        timeout = subprocess.call()

def wrap_program(raw_code : str):
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(PATHS.program, "w") as f:
        for c in code:
            print(c, file=f)
