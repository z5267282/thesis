import React from "react";

import styles from "./App.module.css";

import CodeBox from "./components/CodeBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

import dummy_loop from "./dummy-2d-loop";

import {
  ARROW_DIMENSIONS, FONT_SCALING_FACTOR, LINE_HEIGHT, TRACE_GRAPH_WIDTH
} from "./config";

export default function App() {
  const [dataFrame, setDataFrame] = React.useState(dummy_loop);

  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <CodeBox
          code={dataFrame.code} lines={dataFrame.lines} path={dataFrame.path} counters={dataFrame.counters}
          lineHeight={LINE_HEIGHT} fontScaling={FONT_SCALING_FACTOR} graphWidth={TRACE_GRAPH_WIDTH}
        />
        <div className={styles.outputs}>
          <VariableBox />
          <OutputBox {...ARROW_DIMENSIONS} />
        </div>
      </div>
    </div>
  );
}
