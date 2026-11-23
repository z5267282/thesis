def program():
    def a():
        j = 0
        if j % 2 == 0:
            print("a")
            b()

    def b():
        k = 42
        if k == 0:
            print("b1")
        elif k == 1:
            print("b2")
        elif k == 42:
            print("b3")
            c()
        else:
            print("b_")

    def c():
        print("successful c")

    i = 0
    if i == 1:
        print("one")
    else:
        print("hi")
        a()

"""The program is written with different variable names to make sure state is
not being carried over into new function calls.
Ie. it would be bad if inside the call to a(), the variable i was still in
scope."""

from dataframe import DataFrame
from generate import generate_dataframes

def test_three_calls():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "def c():",
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
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
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
                "def c():",
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
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 6,
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
                "def c():",
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
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 6,
                "rest": [
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
                "def c():",
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
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                "26",
                "27"
            ],
            "curr": 11,
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
                "start": 6,
                "rest": [
                    9,
                    11
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
                "def c():",
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
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                "26",
                "27"
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
                "entry": 11,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "def c():",
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
                "",
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                "26",
                "27"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "j",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [
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
                "entry": 13,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "def c():",
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
                "",
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                "26",
                "27"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "hi\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2
                ]
            },
            "counters": [],
            "evalbox": [
                "0 % 2 == 0"
            ],
            "call": {
                "entry": 13,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                "26",
                "27"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "hi\n",
                "a\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    4
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 15,
                "target": 0,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 6,
            "vars": [],
            "out": [
                "hi\n",
                "a\n"
            ],
            "path": {
                "start": 6,
                "rest": []
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 4,
                "target": 6,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "",
                "16",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "k",
                    "value": "42",
                    "changed": True
                }
            ],
            "out": [
                "hi\n",
                "a\n"
            ],
            "path": {
                "start": 6,
                "rest": [
                    7
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 4,
                "target": 6,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "",
                "16",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 12,
            "vars": [
                {
                    "name": "k",
                    "value": "42",
                    "changed": False
                }
            ],
            "out": [
                "hi\n",
                "a\n"
            ],
            "path": {
                "start": 6,
                "rest": [
                    7,
                    12
                ]
            },
            "counters": [],
            "evalbox": [
                "42 == 42"
            ],
            "call": {
                "entry": 4,
                "target": 6,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        print(\"b3\")",
                "        c()",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "14",
                "15",
                "16",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 14,
            "vars": [
                {
                    "name": "k",
                    "value": "42",
                    "changed": False
                }
            ],
            "out": [
                "hi\n",
                "a\n",
                "b3\n"
            ],
            "path": {
                "start": 6,
                "rest": [
                    7,
                    12,
                    14
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 4,
                "target": 6,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        print(\"b3\")",
                "        c()",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
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
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "14",
                "15",
                "16",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 13,
            "vars": [],
            "out": [
                "hi\n",
                "a\n",
                "b3\n"
            ],
            "path": {
                "start": 13,
                "rest": []
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 10,
                "target": 13,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        print(\"b3\")",
                "        c()",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
                "    print(\"successful c\")",
                "",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "",
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "14",
                "15",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 14,
            "vars": [],
            "out": [
                "hi\n",
                "a\n",
                "b3\n",
                "successful c\n"
            ],
            "path": {
                "start": 13,
                "rest": [
                    14
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 10,
                "target": 13,
                "return": False
            }
        },
        {
            "code": [
                "def a():",
                "    \u00b7\u00b7\u00b7",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        print(\"b3\")",
                "        c()",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
                "    print(\"successful c\")",
                "",
                "i = 0",
                "if i == 1:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "",
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "14",
                "15",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 14,
            "vars": [],
            "out": [
                "hi\n",
                "a\n",
                "b3\n",
                "successful c\n"
            ],
            "path": {
                "start": 13,
                "rest": [
                    14
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 10,
                "target": 13,
                "return": True
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    k = 42",
                "    if k == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif k == 42:",
                "        print(\"b3\")",
                "        c()",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "8",
                "9",
                "",
                "11",
                "",
                "13",
                "14",
                "15",
                "16",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                ""
            ],
            "curr": 14,
            "vars": [
                {
                    "name": "k",
                    "value": "42",
                    "changed": True
                }
            ],
            "out": [
                "hi\n",
                "a\n",
                "b3\n",
                "successful c\n"
            ],
            "path": {
                "start": 6,
                "rest": [
                    7,
                    12,
                    14
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 4,
                "target": 6,
                "return": True
            }
        },
        {
            "code": [
                "def a():",
                "    j = 0",
                "    if j % 2 == 0:",
                "        print(\"a\")",
                "        b()",
                "",
                "def b():",
                "    \u00b7\u00b7\u00b7",
                "def c():",
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
                "6",
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
                "26",
                "27"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "j",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [
                "hi\n",
                "a\n",
                "b3\n",
                "successful c\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    4
                ]
            },
            "counters": [],
            "evalbox": [],
            "call": {
                "entry": 15,
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
                "def c():",
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
                "7",
                "",
                "19",
                "",
                "22",
                "23",
                "",
                "25",
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
                "hi\na\nb3\nsuccessful c\n"
            ],
            "path": None,
            "counters": [],
            "evalbox": [],
            "call": None
        }
    ]
