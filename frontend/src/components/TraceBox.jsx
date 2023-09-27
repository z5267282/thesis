import Counters from "./Counters";
import Lines from "./Lines";
import Path from "./Path";

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

  console.log(path);

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
