import './App.css';

import CodeBox from './components/CodeBox';
import OutputBox from './components/OutputBox';
import VariableBox from './components/VariableBox';

export default function App() {
  return (
    <div className="App">
      <div id="main">
        <CodeBox />
        <div id="outputs">
          <VariableBox />
          <OutputBox />
        </div>
      </div>
    </div>
  );
}
