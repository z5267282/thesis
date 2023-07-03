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

      <svg width={300} height={300}>
        <path d="M 0 0 Q 50 50 0 100" stroke="black" fill="transparent" />
      </svg>
    </div>
  );
}
