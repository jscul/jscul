const debounced = (delay, fn) => {
	let timerId;
	return (...args) => {
		if (timerId) {
			clearTimeout(timerId);
		}
		timerId = setTimeout(() => {
			fn(...args);
			timerId = null;
		}, delay);
	};
};

if (typeof require !== 'undefined' && require.main === module) {
	const myHandler = event => {};
	const dHandler = debounced(200, myHandler);
	domNode.addEventListener('input', dHandler);
	console.log('Done');
}

module.exports = {debounced};
