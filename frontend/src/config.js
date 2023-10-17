// in px
export const LINE_HEIGHT = 25;
// as a ratio of line height above
export const FONT_SCALING_FACTOR = 0.8;

export const TABS = { TRACE : "trace", UPLOAD : "upload" };

export const TRACE_GRAPH_WIDTH = 50;

export const EDITOR_TAB_SPACES = 4;

export const COUNTER_COLOURS = ["#649FFF", "#317FFF"]

export const TMP_FILES = { timed : "timed.py" };

const setServer = () => {
  return process.env.REACT_APP_HOST === "REMOTE" ?
    "https://z5267282.pythonanywhere.com"
  :
    "http://127.0.0.1:5000";
};
export const SERVER = setServer();
