def program():
    def a():
        print("a")
        b()
    
    def b():
        print("b")

    i = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        a()

from dataframe import DataFrame
from generate import generate_dataframes

def test_conditional_nested_call():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
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
                "5",
                "",
                "8",
                "9",
                "",
                "11",
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
                "def b():",
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
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                ""
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 4,
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
                "def b():",
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
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                ""
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 4,
                "rest": [
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
                "def b():",
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
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                "12",
                "13"
            ],
            "curr": 9,
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
                "start": 4,
                "rest": [
                    7,
                    9
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
                "def b():",
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
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                "12",
                "13"
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
                "entry": 9,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "    b()",
                "",
                "def b():",
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
                "2",
                "3",
                "4",
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                "12",
                "13"
            ],
            "curr": 2,
            "vars": [],
            "out": [
                "hi\n",
                "a\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 11,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "    b()",
                "",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                ""
            ],
            "curr": 4,
            "vars": [],
            "out": [
                "hi\n",
                "a\n"
            ],
            "path": {
                "start": 4,
                "rest": []
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 2,
                "target": 4,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "    b()",
                "",
                "def b():",
                "    print(\"b\")",
                "",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "",
                "11",
                ""
            ],
            "curr": 5,
            "vars": [],
            "out": [
                "hi\n",
                "a\n",
                "b\n"
            ],
            "path": {
                "start": 4,
                "rest": [
                    5
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 2,
                "target": 4,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "    b()",
                "",
                "def b():",
                "    print(\"b\")",
                "",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "",
                "11",
                ""
            ],
            "curr": 5,
            "vars": [],
            "out": [
                "hi\n",
                "a\n",
                "b\n"
            ],
            "path": {
                "start": 4,
                "rest": [
                    5
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 2,
                "target": 4,
                "return": True
            }
        },
        {
            "code": [
                "def a():",
                "    print(\"a\")",
                "    b()",
                "",
                "def b():",
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
                "2",
                "3",
                "4",
                "5",
                "",
                "8",
                "9",
                "",
                "11",
                "12",
                "13"
            ],
            "curr": 2,
            "vars": [],
            "out": [
                "hi\n",
                "a\n",
                "b\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 11,
                "target": 0,
                "return": True
            }
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
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
                "5",
                "",
                "8",
                "9",
                "",
                "11",
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
                "hi\na\nb\n"
            ],
            "path": None,
            "counters": [],
            "evalbox": [],
            "call": None
        }
    ]
