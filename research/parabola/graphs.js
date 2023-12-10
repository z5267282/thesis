const func = () => {
    const graph = document.getElementById("func");
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.classList.add("pen");

    const coords = [
        "M 30 0",
        "q -60 12.5 0 25"
    ]
    path.setAttribute("d", coords.join(" "));
    graph.appendChild(path);
}

const good = () => {
    const graph = document.getElementById("graph");
    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.classList.add("pen");

    const L = 15;

    class Delta {
        constructor(angle) {
            this.dx = L * Math.sin(angle);
            this.dy = L * Math.cos(angle);
        }
    }

    const TRACE_GRAPH_WIDTH = 30;
    const LINE_HEIGHT = 25;
    const D = Math.PI / 6;

    const h = 1;

    const m = (4 * TRACE_GRAPH_WIDTH) / (h * LINE_HEIGHT);

    const theta = Math.atan(m)

    const upArrow = new Delta(theta - D);
    const downArrow = new Delta(Math.PI - D - theta);

    const coords = [
        // "M 25 0",
        // "q -60 12.5 0 25"

        "M 0 0",
        `q ${TRACE_GRAPH_WIDTH * 2} ${(h / 2) * LINE_HEIGHT} 0 ${h * LINE_HEIGHT}`,

        // upArrow arrow
        `l ${upArrow.dx} ${-1 * upArrow.dy}`,
        `m ${-1 * upArrow.dx} ${upArrow.dy}`,

        // downArrow arrow
        `l ${downArrow.dx} ${downArrow.dy}`,
        `m ${-1 * downArrow.dx} ${-1 * downArrow.dy}`
    ]
    path.setAttribute("d", coords.join(" "));
    graph.appendChild(path);
}

func();
good();
