import { Fragment } from "react";

import Counters from "./Counters";
import Path from "./Path";

import { addPixels } from "../helper";

import styles from "./TraceBox.module.css";

/**
 * check whether the ith line should be highlighted.
 * the last line should be highlighted
 * @param {*} index
 * @param {*} code 
 */
function colourLine(index, code) {
  return (index === code.length - 1) ? styles.highlight : "";
}

export default function TraceBox({code, lines, path, counters, counterColours, lineHeight, fontScaling, graphWidth}) {
  // this must be inline to import config value
  const lineHeightStyle = {
    lineHeight: addPixels(lineHeight),
    fontSize: addPixels(lineHeight * fontScaling)
  };

  const Lines = () => code.map(
    (line, i) => (
      <Fragment key={`line-${i}`}>
        <span className={colourLine(i, code)}>
          {`${lines[i]}${lines[i] === "" ? "" : "."}`}
        </span>
        <span className={`${styles.preserveSpace} ${colourLine(i, code)}`}>{line}</span>
      </Fragment>
    )
  );

  return (
    <div className={styles.container}>
      <h1 className={styles.largeText}>Trace execution</h1>
      <div className={styles.traceBox}>
        <div className={styles.codeBox} style={lineHeightStyle}>
          <Lines />
        </div>
        {
          (path !== null) &&
            <Path path={path} lineHeight={lineHeight} graphWidth={graphWidth} />
        }
        {
          (counters.length !== 0) &&
            <Counters counters={counters} lineHeight={lineHeight} counterColours={counterColours} />
        }
      </div>
    </div>
  );
} 
