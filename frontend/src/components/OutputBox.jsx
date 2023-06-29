import styles from "./OutputBox.module.css";

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
      <p className="large-text">Output</p>
      <textarea
        value="out"
        className={styles.sideBox}
        spellCheck={false}
        readOnly={true}
      />
    </div>
  );
};
