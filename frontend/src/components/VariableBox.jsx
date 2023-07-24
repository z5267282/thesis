import styles from "./VariableBox.module.css";

export default function VariableBox({variables}) {
  return (
    <label className={styles.container}>
      <h2 className={styles.fontSize}>Variables</h2>
      <textarea id="outputBox" value={variables.join("\n")} spellCheck={false} readOnly/>
    </label>
  );
};
