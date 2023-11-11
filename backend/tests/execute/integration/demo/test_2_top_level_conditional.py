def program():
    i = 0
    print(f"i is {i}")
    if i % 7 == 0:
        print("a special number!")
        print(":D")
    else:
        print("meh")
    print("that's all folks")

from dataframe import DataFrame
from generate import generate_dataframes

def test_2_top_level_conditional():
    assert DataFrame.to_dicts(generate_dataframes(program)) == [
        {
            "code": [
                "i = 0",
                "print(f\"i is {i}\")",
                "if i % 7 == 0:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "6",
                "",
                "8"
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
                "print(f\"i is {i}\")",
                "if i % 7 == 0:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "6",
                "",
                "8"
            ],
            "curr": 1,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": True
                }
            ],
            "out": [
                "i is 0\n"
            ],
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
                "i = 0",
                "print(f\"i is {i}\")",
                "if i % 7 == 0:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "6",
                "",
                "8"
            ],
            "curr": 2,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "i is 0\n"
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
                "0 % 7 == 0"
            ]
        },
        {
            "code": [
                "i = 0",
                "print(f\"i is {i}\")",
                "if i % 7 == 0:",
                "    print(\"a special number!\")",
                "    print(\":D\")",
                "else:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "",
                "8"
            ],
            "curr": 4,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "i is 0\n",
                "a special number!\n",
                ":D\n"
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
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "print(f\"i is {i}\")",
                "if i % 7 == 0:",
                "    print(\"a special number!\")",
                "    print(\":D\")",
                "else:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "",
                "8"
            ],
            "curr": 7,
            "vars": [
                {
                    "name": "i",
                    "value": "0",
                    "changed": False
                }
            ],
            "out": [
                "i is 0\n",
                "a special number!\n",
                ":D\n",
                "that's all folks\n"
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
            "counters": [],
            "evalbox": []
        },
        {
            "code": [
                "i = 0",
                "print(f\"i is {i}\")",
                "if i % 7 == 0:",
                "    \u00b7\u00b7\u00b7",
                "else:",
                "    \u00b7\u00b7\u00b7",
                "print(\"that's all folks\")"
            ],
            "lines": [
                "1",
                "2",
                "3",
                "",
                "6",
                "",
                "8"
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
                "i is 0\n",
                "a special number!\n",
                ":D\n",
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
