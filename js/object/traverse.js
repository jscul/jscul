/**
 * Goes through every property of objects and indices of
 * arrays and calls callback with `(obj, key)` as parameters where
 * `obj` refers to the new object being constructed to be returned. If
 * `callback` alters `obj[key]` then that will be reflected in the
 * return object. If `obj[key]` is set to null, `obj[key]` will not be
 * traversed. The return from the callback doesn't matter unless it's
 * a `Promise`. If a `Promise` is returned then the function becomes
 * asynchronous and returns a `Promise`.
 * @param {Object} obj The object to be parsed
 * @param {Function | Object<Functions>} callback The function to be called on each value.
 * @returns {{tempObj: Array<*>, tempObj: Object<*>}} The tempObjurn object contains flat property changes in an array and tempObj, a deep clone of the original object.
 *
 * @example
 * const test = {
 *     key: 'value',
 *     arr: ['value', [{key: 'value'}]],
 *     json: {json2: {key: ['value']}}
 * }
 *
 * const tempObj = traverse(test, (obj, key) => {
 *     obj[key] = `new ${obj[key]}`
 *     return `${key} changed`
 * });
 *
 * console.log(JSON.stringify(tempObj));
 * console.log(JSON.stringify(test));
 */
const traverse = async (toParse, callback) => {
	const promiseWait = [];
	const obj = privateTraverse(toParse, callback, promiseWait);
	if (promiseWait.length === 0) return obj;
	else return Promise.all(promiseWait).then(() => obj);
};

const privateTraverse = async (toParse, callback, promiseWait) => {
	let tempObj = null;
	if (
		typeof toParse === 'object' &&
		toParse !== null &&
		!Array.isArray(toParse)
	) {
		tempObj = {};
		for (let k in toParse) {
			tempObj[k] = null;
			const result = callback(toParse[k]);
			if (result instanceof Promise) {
				promiseWait.push(result);
				result.then(val => {
					tempObj[k] = privateTraverse(val, callback, promiseWait);
				});
			} else {
				tempObj[k] = privateTraverse(result, callback, promiseWait);
			}
		}
	} else if (Array.isArray(toParse)) {
		tempObj = [];
		for (let i = 0; i < toParse.length; i++) {
			tempObj.push(null);
			const result = callback(toParse[i]);
			if (result instanceof Promise) {
				promiseWait.push(result);
				result.then(val => {
					tempObj[i] = privateTraverse(val, callback, promiseWait);
				});
			} else {
				tempObj[i] = privateTraverse(result, callback, promiseWait);
			}
		}
	} else {
		return toParse;
	}
	return tempObj;
};
// EXAMPLE
if (typeof require != 'undefined' && require.main == module) {
	const test = {
		key: 'value',
		arr: ['value', [{key: 'value'}]],
		json: {json2: {key: ['value']}}
	};

	traverse(test, val => {
		return val;
	}).then(obj => {
		console.log(JSON.stringify(obj, null, ' '));
	});
}

function deepClone(obj) {
	const clone = {};
	for (let i in obj) {
		if (obj[i] !== null && typeof obj[i] === 'object') {
			clone[i] = deepClone(obj[i]);
		} else {
			clone[i] = obj[i];
		}
	}
	return clone;
}

module.exports = {
	traverse,
	deepClone
};
