const Crypto=require('crypto-js')


function hash(bts,type){
    switch (type){
        case "md5":
            return Crypto.MD5(bts).toString()
            break;
        case "sha1":
            return Crypto.SHA1(bts).toString()
        case "sha256":
            return Crypto.SHA256(bts).toString()
            break;

        default:console.log('失败')
    }

}

function _0x5da728() {
    var _0x5ca058 = data['chars']['length'];
    for (var _0x14ad6b = 0x0; _0x14ad6b< _0x5ca058; _0x14ad6b++) {
        for (var _0x5e5711 = 0x0; _0x5e5711 < _0x5ca058; _0x5e5711++) {
            var _0x2176a8 = ((data['bts'][0]+ data['chars']['substr'](_0x14ad6b, 0x1))+ data['chars']['substr'](_0x5e5711, 0x1))+ data['bts'][1];
            if (hash(_0x2176a8,data['ha'])== data['ct']) {
                return _0x2176a8;
            }
        }
    }
}

data={
    "bts": ["1727341339.702|0|gkW", "lF9A8Cd957ej0jYOpf1MEc%3D"],
    "chars": "GfWtpMQgDyqyXxBkQByAtB",
    "ct": "ba8993970b1425ce1017ca131ef2269911c46758",
    "ha": "sha1",
    "is": true,
    "tn": "__jsl_clearance_s",
    "vt": "3600",
    "wt": "1500"
}

console.log(_0x5da728());
// console.log(hash('123', 'sha256'));