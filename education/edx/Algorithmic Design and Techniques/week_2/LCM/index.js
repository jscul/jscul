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
	console.log(String(ret));
});

const gcd = (n = [1, 2]) => {
	if (n[0] === 0) return n[1];
	if (n[1] === 0) return n[0];
	return gcd([n[1] % n[0], n[0]]);
};

const func = (n = [1, 2]) => {
	const d = gcd(n);
	return (BigInt(n[0]) * BigInt(n[1])) / BigInt(d);
};