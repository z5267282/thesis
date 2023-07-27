import React from "react";

import CodeBox from "./components/CodeBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

import data from "./dummy/simple-prog";

import styles from "./App.module.css";

import {
  ARROW_WIDTH, ARROW_HEIGHT, ARROW_HEAD_LENGTH,
  COUNTER_COLOURS, FONT_SCALING_FACTOR, LINE_HEIGHT, TRACE_GRAPH_WIDTH
} from "./config";

export default function App() {
  const [dataFrame, setDataFrame] = React.useState(data);

  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <CodeBox
          code={dataFrame.code} lines={dataFrame.lines} path={dataFrame.path}
          counters={dataFrame.counters} curr={dataFrame.curr} counterColours={COUNTER_COLOURS}
          lineHeight={LINE_HEIGHT} fontScaling={FONT_SCALING_FACTOR} graphWidth={TRACE_GRAPH_WIDTH}
        />
        <div className={styles.outputs}>
          <VariableBox variables={dataFrame.vars} />
          <OutputBox width={ARROW_WIDTH} height={ARROW_HEIGHT} headLength={ARROW_HEAD_LENGTH} outputs={dataFrame.out} />
        </div>
      </div>
    </div>
  );
}
