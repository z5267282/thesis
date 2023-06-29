import styles from "./OutputBox.module.css";

export default function VariableBox() {

  return (
    <label htmlFor="outputBox" className={styles.container}>
      <p className="large-text">Output</p>
      <textarea id="outputBox" value="out" spellCheck={false} readOnly/>
    </label>
  );
};
