import styles from "./TraceBox.module.css";

import { Fragment } from "react";

export default function TraceBox({code, lines}) {
  return (
    <div className={styles.container}>
      <p className={styles.largeText}>Trace execution</p>
      <div className={styles.traceBox}>
        <div className={styles.codeBox}>
          {
            code.map(
              (line, i) => (
                <Fragment key={`line-${i}`}>
                  <span>{`${lines[i]}${lines[i] === "" ? "" : "."}`}</span>
                  <span id={`code-line-${i}`} className={styles.preserveSpace}>{line}</span>
                </Fragment>
              )
            )
          } 
        </div>
        {/* <svg width={300} height={300}>
          <path d="M 0 0 Q 50 50 0 100 T 0 200" stroke="black" fill="transparent" />
        </svg> */}
      </div>
    </div>
  );
} 
