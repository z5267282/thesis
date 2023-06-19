import './style.css';

export default function CodeBox() {
  const formStyle = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  };

  const headerStyle = {
    fontSize: "16pt"
  };

  const update = (event) => {console.log(event.target.value)};

  const buttonBoxStyle = {
    display: "flex",
    justifyContent: "space-evenly",
    width: "20%",
    marginTop: "2%"
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
        defaultValue=""
        onChange={update}
        spellCheck={false}
        autoFocus={false}
      />
      <div style={buttonBoxStyle}>
        <button>prev</button>
        <button>next</button>
      </div>
    </form>
  );
}
