var inOrderTraversal = function (root) {
  const s = [];
  let c = root;
  while (true) {
    if (c) {
      s.push(c);
      c = c.left;
    } else {
      if (!s.length) break;
      c = s.pop();
      console.log(c.val);
      c = c.right;
    }
  }
};
