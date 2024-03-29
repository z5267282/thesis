import { Fragment, useEffect } from "react";

import {
  COUNTER_COLOURS, FONT_SCALING_FACTOR, LINE_HEIGHT, TRACE_GRAPH 
} from "../config";

import styles from "./TraceBox.module.css";
import { IconButton, LinearProgress } from "@mui/material";
import EastIcon from '@mui/icons-material/East';
import WestIcon from '@mui/icons-material/West';

// for assurance
const DEC = -1;
const INC = 1;

export default function TraceBox({
  code, lines, path, counters, curr, index, total,
  changeIndex, disablePrev, disableNext, showTrace
}) { 
  useEffect(() => {
    const handleArrows = (event) => {
      switch (event.key) {
        case "ArrowLeft":
          changeIndex(DEC);
          break;
        case "ArrowRight":
          changeIndex(INC);
          break;
        default:
          ;
      }
    }
    document.addEventListener("keydown", handleArrows);
    return () => document.removeEventListener("keydown", handleArrows);
  }, [showTrace, changeIndex]);

  return (
    <span className={styles.traceBox}>
      <h1 className={styles.largeText}>
        Trace execution
      </h1>
      <div className={styles.transitions}>
        <IconButton
          onClick={() => changeIndex(DEC)} disabled={disablePrev}
          className={disabledClass(disablePrev)}
        >
          <WestIcon />
        </IconButton>
        <IconButton
          onClick={() => changeIndex(INC)} disabled={disableNext}
          className={disabledClass(disableNext)}
        >
          <EastIcon />
        </IconButton>
      </div>
      {
        (code.length !== 0) &&
          <LinearProgress
            variant="determinate"
            sx={{
              width : "80%",
              "& .MuiLinearProgress-bar": {
                 transition: "none"
              }
            }}
            value={calcProgress(index, total)}
          />
      }
      {
        (code.length === 0) ?
          <LoadingBox />
        :
          <TracedLinesBox
            code={code} lines={lines} curr={curr} path={path}
            counters={counters}
          />
      }
    </span>
  );

  /**
  * generate the classname to disabled a button depending on a flag
  * @param {*} flag 
  */
  function disabledClass(flag) {
    return (flag) ? styles.disabled : "";
  }

  function calcProgress(index, total) {
    // the first frame is a filler one without a curr
    if (index === 0) return 0;

    const calc = ((index) / (total - 1) * 100).toFixed(0);
    return parseInt(calc);
  }
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
    lineHeight       : addPixels(LINE_HEIGHT),
    fontSize         : addPixels(LINE_HEIGHT * FONT_SCALING_FACTOR)
  };

  return (
    <div className={`${styles.traceCode} ${styles.tracedLinesBox}`}>
      <div className={styles.tracedLines} style={lineHeightStyle}>
        <Lines code={code} lines={lines} curr={curr} path={path} />
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

  function addPixels(dimension) {
    return `${dimension}px`;
  }

  function Lines({code, lines, curr, path}) {
    const dotted = new Set([path.start, ...path.rest]);
    return code.map(
      (line, i) => {
        const colour = colourLine(i, curr);
        return (
          <Fragment key={`line-${i}`}>
            <span className={`${styles.lineNumber} ${colour}`}>
              {`${lines[i]}${lines[i] === "" ? "" : "."}`}
            </span>
            <span className={`${styles.codeLine} ${colour}`}>
              <span className={styles.preserveSpace}>{line}</span>
              <span className={dotLine(i)} />
            </span>
          </Fragment>
        );
      }
    );

    function dotLine(i) {
      // tracing has not started yet
      if (curr === null) return "";
      return (dotted.has(i)) ? styles.dotted : "";
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
        const gradient = (4 * TRACE_GRAPH.width) / (height);
        const theta = Math.atan(gradient)

        class Delta {
            constructor(angle) {
                this.dx = TRACE_GRAPH.length * Math.sin(angle);
                this.dy = TRACE_GRAPH.length * Math.cos(angle);
            }
        }

        const upArrow = new Delta(theta - TRACE_GRAPH.degree);
        const downArrow = new Delta(Math.PI - TRACE_GRAPH.degree - theta);

        const coords = [
            `q ${TRACE_GRAPH.width * 2} ${height / 2} 0 ${height}`,

            // upArrow arrow
            `l ${upArrow.dx} ${-1 * upArrow.dy}`,
            `m ${-1 * upArrow.dx} ${upArrow.dy}`,

            // downArrow arrow
            `l ${downArrow.dx} ${downArrow.dy}`,
            `m ${-1 * downArrow.dx} ${-1 * downArrow.dy}`
        ]
        path.push(coords.join(" "));
        prev = coord;
      });
      return path;
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
}
