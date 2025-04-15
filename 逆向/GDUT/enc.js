const CryptoJS=require('crypto-js')

function randomString(n) {
    var f = "";
    for (i = 0; i < n; i++)
        f += 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'.charAt(Math.floor(Math.random() * 48));
    return f
}
function getAesString(n, f, c) {
    f = f.replace(/(^\s+)|(\s+$)/g, "");
    f = CryptoJS.enc.Utf8.parse(f);
    c = CryptoJS.enc.Utf8.parse(c);
    return CryptoJS.AES.encrypt(n, f, {
        iv: c,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
}

function enc_pass(pass,salt){
     return getAesString(randomString(64) + pass, salt, randomString(16))
}

// console.log(enc_pass('123', '333'));