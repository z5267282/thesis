const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

import { useState } from "react";

import { Button, ThemeProvider, createTheme } from "@mui/material";
import { grey } from "@mui/material/colors";
import Editor from "react-simple-code-editor";
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism.css';

import { EDITOR_TAB_SPACES, SERVER, TMP_FILES } from "../config";

import styles from "./UploadBox.module.css";

export default function UploadBox({
  traceCode, setTraceCode, setFrames, resetIndex,
  showTraceBox, switchToSubmitTab, openRestrictions 
}) {

  const [disableSubmit, setDisableSubmit] = useState(false);
  const capitalisedButton = {textTransform : "none"};

  const theme = createTheme({
    palette : {
      primary : {
        main : grey[900]
      }
    }
  });

  return (
    <label htmlFor="uploadBox" className={styles.uploadBox}>
      <h1 className={styles.largeText}>Upload code</h1>
      <ThemeProvider theme={theme}>
        <Button
          sx={capitalisedButton} color="primary" onClick={openRestrictions}
        >
          Program Restrictions
        </Button>
      </ThemeProvider>
      <div className={styles.editorBox}>
        <div className={styles.lineNumbers}>
          { traceCode.split("\n").map((_, i) => <span key={`line-${i}`}/>) }
        </div>
        <Editor
          id="uploadBox" value={traceCode} className={styles.editor}
          onValueChange={newTraceCode => setTraceCode(newTraceCode)}
          highlight={code => highlight(code, languages.py)}
          tabSize={EDITOR_TAB_SPACES}
        />
      </div>
      <div className={styles.buttons}>
        <Button
          variant="outlined" disabled={disableSubmit} sx={capitalisedButton}
          onClick={() => handleSubmit(
            traceCode, setFrames, resetIndex, showTraceBox,
            switchToSubmitTab, setDisableSubmit
          )}
        >
          Submit
        </Button>
        <Button
          variant="outlined" sx={capitalisedButton}
          onClick={() => resetState(setTraceCode, resetIndex, setFrames)}
        >
          Reset
        </Button>
      </div>
    </label>
  );
}

function handleSubmit(
  traceCode, setFrames, resetIndex, showTraceBox,
  switchToSubmitTab, setDisableSubmit
) {
  if (traceCode === "") {
    alert("please enter some code");
    return;
  }
  generateDataFrames(
    traceCode, setFrames, resetIndex, showTraceBox,
    switchToSubmitTab, setDisableSubmit
  );
}

function generateDataFrames(
  traceCode, setFrames, resetIndex, showTraceBox,
  switchToSubmitTab, setDisableSubmit
) {
  setDisableSubmit(true);
  const enableSubmit = () => setDisableSubmit(false);
  if (!createFiles(traceCode)) {
    enableSubmit();
    return;
  }

  

  enableSubmit();

  const main = path.join("..", "..", "..", "backend", "src", "main.py")
  const trace = spawn("python3", main);

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
    .catch(err => alert(`An issue occurred with parsing: ${err}`))
    .finally(() => setDisableSubmit(false));
}

/**
 * Create the necessary files in /tmp to run serverless trace.
 * Return whether all files were successfully written.
 * @param {*} program 
 */
function createFiles(program) {
  if (!createTimedFile(program)) return false;
  if (!createRawFile(program)) return false;
  return true;
}

function createTimedFile(program) {
  const contents = `from signal import SIGTERM, signal
import sys
signal(
    SIGTERM, timeout=lambda signum, frame: sys.exit(1)
)
${program}`;
  return writeToTmp(TMP_FILES.timed, contents);
}

function createRawFile(program) {
  return writeToTmp(TMP_FILES.raw, program);
}

/**
 * Given contents, write to a file in /tmp.
 * Return whether the file write succeeded
 * @param {*} fileName in /tmp
 * @param {*} contents of the file
 */
function writeToTmp(fileName, contents) {
  let success = true;
  try {
    const absPath = path.join(path.sep, "tmp", fileName)
    fs.writeFileSync(absPath, contents)
  } catch (err) {
    alert(`an error occurred writing to ${absPath} : ${err}`);
    success = false;
  }
  return success;
}

function resetState(setTraceCode, resetIndex, setFrames) {
  setTraceCode("");
  resetIndex();
  setFrames([]);
}
