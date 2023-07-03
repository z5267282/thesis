const data = {
    code: [
        "i = 1",
        "while i < 9:",
        "    if i % 3 == 0:",
        "        ...",
        "   elif i % 7 == 0:",
        "       ...",
        "   i += 1"
    ],
    lines: [
        "1",
        "2",
        "3",
        "",
        "5",
        "",
        "7"
    ],
    vars: [
        "i = 3"
    ],
    out: [
        "three: 3"
    ],
    path: [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 6]
    ],
    counters: {
        1: [3, 8]
    }
};

export default data;
