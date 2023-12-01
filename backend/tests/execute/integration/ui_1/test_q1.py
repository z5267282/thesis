def program():
    i = 1
    while i < 12345:
        if i % 7841 == 0 and i % 23 == 0:
            i += 3
        elif i > 3000:
            i += 2
        else:
            i += 43
    print("that's all folks")

from dataframe import DataFrame
from generate import generate_dataframes

def test_q1():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "9"
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
                "i = 1",
                "while i < 12345:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "9"
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
                "i = 1",
                "while i < 12345:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "9"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "i",
                    "value": "1",
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
                    "denominator": 4737
                }
            ],
            "evalbox": [
                "1 < 12345"
            ]
        },
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    if i % 7841 == 0 and i % 23 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i > 3000:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "5",
                "",
                "7",
                "",
                "9"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                }
            ],
            "out": [],
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
                    "end": 7,
                    "numerator": 1,
                    "denominator": 4737
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    if i % 7841 == 0 and i % 23 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i > 3000:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        i += 43",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
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
                    "value": "1",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6,
                    7
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 7,
                    "numerator": 1,
                    "denominator": 4737
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "9"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "i",
                    "value": "3011",
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
                    "numerator": 71,
                    "denominator": 4737
                }
            ],
            "evalbox": [
                "3011 < 12345"
            ]
        },
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    if i % 7841 == 0 and i % 23 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i > 3000:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "5",
                "",
                "7",
                "",
                "9"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "i",
                    "value": "3011",
                    "changed": False
                }
            ],
            "out": [],
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
                    "end": 7,
                    "numerator": 71,
                    "denominator": 4737
                }
            ],
            "evalbox": [
                "3011 > 3000"
            ]
        },
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    if i % 7841 == 0 and i % 23 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i > 3000:",
                "        i += 2",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "5",
                "6",
                "7",
                "",
                "9"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "i",
                    "value": "3011",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4,
                    5
                ]
            },
            "counters": [
                {
                    "start": 1,
                    "end": 7,
                    "numerator": 71,
                    "denominator": 4737
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "while i < 12345:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "9"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "i",
                    "value": "12345",
                    "changed": True
                }
            ],
            "out": [
                "that's all folks\n"
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
                "i = 1",
                "while i < 12345:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "",
                "9"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "i",
                    "value": "12345",
                    "changed": False
                }
            ],
            "out": [
                "that's all folks\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
