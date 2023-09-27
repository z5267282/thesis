import Editor from "react-simple-code-editor";
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-javascript';
import 'prismjs/themes/prism.css';

import { SERVER } from "../config";

import styles from "./UploadBox.module.css";

function generateDataFrames(traceCode, setFrames, resetIndex, showTraceBox) {
  fetch(`${SERVER}/analyse`, {
    method  : "PUT",
    headers : { "Content-Type" : "application/json" },
    mode    : "cors",
    body    : JSON.stringify(traceCode),
  })
    .then(res => res.json())
    .then(frames => {
      setFrames(frames);
      resetIndex();
      showTraceBox();
    })
    .catch(err => alert(`An issue occurred with parsing: ${err}`));
}

function resetState(setTraceCode, resetIndex, setFrames) {
  setTraceCode("");
  resetIndex();
  setFrames([]);
}

export default function UploadBox({
  traceCode, setTraceCode, setFrames, resetIndex, showTraceBox
}) {
  return (
    <label htmlFor="uploadBox" className={styles.container}>
      <h1 className={styles.largeText}>Upload code</h1>
      <div className={styles.editorBox}>
        <div className={styles.lineNumbers}>
          { traceCode.split("\n").map((_, i) => <span key={`line-${i}`}/>) }
        </div>
        {/* <textarea
          name="code-upload" spellCheck={false} id="uploadBox" className={styles.codeInput}
          value={traceCode} onInput={(event) => setTraceCode(event.target.value)} 
        /> */}
        <Editor
          value={traceCode}
          onValueChange={newTraceCode => setTraceCode(newTraceCode)}
          highlight={code => highlight(code, languages.js)}
        />

      </div>
      <div className={styles.buttons}>
        <button
          type="submit" className={styles.clicker}
          onClick={() => generateDataFrames(traceCode, setFrames, resetIndex, showTraceBox)}
        >
          Submit
        </button>
        <button
          type="reset" className={styles.clicker}
          onClick={() => resetState(setTraceCode, resetIndex, setFrames)}
        >
          Reset
        </button>
      </div>
    </label>
  );
}
