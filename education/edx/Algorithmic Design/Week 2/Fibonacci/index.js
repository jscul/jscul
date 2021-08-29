var readline = require('readline');

process.stdin.setEncoding('utf8');
var rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false,
});

var allCases = [[]];
rl.on('line', (cmd) => {
	if (cmd) allCases[allCases.length - 1].push(cmd);
	else allCases.push([]);
});

rl.on('close', () => {
	allCases.forEach((input) => {
		const ret = func(
			...input.map((line) => {
				line = line.split(' ').map((seg) => {
					if (!isNaN(seg)) return BigInt(seg);
					return seg;
				});
				if (line.length === 1) return line[0];
				return line;
			})
		);
		console.log(String(ret));
	});
});

// /**
//  *
//  * @param {*} n
//  * @param {*} nums
//  */
// const fib = ([n]) => {
// 	if (n === 0) return 0;
// 	let follow = BigInt(0),
// 		lead = BigInt(1);
// 	while (i < n) {
// 		const temp = follow;
// 		follow = lead;
// 		lead = lead + temp;
// 	}
// 	return lead;
// };

// /**
//  *

// Example input:
// 10

//  * @param {*} n
//  * @param {*} nums
//  */
// const _func = ([n, m]) => {
// 	if (n === 0) return 0;
// 	let follow = BigInt(0),
// 		lead = BigInt(1);
// 	let i = 1;
// 	while (i < n) {
// 		const temp = follow;
// 		follow = lead;
// 		lead = lead + temp;

// 		// https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/#:~:text=The%20Pisano%20Period%20is%20defined,the%20period%20of%20this%20series.&text=For%20M%20%3D%202%2C%20the%20period,Period%20of%205%20is%2020)
// 		// it's a pisano
// 		if (follow % BigInt(m) === BigInt(0) && lead % BigInt(m) === BigInt(1)) {
// 			const res = n % i;
// 			console.log(res, m);
// 			return func([res, m]);
// 		}
// 		i++;
// 	}
// 	return lead % BigInt(m);
// };

/**
 *

Example input:
10

 * @param {*} n
 * @param {*} nums
 */
const func = ([n, m]) => {
	if (n === BigInt(0)) return 0;
	let follow = BigInt(0),
		lead = BigInt(1);
	let i = 1;
	let followMod = lead % BigInt(m); // kick off
	while (i < n) {
		const temp = follow;
		follow = lead;
		lead = lead + temp;

		// https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/#:~:text=The%20Pisano%20Period%20is%20defined,the%20period%20of%20this%20series.&text=For%20M%20%3D%202%2C%20the%20period,Period%20of%205%20is%2020)
		const leadMod = lead % BigInt(m);
		if (followMod === BigInt(0) && leadMod === BigInt(1)) {
			return func([n % BigInt(i), m]);
		}
		followMod = leadMod;
		i++;
	}
	return lead % BigInt(m);
};
