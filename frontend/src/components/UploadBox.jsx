import styles from "./UploadBox.module.css";

export default function UploadBox({traceCode, setTraceCode}) {
  return (
    <label htmlFor="uploadBox" className={styles.container}>
      <p className={styles.largeText}>Upload code</p>
      <div className={styles.editorBox}>
        <div className={styles.lineNumbers}>
          { traceCode.split("\n").map(() => <span />) }
        </div>
        <textarea
          name="code-upload" spellCheck={false} id="uploadBox" className={styles.codeInput} value={traceCode}
          onInput={(event) => setTraceCode(event.target.value)} 
        />
      </div>
    </label>
  );
}
