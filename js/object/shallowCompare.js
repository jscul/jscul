const shallowCompare = (a, b) =>  {
	for (let key in a) if (!(key in b) || a[key] !== b[key]) return false;
	for (let key in b) if (!(key in a)) return false;
	return true;
}
