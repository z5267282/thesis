import React from "react";

import TraceBox from "./TraceBox";
import UploadBox from "./UploadBox";

import styles from "./CodeBox.module.css";

export default function CodeBox({code, lines, path, counters, curr, counterColours, lineHeight, fontScaling, graphWidth, changeIndex}) {
  const [showTrace, setShowTrace] = React.useState(true);
  const [traceCode, setTraceCode] = React.useState("");

  return (
    <div className={styles.container}>
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
        <button onClick={() => changeIndex(-1)}>prev</button>
        <button onClick={() => changeIndex(1)}>next</button>
      </div>
    </div>
  );
}
