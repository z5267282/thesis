import { SERVER } from "../config";

import styles from "./UploadBox.module.css";

export default function UploadBox({traceCode, setTraceCode, setFrames, resetIndex, showTraceBox}) {
  return (
    <label htmlFor="uploadBox" className={styles.container}>
      <h1 className={styles.largeText}>Upload code</h1>
      <div className={styles.editorBox}>
        <div className={styles.lineNumbers}>
          { traceCode.split("\n").map((_, i) => <span key={`line-${i}`}/>) }
        </div>
        <textarea
          name="code-upload" spellCheck={false} id="uploadBox" className={styles.codeInput}
          value={traceCode} onInput={(event) => setTraceCode(event.target.value)} 
        />
      </div>
      <div className={styles.buttons}>
        <button
          type="submit" className={styles.clicker}
          onClick={
            () => {
              fetch(`${SERVER}/analyse`, {
                method : "PUT",
                headers: { "Content-Type" : "application/json" },
                body   : JSON.stringify(traceCode),
              })
                .then(res => res.json())
                .then(frames => {
                  setFrames(frames);
                  resetIndex();
                  showTraceBox();
                })
                .catch(err => {
                  alert(`An issue occurred with parsing: ${err}`);
                });
            }
          }>
          Submit
        </button>
        <button type="reset" className={styles.clicker} onClick={() => {
          setTraceCode("");
          resetIndex();
          setFrames([]);
        }}>
          Reset
        </button>
      </div>
    </label>
  );
}
