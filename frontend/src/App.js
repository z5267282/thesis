import './App.css';

import CodeBox from './components/CodeBox';
import VariableBox from './components/VariableBox';

export default function App() {
  return (
    <div className="App">
      <CodeBox />
      {/* <div classNam="outputs"> */}
      <VariableBox />
      {/* </div> */}
    </div>
  );
}
