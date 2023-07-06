import styles from "./TraceBox.module.css";

import { Fragment } from "react";

// return list of string of the path commands that can be joined with .join()
function genSVGPath(coords) {
  const LINE_HEIGHT = 18;
  const path = [`M 0pt ${coords.start * LINE_HEIGHT + (LINE_HEIGHT / 2)}pt`];
  let prev = coords.start;
  coords.rest.forEach((coord) => {
    const height = (coord - prev) * LINE_HEIGHT;
    path.push(`q 0pt ${height / 2}pt 0pt ${height}pt`);
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
            <svg>
              {/* <path d="M 0pt 9pt q 0pt 9pt 0pt 18pt q 0pt 9pt 0pt 18pt q 0pt 9pt 0pt 18pt q 0pt 27pt 0pt 54pt" stroke="black" fill="transparent" /> */}
              {/* <path d={`${genSVGPath(path).join(" ")}`} stroke="black" fill="transparent" /> */}
              <path d="M10pt 10pt L90pt 10pt L50pt 90pt Z" fill="none" stroke="black" />
            </svg>
        }
      </div>
    </div>
  );
} 
