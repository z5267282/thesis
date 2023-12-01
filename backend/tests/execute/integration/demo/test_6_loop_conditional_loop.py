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
        
        total = 0
        j = 0
        while j <= i:
            total += j
            j += 1
    
        print(f"sum 0..{i} = {total}")
        i += 1
        
    print(f"2s: {twos}, 5s: {fives}")
from dataframe import DataFrame
from generate import generate_dataframes

def test_6_loop_conditional_loop():
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
                "20"
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
                "20"
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
                "20"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "fives",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "i",
                    "value": "1",
                    "changed": False
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
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
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "0",
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
                    8
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 13,
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
                "    if i % 2 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 9,
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
                    "name": "j",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "total",
                    "value": "0",
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
                    8,
                    9
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 13,
                    "numerator": 1,
                    "denominator": 5
                },
                {
                    "start": 9,
                    "end": 10,
                    "numerator": 1,
                    "denominator": 2
                }
            ],
            "evalbox": [
                "0 <= 1"
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        total += j",
                "        j += 1",
                "",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 11,
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
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "0",
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
                    8,
                    9,
                    11
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 15,
                    "numerator": 1,
                    "denominator": 5
                },
                {
                    "start": 9,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 2
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
                "        \u00b7\u00b7\u00b7",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 12,
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
                    "name": "j",
                    "value": "2",
                    "changed": True
                },
                {
                    "name": "total",
                    "value": "1",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    8,
                    12
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 13,
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
                "20"
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
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n"
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
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
                    "name": "j",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n"
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
                    "end": 13,
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
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
                    "name": "j",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
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
                    "end": 14,
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 9,
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
                    "name": "j",
                    "value": "2",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "1",
                    "changed": True
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    5,
                    9
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 14,
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 10,
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
                    "name": "j",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "total",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "1",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    5,
                    9,
                    10
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 14,
                    "numerator": 2,
                    "denominator": 5
                },
                {
                    "start": 10,
                    "end": 11,
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
                "i = 1",
                "twos, fives = 0, 0",
                "while i < 6:",
                "    if i % 2 == 0:",
                "        print(\"two\")",
                "        twos += 1",
                "    elif i % 5 == 0:",
                "        \u00b7\u00b7\u00b7",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        total += j",
                "        j += 1",
                "",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 12,
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
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "1",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    5,
                    9,
                    10,
                    12
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 16,
                    "numerator": 2,
                    "denominator": 5
                },
                {
                    "start": 10,
                    "end": 13,
                    "numerator": 1,
                    "denominator": 3
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 13,
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
                    "name": "j",
                    "value": "3",
                    "changed": True
                },
                {
                    "name": "total",
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
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    3,
                    5,
                    9,
                    13
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 14,
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
                "20"
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
                    "name": "j",
                    "value": "5",
                    "changed": True
                },
                {
                    "name": "total",
                    "value": "10",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": True
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n"
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
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "11",
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
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
                    "name": "j",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "10",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n"
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
                    "end": 13,
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
                "    ",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
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
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "10",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
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
                    "end": 15,
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
                "    ",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 10,
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
                    "name": "j",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
                "five\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5,
                    7,
                    10
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 15,
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
                "    ",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 11,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": True
                },
                {
                    "name": "total",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
                "five\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5,
                    7,
                    10,
                    11
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 15,
                    "numerator": 5,
                    "denominator": 5
                },
                {
                    "start": 11,
                    "end": 12,
                    "numerator": 1,
                    "denominator": 6
                }
            ],
            "evalbox": [
                "0 <= 5"
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
                "    ",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        total += j",
                "        j += 1",
                "",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "12",
                "13",
                "14",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 13,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "0",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
                "five\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5,
                    7,
                    10,
                    11,
                    13
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 17,
                    "numerator": 5,
                    "denominator": 5
                },
                {
                    "start": 11,
                    "end": 14,
                    "numerator": 1,
                    "denominator": 6
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
                "    ",
                "    total = 0",
                "    j = 0",
                "    while j <= i:",
                "        \u00b7\u00b7\u00b7",
                "    print(f\"sum 0..{i} = {total}\")",
                "    i += 1",
                "    ",
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
                "12",
                "13",
                "",
                "17",
                "18",
                "19",
                "20"
            ],
            "curr": 14,
            "vars": [
                {
                    "name": "fives",
                    "value": "1",
                    "changed": False
                },
                {
                    "name": "i",
                    "value": "5",
                    "changed": False
                },
                {
                    "name": "j",
                    "value": "6",
                    "changed": True
                },
                {
                    "name": "total",
                    "value": "15",
                    "changed": True
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
                "five\n",
                "sum 0..5 = 15\n"
            ],
            "path": {
                "start": 0,
                "rest": [
                    1,
                    2,
                    5,
                    7,
                    10,
                    14
                ]
            },
            "counters": [
                {
                    "start": 2,
                    "end": 15,
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
                "20"
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
                    "changed": True
                },
                {
                    "name": "j",
                    "value": "6",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
                "five\n",
                "sum 0..5 = 15\n",
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
                "20"
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
                    "name": "j",
                    "value": "6",
                    "changed": False
                },
                {
                    "name": "total",
                    "value": "15",
                    "changed": False
                },
                {
                    "name": "twos",
                    "value": "2",
                    "changed": False
                }
            ],
            "out": [
                "sum 0..1 = 1\n",
                "two\n",
                "sum 0..2 = 3\n",
                "sum 0..3 = 6\n",
                "two\n",
                "sum 0..4 = 10\n",
                "five\n",
                "sum 0..5 = 15\n",
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
