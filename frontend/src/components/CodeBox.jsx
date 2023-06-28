import './style.css';
import React from 'react';

export default function CodeBox() {
  const [showTrace, setShowTrace] = React.useState(42);

  return (
    <div style={{ display : "flex", width : "20%", justifyContent : "space-evenly", marginBottom : 20 }}>
      
      <button onClick={() => {setShowTrace(50)}}>Trace</button>
      <button onClick={() => {setShowTrace(60)}}>Upload</button>

      <div><p>{`showTrace is: ${showTrace}`}</p></div>

      {/* <button onClick={() => {setShowTrace(true)}}>Trace</button>
      <button onClick={() => {setShowTrace(false)}}>Upload</button> */}

      {/* <button onClick={() => {if (!showTrace) setShowTrace(true)}}>Trace</button>
      <button onClick={() => {if (showTrace) setShowTrace(false)}}>Upload</button> */}
    </div>
  );
}

// export default function CodeBox() {
//   const formStyle = {
//     display: "flex",
//     flexDirection: "column",
//     alignItems: "center",
//     width: "65%"
//   };

//   const buttonBoxStyle = {
//     display: "flex",
//     justifyContent: "space-evenly",
//     width: "50%",
//     marginTop: "2%"
//   }

//   const CODE_KEY = "code";
//   // const [showTrace, setShowTrace] = React.useState(true);
//   const [showTrace, setShowTrace] = React.useState(42);
//   console.log(showTrace)

//   React.useEffect(() => {localStorage.removeItem(CODE_KEY)}, []);

//   return (
//     <form
//       id="code-upload"
//       style={formStyle}
//     >
//       <p className="large-text">Code Input</p>
//       <p>{`showTrace is: ${showTrace}`}</p>
//       <div style={{ display : "flex", width : "20%", justifyContent : "space-evenly", marginBottom : 20 }}>
//         <button onClick={() => {setShowTrace(50)}}>Trace</button>
//         <button onClick={() => {setShowTrace(60)}}>Upload</button>

//         {/* <button onClick={() => {setShowTrace(true)}}>Trace</button>
//         <button onClick={() => {setShowTrace(false)}}>Upload</button> */}

//         {/* <button onClick={() => {if (!showTrace) setShowTrace(true)}}>Trace</button>
//         <button onClick={() => {if (showTrace) setShowTrace(false)}}>Upload</button> */}
//       </div>
//       {
//         (showTrace) ?
//           <textarea
//             rows={30} cols={60} name="code-upload" spellCheck={false} disabled
//             value={localStorage.hasOwnProperty(CODE_KEY) ? localStorage.getItem(CODE_KEY) : "[no code]"}
//           />
//         :
//         <textarea
//           defaultValue="enter code here" rows={30} cols={60} name="code-upload" spellCheck={false}
//           onInput={(event) => localStorage.setItem(CODE_KEY, event.target.value)} 
//         />
//       }
//       <div style={buttonBoxStyle}>
//         <button>prev</button>
//         <button>next</button>
//       </div>
//     </form>
//   );
// }
