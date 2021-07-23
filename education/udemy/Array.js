let arr = []; // O(1) array

arr = new Array(1); // O(1) array w/ length 1

arr[1] = 0; // O(1) array length changes

arr.push(0); // O(1) add to end
let v = arr.pop(); // O(1) retrieve from end

arr.unshift(0); // O(N) add to start
v = arr.shift(); // O(N) retrieve from start
