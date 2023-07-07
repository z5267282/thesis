import styles from "./OutputBox.module.css";

export default function OutputBox() {
  return (
    <label className={styles.container}>
      Output
      <div className={styles.outputBox}>
        <p>fish</p>
        <textarea className={styles.uploadBox} value="out" spellCheck={false} readOnly/>
        <svg>
          <path d="M 0 100 l 0 0" stroke="black" fill="transparent"></path>
        </svg>
      </div>
    </label>
  );
};
