import { useEffect, useRef } from "react";

import styles from "./OutputBox.module.css";

export default function OutputBox({index, outputs}) {
  const textAreaRef = useRef();
  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.scrollTop = textAreaRef.current.scrollHeight;
    }
  }, [index]);

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
