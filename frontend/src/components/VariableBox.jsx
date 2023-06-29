import styles from "./VariableBox.module.css";

export default function VariableBox() {
  return (
    <label htmlFor="outputBox" className={styles.container}>
      <p className="large-text">Variables</p>
      <textarea id="outputBox" value="vars" spellCheck={false} readOnly/>
    </label>
  );
};
