import styles from "./OutputBox.module.css";

import { addPixels } from "../helper";

function genArrowPath(width, height, arrow_length) {
  const verticalLine = `M 0 ${width / 2} l 0 ${height} m 0 ${height * -1}`;
  return verticalLine;
}

export default function OutputBox() {
  const SVG_WIDTH = 30;
  const SVG_HEIGHT = 100;
  const ARROW_HEAD_LENGTH = 15;

  return (
    <label className={styles.container}>
      Output
      <div className={styles.outputBox}>
        <textarea className={styles.uploadBox} value="out" spellCheck={false} readOnly/>
        <svg>
          {/* <path d={genArrowPath(SVG_WIDTH, SVG_HEIGHT, ARROW_HEAD_LENGTH)} stroke="black" fill="transparent"></path> */}
          <path d="M 15 0 l 0 100 m 0 -100" stroke="black" fill="transparent"></path>
        </svg>
      </div>
    </label>
  );
};
