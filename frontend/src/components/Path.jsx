import styles from "./Path.module.css";

/**
 * @param {*} coords object with the starting line and all remaining ones
 * @returns list of string of the path commands that can be joined with .join()
 */
function genSVGPath(coords, lineHeight, graphWidth) {
  const path = [`M 0 ${coords.start * lineHeight + (lineHeight / 2)}`];
  let prev = coords.start;
  coords.rest.forEach((coord) => {
    const height = (coord - prev) * lineHeight;
    path.push(`q ${graphWidth} ${height / 2} 0 ${height}`);
    prev = coord;
  });
  return path;
}

export default function Path({path, lineHeight, graphWidth}) {
  return (
    <svg>
      <path
        d={`${genSVGPath(path, lineHeight, graphWidth).join(" ")}`} stroke="black" fill="transparent"
        className={styles.thickPen}
      />
    </svg>
  );
}
