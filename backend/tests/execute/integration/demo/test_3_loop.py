def program():
    i = 0
    while i < 2:
        print(i)
        i += 1
    print("done")

from dataframe import DataFrame
from generate import generate_dataframes

def test_3_loop():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 0",
                "while i < 2:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "5"
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
                "i = 0",
                "while i < 2:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "5"
            ],
            "curr": 0,
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
                "i = 0",
                "while i < 2:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "5"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 2,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": [
                "0 < 2"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 2:",
                "    print(i)",
                "    i += 1",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    3
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 3,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 2:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "5"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": True
                }
            ],
            "out": [
                "0\n",
                "1\n",
                "done\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3
                ]
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 2:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "5"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "0\n",
                "1\n",
                "done\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
