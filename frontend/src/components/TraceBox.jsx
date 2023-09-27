import { Fragment } from "react";

import {
  COUNTER_COLOURS, FONT_SCALING_FACTOR, LINE_HEIGHT, TRACE_GRAPH_WIDTH
} from "../config";
import { addPixels } from "../helper";

import styles from "./TraceBox.module.css";

export default function TraceBox({
  code, lines, path, counters, curr,
  changeIndex, disablePrev, disableNext
}) {
  return (
    <span className={styles.traceBox}>
      <h1 className={styles.largeText}>
        Trace execution
      </h1>
      <div className={styles.transitionContainer}>
        <button
          onClick={() => changeIndex(-1)} disabled={disablePrev}
          className={disabledClass(disablePrev)}
        >
          ◀
        </button>
        <button
          onClick={() => changeIndex(1)} disabled={disableNext}
          className={disabledClass(disableNext)}
        >
          ▶
        </button>
      </div>
      <div className={styles.buffer}></div>
      {
        (code.length === 0) ?
          <LoadingBox />
        :
          <TracedLinesBox
            code={code} lines={lines} curr={curr} path={path} counters={counters}
          />
      }
    </span>
  );
} 

/**
 * generate the classname to disabled a button depending on a flag
 * @param {*} flag 
 */
function disabledClass(flag) {
  return (flag) ? styles.disabled : "";
}

function LoadingBox() {
  return <div className={`${styles.traceCode} ${styles.loadingBox}`}>
    [ upload your code ]
  </div>;
}

function TracedLinesBox({
  code, lines, curr, path, counters
}) {
  // this must be inline to import config value
  const lineHeightStyle = {
    gridTemplateRows : `repeat(auto-fill, ${addPixels(LINE_HEIGHT)})`,
    lineHeight : addPixels(LINE_HEIGHT),
    fontSize   : addPixels(LINE_HEIGHT * FONT_SCALING_FACTOR)
  };

  return (
    <div className={`${styles.traceCode} ${styles.tracedLinesBox}`}>
      <div className={styles.tracedLines} style={lineHeightStyle}>
        <Lines code={code} lines={lines} curr={curr} />
      </div>
      {
        (path.rest.length !== 0) &&
          <Path path={path} />
      }
      {
        (counters.length !== 0) &&
          <Counters counters={counters} />
      }
    </div>
  );
}

function Path({path}) {
  return (
    <svg>
      <path
        d={`${genSVGPath(path).join(" ")}`} stroke="black" fill="transparent"
        className={styles.thickPen}
      />
    </svg>
  );

  /**
  * @param {*} coords object with the starting line and all remaining ones
  * @returns list of string of the path commands that can be joined with .join()
  */
  function genSVGPath(coords) {
    const path = [`M 0 ${coords.start * LINE_HEIGHT + (LINE_HEIGHT / 2)}`];
    let prev = coords.start;
    coords.rest.forEach((coord) => {
      const height = (coord - prev) * LINE_HEIGHT;
      path.push(`q ${TRACE_GRAPH_WIDTH} ${height / 2} 0 ${height}`);
      prev = coord;
    });
    return path;
  }
}


function Lines({code, lines, curr}) {
  return code.map(
    (line, i) => {
      const colour = colourLine(i, curr);
      return (
        <Fragment key={`line-${i}`}>
          <span className={`${styles.lineNumber} ${colour}`}>
            {`${lines[i]}${lines[i] === "" ? "" : "."}`}
          </span>
          <span className={`${styles.preserveSpace} ${colour}`}>{line}</span>
        </Fragment>
      );
    }
  );

  /**
  * check whether the ith line should be highlighted.
  * the current line should be highlighted
  * @param {*} index
  * @param {*} code 
  */
  function colourLine(index, curr) {
    return (curr !== null && index === curr) ? styles.highlight : "";
  }
} 

function Counters({counters}) {
  return counters.map(
    (counter, i) => 
      <div
        className={styles.counterBox}  key={`counter-${i}`}
        style={genCounterStyle(counter.start, counter.end, LINE_HEIGHT, i)}
      >
        <span className={styles.fraction}>
          <span className={styles.topText}>{counter.numerator}</span>
          /
          <span className={styles.bottomText}>{counter.denominator}</span>
        </span>
      </div>
  );

  /**
  * @param {*}
  * @returns an inline style object with a top margin and heights for the counter's div
  */
  function genCounterStyle(start, end, lineHeight, index) {
    const halfLine = lineHeight / 2;
    return {
      borderColor: colourCounter(index, COUNTER_COLOURS),
      marginTop: addPixels((start * lineHeight) + halfLine),
      height: addPixels((end - start) * lineHeight)
    };
  }

  /**
  * provide a colour for the ith counter
  * @param {*} index of the counter
  * @param {*} colours
  * @returns 
  */
  function colourCounter(index, colours) {
    return colours[index % colours.length]
  }
}
