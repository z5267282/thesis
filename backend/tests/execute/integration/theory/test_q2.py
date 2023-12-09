def program():
    p = 14986230724609375000
    two = True
    while p % 2 == 0:
        p //= 2
        two = not two
    
    if two:
        while p % 3 == 0:
            p //= 3
    else:
        five = False
        while p % 5 == 0:
            p //= 5
            five = not five
    
        if not five:
            while p % 7 == 0:
                p //= 7
        else:
            while p % 11:
                p //= 11

from dataframe import DataFrame
from generate import generate_dataframes

def test_q2():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                ""
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
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                ""
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "p",
                    "value": "14986230724609375000",
                    "changed": True
                },
                {
                    "name": "two",
                    "value": "True",
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
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                ""
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "p",
                    "value": "14986230724609375000",
                    "changed": False
                },
                {
                    "name": "two",
                    "value": "True",
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
                    "denominator": 3
                }
            ],
            "evalbox": [
                "14986230724609375000 % 2 == 0"
            ]
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    p //= 2",
                "    two = not two",
                "",
                "if two:",
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
                "10",
                ""
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "p",
                    "value": "7493115362304687500",
                    "changed": True
                },
                {
                    "name": "two",
                    "value": "False",
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
                    "start": 2,
                    "end": 5,
                    "numerator": 1,
                    "denominator": 3
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                ""
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "p",
                    "value": "1873278840576171875",
                    "changed": True
                },
                {
                    "name": "two",
                    "value": "False",
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
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    five = False",
                "    while p % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    if not five:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                "11",
                "12",
                "",
                "16",
                "",
                "19",
                ""
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "five",
                    "value": "False",
                    "changed": True
                },
                {
                    "name": "p",
                    "value": "1873278840576171875",
                    "changed": False
                },
                {
                    "name": "two",
                    "value": "False",
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
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    five = False",
                "    while p % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    if not five:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                "11",
                "12",
                "",
                "16",
                "",
                "19",
                ""
            ],
            "curr": 8,
            "vars": [
                {
                    "name": "five",
                    "value": "False",
                    "changed": False
                },
                {
                    "name": "p",
                    "value": "1873278840576171875",
                    "changed": False
                },
                {
                    "name": "two",
                    "value": "False",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6,
                    7,
                    8
                ]
            },
            "counters": [
                {
                    "start": 8,
                    "end": 9,
                    "numerator": 1,
                    "denominator": 12
                }
            ],
            "evalbox": [
                "1873278840576171875 % 5 == 0"
            ]
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    five = False",
                "    while p % 5 == 0:",
                "        p //= 5",
                "        five = not five",
                "",
                "    if not five:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "",
                "19",
                ""
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "five",
                    "value": "True",
                    "changed": True
                },
                {
                    "name": "p",
                    "value": "374655768115234375",
                    "changed": True
                },
                {
                    "name": "two",
                    "value": "False",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6,
                    7,
                    8,
                    10
                ]
            },
            "counters": [
                {
                    "start": 8,
                    "end": 11,
                    "numerator": 1,
                    "denominator": 12
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    five = False",
                "    while p % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    if not five:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                "11",
                "12",
                "",
                "16",
                "",
                "19",
                ""
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "five",
                    "value": "False",
                    "changed": True
                },
                {
                    "name": "p",
                    "value": "7672950131",
                    "changed": True
                },
                {
                    "name": "two",
                    "value": "False",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6,
                    7,
                    10
                ]
            },
            "counters": [],
            "evalbox": [
                "not False"
            ]
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    five = False",
                "    while p % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    if not five:",
                "        while p % 7 == 0:",
                "            \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                "11",
                "12",
                "",
                "16",
                "17",
                "",
                "19",
                ""
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "five",
                    "value": "False",
                    "changed": False
                },
                {
                    "name": "p",
                    "value": "7672950131",
                    "changed": False
                },
                {
                    "name": "two",
                    "value": "False",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6,
                    7,
                    10,
                    11
                ]
            },
            "counters": [
                {
                    "start": 11,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 8
                }
            ],
            "evalbox": [
                "7672950131 % 7 == 0"
            ]
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    five = False",
                "    while p % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    if not five:",
                "        while p % 7 == 0:",
                "            p //= 7",
                "    else:",
                "        \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                "11",
                "12",
                "",
                "16",
                "17",
                "18",
                "19",
                ""
            ],
            "curr": 12,
            "vars": [
                {
                    "name": "five",
                    "value": "False",
                    "changed": False
                },
                {
                    "name": "p",
                    "value": "1096135733",
                    "changed": True
                },
                {
                    "name": "two",
                    "value": "False",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    6,
                    7,
                    10,
                    11,
                    12
                ]
            },
            "counters": [
                {
                    "start": 11,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 8
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "p = 14986230724609375000",
                "two = True",
                "while p % 2 == 0:",
                "    \u00b7\u00b7\u00b7",
                "if two:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "7",
                "",
                "10",
                ""
            ],
            "curr": None,
            "vars": [
                {
                    "name": "five",
                    "value": "False",
                    "changed": False
                },
                {
                    "name": "p",
                    "value": "1331",
                    "changed": False
                },
                {
                    "name": "two",
                    "value": "False",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
