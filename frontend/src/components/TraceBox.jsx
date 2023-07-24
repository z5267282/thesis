import styles from "./TraceBox.module.css";

import { addPixels } from "../helper";

import { Fragment } from "react";

/**
 * @param {*} coords object with the starting line and all remaining ones
 * @returns list of string of the path commands that can be joined with .join()
 */
function genSVGPath(coords, lineHeight, graphWidth) {
  const path = [`M 0 ${coords.start * lineHeight + (lineHeight / 2)}`];
  let prev = coords.start;
  coords.rest.forEach((coord) => {
    const height = (coord - prev) * lineHeight;
    path.push(`q ${graphWidth} ${height / 2} 0 ${height}`);
    prev = coord;
  });
  return path;
}

/**
 * @param {*}
 * @returns an inline style object with a top margin and heights for the counter's div
 */
function genCounterStyle(start, end, lineHeight) {
  const halfLine = lineHeight / 2;
  console.log(
    {
      marginTop: addPixels((start * lineHeight) + halfLine),
      height: addPixels((end - start) * lineHeight)
    }
  );
  return {
    marginTop: addPixels((start * lineHeight) + halfLine),
    height: addPixels((end - start) * lineHeight)
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

export default function TraceBox({code, lines, path, counters, lineHeight, fontScaling, graphWidth}) {
  // this must be inline to import config value
  const lineHeightStyle = {
    lineHeight: addPixels(lineHeight),
    fontSize: addPixels(lineHeight * fontScaling)
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.largeText}>Trace execution</h1>
      <div className={styles.traceBox}>
        <div className={styles.codeBox} style={lineHeightStyle}>
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
              <path d={`${genSVGPath(path, lineHeight, graphWidth).join(" ")}`} stroke="black" fill="transparent" />
            </svg>
        }
        {
          (counters.length !== 0) &&
            counters.map(
              (counter, i) => 
                <div className={styles.counterBox} style={genCounterStyle(counter.start, counter.end, lineHeight)}>
                  <span className={styles.fraction}>
                    <span className={styles.topText}>{counter.numerator}</span>
                    /
                    <span className={styles.bottomText}>{counter.denominator}</span>
                  </span>
                </div>
          )
        }
      </div>
    </div>
  );
} 
