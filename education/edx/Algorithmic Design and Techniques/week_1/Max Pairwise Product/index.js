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
	func(
		...input.map((line) => {
			line = line.split(' ').map((seg) => {
				if (!isNaN(seg)) return +seg;
				return seg;
			});
			if (line.length === 1) return line[0];
			return line;
		})
	);
});

/**
 *

Example input:
3
1 2 3

 * @param {*} n
 * @param {*} nums
 */
const func = (n, nums) => {
	let l1 = 0,
		l2 = 1;
	for (let i = 2; i < n; i++) {
		let swap = null;
		if (nums[l1] >= nums[l2]) swap = l2;
		else swap = l1;

		if (nums[i] > nums[swap]) {
			if (swap === l1) l1 = i;
			else l2 = i;
		}
	}
	console.log(nums[l1] * nums[l2]);
};
