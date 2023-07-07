import styles from "./App.module.css";

import CodeBox from "./components/CodeBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

import dummy from "./dummy";

export default function App() {
  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <CodeBox code={dummy.code} lines={dummy.lines} path={dummy.path} counters={dummy.counter} />
        <div className={styles.outputs}>
          <VariableBox />
          <OutputBox />
        </div>
      </div>
    </div>
  );
}
