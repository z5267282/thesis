import styles from "./TraceBox.module.css";

import { Fragment } from "react";

import dummy from "../dummy.js";

export default function TraceBox() {
  console.log(dummy);
  return (
    <div className={styles.container}>
      <p className={styles.largeText}>Trace execution</p>
      <div className={styles.codeBox}>
        {
          dummy.code.map(
            (line, i) => (
              <Fragment key={`line-${i}`}>
                <span>{dummy.lines[i]}</span><span>{line}</span>
              </Fragment>
            )
          )
        } 
      </div>
    </div>
  );
} 
