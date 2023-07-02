import styles from "./TraceBox.module.css";

export default function TraceBox({traceCode}) {
  return (
      <label htmlFor="traceBox" className={styles.container}>
        <p className={styles.largeText}>Trace execution</p>
        <textarea
          rows={30} cols={60} spellCheck={false} disabled value={traceCode} id="traceBox"
        />
      </label>
  );
} 
