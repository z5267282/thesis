const data = {
    code: [
        "i = 1",
        "while i < 9:",
        "   if i % 3 == 0:",
        "        print(f\"three: {i}\")",
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
    path: {
        start: 0,
        rest: [1, 2, 3, 6]
    },
    counter: {
        start: 1,
        end: 6,
        numerator: 3,
        denominator: 8,
    }
};
export default data;
