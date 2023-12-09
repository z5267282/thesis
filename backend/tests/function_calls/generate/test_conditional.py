def program():
    def a():
        print("a")

    i = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        a()

from dataframe import DataFrame
from generate import generate_dataframes

def test_conditional():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5",
                "",
                "7",
                ""
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
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5",
                "",
                "7",
                ""
            ],
            "curr": 2,
            "vars": [],
            "out": [],
            "path": {
                "start": 2,
                "rest": []
            },
            "counters": [],
            "evalbox": [],
            "call": None
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5",
                "",
                "7",
                ""
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 2,
                "rest": [
                    5
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
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    print(\"hi\")",
                "    a()"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5",
                "",
                "7",
                "8",
                "9"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "hi\n"
            ],
            "path": {
                "start": 2,
                "rest": [
                    5,
                    7
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
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    print(\"hi\")",
                "    a()"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5",
                "",
                "7",
                "8",
                "9"
            ],
            "curr": 0,
            "vars": [],
            "out": [
                "hi\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 7,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    print(\"hi\")",
                "    a()"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9"
            ],
            "curr": 1,
            "vars": [],
            "out": [
                "hi\n",
                "a\n"
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
                "entry": 8,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    print(\"hi\")",
                "    a()"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9"
            ],
            "curr": 1,
            "vars": [],
            "out": [
                "hi\n",
                "a\n"
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
                "entry": 8,
                "target": 0,
                "return": True
            }
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "",
                "4",
                "5",
                "",
                "7",
                ""
            ],
            "curr": None,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "hi\na\n"
            ],
            "path": None,
            "counters": [],
            "evalbox": [],
            "call": None
        }
    ]
