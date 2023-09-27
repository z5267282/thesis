import React from "react";

import { Tab, Tabs } from "@mui/material";

import EvalBox from "./components/EvalBox";
import OutputBox from "./components/OutputBox";
import TraceBox from "./components/TraceBox"
import UploadBox from "./components/UploadBox"
import VariableBox from "./components/VariableBox";

import { generateData } from "./helper";

import styles from "./App.module.css";

import {
  COUNTER_COLOURS,
  FONT_SCALING_FACTOR,
  LINE_HEIGHT,
  TABS,
  TRACE_GRAPH_WIDTH
} from "./config";

export default function App() {
  const [selectedTab, setSelectedTab] = React.useState(TABS.UPLOAD);
  const [showTrace, setShowTrace] = React.useState(false);
  const [traceCode, setTraceCode] = React.useState("");

  const [index, setIndex] = React.useState(0);
  const changeIndex = (offset) => {
    const newIndex = index + offset;
    if (newIndex >= 0 && newIndex < frames.length) {
      setIndex(newIndex);
    }
  };
  const resetIndex = () => setIndex(0);
  const [frames, setFrames] = React.useState([]);
  const { dataFrame, disablePrev, disableNext } = generateData(frames, index);

  const capitalisedTab = {textTransform : "none", fontSize : "14pt"};

  return (
    <div className={styles.app}>
      <Tabs value={selectedTab} onChange={(_, newTab) => setSelectedTab(newTab)}>
        <Tab sx={capitalisedTab} value={TABS.TRACE} label="Trace" onClick={() => setShowTrace(true)} />
        <Tab sx={capitalisedTab} value={TABS.UPLOAD} label="Upload " onClick={() => setShowTrace(false)} />
      </Tabs>
      {
        (showTrace) ?
          <div className={styles.traceBox}>
            <TraceBox
              code={dataFrame.code} lines={dataFrame.lines} path={dataFrame.path} counters={dataFrame.counters} curr={dataFrame.curr} counterColours={COUNTER_COLOURS}
              lineHeight={LINE_HEIGHT} fontScaling={FONT_SCALING_FACTOR} graphWidth={TRACE_GRAPH_WIDTH}
              changeIndex={changeIndex} disablePrev={disablePrev} disableNext={disableNext}
            />
            <span className={styles.outputs}>
              {dataFrame.evalbox.length > 0 && (
                <EvalBox evallines={dataFrame.evalbox} />
              )}
              <VariableBox variables={dataFrame.vars} />
              <OutputBox index={index} outputs={dataFrame.out} />
            </span>
          </div>
        :
          <UploadBox
            traceCode={traceCode} setTraceCode={setTraceCode} setFrames={setFrames}
            resetIndex={resetIndex} showTraceBox={() => setShowTrace(true)}
            switchToSubmitTab={() => setSelectedTab(TABS.UPLOAD)}
          />
      }
    </div>
  );
}
