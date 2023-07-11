import styles from "./VariableBox.module.css";

export default function VariableBox() {
  return (
    <label className={styles.container}>
      <h2 className={styles.fontSize}>Variables</h2>
      <textarea id="outputBox" value="vars" spellCheck={false} readOnly/>
    </label>
  );
};
