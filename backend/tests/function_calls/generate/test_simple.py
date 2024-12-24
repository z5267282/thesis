def program():
    def a():
        print("hi")
    
    print("start")
    a()

from dataframe import DataFrame
from generate import generate_dataframes

def test_simple():
    frames = generate_dataframes(program)
    assert DataFrame.to_dicts(frames) == [
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "print(\"start\")",
                "a()"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5"
            ],
            "curr": None,
            "vars": [],
            "out": [],
            "path": None,
            "counters": [],
            "evalbox": [],
            "call": None
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "print(\"start\")",
                "a()"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5"
            ],
            "curr": 3,
            "vars": [],
            "out": [
                "start\n"
            ],
            "path": {
                "start": 2,
                "rest": [
                    3
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": None
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "print(\"start\")",
                "a()"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5"
            ],
            "curr": 0,
            "vars": [],
            "out": [
                "start\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 3,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"hi\")",
                "",
                "print(\"start\")",
                "a()"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "curr": 1,
            "vars": [],
            "out": [
                "start\n",
                "hi\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 4,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"hi\")",
                "",
                "print(\"start\")",
                "a()"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "curr": 1,
            "vars": [],
            "out": [
                "start\n",
                "hi\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 4,
                "target": 0,
                "return": True
            }
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "print(\"start\")",
                "a()"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5"
            ],
            "curr": None,
            "vars": [],
            "out": [
                "start\nhi\n"
            ],
            "path": None,
            "counters": [],
            "evalbox": [],
            "call": None
        }
    ]