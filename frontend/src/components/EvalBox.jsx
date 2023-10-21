import styles from "./EvalBox.module.css";

export default function EvalBox({evallines}) {
  return (
    <>
      <h2 className={styles.fontSize}>Conditional Evaluation</h2>
      <div className={styles.evalBox}>
        {
          evallines.map(
            (line, i) => (
              <span key={`evalline-${i}`}>
                {line}
              </span>
            )
          )
        }
      </div>
    </>
  )
}
