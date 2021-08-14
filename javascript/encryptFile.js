const fs = require(`fs`);
const crypto = require(`crypto`);

const KEY = Buffer.from(
	`NVcSrW0L/qZ9TxllNAB4BAS53XqliRLRw6OQB6GjUeI=`,
	"base64"
);

let key = crypto.createHash("sha256").update(String(`secret`));

const encryptFile = () => {
	const iv = crypto.randomBytes(16);
	const input = fs.createReadStream(`./in.zip`);
	const output = fs.createWriteStream(`./${iv.toString("hex")}.encrypted`);

	const cipher = crypto.createCipheriv(`aes-256-cbc`, KEY, iv);
	input.pipe(cipher).pipe(output);

	output.on(`finish`, function () {
		console.log(`🔒`);
	});
};

const decryptFile = (fileName) => {
	const path = fileName.split("/");
	const [iv, ext] = path[path.length - 1].split(".");
	const input = fs.createReadStream(fileName);
	const output = fs.createWriteStream(`./out.zip`);

	const decipher = crypto.createDecipheriv(
		`aes-256-cbc`,
		KEY,
		Buffer.from(iv, "hex")
	);
	input.pipe(decipher).pipe(output);

	output.on(`finish`, function () {
		console.log(`🔓`);
	});
};

// encryptFile();
decryptFile(`b6583778c28fcff7a3f962564ce6a516.encrypted`);
