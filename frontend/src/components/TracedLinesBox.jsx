import Counters from "./Counters";
import Lines from "./Lines";
import Path from "./Path";

import { addPixels } from "../helper";

import styles from "./TracedLinesBox.module.css";

export default function TracedLinesBox({
  code, lines, curr, path, lineHeight, fontScaling, graphWidth, counters, counterColours
}) {
  // this must be inline to import config value
  const lineHeightStyle = {
    lineHeight : addPixels(lineHeight),
    fontSize   : addPixels(lineHeight * fontScaling)
  };

  return (
    <>
      <div className={styles.tracedLinesBox} style={lineHeightStyle}>
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
    </>
  );
}
