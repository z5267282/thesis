import styles from "./VariableBox.module.css";

export default function VariableBox({variables}) {
  return (
    <div className={styles.variableBox}>
      <h2>Variables</h2>
      <div className={styles.vars}> {
          variables.map(variable => <>
            <span style={{textAlign : "right", whiteSpace : "pre"}}>{`${variable.name} = `}</span>
            <span>{variable.value}</span>
          </>)
        }
      </div>
    </div>
  );
}
