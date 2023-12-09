def program():
    YEAR = 2023
    N = 10_000
    i = 0
    print(f"some facts about the numbers up to {N}")
    while i < N:
        if i % 2 == 0 and i % 7 == 0:
            print(f"fancy fourteen")
            i += 1
        elif i % 3 and i % 7 and i * i > 4 * i:
            print("a 21 whose square is larger than its quadruple")
            i += 2
        elif i % 3221 == 0 and i % 7727 == 3:
            print("secret")
            i += 4
        elif i % 47 and i > YEAR:
            print("a 47 after this year")
            i += 8
        elif i % 53 == 0 and i % 977 == 0:
            print("a big prime")
            i += 16
        i += 32
    print("the end")

from dataframe import DataFrame
from generate import generate_dataframes

def test_q2():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
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
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": True
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n"
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
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 5,
                    "numerator": 1,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "0 < 10000"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "",
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    5
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 15,
                    "numerator": 1,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "0 % 2 == 0 and 0 % 7 == 0"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        print(f\"fancy fourteen\")",
                "        i += 1",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    5,
                    7
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 16,
                    "numerator": 1,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        print(f\"fancy fourteen\")",
                "        i += 1",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 16,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "33",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    5,
                    7,
                    16
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 16,
                    "numerator": 1,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "33",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 5,
                    "numerator": 2,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "33 < 10000"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "",
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 15,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "65",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    15
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 15,
                    "numerator": 2,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "65",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 5,
                    "numerator": 3,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "65 < 10000"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "",
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "65",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    7
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 15,
                    "numerator": 3,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "65 % 3 and 65 % 7 and 65 * 65 > 4 * 65"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        print(\"a 21 whose square is larger than its quadruple\")",
                "        i += 2",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "11",
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "67",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    7,
                    9
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 16,
                    "numerator": 3,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        print(\"a 21 whose square is larger than its quadruple\")",
                "        i += 2",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "11",
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 16,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "99",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    7,
                    9,
                    16
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 16,
                    "numerator": 3,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2079",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 5,
                    "numerator": 64,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "2079 < 10000"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "",
                "12",
                "",
                "15",
                "",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2079",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    11
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 15,
                    "numerator": 64,
                    "denominator": 281
                }
            ],
            "evalbox": [
                "2079 % 47 and 2079 > 2023"
            ]
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        print(\"a 47 after this year\")",
                "        i += 8",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "",
                "12",
                "",
                "15",
                "16",
                "17",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 13,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2087",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    11,
                    13
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 16,
                    "numerator": 64,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    if i % 2 == 0 and i % 7 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3 and i % 7 and i * i > 4 * i:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 3221 == 0 and i % 7727 == 3:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 47 and i > YEAR:",
                "        print(\"a 47 after this year\")",
                "        i += 8",
                "    elif i % 53 == 0 and i % 977 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    i += 32",
                "print(\"the end\")"
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
                "",
                "12",
                "",
                "15",
                "16",
                "17",
                "18",
                "",
                "21",
                "22"
            ],
            "curr": 16,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2119",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    4,
                    11,
                    13,
                    16
                ]
            },
            "counters": [
                {
                    "start": 4,
                    "end": 16,
                    "numerator": 64,
                    "denominator": 281
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "10001",
                    "changed": True
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "the end\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    3,
                    6
                ]
            },
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "YEAR = 2023",
                "N = 10_000",
                "i = 0",
                "print(f\"some facts about the numbers up to {N}\")",
                "while i < N:",
                "    \u00b7\u00b7\u00b7",
                "print(\"the end\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "22"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "N",
                    "value": "10000",
                    "changed": False
                },
                {
                    "name": "YEAR",
                    "value": "2023",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "10001",
                    "changed": False
                }
            ],
            "out": [
                "some facts about the numbers up to 10000\n",
                "fancy fourteen\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 21 whose square is larger than its quadruple\n",
                "a 47 after this year\n",
                "a 21 whose square is larger than its quadruple\n",
                "the end\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
