def program():
    def a():
        print("a")
        b()

    def b():
        print("b")

    print("start")
    a()
    print("end")

from dataframe import DataFrame
from generate import generate_dataframes

def test_nested():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "print(\"start\")",
                "a()",
                "print(\"end\")"
            ],
            "lines": [
                "1",
                "",
                "5",
                "",
                "8",
                "9",
                "10"
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
            ],
            "lines": [
                "1",
                "",
                "5",
                "",
                "8",
                "9",
                "10"
            ],
            "curr": 5,
            "vars": [],
            "out": [
                "start\n"
            ],
            "path": {
                "start": 4,
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
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "print(\"start\")",
                "a()",
                "print(\"end\")"
            ],
            "lines": [
                "1",
                "",
                "5",
                "",
                "8",
                "9",
                "10"
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
                "entry": 5,
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
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
                "10"
            ],
            "curr": 2,
            "vars": [],
            "out": [
                "start\n",
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
                "entry": 7,
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
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
                "10"
            ],
            "curr": 4,
            "vars": [],
            "out": [
                "start\n",
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
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
                "10"
            ],
            "curr": 5,
            "vars": [],
            "out": [
                "start\n",
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
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
                "10"
            ],
            "curr": 5,
            "vars": [],
            "out": [
                "start\n",
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
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
                "10"
            ],
            "curr": 2,
            "vars": [],
            "out": [
                "start\n",
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
                "entry": 7,
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
            ],
            "lines": [
                "1",
                "",
                "5",
                "",
                "8",
                "9",
                "10"
            ],
            "curr": 6,
            "vars": [],
            "out": [
                "start\n",
                "a\n",
                "b\n",
                "end\n"
            ],
            "path": {
                "start": 4,
                "rest": [
                    5,
                    6
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
                "print(\"start\")",
                "a()",
                "print(\"end\")"
            ],
            "lines": [
                "1",
                "",
                "5",
                "",
                "8",
                "9",
                "10"
            ],
            "curr": None,
            "vars": [],
            "out": [
                "start\na\nb\nend\n"
            ],
            "path": None,
            "counters": [],
            "evalbox": [],
            "call": None
        }
    ]
