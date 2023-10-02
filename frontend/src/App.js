import { useEffect, useRef, useState } from "react";

import { Dialog, Tab, Tabs } from "@mui/material";

import EvalBox from "./components/EvalBox";
import TextBox from "./components/TextBox";
import TraceBox from "./components/TraceBox"
import UploadBox from "./components/UploadBox"

import { TABS } from "./config";

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

  const capitalisedTab = {textTransform : "none", fontSize : "14pt"};

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
              changeIndex={changeIndex} disablePrev={disablePrev} disableNext={disableNext}
            />
            <span className={styles.outputs}>
              {
                dataFrame.evalbox.length > 0 && 
                  <EvalBox evallines={dataFrame.evalbox} />
              }
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
  // className not working
  const style = {
    border: "solid",
    borderWidth: "2px",
  };

  return <Dialog open={open} onClose={closeModal} sx={style}>
    <div style={{width : "50%", height : "50%", backgroundColor : "red"}}>
      <ol>
        <li>The only permitted syntax are <code>print</code> statements, conditions</li>
      </ol>
    </div>
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

function VariableBox({variables}) {
  return <TextBox header={"Variables"} text={variables.join("\n")} />;
}

function OutputBox({index, outputs}) {
  const textAreaRef = useRef();
  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.scrollTop = textAreaRef.current.scrollHeight;
    }
  }, [index]);

  return <TextBox
    header={"Output"} text={outputs.join("")} textAreaRef={textAreaRef}
  />
}
