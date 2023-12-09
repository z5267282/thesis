def program():
    X, Y, Z = 2, 2, 3
    
    i = 0
    while i < X:
        print("--X--", end="")
        j = 0
        while j < Y:
            print("!Y!", end="")
            k = 0
            while k < Z:
                print("Z", end="")
                k += 1
    
            j += 1
    
        print(" ", end="")
        i += 1
    
    print("done")

from dataframe import DataFrame
from generate import generate_dataframes

def test_q1():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "19"
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
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "19"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": True
                },
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
                    2
                ]
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "19"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 4,
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
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        \u00b7\u00b7\u00b7",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [
                "--X--"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        \u00b7\u00b7\u00b7",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "--X--"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5,
                    6
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 6,
                    "end": 7,
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
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        print(\"!Y!\", end=\"\")",
                "        k = 0",
                "        while k < Z:",
                "            \u00b7\u00b7\u00b7",
                "        j += 1",
                "",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "10",
                "",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 8,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [
                "--X--",
                "!Y!"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5,
                    6,
                    8
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 15,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 6,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        print(\"!Y!\", end=\"\")",
                "        k = 0",
                "        while k < Z:",
                "            \u00b7\u00b7\u00b7",
                "        j += 1",
                "",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "10",
                "",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "--X--",
                "!Y!"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5,
                    6,
                    8,
                    9
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 15,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 6,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 9,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 3
                }
            ],
            "evalbox": [
                "0 < 3"
            ]
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        print(\"!Y!\", end=\"\")",
                "        k = 0",
                "        while k < Z:",
                "            print(\"Z\", end=\"\")",
                "            k += 1",
                "",
                "        j += 1",
                "",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "1",
                    "changed": True
                }
            ],
            "out": [
                "--X--",
                "!Y!",
                "Z"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5,
                    6,
                    8,
                    9,
                    11
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 17,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 6,
                    "end": 14,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 9,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 3
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        print(\"!Y!\", end=\"\")",
                "        k = 0",
                "        while k < Z:",
                "            \u00b7\u00b7\u00b7",
                "        j += 1",
                "",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "10",
                "",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "3",
                    "changed": True
                }
            ],
            "out": [
                "--X--",
                "!Y!",
                "Z",
                "Z",
                "Z"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5,
                    6,
                    8,
                    11
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 15,
                    "numerator": 1,
                    "denominator": 2
                },
                {
                    "start": 6,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    print(\"--X--\", end=\"\")",
                "    j = 0",
                "    while j < Y:",
                "        \u00b7\u00b7\u00b7",
                "    print(\" \", end=\"\")",
                "    i += 1",
                "",
                "print(\"done\")"
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
                "16",
                "17",
                "18",
                "19"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "3",
                    "changed": False
                }
            ],
            "out": [
                "--X--",
                "!Y!",
                "Z",
                "Z",
                "Z",
                "!Y!",
                "Z",
                "Z",
                "Z",
                " "
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    3,
                    5,
                    9
                ]
            },
            "counters": [
                {
                    "start": 3,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "19"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "3",
                    "changed": False
                }
            ],
            "out": [
                "--X--",
                "!Y!",
                "Z",
                "Z",
                "Z",
                "!Y!",
                "Z",
                "Z",
                "Z",
                " ",
                "--X--",
                "!Y!",
                "Z",
                "Z",
                "Z",
                "!Y!",
                "Z",
                "Z",
                "Z",
                " ",
                "done\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    2,
                    5
                ]
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "X, Y, Z = 2, 2, 3",
                "",
                "i = 0",
                "while i < X:",
                "    \u00b7\u00b7\u00b7",
                "print(\"done\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "19"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "X",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Y",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "Z",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "3",
                    "changed": False
                }
            ],
            "out": [
                "--X--",
                "!Y!",
                "Z",
                "Z",
                "Z",
                "!Y!",
                "Z",
                "Z",
                "Z",
                " ",
                "--X--",
                "!Y!",
                "Z",
                "Z",
                "Z",
                "!Y!",
                "Z",
                "Z",
                "Z",
                " ",
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