class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
		this.prev = null;
	}
}

class DoublyLinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
		this.length = 0;
	}

	push(val) {
		const node = new Node(val);
		if (this.length === 0) {
			this.head = node;
			this.tail = node;
			this.length++;
		} else {
			this.tail.next = node;
			node.prev = this.tail;
			this.tail = node;
			this.length++;
		}
		return this;
	}

	pop() {
		const tail = this.tail;
		if (!tail) return undefined;
		if (tail.prev) {
			tail.prev.next = null;
			this.tail = tail.prev;
		} else {
			this.tail = null;
		}
		this.length--;
		return tail;
	}

	unshift(val) {
		if (this.length === 0) return this.push(val);
		const node = new Node(val);
		node.next = this.head;
		this.head.prev = node;
		this.head = node;
		if (!this.tail.prev) this.tail.prev = this.head;
		this.length++;
		return this;
	}

	shift() {
		const node = this.head;
		if (!node) return undefined;
		node.prev = null;
		this.head = node.next;
		if (this.head) this.head.prev = null;
		else this.tail = null;
		this.length--;
		return node;
	}

	get(i) {
		if (this.length === 0 || i < 0 || i >= this.length) return null;
		let node = this.head;
		let j = 0;
		while (j < i) {
			node = node.next;
			j++;
		}
		return node;
	}

	set(i, val) {
		const node = this.get(i);
		if (!node) return false;
		node.val = val;
		return true;
	}

	insert(i, val) {
		if (this.length === 0 || i === this.length) {
			this.push(val);
			return true;
		} else if (i === 0) {
			this.unshift(val);
			return true;
		}

		const left = this.get(i - 1);
		if (!left) return false;

		const node = new Node(val);
		const right = left.next;

		left.next = node;
		node.prev = left;
		right.prev = node;
		node.next = right;

		this.length++;
		return true;
	}

	remove(i) {
		const node = this.get(i);
		if (!node) return undefined;
		if (node.prev) {
			if (!node.next) this.tail = node.prev;
			node.prev.next = node.next;
			if (node.next) node.next.prev = node.prev;
		} else {
			this.head = node.next;
			if (this.head) this.head.prev = null;
		}
		this.length--;
		return node;
	}

	reverse() {
		if (this.length === 0 || this.length === 1) return this;

		const oldHead = this.head;
		const oldTail = this.tail;

		let node = oldHead;
		let prev = null;

		while (node) {
			let temp = node.next;
			node.next = prev;
			node.prev = temp;
			prev = node;
			node = temp;
		}

		this.tail = oldHead;
		this.head = oldTail;
		return this;
	}

	toArray() {
		const ret = [];
		let node = this.head;
		while (node) {
			ret.push(node.val);
			node = node.next;
		}
		return ret;
	}

	toString() {
		return `${this.toArray().join('->')} length=${this.length}`;
	}
}
