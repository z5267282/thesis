import {dummy} from "../dummy.js";

import styles from "./TraceBox.module.css";

export default function TraceBox() {
  console.log(dummy);
  return (
    <div className={styles.container}>
      <p className={styles.largeText}>Trace execution</p>
      <div className={styles.codeBox}>

      </div>
    </div>
  );
} 
