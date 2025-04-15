const CryptoJS =require('crypto-js')
secret = "0b50b02fd0d73a9c4c8c3a781c30845f"
var data={
    "phone": "17819461984",
    "password": "202cb962ac59075b964b07152d234b70",
    "appid": 16073360
}
function createSign(e) {
    if ("[object Object]" !== Object.prototype.toString.call(e))
        throw new Error("The parameter of query must be a Object.");
    // var t = Math.floor(Date.now() / 1e3);
    var t=1726731245
    Object.assign(e, {
        timestamp: t
    });
    var n = Object.keys(e);
    n.sort();
    for (var r = "", i = 0; i < n.length; i++) {
        var o = n[i];
        r += (0 == i ? "" : "&") + o + "=" + e[o]
    }
    return {
        sign: CryptoJS.MD5(r += secret).toString(),
        timestamp: t,
        md5: CryptoJS.MD5
    }
}

console.log(createSign(data));
