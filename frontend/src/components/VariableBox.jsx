import styles from "./VariableBox.module.css";

export default function VariableBox() {
  return (
    <label className={styles.container}>
      Variables
      <textarea id="outputBox" value="vars" spellCheck={false} readOnly/>
    </label>
  );
};
