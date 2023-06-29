import styles from "./App.module.css";

import CodeBox from "./components/CodeBox";
import OutputBox from "./components/OutputBox";
import VariableBox from "./components/VariableBox";

export default function App() {
  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <CodeBox />
        <div className={styles.outputs}>
          <VariableBox />
          <OutputBox />
        </div>
      </div>
    </div>
  );
}
