def program():
    i = 0
    while i < 5:
        row = ""
        j = 0
        while j <= i:
            row += "X"
            j += 1
    
        print(row)
        i += 1
    print("end!")
from dataframe import DataFrame
from generate import generate_dataframes

def test_5_loop_loop():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 0",
                "while i < 5:",
                "    \u00b7\u00b7\u00b7",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "11"
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
                "while i < 5:",
                "    \u00b7\u00b7\u00b7",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "11"
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
                "while i < 5:",
                "    \u00b7\u00b7\u00b7",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "11"
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
                    "denominator": 5
                }
            ],
            "evalbox": [
                "0 < 5"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 5:",
                "    row = \"\"",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(row)",
                "    i += 1",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "9",
                "10",
                "11"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": "",
                    "changed": True
                }
            ],
            "out": [],
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
                    "end": 7,
                    "numerator": 1,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 5:",
                "    row = \"\"",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(row)",
                "    i += 1",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "9",
                "10",
                "11"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "row",
                    "value": "",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    3,
                    4
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 7,
                    "numerator": 1,
                    "denominator": 5
                },
                {
                    "start": 4,
                    "end": 5,
                    "numerator": 1,
                    "denominator": 1
                }
            ],
            "evalbox": [
                "0 <= 0"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 5:",
                "    row = \"\"",
                "    j = 0",
                "    while j <= i:",
                "        row += \"X\"",
                "        j += 1",
                "",
                "    print(row)",
                "    i += 1",
                "print(\"end!\")"
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
                "11"
            ],
            "curr": 6,
            "vars": [
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
                    "name": "row",
                    "value": "X",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    3,
                    4,
                    6
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 9,
                    "numerator": 1,
                    "denominator": 5
                },
                {
                    "start": 4,
                    "end": 7,
                    "numerator": 1,
                    "denominator": 1
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 5:",
                "    row = \"\"",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(row)",
                "    i += 1",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "9",
                "10",
                "11"
            ],
            "curr": 7,
            "vars": [
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
                    "name": "row",
                    "value": "X",
                    "changed": False
                }
            ],
            "out": [
                "X\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    3,
                    7
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 7,
                    "numerator": 1,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 5:",
                "    \u00b7\u00b7\u00b7",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "11"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "i",
                    "value": "5",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "5",
                    "changed": True
                },
                {
                    "name": "row",
                    "value": "XXXXX",
                    "changed": True
                }
            ],
            "out": [
                "X\n",
                "XX\n",
                "XXX\n",
                "XXXX\n",
                "XXXXX\n",
                "end!\n"
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
                "while i < 5:",
                "    \u00b7\u00b7\u00b7",
                "print(\"end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "11"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "i",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": "XXXXX",
                    "changed": False
                }
            ],
            "out": [
                "X\n",
                "XX\n",
                "XXX\n",
                "XXXX\n",
                "XXXXX\n",
                "end!\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
