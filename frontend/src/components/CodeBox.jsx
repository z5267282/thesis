function CodeBox() {
  const update = (event) => {console.log("hello!")};
  const style = {
    marginTop : "75"
  };
  return (
    <form id="code-upload">
      <textarea
        rows="40" cols="80" name="code-upload" style={style} defaultValue="" onChange={update}
      >
      </textarea>
    </form>
  );
}

export default CodeBox;
