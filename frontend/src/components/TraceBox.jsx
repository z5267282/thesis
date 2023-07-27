import Counters from "./Counters";
import Lines from "./Lines";
import Path from "./Path";

import { addPixels } from "../helper";

import styles from "./TraceBox.module.css";

export default function TraceBox({code, lines, path, counters, curr, counterColours, lineHeight, fontScaling, graphWidth}) {
  // this must be inline to import config value
  const lineHeightStyle = {
    lineHeight: addPixels(lineHeight),
    fontSize: addPixels(lineHeight * fontScaling)
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.largeText}>Trace execution</h1>
      <div className={styles.traceBox}>
        <div className={styles.codeBox} style={lineHeightStyle}>
          <Lines code={code} lines={lines} curr={curr} />
        </div>
        {
          (path !== null) &&
            <Path path={path} lineHeight={lineHeight} graphWidth={graphWidth} />
        }
        {
          (counters.length !== 0) &&
            <Counters counters={counters} lineHeight={lineHeight} counterColours={counterColours} />
        }
      </div>
    </div>
  );
} 
