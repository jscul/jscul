const fs = require(`fs`);
const crypto = require(`crypto`);

const key = `14189dc35ae35e75ff31d7502e245cd9bc7803838fbfd5c773cdcd79b8a28bbd`;

const encryptFile = () => {
    const input = fs.createReadStream(`./pictures.tar.xz`);
    const output = fs.createWriteStream(`./1.encrypted`);

    const cipher = crypto.createCipher(`aes-256-cbc`, key);
    input.pipe(cipher).pipe(output);

    output.on(`finish`, function () {
        console.log(`🔒`);
    });
};

const decryptFile = () => {
    const input = fs.createReadStream(`./1.encrypted`);
    const output = fs.createWriteStream(`./pictures2.tar.xz`);

    const decipher = crypto.createDecipher(`aes-256-cbc`, key);
    input.pipe(decipher).pipe(output);

    output.on(`finish`, function () {
        console.log(`🔓`);
    });
};

encryptFile();
// decryptFile();
