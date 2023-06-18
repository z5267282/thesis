export default function CodeBox() {
  const formStyle = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  };

  const headerStyle = {
    fontSize: "16pt"
  };

  const textStyle = {
    resize: "none",
    padding: "1%",
    fontSize: "12pt",
    border: "solid",
    borderWidth: "1.5pt",
    borderRadius: "1%"
  };
  const update = (event) => {console.log(event.target.value)};

  const buttonBoxStyle = {
    display: "flex",
    justifyContent: "space-evenly",
    width: "20%",
    marginTop: "2%"
  }

  const buttonStyle = {
    fontSize: "14pt",
    border: "solid",
    borderWidth: "1.5pt",
    borderRadius: "5pt",
  }

  return (
    <form
      id="code-upload"
      style={formStyle}
    >
      <p style={headerStyle}>Code Input</p>
      <textarea
        rows={30}
        cols={60}
        name="code-upload"
        style={textStyle}
        defaultValue=""
        onChange={update}
        spellCheck={false}
        autoFocus={false}
      />
      <div style={buttonBoxStyle}>
        <button style={buttonStyle}>prev</button>
        <button style={buttonStyle}>next</button>
      </div>
    </form>
  );
}
