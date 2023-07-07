import styles from "./OutputBox.module.css";

function genArrowPath(width, height, arrow_length) {
  const verticalLine = `M 0 ${width / 2} l 0 ${height} m 0 ${height * -1}`;
  const arrowVector = {
    dx: arrow_length * Math.sqrt(3),
    dy: arrow_length * (Math.sqrt(3) / 2)
  };

  const drawReset = (dx, dy) => {
    const penDown = `l ${-1 * dx} ${-1 * dy}`;
    const reset = `m ${dx} ${dy}`;
    return `${penDown} ${reset}`;
  };
  const left = drawReset(arrowVector.dx, arrowVector.dy);
  const right = drawReset(arrowVector.dx * -1, arrowVector.dy * -1);

  // const res = `${verticalLine} ${left} ${right}`;
  // const res = `${verticalLine} ${right} l -10 0`;
  const res = `${verticalLine} l -10 0`;
  console.log(right);
  console.log(res)
  return res;
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
        <svg width={SVG_WIDTH * 1.5}>
          <path d={genArrowPath(SVG_WIDTH, SVG_HEIGHT, ARROW_HEAD_LENGTH)} stroke="black" fill="transparent"></path>
          {/* <path d="M 15 0 l 0 100 m 0 -100" stroke="black" fill="transparent"></path> */}
        </svg>
      </div>
    </label>
  );
};
