const CryptoJS=require('crypto-js')
function i(t) {
            if (null === t)
                return !0;
            if ("boolean" === typeof t)
                return !1;
            if ("number" === typeof t)
                return !t;
            if (t instanceof Error)
                return "" === t.message;
            switch (Object.prototype.toString.call(t)) {
            case "[object String]":
            case "[object Array]":
                return !t.length;
            case "[object File]":
            case "[object Map]":
            case "[object Set]":
                return !t.size;
            case "[object Object]":
                return !Object.keys(t).length
            }
            return !1
        }
function get_enc(password,orderinfo){
     var a = orderinfo
              , s ="chinapnr"
              , n = CryptoJS.mode.CBC
              , o = CryptoJS.pad.Pkcs7;
            if (i(password))
                return "";
            if (i(a))
                return "";
            var f, r = CryptoJS.enc.Utf8.parse(a), l = {
                mode: n,
                padding: o
            };
            i(s) || (f =CryptoJS.enc.Utf8.parse(s),
            Object.assign(l, {
                iv: f
            }));
            var c = CryptoJS.TripleDES.encrypt(password, r, l)
    p = CryptoJS.enc.Base64.stringify(c.ciphertext)
    return p
}
aaas=get_enc('698698','hfpwallet6666000137842973pay9b42bb10-a124-4863-9f00-f16647feb7e8')
console.log(aaas)