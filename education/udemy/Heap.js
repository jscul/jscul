class Heap {
	constructor(comparator = (p, c) => p - c) {
		this.values = [];
		this.comparator = comparator;
	}

	push(val) {
		this.values.push(val);
		if (this.values.length > 1) this.bubbleUp();
		return this.values.length;
	}

	pop() {
		if (!this.values.length) return null;
		let bottom = this.values.pop();
		if (!this.values.length) return bottom;
		const top = this.values[0];
		this.values[0] = bottom;
		this.bubbleDown();
		return top;
	}

	bubbleDown() {
		let i = 0;
		const l = this.values.length,
			values = this.values;

		while (i < l) {
			const c1 = i * 2 + 1,
				c2 = i * 2 + 2;

			let swap = null;

			if (c1 >= l && c2 >= l) break;
			else if (c1 >= l) swap = c2;
			else if (c2 >= l) swap = c1;
			else if (this.comparator(values[c1], values[c2]) > 0) swap = c1;
			else swap = c2;

			if (swap && this.comparator(values[swap], values[i]) > 0) {
				const temp = values[swap];
				values[swap] = values[i];
				values[i] = temp;
				i = swap;
			} else {
				break;
			}
		}
	}

	bubbleUp() {
		let c = this.values.length - 1;
		while (c > 0) {
			const p = Math.floor((c - 1) / 2);
			if (this.comparator(this.values[p], this.values[c]) > 0) break;
			const temp = this.values[p];
			this.values[p] = this.values[c];
			this.values[c] = temp;
			c = p;
		}
	}

	toString() {
		return this.values.join(',');
	}
}

// let h = new Heap((a, b) => b - a);
// h.push(1);
// h.push(2);
// h.push(3);
// h.push(3);
// h.push(6);
// console.log(`${h}`);
// console.log(h.pop());
// console.log(`${h}`);
// console.log(h.pop());
// console.log(`${h}`);
// console.log(h.pop());
// console.log(`${h}`);
// console.log(h.pop());
// console.log(`${h}`);
// console.log(h.pop());
// console.log(`${h}`);
// console.log(h.pop());

module.exports = Heap;
