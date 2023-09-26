import React from "react";

import TraceBox from "./TraceBox";
import UploadBox from "./UploadBox";

import styles from "./CodeBox.module.css";
import { Tab, Tabs } from "@mui/material";

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
        <Tabs centered textColor="secondary" indicatorColor="secondary">
          <Tab label="Trace" onClick={() => {setShowTrace(true)}} />
          <Tab label="Upload " onClick={() => {setShowTrace(false)}} />
        </Tabs>
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
