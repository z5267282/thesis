import { useState } from "react";

import { Button, Dialog, DialogContent, Tab, Tabs, TextField } from "@mui/material";

import EvalBox from "./components/EvalBox";
import OutputBox from "./components/OutputBox";
import TraceBox from "./components/TraceBox"
import UploadBox from "./components/UploadBox"
import VariableBox from "./components/VariableBox";

import { SERVER, TABS } from "./config";

import styles from "./App.module.css";

export default function App() {
  const [selectedTab, setSelectedTab] = useState(TABS.UPLOAD);
  const [showTrace, setShowTrace] = useState(false);
  const [traceCode, setTraceCode] = useState("");
  const [showRestrictions, setShowRestrictions] = useState(false);

  const [index, setIndex] = useState(0);
  const changeIndex = (offset) => {
    const newIndex = index + offset;
    if (newIndex >= 0 && newIndex < frames.length) {
      setIndex(newIndex);
    }
  };
  const resetIndex = () => setIndex(0);
  const [frames, setFrames] = useState([]);
  const { dataFrame, disablePrev, disableNext } = generateData(frames, index);

  const capitalisedTab = { textTransform : "none", fontSize : "14pt" };

  const [zid, setZid] = useState("");
  const [auth, setAuth] = useState(false);
  const [control, setControl] = useState(false);
  const determineControl = (newControl) => {
    setAuth(true);
    setControl(newControl);
  }

  const error = (zid !== "" && zid !== "super" && !/^z[0-9]{7}$/.test(zid));

  if (!auth) {
    return (
      <div className={styles.screen}>
        <div style={{marginBottom : "2.5%"}}>
          Enter your zid
        </div>
        <TextField
          id="zid-input" label="zid" variant="outlined"
          value={zid} onChange={(event) => setZid(event.target.value)}
          error={error} helperText={error ? "enter a z with 7 digits" : ""}
        />
        <Button
          variant="outlined" style={{marginTop : "2.5%"}}
          disabled={zid === "" || error}
          onClick={() => {
            if (zid === "super") {
              determineControl(false);
              return;
            }

            const url = new URL(`${SERVER}/auth`);
            url.searchParams.append("zid", zid);
            fetch(url, {
              method  : "GET",
              headers : { "Content-Type" : "application/json" },
              mode    : "cors",
            })
              .then(res => res.json())
              .then(control => determineControl(control))
              .catch(err => alert(`there was an error during authentication: ${err}`))
          }}
        >
          Submit
        </Button>
      </div>
    );
  }

  if (control) {
    return (
      <div className={styles.screen} style={{fontSize : "14pt"}}>
        <div>
          You are part of the control group and <b>won't</b> have access to the tool.
        </div>
        <div style={{marginTop : "2.5%"}}>
          You are free to use your local computer to run and experiment with the code snippets.
        </div>
      </div>
    );
  }

  return (
    <div className={styles.app}>
      <RestrictionsModal
        open={showRestrictions} closeModal={() => setShowRestrictions(false)}
      />
      <Tabs value={selectedTab} onChange={(_, newTab) => setSelectedTab(newTab)}>
        <Tab sx={capitalisedTab} value={TABS.TRACE} label="Trace" onClick={() => setShowTrace(true)} />
        <Tab sx={capitalisedTab} value={TABS.UPLOAD} label="Upload " onClick={() => setShowTrace(false)} />
      </Tabs>
      {
        (showTrace) ?
          <div className={styles.traceBox}>
            <TraceBox
              code={dataFrame.code} lines={dataFrame.lines}
              path={dataFrame.path} counters={dataFrame.counters} curr={dataFrame.curr}
              index={index} total={frames.length}
              changeIndex={changeIndex} disablePrev={disablePrev} disableNext={disableNext}
              showTrace={showTrace}
            />
            <span className={styles.outputs}>
              <EvalBox evallines={dataFrame.evalbox} />
              <VariableBox variables={dataFrame.vars} />
              <OutputBox index={index} outputs={dataFrame.out} />
            </span>
          </div>
        :
          <UploadBox
            traceCode={traceCode} setTraceCode={setTraceCode} setFrames={setFrames}
            resetIndex={resetIndex} showTraceBox={() => setShowTrace(true)}
            switchToSubmitTab={() => setSelectedTab(TABS.TRACE)}
            openRestrictions={() => setShowRestrictions(true)}
          />
      }
    </div>
  );
}

function RestrictionsModal({open, closeModal}) {
  return <Dialog open={open} onClose={closeModal} fullWidth>
    <DialogContent>
      <ol>
        <li>
          Programs can only consist of the following syntax:
          <ol type="i">
            <li>variable assignments</li>
            <li><code>print</code> statements</li>
            <li>conditionals: <code>if</code>, <code>elif</code>, <code>else</code></li>
            <li><code>while</code> loops</li>
          </ol>
        </li>
        <li>Programs must work and run in under 1 second</li>
        <li>Variables must be one of the following primitive datatypes: <code>str</code>, <code>int</code>, <code>bool</code></li>
      </ol>
    </DialogContent>
  </Dialog>
}

function generateData(frames, index) {
  if (frames.length === 0) {
    return {
      dataFrame   : generateDefaultData(),
      disablePrev : true,
      disableNext : true
    };
  }

  return {
      dataFrame   : frames[index],
      disablePrev : (index === 0),
      disableNext : (index === frames.length - 1)
  }

  function generateDefaultData() {
    return {
      code     : [],
      lines    : [],
      curr     : null,
      vars     : [],
      out      : [],
      path     : null,
      counters : [],
      evalbox  : []
    }
  }
}
