import { useState } from "react";

import { Button, ThemeProvider, createTheme } from "@mui/material";
import { grey } from "@mui/material/colors";
import Editor from "react-simple-code-editor";
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism.css';

import { EDITOR_TAB_SPACES, SERVER } from "../config";

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
  fetch(`${SERVER}/analyse`, {
    method  : "PUT",
    headers : { "Content-Type" : "application/json" },
    mode    : "cors",
    body    : JSON.stringify(traceCode),
  })
    .then(res =>
      (res.ok) ?
        res.json()
      :
        res.text().then(errorText =>
          Promise.reject(new Error(errorText))
        )
    ).
    then(frames => {
      setFrames(frames);
      resetIndex();
      showTraceBox();
      switchToSubmitTab();
    })
    .catch(err =>
      alert(
        (err instanceof Error) ?
          err.message
        :
          `an error occurred during parsing ${err}`
      )
    )
    .finally(() => setDisableSubmit(false));
}

function resetState(setTraceCode, resetIndex, setFrames) {
  setTraceCode("");
  resetIndex();
  setFrames([]);
}
