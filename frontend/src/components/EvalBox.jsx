import styles from "./EvalBox.module.css";

export default function EvalBox({evallines}) {
  return (
    <div className={styles.evalBox}>
      {
        evallines.map((line, i) => (
          <span key={`evalline-${i}`}>
            {line}
          </span>
        ))
      }
    </div>
  )
}
