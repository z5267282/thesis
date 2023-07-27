import { Fragment } from "react";

import styles from "./Lines.module.css";

/**
 * check whether the ith line should be highlighted.
 * the last line should be highlighted
 * @param {*} index
 * @param {*} code 
 */
function colourLine(index, code) {
  return (index === code.length - 1) ? styles.highlight : "";
}

export default function Lines({code, lines}) {
  return code.map(
    (line, i) => (
      <Fragment key={`line-${i}`}>
        <span className={colourLine(i, code)}>
          {`${lines[i]}${lines[i] === "" ? "" : "."}`}
        </span>
        <span className={`${styles.preserveSpace} ${colourLine(i, code)}`}>{line}</span>
      </Fragment>
    )
  );
} 
