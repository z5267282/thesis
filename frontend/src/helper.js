export function addPixels(dimension) {
  return `${dimension}px`;
}

export function generateDefaultData() {
  return {
    code     : ["[ upload code for execution "],
    lines    : [],
    curr     : null,
    vars     : {},
    out      : [],
    path     : null,
    counters : [],
    evalbox  : []
  }
}

export function generateLoadingData() {
  return {
    dataFrame   : generateDefaultData(),
    disablePrev : true,
    disableNext : true,
  }
}
