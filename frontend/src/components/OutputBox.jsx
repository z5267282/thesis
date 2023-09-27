import { useEffect, useRef } from "react";
import { addPixels } from "../helper";

import styles from "./OutputBox.module.css";

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

export default function OutputBox({index, width, height, headLength, outputs}) {
  const textAreaRef = useRef();

  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.scrollTop = textAreaRef.current.scrollHeight;
    }
  }, [index]);

  return (
    <label className={styles.container} htmlFor="output-box">
      <h2 className={styles.fontSize}>Output</h2>
      <div className={styles.outputBox}>
        <svg className={styles.arrow} style={{ width: addPixels(width) }}>
          <path
            d={genArrowPath(width, height, headLength)} stroke="black" fill="transparent"
            className={styles.thickPen}
          />
        </svg>
        <textarea
          id="output-box" className={`${styles.uploadBox} ${styles.fontSize}`}
          ref={textAreaRef} value={outputs.join("")} spellCheck={false} readOnly
        />
      </div>
    </label>
  );
};
