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
            (line, i) => {
              const preservedSpacing = line.replace(/^ /g, "\u00A0");
              return (
                  <Fragment key={`line-${i}`}>
                    <span>{dummy.lines[i]}</span>
                    <span id={`code-line-${i}`}>{preservedSpacing}</span>
                  </Fragment>
              );
            }
          )
        } 
      </div>
    </div>
  );
} 
