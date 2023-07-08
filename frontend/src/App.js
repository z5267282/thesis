import styles from "./App.module.css";

import CodeBox from "./components/CodeBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

import dummy from "./dummy";
import { ARROW_DIMENSIONS, LINE_HEIGHT } from "./config";

export default function App() {
  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <CodeBox code={dummy.code} lines={dummy.lines} path={dummy.path} counter={dummy.counter} lineHeight={LINE_HEIGHT} />
        <div className={styles.outputs}>
          <VariableBox />
          <OutputBox {...ARROW_DIMENSIONS} />
        </div>
      </div>
    </div>
  );
}
