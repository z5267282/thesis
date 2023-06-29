import React from "react";
import styles from "./OutputBox.module.css";

export default function CodeBox() {
  const formStyle = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    width: "65%"
  };

  const buttonBoxStyle = {
    display: "flex",
    justifyContent: "space-evenly",
    width: "50%",
    marginTop: "2%"
  }

  const [showTrace, setShowTrace] = React.useState(false);
  const [traceCode, setTraceCode] = React.useState("");

  return (
    <div style={formStyle}>
      <div style={{ display : "flex", width : "50%", justifyContent : "space-evenly", marginBottom : 20 }}>
        <button type="button" onClick={() => {setShowTrace(true)}}>Trace</button>
        <button type="button" onClick={() => {setShowTrace(false)}}>Upload</button>
      </div>
      <label htmlFor="box" style={{ display : "flex", flexDirection : "column", alignItems : "center" }}>
        <p className={styles.largeText}>
          { (showTrace) ? "Trace execution" : "Upload code" }
        </p>
        {
          (showTrace) ?
            <textarea
              rows={30} cols={60} name="code-upload" spellCheck={false} disabled value={traceCode} id="box"
            />
          :
          <textarea
            rows={30} cols={60} name="code-upload" spellCheck={false} id="box"
            onInput={(event) => setTraceCode(event.target.value)} 
          />
        }
      </label>
      <div style={buttonBoxStyle}>
        <button>prev</button>
        <button>next</button>
      </div>
    </div>
  );
}
