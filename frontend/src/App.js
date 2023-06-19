import './App.css';

import CodeBox from './components/CodeBox';
import OutputBox from './components/OutputBox';
import VariableBox from './components/VariableBox';

export default function App() {
  return (
    <div className="App">
      <CodeBox />
      <div className="outputs">
        <VariableBox />
        <OutputBox />
      </div>
    </div>
  );
}
