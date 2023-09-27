import styles from "./TextBox.module.css";

export default function TextBox({header, text, textAreaRef}) {
  const generatedID = `${header.toLowerCase()}Box`;

  return (
    <label className={styles.textBox} htmlFor={generatedID}>
      <h2 className={styles.fontSize}>{header}</h2>
      <textarea
        id={generatedID} className={`${styles.variableBox} ${styles.fontSize}`}
        value={text} spellCheck={false} readOnly ref={textAreaRef}
      />
    </label>
  );
};
