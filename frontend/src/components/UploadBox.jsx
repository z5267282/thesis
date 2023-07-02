import styles from "./UploadBox.module.css";

export default function UploadBox({traceCode, setTraceCode}) {
  return (
    <div className={styles.editorBox}>
      <div className={styles.lineNumbers}>
        { traceCode.split("\n").map(() => <span />) }
      </div>
      <textarea
        name="code-upload" spellCheck={false} id="box" className={styles.codeInput}
        onInput={(event) => setTraceCode(event.target.value)} 
      />
    </div>
  );
}
