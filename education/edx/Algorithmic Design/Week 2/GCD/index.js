var readline = require('readline');

process.stdin.setEncoding('utf8');
var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false,
});

var input = [];
rl.on('line', (cmd) => {
	input.push(cmd);
});

rl.on('close', () => {
	const ret = func(
		...input.map((line) => {
			line = line.split(' ').map((seg) => {
				if (!isNaN(seg)) return +seg;
				return seg;
			});
			if (line.length === 1) return line[0];
			return line;
		})
	);
	console.log(ret);
});

/**
 *

Example input:
10

 * @param {*} n
 * @param {*} nums
 */
const func = (n = [1, 2]) => {
	if (n[0] === 0) return n[1];
	if (n[1] === 0) return n[0];
	return func([n[1] % n[0], n[0]]);
};
