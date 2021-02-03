// ES6 code
const throttled = (delay, fn) => {
  let lastCall = 0;
  return function (...args) {
    const now = new Date().getTime();
    if (now - lastCall < delay) {
      return;
    }
    lastCall = now;
    return fn(...args);
  };
};

if (typeof require !== 'undefined' && require.main === module) {
  const myHandler = event => {};
  const tHandler = throttled(200, myHandler);
  domNode.addEventListener('mousemove', tHandler);
  console.log('Done');
}

module.exports = {throttled};
