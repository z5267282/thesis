import { useState } from "react";

import { Box, Button, Modal, ThemeProvider, createTheme } from "@mui/material";
import { grey } from "@mui/material/colors";
import Editor from "react-simple-code-editor";
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism.css';

import { EDITOR_TAB_SPACES, SERVER } from "../config";

import styles from "./UploadBox.module.css";

export default function UploadBox({
  traceCode, setTraceCode, setFrames, resetIndex, showTraceBox, switchToSubmitTab
}) {
  const [showRestrictions, setShowRestrictions] = useState(false);

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
    <label htmlFor="uploadBox" className={styles.container}>
      <h1 className={styles.largeText}>Upload code</h1>
      <ThemeProvider theme={theme}>
        <Button
          sx={capitalisedButton} color="primary" onClick={() => setShowRestrictions(true)}
        >
          Program Restrictions
        </Button>
      </ThemeProvider>
      <RestrictionsModal
        open={showRestrictions} closeModal={() => setShowRestrictions(false)}
      />
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

function RestrictionsModal({open, closeModal}) {
  return <Modal className={styles.restrictions} open={open} onClose={closeModal}>
    <Box>
      <ol>
        <li>The only permitted syntax are <code>print</code> statements, conditions</li>
      </ol>
    </Box>
  </Modal>
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

function resetState(setTraceCode, resetIndex, setFrames) {
  setTraceCode("");
  resetIndex();
  setFrames([]);
}
