// in px
export const LINE_HEIGHT = 25;
// as a ratio of line height above
export const FONT_SCALING_FACTOR = 0.8;

export const TRACE_GRAPH_WIDTH = 50;

// arrow related
export const ARROW_WIDTH = 30;
export const ARROW_HEIGHT = 100;
export const ARROW_HEAD_LENGTH = 10;

// export const COUNTER_COLOURS = ["lime", "aqua"];
export const COUNTER_COLOURS = ["blue", "green"];

const setServer = () => {
    return (process.env.REACT_APP_THESIS_HOST === "REMOTE") ?
        "https://z5267282.pythonanywhere.com/"
    :
        "http://127.0.0.1:5000";
}
export const SERVER = setServer();
