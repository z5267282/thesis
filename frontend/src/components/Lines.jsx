import { Fragment } from "react";

import styles from "./Lines.module.css";

/**
 * check whether the ith line should be highlighted.
 * the current line should be highlighted
 * @param {*} index
 * @param {*} code 
 */
function colourLine(index, curr) {
  return (curr !== null && index === curr) ? styles.highlight : "";
}

export default function Lines({code, lines, curr}) {
  return code.map(
    (line, i) => {
      const colour = colourLine(i, curr);
      return (
        <Fragment key={`line-${i}`}>
          <span className={`${styles.lineNumber} ${colour}`}>
            {`${lines[i]}${lines[i] === "" ? "" : "."}`}
          </span>
          <span className={`${styles.preserveSpace} ${colour}`}>{line}</span>
        </Fragment>
      );
    }
  );
} 
