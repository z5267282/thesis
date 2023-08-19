const data = [
    {
        code: [
            "i = 0",
            "while i < 3:",
            "   j = 0",
            "   while j < 3:",
            "       print(\"X\")",
            "       j += 1",
            "   print(\"\")",
            "   i += 1"
        ],
        lines: [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8"
        ],
        curr : 5,
        vars: [
            "i = 0",
            "j = 3"
        ],
        out: [
            "XXX"
        ],
        path: {
            start: 0,
            rest: [1, 2, 3, 5]
        },
        counters: [
            {
                start: 3,
                end: 5,
                numerator: 3,
                denominator: 3,
            },
            {
                start: 1,
                end: 7,
                numerator: 1,
                denominator: 3,
            }
        ]
    }
];
export default data;
