const cryptoJS=require('crypto-js')
cnonce =function () { var e =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];
                        function t(t) {
                            var n = "";
                            return n += e[t >>> 28 & 15],
                            n += e[t >>> 24 & 15],
                            n += e[t >>> 20 & 15],
                            n += e[t >>> 16 & 15],
                            n += e[t >>> 12 & 15],
                            n += e[t >>> 8 & 15],
                            n += e[t >>> 4 & 15],
                            n += e[t >>> 0 & 15],
                            n
                        }
                        return t(Math.floor(Math.random() * Math.pow(2, 32))) + t(Math.floor(Math.random() * Math.pow(2, 32)))
                    }

function get_enc(ss){
    i = cnonce()
s= ss
DLZH = '17896686831'
r = cryptoJS.SHA256('20030531lkyA').toString().toUpperCase()
DLMM = cryptoJS.SHA256(s + r + i).toString().toUpperCase()
return [DLMM,i]
}
var key = cryptoJS.enc.Hex.parse("362430485f3370342435313538394f25304b644f3f313233362e2a3f38392440");
var iv = cryptoJS.enc.Hex.parse("36303132373835393031303636363738");

function get_result(res){
     var decrypt = cryptoJS.AES.decrypt(res, key, {
        iv: iv,
        mode: cryptoJS.mode.CBC,
        padding: cryptoJS.pad.Pkcs7
    });
    return decrypt.toString(cryptoJS.enc.Utf8);
}

function get_sqlp(sqlp){
    i = sqlp + "_2Cqooc&#(*@&(" + n
    return cryptoJS.MD5(i).toString()
}

