import styles from "./OutputBox.module.css";

import { addPixels } from "../helper";

function genArrowPath(width, height, arrow_length) {
  const halfWidth = width / 2;
  const verticalLine = `M ${halfWidth} ${halfWidth}l 0 ${height} m 0 ${height * -1}`;
  // using an angle of 30 degrees
  const arrowVector = {
    dx: arrow_length / 2,
    dy: arrow_length * (Math.sqrt(3) / 2)
  };

  const drawReset = (dx, dy) => {
    const penDown = `l ${-1 * dx} ${dy}`;
    const reset = `m ${dx} ${-1 * dy}`;
    return `${penDown} ${reset}`;
  };
  const left = drawReset(arrowVector.dx, arrowVector.dy);
  const right = drawReset(arrowVector.dx * -1, arrowVector.dy);

  return `${verticalLine} ${left} ${right}`;
}

export default function OutputBox({width, height, head_length}) {
  return (
    <label className={styles.container}>
      Output
      <div className={styles.outputBox}>
        <textarea className={styles.uploadBox} value="out" spellCheck={false} readOnly/>
        <svg className={styles.arrow} style={{ width: addPixels(width) }}>
          <path d={genArrowPath(width, height, head_length)} stroke="black" fill="transparent"></path>
        </svg>
      </div>
    </label>
  );
};
