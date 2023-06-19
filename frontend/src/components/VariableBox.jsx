import './style.css';

export default function VariableBox() {
  const style = {
    width: "100%",
    height: "30%",
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  };

  return (
    <div
      style={style}
    >
      <p className="large-text">Variables</p>
      <textarea
        className="side-box"
        value="vars"
        spellCheck={false}
        readOnly={true}
      />
    </div>
  );
};
