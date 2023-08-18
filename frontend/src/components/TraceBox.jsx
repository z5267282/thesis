import LoadingBox from "./LoadingBox";
import TracedLinesBox from "./TracedLinesBox";

import styles from "./TraceBox.module.css";

export default function TraceBox({
  code, lines, path, counters, curr, counterColours, lineHeight, fontScaling, graphWidth
}) {
  return (
    <div className={styles.container}>
      <h1 className={styles.largeText}>
        Trace execution
      </h1>
      <div className={styles.traceBox}>
        {
          (code.length === 0) ?
            <LoadingBox />
          :
            <TracedLinesBox
              code={code} lines={lines} curr={curr} path={path}
              lineHeight={lineHeight} fontScaling={fontScaling}
              graphWidth={graphWidth} counters={counters} counterColours
            />
        }
      </div>
    </div>
  );
} 
