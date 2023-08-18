from flask import Flask, request

import json
import os
import sys

sys.path.append("src")

from cfg import LEADING_SPACES
from main import main

app = Flask(__name__)

@app.put("/analyse")
def analyse():
    raw_code : str = request.get_json()
    wrap_program(raw_code)
    dataframes = main()
    return json.dumps([ d.to_dict() for d in dataframes ])

def wrap_program(raw_code : str):
    code     : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(os.path.join("src", "program.py"), "w") as f:
        for c in code:
            print(c, file=f)
