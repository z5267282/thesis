import styles from "./OutputBox.module.css";

export default function VariableBox() {
  return (
    <label className={styles.container}>
      Output
      <textarea value="out" spellCheck={false} readOnly/>
    </label>
  );
};
