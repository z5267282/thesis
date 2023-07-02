import styles from "./CodeBox.module.css";

import React from "react";

export default function CodeBox() {
  const [showTrace, setShowTrace] = React.useState(false);
  const [traceCode, setTraceCode] = React.useState("");

  const TraceBox = (
    <textarea
      rows={30} cols={60} spellCheck={false} disabled value={traceCode} id="box"
    />
  );

  const UploadBox = (
    <div className={styles.editorBox}>
      <div className={styles.lineNumbers}>
        { traceCode.split("\n").map(() => <span />) }
      </div>
      <textarea
        name="code-upload" spellCheck={false} id="box"
        onInput={(event) => setTraceCode(event.target.value)} 
      />
    </div>
  );

  return (
    <div className={styles.container}>
      <div className={styles.tabSelector}>
        <button type="button" onClick={() => {setShowTrace(true)}}>Trace</button>
        <button type="button" onClick={() => {setShowTrace(false)}}>Upload</button>
      </div>
      <label htmlFor="box" className={styles.codeBox}>
        <p className={styles.largeText}>
          { (showTrace) ? "Trace execution" : "Upload code" }
        </p>
        { (showTrace) ? TraceBox : UploadBox }
      </label>
      <div className={styles.transitionContainer}>
        <button>prev</button>
        <button>next</button>
      </div>
    </div>
  );
}
