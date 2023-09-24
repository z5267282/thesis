import React from "react";

import CodeBox from "./components/CodeBox";
import EvalBox from "./components/EvalBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

import { generateData } from "./helper";

import styles from "./App.module.css";

import {
  ARROW_WIDTH, ARROW_HEIGHT, ARROW_HEAD_LENGTH,
  COUNTER_COLOURS, FONT_SCALING_FACTOR, LINE_HEIGHT, TRACE_GRAPH_WIDTH, SERVER
} from "./config";

export default function App() {
  const [frames, setFrames] = React.useState([]);
  const [index, setIndex] = React.useState(0);
  const [showTrace, setShowTrace] = React.useState(true);

  const changeIndex = (offset) => {
    const newIndex = index + offset;
    if (newIndex >= 0 && newIndex < frames.length) {
      setIndex(newIndex);
    }
  }
  const resetIndex = () => setIndex(0);

  const { dataFrame, disablePrev, disableNext } = generateData(frames, index);

  return (
    <div className={styles.App}>
      <div>The server is: "{SERVER}"</div>
      <div>environment : "{process.env.REACT_APP_THESIS_HOST}"</div>
      <CodeBox
        code={dataFrame.code} lines={dataFrame.lines} path={dataFrame.path}
        counters={dataFrame.counters} curr={dataFrame.curr} counterColours={COUNTER_COLOURS}
        lineHeight={LINE_HEIGHT} fontScaling={FONT_SCALING_FACTOR} graphWidth={TRACE_GRAPH_WIDTH}
        changeIndex={changeIndex} disablePrev={disablePrev} disableNext={disableNext}
        setFrames={setFrames} resetIndex={resetIndex} showTrace={showTrace} setShowTrace={setShowTrace}
      />
      {
        (showTrace) && 
          <div className={styles.outputs}>
            {
              (dataFrame.evalbox.length > 0) &&
                <EvalBox evallines={dataFrame.evalbox} />
            }
            <VariableBox variables={dataFrame.vars} />
            <OutputBox width={ARROW_WIDTH} height={ARROW_HEIGHT} headLength={ARROW_HEAD_LENGTH} outputs={dataFrame.out} />
          </div>
      }
    </div>
  );
}
