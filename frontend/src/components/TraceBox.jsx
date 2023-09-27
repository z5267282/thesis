import { Fragment } from "react";

import { addPixels } from "../helper";

import styles from "./TraceBox.module.css";

export default function TraceBox({
  code, lines, path, counters, curr, counterColours, lineHeight, fontScaling, graphWidth,
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
          className={disablePrev ? styles.disabled : ""}
        >
          ◀
        </button>
        <button
          onClick={() => changeIndex(1)} disabled={disableNext}
          className={disableNext ? styles.disabled : ""}
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
            code={code} lines={lines} curr={curr} path={path}
            lineHeight={lineHeight} fontScaling={fontScaling}
            graphWidth={graphWidth} counters={counters} counterColours={counterColours}
          />
      }
    </span>
  );
} 

function LoadingBox() {
  return <div className={`${styles.traceCode} ${styles.loadingBox}`}>
    [ upload your code ]
  </div>;
}

function TracedLinesBox({
  code, lines, curr, path, lineHeight, fontScaling, graphWidth, counters, counterColours
}) {
  // this must be inline to import config value
  const lineHeightStyle = {
    gridTemplateRows : `repeat(auto-fill, ${addPixels(lineHeight)})`,
    lineHeight       : addPixels(lineHeight),
    fontSize         : addPixels(lineHeight * fontScaling)
  };

  return (
    <div className={`${styles.traceCode} ${styles.tracedLinesBox}`}>
      <div className={styles.tracedLines} style={lineHeightStyle}>
        <Lines code={code} lines={lines} curr={curr} />
      </div>
      {
        (path.rest.length !== 0) &&
          <Path path={path} lineHeight={lineHeight} graphWidth={graphWidth} />
      }
      {
        (counters.length !== 0) &&
          <Counters counters={counters} lineHeight={lineHeight} counterColours={counterColours} />
      }
    </div>
  );
}

function Path({path, lineHeight, graphWidth}) {
  return (
    <svg>
      <path
        d={`${genSVGPath(path, lineHeight, graphWidth).join(" ")}`} stroke="black" fill="transparent"
        className={styles.thickPen}
      />
    </svg>
  );

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
} 

/**
 * check whether the ith line should be highlighted.
 * the current line should be highlighted
 * @param {*} index
 * @param {*} code 
 */
function colourLine(index, curr) {
  return (curr !== null && index === curr) ? styles.highlight : "";
}

function Counters({counters, lineHeight, counterColours}) {
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

/**
 * provide a colour for the ith counter
 * @param {*} index of the counter
 * @param {*} colours
 * @returns 
 */
function colourCounter(index, colours) {
  return colours[index % colours.length]
}
