def program():
    i = 1
    twos, fives = 0, 0
    while i < 6:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 5 == 0:
            print("five")
            fives += 1
        i += 1
    
    print(f"2s: {twos}, 5s: {fives}")

from dataframe import DataFrame
from generate import generate_dataframes

def test_4_loop_conditional():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
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
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "twos",
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
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "twos",
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
                    "start": 2,
                    "end": 3,
                    "numerator": 1,
                    "denominator": 5
                }
            ],
            "evalbox": [
                "1 < 6"
            ]
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "7",
                "",
                "10",
                "11",
                "12"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    7
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 8,
                    "numerator": 1,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "twos",
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
                    "start": 2,
                    "end": 3,
                    "numerator": 2,
                    "denominator": 5
                }
            ],
            "evalbox": [
                "2 < 6"
            ]
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "7",
                "",
                "10",
                "11",
                "12"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 8,
                    "numerator": 2,
                    "denominator": 5
                }
            ],
            "evalbox": [
                "2 % 2 == 0"
            ]
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        print(\"two\")",
                "        twos += 1",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
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
                "10",
                "11",
                "12"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "1",
                    "changed": True
                }
            ],
            "out": [
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    5
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 9,
                    "numerator": 2,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        print(\"two\")",
                "        twos += 1",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
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
                "10",
                "11",
                "12"
            ],
            "curr": 8,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "3",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "1",
                    "changed": False
                }
            ],
            "out": [
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    5,
                    8
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 9,
                    "numerator": 2,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "5",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": True
                }
            ],
            "out": [
                "two\n",
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 3,
                    "numerator": 5,
                    "denominator": 5
                }
            ],
            "evalbox": [
                "5 < 6"
            ]
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "7",
                "",
                "10",
                "11",
                "12"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "two\n",
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 8,
                    "numerator": 5,
                    "denominator": 5
                }
            ],
            "evalbox": [
                "5 % 5 == 0"
            ]
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == 0:",
                "        print(\"five\")",
                "        fives += 1",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "two\n",
                "two\n",
                "five\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5,
                    7
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 9,
                    "numerator": 5,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == 0:",
                "        print(\"five\")",
                "        fives += 1",
                "    i += 1",
                "",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "",
                "7",
                "8",
                "9",
                "10",
                "11",
                "12"
            ],
            "curr": 8,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "6",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "two\n",
                "two\n",
                "five\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5,
                    7,
                    8
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 9,
                    "numerator": 5,
                    "denominator": 5
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "6",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "two\n",
                "two\n",
                "five\n",
                "2s: 2, 5s: 1\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    4
                ]
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    \u00b7\u00b7\u00b7",
                "print(f\"2s: {twos}, 5s: {fives}\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "12"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "6",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "two\n",
                "two\n",
                "five\n",
                "2s: 2, 5s: 1\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]