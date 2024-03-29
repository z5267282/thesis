def program():
    i = 42
    j = 69
    print(f"{i} + {j} = {i + j}")

from dataframe import DataFrame
from generate import generate_dataframes

def test_1_top_level():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 42",
                "j = 69",
                "print(f\"{i} + {j} = {i + j}\")"
            ],
            "lines": [
                "1",
                "2",
                "3"
            ],
            "curr": None,
            "vars": [],
            "out": [],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "i = 42",
                "j = 69",
                "print(f\"{i} + {j} = {i + j}\")"
            ],
            "lines": [
                "1",
                "2",
                "3"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "i",
                    "value": "42",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "69",
                    "changed": True
                }
            ],
            "out": [
                "42 + 69 = 111\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2
                ]
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "i = 42",
                "j = 69",
                "print(f\"{i} + {j} = {i + j}\")"
            ],
            "lines": [
                "1",
                "2",
                "3"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "i",
                    "value": "42",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "69",
                    "changed": False
                }
            ],
            "out": [
                "42 + 69 = 111\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
