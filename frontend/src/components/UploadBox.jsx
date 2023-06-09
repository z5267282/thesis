import styles from "./UploadBox.module.css";

export default function UploadBox({traceCode, setTraceCode}) {
  return (
    <label htmlFor="uploadBox" className={styles.container}>
      <h1 className={styles.largeText}>Upload code</h1>
      <div className={styles.editorBox}>
        <div className={styles.lineNumbers}>
          { traceCode.split("\n").map((_, i) => <span key={`line-${i}`}/>) }
        </div>
        <textarea
          name="code-upload" spellCheck={false} id="uploadBox" className={styles.codeInput} value={traceCode}
          onInput={(event) => setTraceCode(event.target.value)} 
        />
      </div>
    </label>
  );
}
