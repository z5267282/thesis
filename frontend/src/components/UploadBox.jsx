import Editor from "react-simple-code-editor";
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism.css';

import { EDITOR_TAB_SPACES, SERVER } from "../config";

import styles from "./UploadBox.module.css";

export default function UploadBox({
  traceCode, setTraceCode, setFrames, resetIndex, showTraceBox, switchToSubmitTab
}) {
  return (
    <label htmlFor="uploadBox" className={styles.container}>
      <h1 className={styles.largeText}>Upload code</h1>
      <div className={styles.editorBox}>
        {/* <div className={styles.lineNumbers}>
          { traceCode.split("\n").map((_, i) => <span key={}/>) }
        </div> */}
        <Editor
          id="uploadBox" value={traceCode} className={styles.editor}
          onValueChange={newTraceCode => setTraceCode(newTraceCode)}
          highlight={code =>
            highlight(code, languages.py)
              .split("\n")
              .map((line, i) =>
                <span className={styles.lineNumber} key={`line-${i}`}>{line}</span>
              )
          }
          tabSize={EDITOR_TAB_SPACES}
        />
      </div>
      <div className={styles.buttons}>
        <button
          type="submit" className={styles.clicker}
          onClick={() => handleSubmit(
            traceCode, setFrames, resetIndex, showTraceBox, switchToSubmitTab
          )}
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

function handleSubmit(
  traceCode, setFrames, resetIndex, showTraceBox, switchToSubmitTab
) {
  if (traceCode === "") {
    alert("please enter some code");
    return;
  }
  generateDataFrames(
    traceCode, setFrames, resetIndex, showTraceBox, switchToSubmitTab
  );
}

function generateDataFrames(
  traceCode, setFrames, resetIndex, showTraceBox, switchToSubmitTab
) {
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
      switchToSubmitTab();
    })
    .catch(err => alert(`An issue occurred with parsing: ${err}`));
}

function resetState(setTraceCode, resetIndex, setFrames) {
  setTraceCode("");
  resetIndex();
  setFrames([]);
}
