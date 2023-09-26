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
  ARROW_WIDTH,
  ARROW_HEIGHT,
  ARROW_HEAD_LENGTH,
  COUNTER_COLOURS,
  FONT_SCALING_FACTOR,
  LINE_HEIGHT,
  TRACE_GRAPH_WIDTH
} from "./config";

export default function App() {
  const [selectedTab, setSelectedTab] = React.useState("upload");
  const changeTab = (_, newTab) => setSelectedTab(newTab);
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

  return (
    <div className={styles.App}>
      <Tabs value={selectedTab} onChange={changeTab} style={{backgroundColor : "red"}}>
        <Tab value="trace" label="Trace" onClick={() => {setShowTrace(true)}} />
        <Tab value="upload" label="Upload " onClick={() => {setShowTrace(false)}} />
      </Tabs>
      <div className={styles.main}>
        {
          (showTrace) ?
            <TraceBox
              code={dataFrame.code} lines={dataFrame.lines} path={dataFrame.path} counters={dataFrame.counters} curr={dataFrame.curr} counterColours={COUNTER_COLOURS}
              lineHeight={LINE_HEIGHT} fontScaling={FONT_SCALING_FACTOR} graphWidth={TRACE_GRAPH_WIDTH}
              changeIndex={changeIndex} disablePrev={disablePrev} disableNext={disableNext}
            />
          :
            <UploadBox
              traceCode={traceCode} setTraceCode={setTraceCode} setFrames={setFrames}
              resetIndex={resetIndex} showTraceBox={() => setShowTrace(true)}
            />
        }
        {
          showTrace && (
            <div className={styles.outputs}>
              {dataFrame.evalbox.length > 0 && (
                <EvalBox evallines={dataFrame.evalbox} />
              )}
              <VariableBox variables={dataFrame.vars} />
              <OutputBox
                width={ARROW_WIDTH}
                height={ARROW_HEIGHT}
                headLength={ARROW_HEAD_LENGTH}
                outputs={dataFrame.out}
              />
            </div>
          )
        }
      </div>
    </div>
  );
}
