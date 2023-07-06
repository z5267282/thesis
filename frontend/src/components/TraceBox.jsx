import styles from "./TraceBox.module.css";

import { Fragment } from "react";

// return list of string of the path commands that can be joined with .join()
function genSVGPath(coords) {
  const LINE_HEIGHT = 25;
  const path = [`M 0 ${coords.start * LINE_HEIGHT + (LINE_HEIGHT / 2)}`];
  let prev = coords.start;
  coords.rest.forEach((coord) => {
    const height = (coord - prev) * LINE_HEIGHT;
    path.push(`q 50 ${height / 2} 0 ${height}`);
    prev = coord;
  });
  console.log(path.join(" "));
  return path;
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
                  <span>{`${lines[i]}${lines[i] === "" ? "" : "."}`}</span>
                  <span className={styles.preserveSpace}>{line}</span>
                </Fragment>
              )
            )
          } 
        </div>
        {
          (Object.keys(path).length > 0) &&
            <svg height="100%">
              <path d={`${genSVGPath(path).join(" ")}`} stroke="black" fill="transparent" />
            </svg>
        }
      </div>
    </div>
  );
} 
