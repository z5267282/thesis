import { Fragment } from "react";

import styles from "./VariableBox.module.css";

export default function VariableBox({variables}) {
  return (
    <div className={styles.variableBox}>
      <h2>Variables</h2>
      <div className={styles.vars}> {
          variables.map((variable, i) =>
            <Fragment key={`variable-${i}`}>
              <span
                className={`${styles.varName} ${colourIn(variable)}`}
              >
                {variable.name}
              </span>
              <span className={styles.barrier}>=</span>
              <span className={colourIn(variable)}>{variable.value}</span>
            </Fragment>
          )
        }
      </div>
    </div>
  );
}

function colourIn(variable) {
  return (variable.changed) ? styles.highlight : "";
}
