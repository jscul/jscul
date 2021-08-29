const fs = require("fs"),
	request = require("request");

const fsExtra = require("fs-extra");

const DELETE_FILES_IN_DIR = false;

const download = (uri, filename, callback) => {
	request.head({uri, headers: {}}, (err, res, body) => {
		request(uri).pipe(fs.createWriteStream(filename)).on("close", callback);
	});
};

const projects = {
	downloads: ["https://picsum.photos/200/300", "https://picsum.photos/200"],
};

Promise.all(
	...Object.keys(projects).map((name) => {
		if (fs.existsSync(name)) {
			if (DELETE_FILES_IN_DIR) fsExtra.emptyDirSync(name);
		} else {
			fs.mkdirSync(name);
		}
		return projects[name].map((uri, i) => {
			return new Promise((res, rej) => {
				if (uri)
					download(uri.split("?")[0], `${name}/${i}.png`, () => {
						res();
					});
				else res();
			});
		});
	})
);
