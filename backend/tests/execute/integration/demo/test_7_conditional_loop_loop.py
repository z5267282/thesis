def program():
    i = 0
    while i < 4:
        if i == 0:
            row = ""
            j = i
            while j >= 0:
                row = f"{row} {j}"
                j -= 1
            print(row)
        elif i == 2:
            row = ""
            j = 0
            while j <= i:
                row = f"{row} {j}"
                j += 1
            print(row)
        i += 1
    print("the end!")
from dataframe import DataFrame
from generate import generate_dataframes

def test_7_conditional_loop_loop():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
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
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
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
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
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
                    "denominator": 4
                }
            ],
            "evalbox": [
                "0 < 4"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "",
                "17",
                "18"
            ],
            "curr": 2,
            "vars": [
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
                    1,
                    2
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 6,
                    "numerator": 1,
                    "denominator": 4
                }
            ],
            "evalbox": [
                "0 == 0"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        row = \"\"",
                "        j = i",
                "        while j >= 0:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "",
                "9",
                "10",
                "",
                "17",
                "18"
            ],
            "curr": 4,
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
                    2,
                    4
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        row = \"\"",
                "        j = i",
                "        while j >= 0:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "",
                "9",
                "10",
                "",
                "17",
                "18"
            ],
            "curr": 5,
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
                    2,
                    4,
                    5
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 4
                },
                {
                    "start": 5,
                    "end": 6,
                    "numerator": 1,
                    "denominator": 1
                }
            ],
            "evalbox": [
                "0 >= 0"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        row = \"\"",
                "        j = i",
                "        while j >= 0:",
                "            row = f\"{row} {j}\"",
                "            j -= 1",
                "        print(row)",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
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
                "17",
                "18"
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
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    4,
                    5,
                    7
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 11,
                    "numerator": 1,
                    "denominator": 4
                },
                {
                    "start": 5,
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
                "while i < 4:",
                "    if i == 0:",
                "        row = \"\"",
                "        j = i",
                "        while j >= 0:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "",
                "9",
                "10",
                "",
                "17",
                "18"
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
                    "value": "-1",
                    "changed": True
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": False
                }
            ],
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    4,
                    7
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        row = \"\"",
                "        j = i",
                "        while j >= 0:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "",
                "9",
                "10",
                "",
                "17",
                "18"
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "-1",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": False
                }
            ],
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    4,
                    7,
                    10
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "i",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "-1",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": False
                }
            ],
            "out": [
                " 0\n"
            ],
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
                    "numerator": 2,
                    "denominator": 4
                }
            ],
            "evalbox": [
                "1 < 4"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "",
                "17",
                "18"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "-1",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": False
                }
            ],
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 6,
                    "numerator": 2,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "-1",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": False
                }
            ],
            "out": [
                " 0\n"
            ],
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
                    "numerator": 3,
                    "denominator": 4
                }
            ],
            "evalbox": [
                "2 < 4"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "",
                "17",
                "18"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "-1",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": False
                }
            ],
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 6,
                    "numerator": 3,
                    "denominator": 4
                }
            ],
            "evalbox": [
                "2 == 2"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        row = \"\"",
                "        j = 0",
                "        while j <= i:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "11",
                "12",
                "13",
                "",
                "16",
                "17",
                "18"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "-1",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": "",
                    "changed": True
                }
            ],
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4,
                    6
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 3,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        row = \"\"",
                "        j = 0",
                "        while j <= i:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "11",
                "12",
                "13",
                "",
                "16",
                "17",
                "18"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
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
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4,
                    6,
                    7
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 3,
                    "denominator": 4
                },
                {
                    "start": 7,
                    "end": 8,
                    "numerator": 1,
                    "denominator": 3
                }
            ],
            "evalbox": [
                "0 <= 2"
            ]
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        row = \"\"",
                "        j = 0",
                "        while j <= i:",
                "            row = f\"{row} {j}\"",
                "            j += 1",
                "        print(row)",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0",
                    "changed": True
                }
            ],
            "out": [
                " 0\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4,
                    6,
                    7,
                    9
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 11,
                    "numerator": 3,
                    "denominator": 4
                },
                {
                    "start": 7,
                    "end": 9,
                    "numerator": 1,
                    "denominator": 3
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        row = \"\"",
                "        j = 0",
                "        while j <= i:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "11",
                "12",
                "13",
                "",
                "16",
                "17",
                "18"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": True
                },
                {
                    "name": "row",
                    "value": " 0 1 2",
                    "changed": True
                }
            ],
            "out": [
                " 0\n",
                " 0 1 2\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4,
                    6,
                    9
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 3,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    if i == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i == 2:",
                "        row = \"\"",
                "        j = 0",
                "        while j <= i:",
                "            \u00b7\u00b7\u00b7",
                "        print(row)",
                "    i += 1",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "10",
                "11",
                "12",
                "13",
                "",
                "16",
                "17",
                "18"
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0 1 2",
                    "changed": False
                }
            ],
            "out": [
                " 0\n",
                " 0 1 2\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4,
                    6,
                    9,
                    10
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 10,
                    "numerator": 3,
                    "denominator": 4
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "i",
                    "value": "4",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0 1 2",
                    "changed": False
                }
            ],
            "out": [
                " 0\n",
                " 0 1 2\n",
                "the end!\n"
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
                "while i < 4:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end!\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "18"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "row",
                    "value": " 0 1 2",
                    "changed": False
                }
            ],
            "out": [
                " 0\n",
                " 0 1 2\n",
                "the end!\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
