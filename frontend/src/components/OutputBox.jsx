import styles from "./OutputBox.module.css";

import { addPixels } from "../helper";

function genArrowPath(width, height, arrowLength) {
  const halfWidth = width / 2;
  const verticalLine = `M ${halfWidth} ${halfWidth}l 0 ${height} m 0 ${height * -1}`;
  // using an angle of 30 degrees
  const arrowVector = {
    dx: arrowLength / 2,
    dy: arrowLength * (Math.sqrt(3) / 2)
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

export default function OutputBox({width, height, headLength, outputs}) {
  return (
    <label className={styles.container}>
      <h2 className={styles.fontSize}>Output</h2>
      <div className={styles.outputBox}>
        <svg className={styles.arrow} style={{ width: addPixels(width) }}>
          <path d={genArrowPath(width, height, headLength)} stroke="black" fill="transparent"></path>
        </svg>
        <textarea className={styles.uploadBox} value={outputs.join("\n")} spellCheck={false} readOnly/>
      </div>
    </label>
  );
};
