import styles from "./OutputBox.module.css";

import { addPixels } from "../helper";

export default function OutputBox() {
  const SVG_WIDTH = 30;
  return (
    <label className={styles.container}>
      Output
      <div className={styles.outputBox}>
        <textarea className={styles.uploadBox} value="out" spellCheck={false} readOnly/>
        <svg>
          <path d=""></path>
        </svg>
        {/* <svg>
          <path d="M 0 100 l 0 0" stroke="black" fill="transparent"></path>
        </svg> */}
      </div>
    </label>
  );
};
