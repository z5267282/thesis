import './style.css';

export default function VariableBox() {
  const style = {
    width: "20%",
    height: "5%"
  };

  return (
    <textarea
      value="fish"
      spellCheck={false}
      readOnly={true}
      style={style}
    />
  );
};
