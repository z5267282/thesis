import styles from "./CodeBox.module.css";

import TraceBox from "./TraceBox";
import UploadBox from "./UploadBox";

import React from "react";

export default function CodeBox({code, lines, path, counters}) {
  const [showTrace, setShowTrace] = React.useState(true);
  const [traceCode, setTraceCode] = React.useState("");

  return (
    <div className={styles.container}>
      <div className={styles.tabSelector}>
        <button type="button" onClick={() => {setShowTrace(true)}}>Trace</button>
        <button type="button" onClick={() => {setShowTrace(false)}}>Upload</button>
      </div>
      {
        (showTrace) ?
          <TraceBox code={code} lines={lines} path={path} counters={counters} />
        :
          <UploadBox traceCode={traceCode} setTraceCode={setTraceCode} />
      }
      <div className={styles.transitionContainer}>
        <button>prev</button>
        <button>next</button>
      </div>
    </div>
  );
}
