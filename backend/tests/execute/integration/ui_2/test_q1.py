def program():
    HI = 100_000
    i, j, k = 0, 1, 2
    while i + j + k <= HI:
        name = "boat"
        if i % j == 0:
            name = "bubble"
        elif (j + k) % 3 == 1:
            name = "fish"
        elif (k - i) % 7 > j % 4:
            name = "spider"
        
        if k * i < j * 23:
            entity = "inc"
        elif i % 5 == (j + k) % 5:
            entity = "llc"
        else:
            entity = "pty ltd"
        
        company = f"{name} {entity}."
        print(f"choice : {company}")
        i += j
        j += k
        k = (i + j) + (2 * k) % 14
    print("that's all")

from dataframe import DataFrame
from generate import generate_dataframes

def test_q1():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
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
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "2",
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
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
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
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "2",
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
                    "denominator": 11
                }
            ],
            "evalbox": [
                "0 + 1 + 2 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
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
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
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
                    "end": 20,
                    "numerator": 1,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
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
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    4
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 1,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "0 % 1 == 0"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        name = \"bubble\"",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
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
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 5,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
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
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "bubble",
                    "changed": True
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    4,
                    5
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 1,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        name = \"bubble\"",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
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
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
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
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "bubble",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    10
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 1,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "2 * 0 < 1 * 23"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        name = \"bubble\"",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        entity = \"inc\"",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
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
                "9",
                "",
                "12",
                "13",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "bubble",
                    "changed": False
                }
            ],
            "out": [],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    10,
                    11
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 1,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        name = \"bubble\"",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        entity = \"inc\"",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
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
                "9",
                "",
                "12",
                "13",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 20,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "bubble inc.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "8",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "bubble",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    10,
                    11,
                    20
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 1,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "bubble inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "8",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "bubble",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n"
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
                    "numerator": 2,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "1 + 3 + 8 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "bubble inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "8",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n"
            ],
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
                    "end": 20,
                    "numerator": 2,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "bubble inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "8",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    10
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 2,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "8 * 1 < 3 * 23"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        entity = \"inc\"",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "13",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "bubble inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "8",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    10,
                    11
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 2,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        entity = \"inc\"",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "13",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 20,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    10,
                    11,
                    20
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 2,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
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
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "4 + 11 + 17 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
            ],
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
                    "end": 20,
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "(11 + 17) % 3 == 1"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 10,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7,
                    10
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "17 * 4 < 11 * 23"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        entity = \"inc\"",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "13",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "4",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "11",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "17",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7,
                    10,
                    11
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        entity = \"inc\"",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "13",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 20,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7,
                    10,
                    11,
                    20
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 3,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
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
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "15 + 28 + 49 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
            ],
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
                    "end": 20,
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 8,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "(49 - 15) % 7 > 28 % 4"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 15,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "inc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9,
                    15
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        entity = \"pty ltd\"",
                "    ",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 16,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish inc.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "28",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "49",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9,
                    15,
                    16
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 22,
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        entity = \"pty ltd\"",
                "    ",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 22,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "43",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "77",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "120",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9,
                    15,
                    16,
                    22
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 22,
                    "numerator": 4,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "43",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "77",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "120",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n"
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
                    "denominator": 11
                }
            ],
            "evalbox": [
                "43 + 77 + 120 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "43",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "77",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "120",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n"
            ],
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
                    "end": 20,
                    "numerator": 5,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 14,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "43",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "77",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "120",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    14
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 5,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        entity = \"pty ltd\"",
                "    ",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 15,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "43",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "77",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "120",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    14,
                    15
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 5,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        entity = \"pty ltd\"",
                "    ",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 21,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "120",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "197",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "319",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    14,
                    15,
                    21
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 5,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "317",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "516",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "841",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n"
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
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "317 + 516 + 841 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "317",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "516",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "841",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n"
            ],
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
                    "end": 20,
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 6,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "317",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "516",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "841",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "(516 + 841) % 3 == 1"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "317",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "516",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "841",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 12,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "317",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "516",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "841",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7,
                    12
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "317 % 5 == (516 + 841) % 5"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        entity = \"llc\"",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "",
                "14",
                "15",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 13,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "llc",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "317",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "516",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "841",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7,
                    12,
                    13
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        name = \"fish\"",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        entity = \"llc\"",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "8",
                "9",
                "",
                "12",
                "",
                "14",
                "15",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 20,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "fish llc.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "llc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "833",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "1357",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "2192",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "fish",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    6,
                    7,
                    12,
                    13,
                    20
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 7,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "2190",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "3549",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "5741",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n"
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
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "2190 + 3549 + 5741 <= 100000"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 3,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2190",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3549",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "5741",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n"
            ],
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
                    "end": 20,
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        \u00b7\u00b7\u00b7",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 8,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2190",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3549",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "5741",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 20,
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "(5741 - 2190) % 7 > 3549 % 4"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 9,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2190",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3549",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "5741",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        \u00b7\u00b7\u00b7",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 13,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "2190",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3549",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "5741",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9,
                    13
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": [
                "2190 % 5 == (3549 + 5741) % 5"
            ]
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        entity = \"llc\"",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "15",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 14,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "llc",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "2190",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "3549",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "5741",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9,
                    13,
                    14
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    name = \"boat\"",
                "    if i % j == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif (j + k) % 3 == 1:",
                "        \u00b7\u00b7\u00b7",
                "    elif (k - i) % 7 > j % 4:",
                "        name = \"spider\"",
                "    ",
                "    if k * i < j * 23:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == (j + k) % 5:",
                "        entity = \"llc\"",
                "    else:",
                "        \u00b7\u00b7\u00b7",
                "    company = f\"{name} {entity}.\"",
                "    print(f\"choice : {company}\")",
                "    i += j",
                "    j += k",
                "    k = (i + j) + (2 * k) % 14",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "",
                "7",
                "",
                "9",
                "10",
                "11",
                "12",
                "",
                "14",
                "15",
                "16",
                "",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24"
            ],
            "curr": 21,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "spider llc.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "llc",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "5739",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "9290",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "15031",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "spider",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n",
                "choice : spider llc.\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    8,
                    9,
                    13,
                    14,
                    21
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 21,
                    "numerator": 9,
                    "denominator": 11
                }
            ],
            "evalbox": []
        },
        {
            "code": [
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": True
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "39350",
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "63675",
                    "changed": True
                },
                {
                    "name": "k",
                    "value": "103025",
                    "changed": True
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": True
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n",
                "choice : spider llc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "that's all\n"
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
                "HI = 100_000",
                "i, j, k = 0, 1, 2",
                "while i + j + k <= HI:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "24"
            ],
            "curr": None,
            "vars": [
                {
                    "name": "HI",
                    "value": "100000",
                    "changed": False
                },
                {
                    "name": "company",
                    "value": "boat pty ltd.",
                    "changed": False
                },
                {
                    "name": "entity",
                    "value": "pty ltd",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "39350",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "63675",
                    "changed": False
                },
                {
                    "name": "k",
                    "value": "103025",
                    "changed": False
                },
                {
                    "name": "name",
                    "value": "boat",
                    "changed": False
                }
            ],
            "out": [
                "choice : bubble inc.\n",
                "choice : boat inc.\n",
                "choice : fish inc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "choice : spider pty ltd.\n",
                "choice : fish llc.\n",
                "choice : boat pty ltd.\n",
                "choice : spider llc.\n",
                "choice : spider pty ltd.\n",
                "choice : boat pty ltd.\n",
                "that's all\n"
            ],
            "path": {
                "start": 0,
                "rest": []
            },
            "counters": [],
            "evalbox": []
        }
    ]
