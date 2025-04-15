//
// e='{"id":"6bedfbbb-661b-40aa-ba9e-a5b3067c607e","c":1727204630720,"s":0,"r":0,"sb":0,"sr":0,"se":0,"fs":0,"sp":0}'    //_hjSession_3143029
// e1='{"id":"e136b27f-0ff2-4cac-be17-0fc1963d77d1","c":1727203948442,"s":0,"r":0,"sb":0,"sr":0,"se":0,"fs":0,"sp":0}'
// e2='{"id":"d8b77e99-2446-5441-a0eb-7c3b9b292ecc","created":1727204471339,"existing":false}'   //_hjSessionUser_3143029
//
// e3='{"id":"6bedfbbb-661b-40aa-ba9e-a5b3067c607e","c":1727204630720,"s":0,"r":0,"sb":0,"sr":0,"se":0,"fs":1,"sp":0}'
// var a=(0,btoa)(e3)
// var b=(0,btoa)(e2)
// _hjSessionUser_3143029=eyJpZCI6Ijc2YmJlN2M0LTkyYmQtNTk4NC1hZDljLTBkMWE0YzE0ODQ2NSIsImNyZWF0ZWQiOjE3MjcyMDMzODQ0MzgsImV4aXN0aW5nIjpmYWxzZX0=
// console.log(a)
// console.log(b)

// hjSession_3143029=eyJpZCI6IjY5YzI3ZTY5LWM3MTAtNDQ5Yi05NmZmLWNlOTk2ZTI4YTU5MiIsImMiOjE3MjcyMDI5NDY2NzYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowfQ==
function g() {
    f = new Uint8Array(16)
    console.log(f)
    if (!Math.random() && !(Math.random = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto)))
        throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported");
    return Math.random(f)
}

var p = function(e, t, n) {
    var r = (e = e || {}).random || (e.rng || g)();
    if (r[6] = 15 & r[6] | 64,
        r[8] = 63 & r[8] | 128,
        t) {
        n = n || 0;
        for (var o = 0; o < 16; ++o)
            t[n + o] = r[o];
        return t
    }

    return s(r)
}

function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var random = Math.random() * 16 | 0;
        var value = (c === 'x' ? random : (random & 0x3 | 0x8));
        return value.toString(16);
    });
}


timetime=Date['now']()
uuid=generateUUID()
function  get_hjSession_(uuid,timestr){
    var ret=(0,btoa)('{"id":"'+uuid+'","c":'+timestr+',"s":0,"r":0,"sb":0,"sr":0,"se":0,"fs":0,"sp":0}')
    return ret
}function  get_hjSessionUser_(uuid,timestr){
    var ret=(0,btoa)('{"id":"'+uuid+'","created":'+timestr+',"existing":false}')
    return ret
}

console.log(get_hjSession_(uuid, timetime));
console.log(get_hjSessionUser_(uuid, timetime));