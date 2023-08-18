export function addPixels(dimension) {
  return `${dimension}px`;
}

export function generateDefaultData() {
  return {
    code     : ["[ upload code for execution "],
    lines    : [],
    curr     : null,
    vars     : [],
    out      : [],
    path     : null,
    counters : [],
    evalbox  : []
  }
}

export function generateData(frames, index) {
  if (frames.length === 0) {
    return {
      dataFrame   : generateDefaultData(),
      disablePrev : true,
      disableNext : true
    };
  }

  return {
      dataFrame   : frames[index],
      disablePrev : (index === 0),
      disableNext : (index === frames.length - 1)
  }
}
