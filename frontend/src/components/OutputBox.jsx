import { useEffect, useRef } from "react";

import styles from "./OutputBox.module.css";

export default function OutputBox({index, outputs}) {
  const textAreaRef = useRef();

  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.scrollTop = textAreaRef.current.scrollHeight;
    }
  }, [index]);

  const generatedID = "OutputBox";

  return (
    <label className={styles.textBox} htmlFor={generatedID}>
      <h2 className={styles.fontSize}>Output</h2>
      <textarea
        id={generatedID} className={`${styles.variableBox} ${styles.fontSize}`}
        // we remove trailing newline for presentation on frontend
        value={outputs.join("").trimEnd()}
        spellCheck={false} readOnly
        ref={textAreaRef}
      />
    </label>
  );
};
