/**
    i = 7
    print("doing some counting")
    if i % 2 == 0:
	    print("a multiple of 2")
    elif i % 7 == 0:
	    print("a holy number!")
	    print("seven")
 */

const data = [
    {
        code: [
            "i = 7",
            "print(\"doing some counting\")",
            "if i % 2 == 0:",
            "    ...",
            "elif i % 7 == 0:",
            "    ...",
        ],
        lines: [
            "1", "2", "3", "", "4", ""
        ],
        curr: 0,
        vars: ["i = 7"],
        out: [],
        path: null,
        counters: []
    },
    {
        code: [
            "i = 7",
            "print(\"doing some counting\")",
            "if i % 2 == 0:",
            "    ...",
            "elif i % 7 == 0:",
            "    ...",
        ],
        lines: [
            "1", "2", "3", "", "4", ""
        ],
        curr: 1,
        vars: ["i = 7"],
        out: ["doing some counting"],
        path: {
            start: 0, rest: [1]
        },
        counters: []
    },
    {
        code: [
            "i = 7",
            "print(\"doing some counting\")",
            "if i % 2 == 0:",
            "    ...",
            "elif i % 7 == 0:",
            "    ...",
        ],
        lines: [
            "1", "2", "3", "", "4", ""
        ],
        curr: 4,
        vars: ["i = 7"],
        out: ["doing some counting"],
        path: {
            start: 0, rest: [1, 4]
        },
        counters: []
    },
    {
        code: [
            "i = 7",
            "print(\"doing some counting\")",
            "if i % 2 == 0:",
            "    ...",
            "elif i % 7 == 0:",
            "    print(\"a holy number!\")",
            "    print(\"seven\")"
        ],
        lines: [
            "1", "2", "3", "", "4", "5", "6"
        ],
        curr: 6,
        vars: ["i = 7"],
        out: [
            "seven",
            "a holy number!",
            "doing some counting"
        ],
        path: {
            start: 0, rest: [1, 4, 6]
        },
        counters: []
    },
];
export default data;
