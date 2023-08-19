import React from "react";

import TraceBox from "./TraceBox";
import UploadBox from "./UploadBox";

import styles from "./CodeBox.module.css";

export default function CodeBox({
    code, lines, path, counters, curr, counterColours,
    lineHeight, fontScaling, graphWidth,
    changeIndex, disablePrev, disableNext,
    setFrames, resetIndex,  showTrace, setShowTrace
}) {
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
            changeIndex={changeIndex} disablePrev={disablePrev} disableNext={disableNext}
          />
        :
          <UploadBox
            traceCode={traceCode} setTraceCode={setTraceCode} setFrames={setFrames}
            resetIndex={resetIndex} showTraceBox={() => setShowTrace(true)}
          />
      }
    </div>
  );
}
