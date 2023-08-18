import styles from "./VariableBox.module.css";

export default function VariableBox({variables}) {
  return (
    <label className={styles.container} htmlFor="variable-box">
      <h2 className={styles.fontSize}>Variables</h2>
      <textarea id="variable-box" className={styles.variableBox} value={variables.join("\n")} spellCheck={false} readOnly/>
    </label>
  );
};
