import styles from "./TraceBox.module.css";

import { Fragment } from "react";

/**
 * @param {*} coords object with the starting line and all remaining ones
 * @returns list of string of the path commands that can be joined with .join()
 */
function genSVGPath(coords) {
  const LINE_HEIGHT = 25;
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
 * check whether the ith line should be highlighted.
 * the last line should be highlighted
 * @param {*} i 
 * @param {*} code 
 */
function colourLine(i, code) {
  return (i === code.length - 1) ? styles.highlight : "";
}

export default function TraceBox({code, lines, path}) {
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
          (Object.keys(path).length > 0) &&
            // have this here to force the svg to take up whole height of code box
            <svg height="100%" width={50}>
              <path d={`${genSVGPath(path).join(" ")}`} stroke="black" fill="transparent" />
            </svg>
        }
      </div>
    </div>
  );
} 
