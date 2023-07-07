import styles from "./TraceBox.module.css";

import { FONT_SCALING_FACTOR, LINE_HEIGHT } from "../config";

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
  const halfLine = LINE_HEIGHT / 2;
  return {
    marginTop: (start * LINE_HEIGHT) + halfLine,
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

function addPixels(dimension) {
  return `${dimension}px`;
}

export default function TraceBox({code, lines, path, counter}) {
  // this must be inline to import config value
  const lineHeight = {
    lineHeight: addPixels(LINE_HEIGHT),
    fontSize: addPixels(LINE_HEIGHT * FONT_SCALING_FACTOR)
  };

  return (
    <div className={styles.container}>
      <p className={styles.largeText}>Trace execution</p>
      <div className={styles.traceBox}>
        <div className={styles.codeBox} style={lineHeight}>
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
            <svg>
              <path d={`${genSVGPath(path).join(" ")}`} stroke="black" fill="transparent" />
            </svg>
        }
        {
          (counter !== null) && 
            <div className={styles.counterBox} style={genCounterStyle(counter.start, counter.end)}>
              <span className={styles.fraction}>
                <span className={styles.topText}>{counter.numerator}</span>
                /
                <span className={styles.bottomText}>{counter.denominator}</span>
              </span>
            </div>
        }
      </div>
    </div>
  );
} 
