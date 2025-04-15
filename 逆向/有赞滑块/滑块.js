const CryptoJS = require('crypto-js')


//传入randomstr 从中提取key和iv

aes = function (t) {
    var e = t.data
        , n = t.key
        , i = t.iv;
    return e = CryptoJS.enc.Utf8.parse(e),
        CryptoJS.AES.encrypt(e, n, {
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Iso10126,
            iv: i
        }).toString()
}
var get_key_iv = function (s,_cx,_cy) {
    var t = {
        cx: _cx,
        cy: _cy,
        scale: 0.5,
        slidingEvents: [
            {
                "mx": 47,
                "my": 181,
                "ts": 1726471634971
            },
            {
                "mx": 0,
                "my": 1,
                "ts": 74
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 4
            },
            {
                "mx": 0,
                "my": 1,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 3
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 1,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 0,
                "my": 1,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 0
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 1,
                "ts": 3
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 0
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 3
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 0,
                "my": 1,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 1
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 3
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 2
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 5
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 3
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 7
            },
            {
                "mx": 0,
                "my": 1,
                "ts": 7
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 9
            }
        ]
    }
    c = s.split("").reverse().join("").split("@")
    return aes({data:JSON.stringify(t),
        key:CryptoJS.enc.Utf8.parse(c[0]),
        iv:CryptoJS.enc.Utf8.parse(c[1])}
    )
}
// rrr=get_key_iv('HbMNrE74N1nPeC9K@e24d5wP4RSkiBoYV',data,cx,cy)
// console.log(rrr)