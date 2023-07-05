import styles from "./TraceBox.module.css";

import { Fragment, useEffect, useRef } from "react";

export default function TraceBox({code, lines}) {
  const lineRefs = useRef([]);
  let dimenensions = [];

  useEffect(() => {
    dimenensions = lineRefs.current.map((ref) => ref.getBoundingClientRect());
    console.log(dimenensions);
  }, []);

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
                  <span
                    className={styles.preserveSpace}
                    ref={(element) => lineRefs.current.push(element)}
                  >
                    {line}
                  </span>
                </Fragment>
              )
            )
          } 
        </div>
        <svg>
          {/* <path d="M 0 0 Q 50 50 0 100 T 0 200 T 0 600" stroke="black" fill="transparent" /> */}
          <path d="M 0 0 Q 50 50 0 100 Q 50 150 0 200" stroke="black" fill="transparent" />
          {/* <path d="M 0 200 Q 50 250 0 300" stroke="black" fill="transparent" /> */}
        </svg>
      </div>
    </div>
  );
} 
