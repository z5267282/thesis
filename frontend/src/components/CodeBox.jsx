import React from "react";
import styles from "./CodeBox.module.css";

export default function CodeBox() {
  const [showTrace, setShowTrace] = React.useState(false);
  const [traceCode, setTraceCode] = React.useState("");

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
        {
          (showTrace) ?
            <textarea
              rows={30} cols={60} name="code-upload" spellCheck={false} disabled value={traceCode} id="box"
            />
          :
          <textarea
            rows={30} cols={60} name="code-upload" spellCheck={false} id="box"
            onInput={(event) => setTraceCode(event.target.value)} 
          />
        }
      </label>
      <div className={styles.transitionContainer}>
        <button>prev</button>
        <button>next</button>
      </div>
    </div>
  );
}
