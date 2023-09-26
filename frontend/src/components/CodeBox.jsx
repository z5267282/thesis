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

  return (
    <div className={styles.codeBox}>
      <div className={styles.tabSelector}>
      </div>
    </div>
  );
}
