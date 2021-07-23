const Heap = require('./Heap');

class Graph {
	constructor() {
		this.map = new Map();
	}

	addVertex(v) {
		this.map.set(v, new Map());
	}

	removeVertex(v) {
		for (const adjacent of this.map[v]) this.removeEdge(adjacent, v);
		this.map.delete(v);
	}

	addEdge(v1, v2, properties = {}) {
		this.map.get(v1).set(v2, properties);
		this.map.get(v2).set(v1, properties);
	}

	removeEdge(v1, v2) {
		this.map.get(v1).delete(v2);
		this.map.get(v2).delete(v1);
	}

	*[Symbol.iterator]() {
		yield* this.dfs();
	}

	*dfs(v = '123') {
		let stack = [v];
		let seen = new Set();

		while (stack.length) {
			const v = stack.pop();
			seen.add(v);
			for (const [vertex, adjacencies] of this.map.get(v)) {
				if (!seen.has(vertex)) stack.push(vertex);
			}
			yield v;
		}
	}

	*bfs(v = '123') {
		let stack = [v];
		let seen = new Set();

		while (stack.length) {
			const v = stack.shift();
			seen.add(v);
			for (const [vertex, adjacencies] of this.map.get(v)) {
				if (!seen.has(vertex)) stack.push(vertex);
			}
			yield v;
		}
	}

	*dijkstra(start, finish) {
		let stack = [v];
		let seen = new Set();

		while (stack.length) {
			const v = stack.shift();
			seen.add(v);
			for (const [vertex, adjacencies] of this.map.get(v)) {
				if (!seen.has(vertex)) stack.push(vertex);
			}
			yield v;
		}
	}
}

(async () => {
	const g = new Graph();
	g.addVertex('123');
	g.addVertex('124');
	g.addVertex('125');
	const test = {name: `126`};
	g.addVertex(test);
	g.addEdge('123', '124', {w: 4});
	g.addEdge('125', '124');
	g.addEdge('125', test);

	console.log(g);

	for (const v of g) {
		await new Promise((res, rej) => {
			setTimeout(res, 1000);
		});
		console.log(v);
	}
})();

module.exports = Graph;
