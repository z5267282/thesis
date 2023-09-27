
import styles from "./OutputBox.module.css";

export default function OutputBox({index, outputs}) {

  return (
    <label className={styles.container} htmlFor="output-box">
      <h2 className={styles.fontSize}>Output</h2>
      <div className={styles.outputBox}>
        <textarea
          id="output-box" className={`${styles.uploadBox} ${styles.fontSize}`}
          ref={textAreaRef} value={outputs.join("")} spellCheck={false} readOnly
        />
      </div>
    </label>
  );
};
