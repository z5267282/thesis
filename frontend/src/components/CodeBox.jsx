import React from "react";

import TraceBox from "./TraceBox";
import UploadBox from "./UploadBox";

import styles from "./CodeBox.module.css";

export default function CodeBox({
    code, lines, path, counters, curr, counterColours,
    lineHeight, fontScaling, graphWidth,
    changeIndex, disablePrev, disableNext
}) {
  const [showTrace, setShowTrace] = React.useState(true);
  const [traceCode, setTraceCode] = React.useState("");

  return (
    <div className={styles.codeBox}>
      <div className={styles.tabSelector}>
        <button className={styles.customButton} type="button" onClick={() => {setShowTrace(true)}}>Trace</button>
        <button className={styles.customButton} type="button" onClick={() => {setShowTrace(false)}}>Upload</button>
      </div>
      {
        (showTrace) ?
          <TraceBox
            code={code} lines={lines} path={path} counters={counters} curr={curr} counterColours={counterColours}
            lineHeight={lineHeight} fontScaling={fontScaling} graphWidth={graphWidth}
          />
        :
          <UploadBox
            traceCode={traceCode} setTraceCode={setTraceCode}
          />
      }
      <div className={styles.transitionContainer}>
        <button
          onClick={() => changeIndex(-1)} disabled={disablePrev}
          className={disablePrev ? styles.disabled : ""}
        >
          prev
        </button>
        <button
          onClick={() => changeIndex(1)} disabled={disableNext}
          className={disableNext ? styles.disabled : ""}
        >
          next
        </button>
      </div>
    </div>
  );
}
