import { addPixels } from "../helper";

import styles from "./Counters.module.css";

/**
 * provide a colour for the ith counter
 * @param {*} index of the counter
 * @param {*} colours
 * @returns 
 */
function colourCounter(index, colours) {
  return colours[index % colours.length]
}

/**
 * @param {*}
 * @returns an inline style object with a top margin and heights for the counter's div
 */
function genCounterStyle(start, end, lineHeight, index, colours) {
  const halfLine = lineHeight / 2;
  return {
    borderColor: colourCounter(index, colours),
    marginTop: addPixels((start * lineHeight) + halfLine),
    height: addPixels((end - start) * lineHeight)
  };
}

export default function Counters({counters, lineHeight, counterColours}) {
  return counters.map(
    (counter, i) => 
      <div
        className={styles.counterBox}  key={`counter-${i}`}
        style={genCounterStyle(counter.start, counter.end, lineHeight, i, counterColours)}
      >
        <span className={styles.fraction}>
          <span className={styles.topText}>{counter.numerator}</span>
          /
          <span className={styles.bottomText}>{counter.denominator}</span>
        </span>
      </div>
  );
}
