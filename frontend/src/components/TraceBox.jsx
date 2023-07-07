import styles from "./TraceBox.module.css";

import { LINE_HEIGHT } from "../config";

import { Fragment } from "react";

/**
 * @param {*} coords object with the starting line and all remaining ones
 * @returns list of string of the path commands that can be joined with .join()
 */
function genSVGPath(coords) {
  const path = [`M 0 ${coords.start * LINE_HEIGHT + (LINE_HEIGHT / 2)}`];
  let prev = coords.start;
  coords.rest.forEach((coord) => {
    const height = (coord - prev) * LINE_HEIGHT;
    path.push(`q 50 ${height / 2} 0 ${height}`);
    prev = coord;
  });
  return path;
}

/**
 * @param {*}
 * @returns an inline style object with a top margin and heights for the counter's div
 */
function genCounterStyle(start, end) {
  const half_line = LINE_HEIGHT / 2;
  return {
    marginTop: (start * LINE_HEIGHT) + half_line,
    height: (end - start) * LINE_HEIGHT
  };
}

/**
 * check whether the ith line should be highlighted.
 * the last line should be highlighted
 * @param {*} i 
 * @param {*} code 
 */
function colourLine(i, code) {
  return (i === code.length - 1) ? styles.highlight : "";
}

export default function TraceBox({code, lines, path, counter}) {
  console.log(genCounterStyle(counter.start, counter.end));
  return (
    <div className={styles.container}>
      <p className={styles.largeText}>Trace execution</p>
      <div className={styles.traceBox}>
        <div className={styles.codeBox}>
          {
            code.map(
              (line, i) => (
                <Fragment key={`line-${i}`}>
                  <span className={colourLine(i, code)}>
                    {`${lines[i]}${lines[i] === "" ? "" : "."}`}
                  </span>
                  <span className={`${styles.preserveSpace} ${colourLine(i, code)}`}>{line}</span>
                </Fragment>
              )
            )
          } 
        </div>
        {
          (path !== null) &&
            // have this here to force the svg to take up whole height of code box
            <svg height="100%" width={50}>
              <path d={`${genSVGPath(path).join(" ")}`} stroke="black" fill="transparent" />
            </svg>
        }
        {
          (counter !== null) && 
            <div className={styles.counterBox} style={genCounterStyle(counter.start, counter.end)}>
              <sup>{counter.numerator}</sup>/<sub>{counter.denominator}</sub>
            </div>
        }
      </div>
    </div>
  );
} 
