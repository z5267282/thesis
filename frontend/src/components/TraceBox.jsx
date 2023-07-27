import { Fragment } from "react";

import { addPixels } from "../helper";

import styles from "./TraceBox.module.css";

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
 * provide a colour for the ith counter
 * @param {*} index of the counter
 * @param {*} colours
 * @returns 
 */
function colourCounter(index, colours) {
  return colours[index % colours.length]
}

/**
 * @param {*}
 * @returns an inline style object with a top margin and heights for the counter's div
 */
function genCounterStyle(start, end, lineHeight, index, colours) {
  const halfLine = lineHeight / 2;
  return {
    borderColor: colourCounter(index, colours),
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

export default function TraceBox({code, lines, path, counters, counterColours, lineHeight, fontScaling, graphWidth}) {
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
                <div
                  className={styles.counterBox}  key={`counter-${i}`}
                  style={genCounterStyle(counter.start, counter.end, lineHeight, i, counterColours)}
                >
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
