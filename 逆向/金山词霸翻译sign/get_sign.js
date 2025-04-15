const CryptoJS=require('crypto-js');
var t={
    "from": "en",
    "to": "zh",
    "q": "dog"
};
function getsign(t) {
    var r = CryptoJS.MD5("6key_web_new_fanyi".concat('6dVjYLFyzfkFkk').concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);
    return r = enc(r)
}
s = function(e) {
    e = decodeURIComponent(e);
    for (var t = String.fromCharCode(e.charCodeAt(0) - e.length), r = 1; r < e.length; r++)
        t += String.fromCharCode(e.charCodeAt(r) - t.charCodeAt(r - 1));
    return t
};
enc=function (e) {
    var t = "%5C%C2%80%C2%9A%C2%A8%C2%B6%C2%B8y%C2%9B%C2%B2%C2%8F%7C%7F%C2%97%C3%88%C2%A9d"
        , r = CryptoJS.enc.Utf8.parse(s(t))
        , o = CryptoJS.AES.encrypt(e, r, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return o.toString()
}
dec= function (e) {
    var t = "aahc3TfyfCEmER33"
        , r = CryptoJS.enc.Utf8.parse(t)
        , o = CryptoJS.AES.decrypt(e, r, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return o.toString(CryptoJS.enc.Utf8)
}
console.log(getsign(t))