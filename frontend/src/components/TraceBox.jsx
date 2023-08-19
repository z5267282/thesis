import LoadingBox from "./LoadingBox";
import TracedLinesBox from "./TracedLinesBox";

import styles from "./TraceBox.module.css";

export default function TraceBox({
  code, lines, path, counters, curr, counterColours, lineHeight, fontScaling, graphWidth,
  changeIndex, disablePrev, disableNext
}) {
  return (
    <div className={styles.traceBox}>
      <h1 className={styles.largeText}>
        Trace execution
      </h1>
      <div className={styles.transitionContainer}>
        <button
          onClick={() => changeIndex(-1)} disabled={disablePrev}
          className={disablePrev ? styles.disabled : ""}
        >
          prev
        </button>
        <button
          onClick={() => changeIndex(1)} disabled={disableNext}
          className={disableNext ? styles.disabled : ""}
        >
          next
        </button>
      </div>
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
    </div>
  );
} 
