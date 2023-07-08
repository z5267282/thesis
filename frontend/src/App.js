import styles from "./App.module.css";

import CodeBox from "./components/CodeBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

import dummy from "./dummy";
import {
  ARROW_DIMENSIONS, FONT_SCALING_FACTOR, LINE_HEIGHT, TRACE_GRAPH_WIDTH
} from "./config";

export default function App() {
  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <CodeBox
          code={dummy.code} lines={dummy.lines} path={dummy.path} counter={dummy.counter}
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
