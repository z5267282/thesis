from flask import Flask, request
from flask_cors import CORS

import json
import os
import sys

sys.path.append("src")

from cfg import LEADING_SPACES

app = Flask(__name__)
CORS(app)

@app.put("/analyse")
def analyse():
    raw_code : str = request.get_json()
    wrap_program(raw_code)
    # we must alter the program source code, then import it
    from main import main
    dataframes = main()

    with open("/tmp/a.json", "w") as f:
        json.dump([ d.to_dict() for d in dataframes ], f, indent=2)

    return json.dumps([ d.to_dict() for d in dataframes ])

def wrap_program(raw_code : str):
    code : list[str] = ["def program():"]
    code.extend(
        "{}{}".format(" " * LEADING_SPACES, raw)
            for raw in raw_code.split("\n")
    )
    with open(os.path.join("src", "program.py"), "w") as f:
        for c in code:
            print(c, file=f)
