var proxyConfig = {
    isLog : false,
    enable : false
}


function getEnvs(proxyObjs) {
    if(!proxyConfig.enable) return;
    for (let i = 0; i < proxyObjs.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        if(${proxyConfig.isLog})
            console.log("方法:", "get  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        
        return target[property];
      },
      set: function(target, property, value, receiver) {
        if(${proxyConfig.isLog})
            console.log("方法:", "set  ", "对象:", "${proxyObjs[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
        return Reflect.set(...arguments);
      }
    }`;
        eval(`try {
            ${proxyObjs[i]};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        } catch (e) {
            ${proxyObjs[i]} = {};
            ${proxyObjs[i]} = new Proxy(${proxyObjs[i]}, ${handler});
        }`);
    }
}
function getEnv(proxyObj,desc){
    if(!proxyConfig.enable) return proxyObj;
    const handler = {
        get: function(target, property, receiver) {
            if(proxyConfig.isLog)
                console.log("方法:", "get  ", "对象:", desc, "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
            return target[property];
        },
        set: function(target, property, value, receiver) {
            if(proxyConfig.isLog)
                console.log("方法:", "set  ", "对象:", desc, "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
            return Reflect.set(...arguments);
        }
    };
    try {
        proxyObj;
        proxyObj = new Proxy(proxyObj, handler);
    } catch (e) {
        proxyObj = {};
        proxyObj = new Proxy(proxyObj, handler);
    }finally{
        return proxyObj;
    }
}
window = global = {};
//atob btoa
window.RSA_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDnOWe/gs033L/2/xR3oi6SLAMPBY5VledUqqH6dbCNOdrGX4xW+1x6NUfvmwpHRBA2C7xWDDvOIldTl0rMtERTDy9homrVqEcW6/TY+dSVFL3e2Yg2sVaehHv7FhmATkgfC2FcXt8Wvm99QpKRSrGKpcFYJwOj2F8hJh+rTG0IPQIDAQAB-----END PUBLIC KEY-----"
window.atob = atob, window.btoa = btoa;
document={
    createTextNode:function(x){return getEnv({},'document.createTextNode')},
    compatMode:"CSS1Compat",
    characterSet:'UTF-8',
    images:getEnv([],"document.images"),
    all:getEnv({
        __proto__ : getEnv({},"document.all.__proto__")
    },"document.all"),
    createElement:function(arg1){
        //console.log("调用方法： createElement ","对象： document","arg1 ",arg1)
        if(arg1 === 'span'){
            return {
                classList : getEnv({},"document.createElement.span.classList")
            }
        }
        if(arg1 === 'canvas'){
            return {
                toDataURL: toDataURL()
            }
        }
        if(arg1 === 'style'){
            return {
                setAttribute:function(){

                }
            }
        }
        return getEnv({},"document.createElement");
    },
    documentElement:getEnv({},"document.documentElement"),
    createEvent: function(arg1,arg2){
        console.log("调用方法： createEvent ","对象： document","arg1 ",arg1,"arg2 ",arg2)
        return getEnv({},"document.createEvent")
    },
    addEventListener:function(arg1,arg2){
        console.log("调用方法： addEventListener ","对象： document","arg1 ",arg1,"arg2 ",arg2)
        return getEnv({},"document.addEventListener")
    },
    querySelector:function(){
        return {}
    },
    body:getEnv({},"document.body")
}

window.document =document;


navigator={
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    microphone: "granted",
    appCodeName:"Mozilla",
    appName:"Netscape",
    appVersion:"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    bluetooth:getEnv({},"navigator.bluetooth"),
    cookieEnabled: true,
    credentials:getEnv({},"navigator.credentials"),
    deviceMemory:8,
    hardwareConcurrency:32,
    language:"zh-CN",
    languages:["zh-CN","zh"],
    maxTouchPoints:0,
    platform:"Win32",
    product:"Gecko",
    productSub:"20030107",
    plugins:getEnv({},"navigator.plugins"),
    storage:{
        estimate:getEnv({},"navigator.storage.estimate")
    },
    vendor: "Google Inc.",
    vendorSub:"",
    webdriver : false,
    getBattery: Promise,
    pemrissions:{
        "microphone": "granted"
    },
    connection:{
        downlink:10,
        effectiveType:"4g",
        rtt:0,
        saveData:false
    },
    userAgentData:{
        "brands": [
            {
                "brand": "Chromium",
                "version": "130"
            },
            {
                "brand": "Google Chrome",
                "version": "130"
            },
            {
                "brand": "Not?A_Brand",
                "version": "99"
            }
        ],
        "mobile": false,
        "platform": "Windows"
    },
    requestMediaKeySystemAccess : function(arg1,arg2){
        console.log("调用方法： requestMediaKeySystemAccess ","对象： navigator","arg1 ",arg1,"arg2 ",arg2)
        return getEnv({},"navigator.requestMediaKeySystemAccess");
    },
    vibrate : function(arg1,arg2){
        console.log("调用方法： vibrate ","对象： navigator","arg1 ",arg1,"arg2 ",arg2)
        return getEnv({},"navigator.vibrate");
    },
    __proto__ : getEnv({},"navigator.__proto__")
}
window.navigator = navigator;


screen = {
    availHeight : 1002,
    availLeft : 0,
    availTop : 0,
    availWidth : 1680,
    colorDepth : 24,
    height : 1050,
    isExtended : false ,
    pixelDepth : 24 ,
    width : 1680,
}
window.screen = screen

location={
    "ancestorOrigins": getEnv({},"location.ancestorOrigins"),
    "href": "https://www.douyin.com/user/MS4wLjABAAAA-QlAXXMYf-r-KFFEco3JLNrE3aSDvtFyVQwgCD5XpoY",
    "origin": "https://www.douyin.com",
    "protocol": "https:",
    "host": "www.douyin.com",
    "hostname": "www.douyin.com",
    "port": "",
    "pathname": "/user/MS4wLjABAAAA-QlAXXMYf-r-KFFEco3JLNrE3aSDvtFyVQwgCD5XpoY",
    "search": "",
    "hash": ""
}
window.location=location

history={
    length:1,
    scrollRestoration: "manual",
    state:null
}
window.history = history



proxyObjs = [
    'window', 'document', 'location', 'navigator', 'history', 'screen'
]
getEnvs(proxyObjs);
!function(n) {
    var i = {};
    function r(t) {
        if (i[t])
            return i[t].exports;
        var e = i[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return n[t].call(e.exports, e, e.exports, r),
        e.l = !0,
        e.exports
    }
    r.m = n,
    r.c = i,
    r.d = function(t, e, n) {
        r.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: n
        })
    }
    ,
    r.r = function(t) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }
    ,
    r.t = function(e, t) {
        if (1 & t && (e = r(e)),
        8 & t)
            return e;
        if (4 & t && "object" == typeof e && e && e.__esModule)
            return e;
        var n = Object.create(null);
        if (r.r(n),
        Object.defineProperty(n, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var i in e)
                r.d(n, i, function(t) {
                    return e[t]
                }
                .bind(null, i));
        return n
    }
    ,
    r.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t.default
        }
        : function() {
            return t
        }
        ;
        return r.d(e, "a", e),
        e
    }
    ,
    r.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }
    ,
    r.p = "",
    r(r.s = 12)
}([function(t, e, n) {
    var i, h, r, o, a, s, d, c, l, u, f, p, g;
    t.exports = (i = i || (h = Math,
    r = Object.create || function() {
        function n() {}
        return function(t) {
            var e;
            return n.prototype = t,
            e = new n,
            n.prototype = null,
            e
        }
    }(),
    a = (o = {}).lib = {},
    s = a.Base = {
        extend: function(t) {
            var e = r(this);
            return t && e.mixIn(t),
            e.hasOwnProperty("init") && this.init !== e.init || (e.init = function() {
                e.$super.init.apply(this, arguments)
            }
            ),
            (e.init.prototype = e).$super = this,
            e
        },
        create: function() {
            var t = this.extend();
            return t.init.apply(t, arguments),
            t
        },
        init: function() {},
        mixIn: function(t) {
            for (var e in t)
                t.hasOwnProperty(e) && (this[e] = t[e]);
            t.hasOwnProperty("toString") && (this.toString = t.toString)
        },
        clone: function() {
            return this.init.prototype.extend(this)
        }
    },
    d = a.WordArray = s.extend({
        init: function(t, e) {
            t = this.words = t || [],
            this.sigBytes = null != e ? e : 4 * t.length
        },
        toString: function(t) {
            return (t || l).stringify(this)
        },
        concat: function(t) {
            var e = this.words
              , n = t.words
              , i = this.sigBytes
              , r = t.sigBytes;
            if (this.clamp(),
            i % 4)
                for (var o = 0; o < r; o++) {
                    var a = n[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                    e[i + o >>> 2] |= a << 24 - (i + o) % 4 * 8
                }
            else
                for (var o = 0; o < r; o += 4)
                    e[i + o >>> 2] = n[o >>> 2];
            return this.sigBytes += r,
            this
        },
        clamp: function() {
            var t = this.words
              , e = this.sigBytes;
            t[e >>> 2] &= 4294967295 << 32 - e % 4 * 8,
            t.length = h.ceil(e / 4)
        },
        clone: function() {
            var t = s.clone.call(this);
            return t.words = this.words.slice(0),
            t
        },
        random: function(t) {
            for (var e, n = [], i = function(e) {
                var e = e
                  , n = 987654321
                  , i = 4294967295;
                return function() {
                    var t = ((n = 36969 * (65535 & n) + (n >> 16) & i) << 16) + (e = 18e3 * (65535 & e) + (e >> 16) & i) & i;
                    return t /= 4294967296,
                    (t += .5) * (.5 < h.random() ? 1 : -1)
                }
            }, r = 0; r < t; r += 4) {
                var o = i(4294967296 * (e || h.random()));
                e = 987654071 * o(),
                n.push(4294967296 * o() | 0)
            }
            return new d.init(n,t)
        }
    }),
    c = o.enc = {},
    l = c.Hex = {
        stringify: function(t) {
            for (var e = t.words, n = t.sigBytes, i = [], r = 0; r < n; r++) {
                var o = e[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                i.push((o >>> 4).toString(16)),
                i.push((15 & o).toString(16))
            }
            return i.join("")
        },
        parse: function(t) {
            for (var e = t.length, n = [], i = 0; i < e; i += 2)
                n[i >>> 3] |= parseInt(t.substr(i, 2), 16) << 24 - i % 8 * 4;
            return new d.init(n,e / 2)
        }
    },
    u = c.Latin1 = {
        stringify: function(t) {
            for (var e = t.words, n = t.sigBytes, i = [], r = 0; r < n; r++) {
                var o = e[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                i.push(String.fromCharCode(o))
            }
            return i.join("")
        },
        parse: function(t) {
            for (var e = t.length, n = [], i = 0; i < e; i++)
                n[i >>> 2] |= (255 & t.charCodeAt(i)) << 24 - i % 4 * 8;
            return new d.init(n,e)
        }
    },
    window.parse = u.parse,
    f = c.Utf8 = {
        stringify: function(t) {
            try {
                return decodeURIComponent(escape(u.stringify(t)))
            } catch (t) {
                throw new Error("Malformed UTF-8 data")
            }
        },
        parse: function(t) {
            return u.parse(unescape(encodeURIComponent(t)))
        }
    },
    p = a.BufferedBlockAlgorithm = s.extend({
        reset: function() {
            this._data = new d.init,
            this._nDataBytes = 0
        },
        _append: function(t) {
            "string" == typeof t && (t = f.parse(t)),
            this._data.concat(t),
            this._nDataBytes += t.sigBytes
        },
        _process: function(t) {
            var e = this._data
              , n = e.words
              , i = e.sigBytes
              , r = this.blockSize
              , o = 4 * r
              , a = i / o
              , s = (a = t ? h.ceil(a) : h.max((0 | a) - this._minBufferSize, 0)) * r
              , c = h.min(4 * s, i);
            if (s) {
                for (var l = 0; l < s; l += r)
                    this._doProcessBlock(n, l);
                var u = n.splice(0, s);
                e.sigBytes -= c
            }
            return new d.init(u,c)
        },
        clone: function() {
            var t = s.clone.call(this);
            return t._data = this._data.clone(),
            t
        },
        _minBufferSize: 0
    }),
    a.Hasher = p.extend({
        cfg: s.extend(),
        init: function(t) {
            this.cfg = this.cfg.extend(t),
            this.reset()
        },
        reset: function() {
            p.reset.call(this),
            this._doReset()
        },
        update: function(t) {
            return this._append(t),
            this._process(),
            this
        },
        finalize: function(t) {
            t && this._append(t);
            var e = this._doFinalize();
            return e
        },
        blockSize: 16,
        _createHelper: function(n) {
            return function(t, e) {
                return new n.init(e).finalize(t)
            }
        },
        _createHmacHelper: function(n) {
            return function(t, e) {
                return new g.HMAC.init(n,e).finalize(t)
            }
        }
    }),
    g = o.algo = {},
    o),
    i)
}
, function(t, e) {
    t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADYAAAA2CAMAAAC7m5rvAAAAV1BMVEUAAAAEBAQBAQEAAAAAAAAHBwcDAwNHcEwAAAAAAAD09PS/v7/8/PwBAQGcnJz4+Pj9/f3Pz8/////x8fHS0tK7u7vq6updXV3l5eXt7e3e3t75+fn///8na/+JAAAAHHRSTlMCCxUaBxAeAAEErVTgJ0TI7zb1k3QlqCt5g0vUK9r+DQAAArtJREFUSMeVlouOqjAQhumNpcCCgoi4ff/nPHNpC9ICnklMMOFjOte/xU9qVVEs7WiMlMYIbW1RVftXiixmb849pVIACqGLlEuwqgJKjw64siyVRH8pV6RQYa0WNXK/v2XJ3DnGlBbCyA8O3J1gDBGlyqfnlCR3h9jqyjTLs4esMAfuTjDOhRbmPrYuWneNkaupdlu7wpgyy4Av356PpvuDhwcd8jg2piZ81dUNVGwOlDLHKWHqjkH1CG2oswIQdsfkvbA3lKdim+TLTdQEvm4NdRQV+7FtrmxPQsG06IHq+FUDX3hI5UfgsJVD9zbegXjXb4Mm8hRj6GwKcdGsYIeR5amAWQ3R9CEYGE2LJPzyVMD03R8RfcE84/SgFXmKMB9ZvclctCpLRayNzqhKG/scR28egzPegjM+1h4Jk8VnYEwv6xmT/tstDI6YsZqbQubadjf7nF78b3VPofkz/hxgPPtYVesxyEh3jdnpNQmDoMdgOOcLDFvpz7XUcv+FWePcIGlTf39ILlPLG/77lEC+39C3SqmAfVMAbKUXVXeDXZcbMBSGZYtlmiuttRa3mIGDVs5QFkNr8duhALvBSWesomUDZxzDK7kx3XPUjeLtNlXKLYUd55Woj3nknuQVNKwriLnqU78g+0N0drDwNG+RiicTGx+POK5fza5XGg6/UizpKy76fs1Zfpkbmg5v8GjeQLXzKgkf0jHEFStpI7PBI8S1BoZ1PRAqJYkkkw0c37XdGnbEgiz2URZxQMgaUuV+3lKJCI8swjWI8Dx3zaOmC8Mw0ncidSn5ZHVXhvuXb9irCwYENXqINMW3Qf46c1/qvh2Gtq+XTikPbZvn4PKEl0kpmfDV+BCt7FVNc7WiiQhVJxdDWtm+1CypOvTo6TWUFEJHC/JYXVx6vSBFQU3VsTgUJR6aVBvJ/gHQeVzeaHqlAQAAAABJRU5ErkJggg=="
}
, function(t, e) {
    t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXcAAAA2CAMAAAALbSmxAAAAQlBMVEVHcEzW2O0FBQUPDxAEBAQEBAQBAQEAAAABAQHZ3PHKzuCussK9wNLU2OyIiZbW2u+bnavQ1OfR1ejS1uq8wNHIzN+f90J/AAAAFnRSTlMAuhMcCQ4XAQW3aT9lrDK0HIaToFJ8MqDAuAAADqZJREFUeNrsmteCnToMRcGUAzaYZv7/V6+qCyW5mWTehpdkOCDsZVnaElTVy/GBY4CjhaOTA//f4skBf/1UP8e/Pj6CnZkbPBL6H/DfiZ2pGzdtx7zU87GfwV/J/5D6BuxA3Z1LPdZ8jHAcdv0B/63cEXs4lPmyb6c9t2MZx3NV8D/cv8Xb102oH5Pvewnw7pxH2/6A/4ZsKqHdzYx9dw1Sj0m1C/O+/nD/59RJJgL2hbDPoUHsqiHJ0dft+AH/LdDb1jP2wwt21e3449CGPaXWH3T/Qq8P7NOGM+rRAHaiPsSDXN7ZtxCvoepzO/H5y+D3+cvbr0au5z5/cDzbfZv6+0SuxenEQaZB7oCdXTtih3Vwa/cE/jej+1tsX749VnovlH9HXXzu8fzLulS/InEtTttudc55P1NK9Ql7ukKaBr6TbXBf4DSY64m/CH9fAp8zG4r+RobzRje/dng6Pi926WS5kOWylC2WVJyGbR7pIOwnR5k2p65NA2kcXMjnw7lN5kvgLwa/VHUPSRJEM7eRXa7MImtbHnzH8GT3berPJBTqagW6cvc37N0a7Lbv+zmhuIyRP+euGUAfl/7+CveE4wtJvPAWkcEFhTYvRIorO/2pzduCWZPkwa6qjstCXkm0rcxETk1Qi44zEHUuTDslVSQrl+E96xTrV4j9pxfyGRG5MJtOcooviZ/S4J8ZiM2OrLGnZrKf8pHKlQX77rLFhfKD3ctCfsq/40LxEGRq6wHUN6e2zXrWJ1ZLCftql0Rd4tAV/KcK1tqQpjN8Vjhh1+5X2O5JM8t21Wp3bgqxgccc+5h2ZdhhO+Z63s/AJbeCH1ocmDdxAjhyOYLzzMHeDy/rcbfbooUuPQEtTvHv4ePg5ykOoSJvh+J0PFxaakycLtng8vWCndS9gI+ZYoXlW7xJ2tPCbVs23z890MBYTOe3Ci/HjrtYR+v6BH4YAoZTGz1n2PL5jTtebGLITQdT6Z7sgoVZXI5GvgPT6ODDgJ5d+15CN3F32O9KW6bMIhSFLD/m4Dhkdwk2GXiZK2LajW6VwWHw8vrXu0LLfyzzDw53z13gpukupyJ32Gx7Ae5M+1M4z5rChs92YYxLkiW7yB0Zod36ardD7ibFiA9yN3HqjixNjYCvYAgr+PJkdLtcRVPEvlgM6dQiM94uUlhxDlB1NuDTxtAz+LYFanXQPPEswQo1dj+HCzkVtVv+zutJ4UV3bwnPZp13YcPhTmkkK5MLETxQWyY6zo1ktOv7SYILtqn4N4wznXm0S9x54uwhyD3tp5MeeOjzMDYc6O29uRSmQ1JHE96ze9IwGor8LlpTNY9MFic0e76wxRu3TPlc2bYPwu1yqrVbSJp1+NXluWpCF8AlW1yPQwRPmYmlYoDfZpjBro6D3KlOpIsnrhpluh7R0m88EJzVza4R7opjEO6yrC1kx01EIg6hoiHspjcvQRhuCYj9vDbIzM5iUx1eY6pV1qZb4WGLrsEzrItCu52iv/MAWGq3QuXlahM9YMYY18uwOw/BdNM8itH2DDz+nkwrd0Z9yk905zoKd/YftitCOto1ZgOHSxqPdptwbymd1P5IjloNAGd0fSZeiqp2oOgPu6op3Xag56eAFWc7UGxxFJCwgx/4vnVdBVaF/0VadMr4MIl8wPpgNXQquKTP4DINge0KGjfEyweygK8i4/VDSjUUoUKvw247+HtZU96pXbMQTyYj3AWmg5E70WuRe8+xEx0rNFe76O+yRzr2oH1McRidf2+mmFHaCoe39ZlUvypgXF7CblKUll7xmAWsTxQROCcaAPrTzoPHsamXikDBU8ZxR2Lz5Ga08zhzjJvQxnwkAsltnOZGubyj0H9Kw7o3mbbC6A7+dCQOICmh4nPsOejd8NuZMpT6uwTSNbkUrDY8dFJvb9/sCvdGU1uXcUcTY2g8ZRS6sxpm9grT3SQ2UezQffem2BAagLCO8nmAT5HGwgiA6eIbJbqYNG4LTPFUWLQMI5LI/ayLU51wh/+FpC4WR6uJz9lzAaJFScWJZpyyfZ8XYLjHgaSryaujCiz9PaivMncx377Yjdx16TAOR+44WfhpV0dsK5xXk9LwrfBAvXU0+YbQOMQyx925U6Tx6E1xuMydwSN3sGf5ddY0baLFesNq9bAsVDkzEHccHv5n2W1WTBtahuWc7KGXd4k7Xu8yhxpSy4IylmfP0OovxXdqyNbJo7IVVGn8ZLdV7g1LvsQdJg3OfUIiDmq2q6xm4RikC+xB5MktDmlECXli5btQq9a7q1UuCHcxUnCnsEmSoNFT1I7rJ10Lp9UGgnEG4/Wk2xWx46sZihiwxdJIYBSBb5TsU4pOjLaAocEHCurInUQK7MNFpfaF+4td4r6c2THLCwwOluCgcCw0TLi3OnEID9ylTMWc6p7CP4V+zqA59xRpFooy2T574L7RRAkkZjHLS0Vzx7CN08PlI8ffjwXCE3JHN8V428dmNZ3asxTPabXuI5+iA8n+AocoRFXfzsPhbmK/5P5il7jfKnrmHhe12TSzVhurnb7krt8UZJLllnWZe76780hT15lYGG7c2dccM/YjVzCWKxni4DGoAlDhztufsPcYJmlXZMu0jdrIoxQPgzj5kTqxnLtEW7jz4D1J26lEtqUIXnJ/sfvOnfW0pQc6mbRB7kvf3OFF7OcLdokz2WQz8I4qrdjAT9y7yH2iPU5ZyIhgsHoKGcOzUeyW3BsoEUNgWk1DwYWvt2Ndl9wtD+4WZyAFziPttIYHQZvSlNTmKXvBeff3u12O71Lx8nEwd5jfJOmEM8pG3C2fS532rCN/jFEIPmhMrrj6K3cW8RQmaJeRpr5y5ykvqh+YO26BJerkfSS4kbvp/LlEMMpdokQnuz/jnsfhoWiABw0zHGi4IkTuBx37aUOTNS9L7p83u13Kq4Wegb8OUpSNJiLEXaEZqUXbsmVP2Knk79KaFNF/p/FcU4NIHXVdLcsz7nXOHU+NJOuQ+9wkQU2DTdzPvBmVuLPVO/dMd3BDEMssrLOuIYXl41bnaqTLmvXveqa0m3Qkl8+Ru7v01tBXKu7cNk2mR6UcReyLby4KMsUhlC3LNbyrw9NuvHGnIZXcjXLvf+3vPVqcsTfu/Xbl3t65U0v67PvUCkMxZ6kmugTikHOXiJa/iSq5v9qNdZP0NKRu6qWyK6J+X6Gm0kicdz3oe7HFFdjzV7bs7jZViVWRcpm7Zh8WAVwmYCkYufcF9xhtH+K7HyUow//3/8GdWjDiNp2GF6rA8GOJOR6amzd1/LyX9Hng/mr3pU/Qo3hc4vMWnmNFcVAEnVrqOE89Yk+BKKA4kjL2Wuhq9tEfaWxJIE4591a5X/RMneuZJkjCaHpSwZG78Lhw10BjdZNBvD1QuQEfyXc8ml4D7lbn1Ir30SX3z5td4p7VsdQXk3aJS6UBZ5SKfqcub/oO0jiqvmdXjmMoOriO+mkm1eYv3Ck1OepPoK/6OuPe59xZx8/P+r2Hv5eeR2/rgrsWZlfuNDHLzWvQTBsvpHGjqH/pCEj1RtzzF5dxcyt32djPdvN+ZNkHxt2pk5J0u2Cc4cYXLAKJafi1QZ1Gr/H6Entq5cK/+OLPGvMgdWIzMHGnYDvj0ja7lqnM3WTcKc681Kv9pCUfX7VL3aQ88Hmx25HJXP6uFswcavCkxoM2pymeIR7knquU9AIlcae9y+X41e69//4R7l4erO1LUlM9xmL99HfeTmvPIyqGrAX50Q/FtAse5NVg9/TKWrnHVaFqY1w2C8XzIlEZk6h25sXf0ZGP+jjDeenPGP53OZ1DWazFKd1mtCAeoxeo4ArcR5uh1KUZoT1sie19iql0p1PuyUA2F+JuYkB9thvfN3Xl+yaalIsv4ECv0AC43j9u72/nkD6N/FTDZ3OdvH+gNummQ3n8UkC4r9kHCfg0bthi78OyPoktSrGGS+GPx34kKXRpRk6TzJVvozEw9y51LO5v409KRsgsmPRyjfqLmyHuke0j9wj082SXO2txCOn96iyvWWPgQHaex9ddPtJYzviWiN0VyJxOXq52bgOIc3jFHrl3XaotVn5xvPseuUsfuGzJwynUkTs60VL032mxw0wWDoeKZDeG++/yngmflz5OiRVGZ8WlYs8e1Uj2qRvnv2U1RK27JysJklP2ScOT3TZ+TxCv2uh7AievG9KL+f/aOdslB0EYitJZralYqwXf/1VX5CvEoLZbZnbGOv1lJUpEJMm5LntEhJKC05/6J3odYtxv5qFuepqRe5uGUPTk0BWR4kY26yBNWSiSQWZyrZJ6nfX7vGbXPQc31FLbYhMWF/pz4PMlzJOpUdlWyzCo/ISJ8SJcWmQWCaQvnN0KCKIV1ZDYsM2fz/sjXFfPhtqu070b1TVGnXCIN99WC/xEYyxeVxEujimdkpKrz1ddMZkVsCvzYwxgcI7AawS+C6hXcmWrUvoaimI6w9ilR7GG/X6MpQYgLYUJ7Ry4TLkP8zJpJT1iFydlL4PiGyFbfKVl8E3+gIFCM1gqMYgoRUSHQMP6PW3C2W0gi+SuPQGRVpar4n5wuwm9LqGmngxGnjZdUccb1AzSPOAsDuJtANJ+8Vx0sxKSpxIWcofS2Bvy2PLaNmOXXkLesNsfTAspXahK72C1JLlQGE3i6ENyAZZMJjFwg6qBsIOXHWL1xE6jnMxjV/qwezEZIUNsi2yPA/dALqCCTx+FpM/uRwqaN2Qs4JY4b8OUjNcOHLjtda4vnN0DPcZN8XJJaeJ4+wBMQYbgonqGRnxFgJH9T8iEqD3GDr+g1SklO/2rjUHhIe8yZFJdovqDzgAflyujd/+JBH3D894OCQ8n/QKyixn6QqNH+GXNuQSay3ATc9w6aumSAbL1Ag/V89W+Avp8ONknJ5z6zMg65sBIqfvjdnFJCKV/KD9ZUqVf6HH6344HGPR4QwKz+5KXwbRw8c8jnEx+H9GnWup2GsdxanWfkUyW9fxZxfKQiAe3cwLf7XOOB7Smqb6fFCuw/QK4hFJoJgmn4wAAAABJRU5ErkJggg=="
}
, function(t, e) {
    t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARQAAAA2CAMAAAAxvZbCAAAAS1BMVEVHcEwAAAAAAAARERPZ2vDU2OwHBwcAAAADAwMAAAAAAAAODg8BAQGytcbN0OTDxtnS1enS1urV2e3Iy960t8iTlaRvb3mpq7vO0uWmqkiCAAAAGXRSTlMAFBAOuLsLAgUHEh0YPIJfl6Suc1A8KR+P56WgUwAADiFJREFUaN7lW9m2rCgSTUVTVBAFp///0o6JQc2sW31Xr9UPSVd1naOAsIlhRxDn9freuk7rvn9DU9jwh3ff91p33F6/12DXBImq6wFbXdcMTIblBzFhSKyb5sU3fpnDujEsKC0/iQpi8n7byTdNC63htoRDYPlFVAgTOzMibevPKYQwwe/NdLwLVH4Nk+MUSBa3mapCo6KUDb5xqtCgX7KwureiOOc2GlMN0cq+lfPz8VuiQhtFR2xbwsSv44iQJH/c990xASr/W1Hpur/28v92aPeX32BAAJH+fbQkJstOmKgICDXduzk75j8t4dn+qcu/m6H7w9g/jP5jl7vW9MTW1EKYzIQJiAkiwA3f99q6gq58Rffeym9eV5FfX1YThzynuI7Un7ZyHcJLz+fID/Mc+cih3SBh+lo70h2Uk7GqYf9pNGMGvvr4BxcU0X20clPFirn3RfDSFPo2VZoiH1J8eqOdtNL4TraWqETx1dg1NvjtRl/fx2bttnkSlI3kJM/EkABmwHGPWn1DJXZ8tmJNcTf4oyq4z4U5itLeptDFeAk/+hso8XjjCK1jpJJWoBNq7xTIxGimnEatyNWoISYTyIkBe9InZHEwcv6qIhdN33jCwj0Ju7KpAsXufRwqLhjEMqT1xuWoyfKeeMF5Cv6kPngvwJzsdWzaDK0UhyB48I0Ffi+k3tmMdIxkJJxReZojREQElE0wERnHjR5rOM95npxlP63iNktM3qtbP7UtH9QrRCDgAYJS1/IyLmdqmlnVymLbcuMv9nrylg4XQcGxfRGkdsec2sqO80B+seKKYTh1g4+uiPU6P9pWJ/rqEJIFtmvt6pDKzsZcMTnwsVDc1oeNYIn7LEA5ms/NZQx1ICBqEl8EBU5IlaJtG3q43+fgD2qAzB94uggKH05hrmw+WWcIlYliFHak1PNYaEHD4EoxoNbYIdJXYvAwP0XDdb2HNlR5oSRIbTESW0BpSetJoOgvoLRuyIIVGAhCBUGpyp3BcjzuoXqA0rJw0p6WHZQYQTGGxyYvZPM2+SU88AERSqi8aMPhKyh0MLCIeWOFUqzG1rI+iu3GHldM0DsVqBSSMoXpU1tvklKxpL0RFJTKKHW6VxhhwH6qfbm2mUHpNaJ2wqAZtNwIKtmjqkPt4DkDvaxIntzo5TfGr1MTobJbadB5RgVd7V6jXWRhjbaTLbIYfwafTpOcdGD1OiMq7J4+2H5VmK5kwNKEJCmGzZJyTYs/CyrQgU7R0esBDQdbdjLuLFswPy15HBc2fSZybvFXaGWNgVXCAo1ZUexGB7seEyrQB1CZRDHgC/D6HEfmZbgHhN0lf8Jol6RA9wEx8WE3tFLoujtGBW1xfbf9H53Pxf1oAQW3PSAoY2TO8FXS90ne8pIzskq8KFCpc4+gSHSGn6D34JQ8rBVe4qsNZMSO1HeKGk/c4pxqUg30briKM64CBAXoK8oJW82CSWSzR3Jy7makZfIs+9yIXYFZSoYhyanPoIiosKTwbvCMgmwMemhSVMBkHwWVh7ip4zj23e3QUCf2spFCvn3jQVLo0EbEBOcft7jeOjtiWRXxVQSF377o1GZTVaUTvxDpfkVMpuiEk3M/EZWsQNeEnarjGX8SFfzmEm0N2IUlWx3yFGBvzOndSBozDIX+YA97M41tToMFWiKY+rkyOykEYoLYjKRArYu6JjymVpnEn0YcLjsLSpgk639jp5YwMSbJt4RAFCDRRzIot7zu3awIKroLD6tN/gzX4NBXVmaF31fDqCAehvSJ9vwRFJmBDg46TJXZUF0Qk3Y5uTElNRXT9m0jkO15OlIfAaVGUAIKKwlK/wx7xT02ZzRRBZfAxcEhRP0R12NT2xLrSo92saVspO6tQVCAaFlYIyrGZHzx1rf4G7Cxt/Wp4fPyl0DivJKdBlgdYuLPNMWECSJTTZJcJQSh88SE5Yw6/NKw51V2/MSk65E0Ntlsl2r1BmOE+iNDaUA8xQ9bbhN/IxZ7fuC8JErwbz2AToGtbB8sYo0aDMCROE2kGShEVYigIF01qC0rYOs3lzjESF0yKILghN5HDC2KCjEd2vLNsxZ8uyFCclcvNsDk++sHKDc5SKSWhY0kJeTdJHtR+BbY0Th+BCVGcQALMjKeBtVsYt8+DAENAtGU0WGon8zwaBzy2oBs/gJKZeCLcwwlMAhYjLlaywITdDz+gkkhRYjAehnb2cy0SJuvbRXq2X0BRUjIGzFBEcCNHPA/cjMrbWuINA2xAw9oeRYYDaAwCxxOPOfxZHfN74mwmB3/IXJU77zvYVjJAJkkTnNVv8j3fAQlGVn7CRMUFbTR9iopHDgiG8J9OFqQuW4bbcr0AIWiHxYjdECZlClyFF4ISSVWiZI/itR33EamKROZEphpaTycOHIYHAN42Bk3YYz3E4MCbl2E4SMo0zdJiTEIhgzmAyYCysYGu4j6s2h7oR93Tqu7E4n3eIeM94skX0DhTCi02jfpQU7vYExjVu93JjRTw+FNnRXOj+sMGr6StUF/5IkmY+CcQSHX6tAiYwsDgdKKf36wdeSWMCKz1qskkRztRgzt9f5Z7WBZHWe9a/bQbDIoG9KjRl8D9iBESROhFVAo1CdN8QR/Xkgk2icS1YVZZZSUPZshAAXxAMqCCKzke9gqXSSFQRGaPyhUn2YbzW3fHBgjJuR4cJpnLgkNzsyqpct8NPH8QLE6n7U9UaFy7KP7JdtO2cAkUoBGrpmWSzoH5mNQqpzzws+Q49zYzQ5kStDCVUeQhnDtJLA8H0fKjPRNUkYBhV2y48iqzJ3E/AlmVfz+MT/AoMx0NMNN8wiVo0meHk2EY1Bi6KOyQ2kSKDwR6qSrMfpNtBBXI6AUgkKC6qGT43CW8girBJnorw0ExsBlaapAzmyhQJk2GkExVSkpkbwdtPNswmJO901y4rcPzjjROrRzOUVx0bxThAgmRVLSHkOZDES9K/JpWyBQaMv6dVpyK1sRQHQCylV7Tokb0QJYAoV9goAyMigUWjGhAezj6esIiikkRVh7/8LjFsFJSQlUYr4htE/SltXrlOzQneFIuLQlEgyfOKtiIta7HNxiiDqlL4GQqjkRoG+gsGek9e0L0oaqWuI3Fd7vzoEjwg1TBmhU+KcrKDslFqKkRIfz0msjpKCI95Ti4OQDJjkZvqL05pjpQoN9zJfQhJYypGkqOmNJoXA85mhh0WJojP3bUlv0AxTyAi0LYw3zL8dQeTH7jioBWgRl5pTBTv8XJFTLoGwAGgoR+JILKJ0mDzhv+eDqYaN6g6w7+npTgyzhjRer6wdBERq8jCmsRohRRZk2a1oQar9J7PQKSoegXDB42BTN4ccmuE4BLXmLfhQ+KXbKjWw70Z6Y0C5bab0JFIiMNtEsMbSiPpxjwlhqE9IArp3vTC+Y3K+3QL1aVyQcbspDTDOpB4V3aT2oPX7MqTZK7JWgkAm3GZTsfdIDzJtxpEM+DZAf9kjcUZumdUdHjNu15JR3VqG4CDKIlEq4gkKmldi6FBj4k4pQxC2cF3Kvb7dbKycvhvrJ/ilNlPnqvuH1AF2Z8NUa7TAUk+sCFFYOBiVKob6DIon2WQ6W82ioRDyJWw+KFzfJLoUVU4ZjTGZV0SU3dDF8AUUCQry7OpZHIO/XmA/mZeLdVD3E7B3WrkB09wGTV/dCTM5921YHCC/Z+Z6izxRPbaYqrCaCAjIKhyR2la4uuAfpqvJkZHiI5uzcskciRqAMTGixC9mpoVolXCQnk2IhVGIQSMeZs/EGCllWtgHKXe8vKB0rkhmJxWQlp6osRs5+LZ1s4XrsNUYuflsJFMoRTXKnQUM77eRJdDZaQOHwETaJ/HhLNpKvcSIm3AMFpd2y6EDIB5Z4XfNtApIhaI67cHJ8nWewNH5O/4F2xnsfvumKR7re7v+Y0Ld+CgEsO+0z7JGi3m/835dYH+Gbp+BWTDqOuB6i8Xu+/YqgpCcRFJHDcMJOlrxjsoHQf4wGDeTGLzPpU7JTdp5m7IYe55bbmSoRV28xi/JM/CxDcSmxWwdt3SSNXtwUkzspTt6HI4UyzwTmTKj45UQs7DZyNIhGiJIhlu7mar7VuoBS30DhJcTrKi8Kp/ED3g1ZUN+xx1bFazG5kHMmNPeUzMQqp2Y0PO5D7odBIWIuySy+XKkvJZDJVFP2bw42ZsE/VR2ATVntsdcp9OWbh1rNfqV54WDD+1IrQDe7k1ICUwSFQY/3fYtNnu5opkPV+VBefAzzlq4ZX93sQUDhELaP6T3JM0OsfEucUuq0zlGcjUn4W60scwJ2X1ivkq4Rv1TtyL2PgJGz//aIFduHLuoy2A45LgKI+oQPpAIGUMF2lDUDh9RPxDXqAxp/MT+jDIaiegwpW1DpCrRPtS2Ul0DWEBMYOEeWenv0ZeGKzkUpb6a3HCHl+rcvdde5+iff2F2qbi43bSkNkcpVOqkzyg86ALHOsnWtbpHgEHq8izvNVKLypUxGF+VNz37FXqZ4AO+4eJExsUbrpf7teyl6V1Qy5RKrstqqKLsqR2TB4wep0qm/1yE9ir24S/+sVPpTQVWnP/QrNnMsLollDgzfEgYh8YkO71a/9t9UAX4vCrzD1Onbwj+VvKUCNs0g6mc93NfSu68dS18KqEzqLkvKck0gY1IX8vnP1Zf/rh7xe0XnX6D6lzP8oc7ydcye7Fsqq6pt9MUuYdL9P/6wpeu6/8/f0+AH8ZLKWblCtyGS9CUmLJ93Qz9Qkd8dgZkX0N7EeZb1emn6c3/PAmGOO8uKKh+sudYk/OJfg1ECCQLciWj6LrRU/eRfs1wLr5kOXutKfhWTyBjuNO/H/mzwP/q5W8U07M8OAAAAAElFTkSuQmCC"
}
, function(t, e, n) {
    var i;
    t.exports = (i = n(0),
    i.enc.Latin1)
}
, function(i, r, o) {
    var a, s;
    !function(t, e, n) {
        "use strict";
        "undefined" != typeof window && o(18) ? void 0 === (s = "function" == typeof (a = n) ? a.call(r, o, r, i) : a) || (i.exports = s) : void 0 !== i && i.exports ? i.exports = n() : e.exports ? e.exports = n() : e.Fingerprint2 = n()
    window.x64hash128 = i.exports.x64hash128
    }(0, this, function() {
        "use strict";
        void 0 === Array.isArray && (Array.isArray = function(t) {
            return "[object Array]" === Object.prototype.toString.call(t)
        }
        );
        var h = function(t, e) {
            t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]],
            e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]];
            var n = [0, 0, 0, 0];
            return n[3] += t[3] + e[3],
            n[2] += n[3] >>> 16,
            n[3] &= 65535,
            n[2] += t[2] + e[2],
            n[1] += n[2] >>> 16,
            n[2] &= 65535,
            n[1] += t[1] + e[1],
            n[0] += n[1] >>> 16,
            n[1] &= 65535,
            n[0] += t[0] + e[0],
            n[0] &= 65535,
            [n[0] << 16 | n[1], n[2] << 16 | n[3]]
        }
          , d = function(t, e) {
            t = [t[0] >>> 16, 65535 & t[0], t[1] >>> 16, 65535 & t[1]],
            e = [e[0] >>> 16, 65535 & e[0], e[1] >>> 16, 65535 & e[1]];
            var n = [0, 0, 0, 0];
            return n[3] += t[3] * e[3],
            n[2] += n[3] >>> 16,
            n[3] &= 65535,
            n[2] += t[2] * e[3],
            n[1] += n[2] >>> 16,
            n[2] &= 65535,
            n[2] += t[3] * e[2],
            n[1] += n[2] >>> 16,
            n[2] &= 65535,
            n[1] += t[1] * e[3],
            n[0] += n[1] >>> 16,
            n[1] &= 65535,
            n[1] += t[2] * e[2],
            n[0] += n[1] >>> 16,
            n[1] &= 65535,
            n[1] += t[3] * e[1],
            n[0] += n[1] >>> 16,
            n[1] &= 65535,
            n[0] += t[0] * e[3] + t[1] * e[2] + t[2] * e[1] + t[3] * e[0],
            n[0] &= 65535,
            [n[0] << 16 | n[1], n[2] << 16 | n[3]]
        }
          , f = function(t, e) {
            return 32 === (e %= 64) ? [t[1], t[0]] : e < 32 ? [t[0] << e | t[1] >>> 32 - e, t[1] << e | t[0] >>> 32 - e] : (e -= 32,
            [t[1] << e | t[0] >>> 32 - e, t[0] << e | t[1] >>> 32 - e])
        }
          , p = function(t, e) {
            return 0 === (e %= 64) ? t : e < 32 ? [t[0] << e | t[1] >>> 32 - e, t[1] << e] : [t[1] << e - 32, 0]
        }
          , g = function(t, e) {
            return [t[0] ^ e[0], t[1] ^ e[1]]
        }
          , m = function(t) {
            return t = g(t, [0, t[0] >>> 1]),
            t = d(t, [4283543511, 3981806797]),
            t = g(t, [0, t[0] >>> 1]),
            t = d(t, [3301882366, 444984403]),
            t = g(t, [0, t[0] >>> 1])
        }
          , s = function(t, e) {
            e = e || 0;
            for (var n = (t = t || "").length % 16, i = t.length - n, r = [0, e], o = [0, e], a = [0, 0], s = [0, 0], c = [2277735313, 289559509], l = [1291169091, 658871167], u = 0; u < i; u += 16)
                a = [255 & t.charCodeAt(u + 4) | (255 & t.charCodeAt(u + 5)) << 8 | (255 & t.charCodeAt(u + 6)) << 16 | (255 & t.charCodeAt(u + 7)) << 24, 255 & t.charCodeAt(u) | (255 & t.charCodeAt(u + 1)) << 8 | (255 & t.charCodeAt(u + 2)) << 16 | (255 & t.charCodeAt(u + 3)) << 24],
                s = [255 & t.charCodeAt(u + 12) | (255 & t.charCodeAt(u + 13)) << 8 | (255 & t.charCodeAt(u + 14)) << 16 | (255 & t.charCodeAt(u + 15)) << 24, 255 & t.charCodeAt(u + 8) | (255 & t.charCodeAt(u + 9)) << 8 | (255 & t.charCodeAt(u + 10)) << 16 | (255 & t.charCodeAt(u + 11)) << 24],
                a = d(a, c),
                a = f(a, 31),
                a = d(a, l),
                r = g(r, a),
                r = f(r, 27),
                r = h(r, o),
                r = h(d(r, [0, 5]), [0, 1390208809]),
                s = d(s, l),
                s = f(s, 33),
                s = d(s, c),
                o = g(o, s),
                o = f(o, 31),
                o = h(o, r),
                o = h(d(o, [0, 5]), [0, 944331445]);
            switch (a = [0, 0],
            s = [0, 0],
            n) {
            case 15:
                s = g(s, p([0, t.charCodeAt(u + 14)], 48));
            case 14:
                s = g(s, p([0, t.charCodeAt(u + 13)], 40));
            case 13:
                s = g(s, p([0, t.charCodeAt(u + 12)], 32));
            case 12:
                s = g(s, p([0, t.charCodeAt(u + 11)], 24));
            case 11:
                s = g(s, p([0, t.charCodeAt(u + 10)], 16));
            case 10:
                s = g(s, p([0, t.charCodeAt(u + 9)], 8));
            case 9:
                s = g(s, [0, t.charCodeAt(u + 8)]),
                s = d(s, l),
                s = f(s, 33),
                s = d(s, c),
                o = g(o, s);
            case 8:
                a = g(a, p([0, t.charCodeAt(u + 7)], 56));
            case 7:
                a = g(a, p([0, t.charCodeAt(u + 6)], 48));
            case 6:
                a = g(a, p([0, t.charCodeAt(u + 5)], 40));
            case 5:
                a = g(a, p([0, t.charCodeAt(u + 4)], 32));
            case 4:
                a = g(a, p([0, t.charCodeAt(u + 3)], 24));
            case 3:
                a = g(a, p([0, t.charCodeAt(u + 2)], 16));
            case 2:
                a = g(a, p([0, t.charCodeAt(u + 1)], 8));
            case 1:
                a = g(a, [0, t.charCodeAt(u)]),
                a = d(a, c),
                a = f(a, 31),
                a = d(a, l),
                r = g(r, a)
            }
            return r = g(r, [0, t.length]),
            o = g(o, [0, t.length]),
            r = h(r, o),
            o = h(o, r),
            r = m(r),
            o = m(o),
            r = h(r, o),
            o = h(o, r),
            ("00000000" + (r[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (r[1] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[0] >>> 0).toString(16)).slice(-8) + ("00000000" + (o[1] >>> 0).toString(16)).slice(-8)
        }
          , t = {
            preprocessor: null,
            audio: {
                timeout: 1e3,
                excludeIOS11: !0
            },
            fonts: {
                swfContainerId: "fingerprintjs2",
                swfPath: "flash/compiled/FontList.swf",
                userDefinedFonts: [],
                extendedJsFonts: !1
            },
            screen: {
                detectScreenOrientation: !0
            },
            plugins: {
                sortPluginsFor: [/palemoon/i],
                excludeIE: !1
            },
            extraComponents: [],
            excludes: {
                enumerateDevices: !0,
                pixelRatio: !0,
                doNotTrack: !0,
                fontsFlash: !0,
                adBlock: !0
            },
            NOT_AVAILABLE: "not available",
            ERROR: "error",
            EXCLUDED: "excluded"
        }
          , l = function(t, e) {
            if (Array.prototype.forEach && t.forEach === Array.prototype.forEach)
                t.forEach(e);
            else if (t.length === +t.length)
                for (var n = 0, i = t.length; n < i; n++)
                    e(t[n], n, t);
            else
                for (var r in t)
                    t.hasOwnProperty(r) && e(t[r], r, t)
        }
          , c = function(t, i) {
            var r = [];
            return null == t ? r : Array.prototype.map && t.map === Array.prototype.map ? t.map(i) : (l(t, function(t, e, n) {
                r.push(i(t, e, n))
            }),
            r)
        }
          , n = function() {
            return navigator.mediaDevices && navigator.mediaDevices.enumerateDevices
        }
          , i = function(t) {
            var e = [window.screen.width, window.screen.height];
            return t.screen.detectScreenOrientation && e.sort().reverse(),
            e
        }
          , r = function(t) {
            if (window.screen.availWidth && window.screen.availHeight) {
                var e = [window.screen.availHeight, window.screen.availWidth];
                return t.screen.detectScreenOrientation && e.sort().reverse(),
                e
            }
            return t.NOT_AVAILABLE
        }
          , o = function(t) {
            if (null == navigator.plugins)
                return t.NOT_AVAILABLE;
            for (var e = [], n = 0, i = navigator.plugins.length; n < i; n++)
                navigator.plugins[n] && e.push(navigator.plugins[n]);
            return u(t) && (e = e.sort(function(t, e) {
                return t.name > e.name ? 1 : t.name < e.name ? -1 : 0
            })),
            c(e, function(t) {
                var e = c(t, function(t) {
                    return [t.type, t.suffixes]
                });
                return [t.name, t.description, e]
            })
        }
          , a = function(e) {
            var t = [];
            if (Object.getOwnPropertyDescriptor && Object.getOwnPropertyDescriptor(window, "ActiveXObject") || "ActiveXObject"in window) {
                t = c(["AcroPDF.PDF", "Adodb.Stream", "AgControl.AgControl", "DevalVRXCtrl.DevalVRXCtrl.1", "MacromediaFlashPaper.MacromediaFlashPaper", "Msxml2.DOMDocument", "Msxml2.XMLHTTP", "PDF.PdfCtrl", "QuickTime.QuickTime", "QuickTimeCheckObject.QuickTimeCheck.1", "RealPlayer", "RealPlayer.RealPlayer(tm) ActiveX Control (32-bit)", "RealVideo.RealVideo(tm) ActiveX Control (32-bit)", "Scripting.Dictionary", "SWCtl.SWCtl", "Shell.UIHelper", "ShockwaveFlash.ShockwaveFlash", "Skype.Detection", "TDCCtl.TDCCtl", "WMPlayer.OCX", "rmocx.RealPlayer G2 Control", "rmocx.RealPlayer G2 Control.1"], function(t) {
                    try {
                        return new window.ActiveXObject(t),
                        t
                    } catch (t) {
                        return e.ERROR
                    }
                })
            } else
                t.push(e.NOT_AVAILABLE);
            return navigator.plugins && (t = t.concat(o(e))),
            t
        }
          , u = function(t) {
            for (var e = !1, n = 0, i = t.plugins.sortPluginsFor.length; n < i; n++) {
                var r = t.plugins.sortPluginsFor[n];
                if (navigator.userAgent.match(r)) {
                    e = !0;
                    break
                }
            }
            return e
        }
          , y = function(e) {
            try {
                return !!window.sessionStorage
            } catch (t) {
                return e.ERROR
            }
        }
          , v = function(e) {
            try {
                return !!window.localStorage
            } catch (t) {
                return e.ERROR
            }
        }
          , b = function(e) {
            if (M())
                return e.EXCLUDED;
            try {
                return !!window.indexedDB
            } catch (t) {
                return e.ERROR
            }
        }
          , w = function(t) {
            return navigator.hardwareConcurrency ? navigator.hardwareConcurrency : t.NOT_AVAILABLE
        }
          , T = function(t) {
            return navigator.cpuClass || t.NOT_AVAILABLE
        }
          , A = function(t) {
            return navigator.platform ? navigator.platform : t.NOT_AVAILABLE
        }
          , E = function(t) {
            return navigator.doNotTrack ? navigator.doNotTrack : navigator.msDoNotTrack ? navigator.msDoNotTrack : window.doNotTrack ? window.doNotTrack : t.NOT_AVAILABLE
        }
          , e = function() {
            var e, t = 0;
            void 0 !== navigator.maxTouchPoints ? t = navigator.maxTouchPoints : void 0 !== navigator.msMaxTouchPoints && (t = navigator.msMaxTouchPoints);
            try {
                document.createEvent("TouchEvent"),
                e = !0
            } catch (t) {
                e = !1
            }
            return [t, e, "ontouchstart"in window]
        }
          , x = function(t) {
            var e = []
              , n = document.createElement("canvas");
            n.width = 2e3,
            n.height = 200,
            n.style.display = "inline";
            var i = n.getContext("2d");
            return i.rect(0, 0, 10, 10),
            i.rect(2, 2, 6, 6),
            e.push("canvas winding:" + (!1 === i.isPointInPath(5, 5, "evenodd") ? "yes" : "no")),
            i.textBaseline = "alphabetic",
            i.fillStyle = "#f60",
            i.fillRect(125, 1, 62, 20),
            i.fillStyle = "#069",
            t.dontUseFakeFontInCanvas ? i.font = "11pt Arial" : i.font = "11pt no-real-font-123",
            i.fillText("Cwm fjordbank glyphs vext quiz, 😃", 2, 15),
            i.fillStyle = "rgba(102, 204, 0, 0.2)",
            i.font = "18pt Arial",
            i.fillText("Cwm fjordbank glyphs vext quiz, 😃", 4, 45),
            i.globalCompositeOperation = "multiply",
            i.fillStyle = "rgb(255,0,255)",
            i.beginPath(),
            i.arc(50, 50, 50, 0, 2 * Math.PI, !0),
            i.closePath(),
            i.fill(),
            i.fillStyle = "rgb(0,255,255)",
            i.beginPath(),
            i.arc(100, 50, 50, 0, 2 * Math.PI, !0),
            i.closePath(),
            i.fill(),
            i.fillStyle = "rgb(255,255,0)",
            i.beginPath(),
            i.arc(75, 100, 50, 0, 2 * Math.PI, !0),
            i.closePath(),
            i.fill(),
            i.fillStyle = "rgb(255,0,255)",
            i.arc(75, 75, 75, 0, 2 * Math.PI, !0),
            i.arc(75, 75, 25, 0, 2 * Math.PI, !0),
            i.fill("evenodd"),
            n.toDataURL && e.push("canvas fp:" + n.toDataURL()),
            e
        }
          , S = function() {
            var a, t = function(t) {
                return a.clearColor(0, 0, 0, 1),
                a.enable(a.DEPTH_TEST),
                a.depthFunc(a.LEQUAL),
                a.clear(a.COLOR_BUFFER_BIT | a.DEPTH_BUFFER_BIT),
                "[" + t[0] + ", " + t[1] + "]"
            };
            if (!(a = U()))
                return null;
            var s = []
              , e = a.createBuffer();
            a.bindBuffer(a.ARRAY_BUFFER, e);
            var n = new Float32Array([-.2, -.9, 0, .4, -.26, 0, 0, .732134444, 0]);
            a.bufferData(a.ARRAY_BUFFER, n, a.STATIC_DRAW),
            e.itemSize = 3,
            e.numItems = 3;
            var i = a.createProgram()
              , r = a.createShader(a.VERTEX_SHADER);
            a.shaderSource(r, "attribute vec2 attrVertex;varying vec2 varyinTexCoordinate;uniform vec2 uniformOffset;void main(){varyinTexCoordinate=attrVertex+uniformOffset;gl_Position=vec4(attrVertex,0,1);}"),
            a.compileShader(r);
            var o = a.createShader(a.FRAGMENT_SHADER);
            a.shaderSource(o, "precision mediump float;varying vec2 varyinTexCoordinate;void main() {gl_FragColor=vec4(varyinTexCoordinate,0,1);}"),
            a.compileShader(o),
            a.attachShader(i, r),
            a.attachShader(i, o),
            a.linkProgram(i),
            a.useProgram(i),
            i.vertexPosAttrib = a.getAttribLocation(i, "attrVertex"),
            i.offsetUniform = a.getUniformLocation(i, "uniformOffset"),
            a.enableVertexAttribArray(i.vertexPosArray),
            a.vertexAttribPointer(i.vertexPosAttrib, e.itemSize, a.FLOAT, !1, 0, 0),
            a.uniform2f(i.offsetUniform, 1, 1),
            a.drawArrays(a.TRIANGLE_STRIP, 0, e.numItems);
            try {
                s.push(a.canvas.toDataURL())
            } catch (t) {}
            s.push("extensions:" + (a.getSupportedExtensions() || []).join(";")),
            s.push("webgl aliased line width range:" + t(a.getParameter(a.ALIASED_LINE_WIDTH_RANGE))),
            s.push("webgl aliased point size range:" + t(a.getParameter(a.ALIASED_POINT_SIZE_RANGE))),
            s.push("webgl alpha bits:" + a.getParameter(a.ALPHA_BITS)),
            s.push("webgl antialiasing:" + (a.getContextAttributes().antialias ? "yes" : "no")),
            s.push("webgl blue bits:" + a.getParameter(a.BLUE_BITS)),
            s.push("webgl depth bits:" + a.getParameter(a.DEPTH_BITS)),
            s.push("webgl green bits:" + a.getParameter(a.GREEN_BITS)),
            s.push("webgl max anisotropy:" + function(t) {
                var e = t.getExtension("EXT_texture_filter_anisotropic") || t.getExtension("WEBKIT_EXT_texture_filter_anisotropic") || t.getExtension("MOZ_EXT_texture_filter_anisotropic");
                if (e) {
                    var n = t.getParameter(e.MAX_TEXTURE_MAX_ANISOTROPY_EXT);
                    return 0 === n && (n = 2),
                    n
                }
                return null
            }(a)),
            s.push("webgl max combined texture image units:" + a.getParameter(a.MAX_COMBINED_TEXTURE_IMAGE_UNITS)),
            s.push("webgl max cube map texture size:" + a.getParameter(a.MAX_CUBE_MAP_TEXTURE_SIZE)),
            s.push("webgl max fragment uniform vectors:" + a.getParameter(a.MAX_FRAGMENT_UNIFORM_VECTORS)),
            s.push("webgl max render buffer size:" + a.getParameter(a.MAX_RENDERBUFFER_SIZE)),
            s.push("webgl max texture image units:" + a.getParameter(a.MAX_TEXTURE_IMAGE_UNITS)),
            s.push("webgl max texture size:" + a.getParameter(a.MAX_TEXTURE_SIZE)),
            s.push("webgl max varying vectors:" + a.getParameter(a.MAX_VARYING_VECTORS)),
            s.push("webgl max vertex attribs:" + a.getParameter(a.MAX_VERTEX_ATTRIBS)),
            s.push("webgl max vertex texture image units:" + a.getParameter(a.MAX_VERTEX_TEXTURE_IMAGE_UNITS)),
            s.push("webgl max vertex uniform vectors:" + a.getParameter(a.MAX_VERTEX_UNIFORM_VECTORS)),
            s.push("webgl max viewport dims:" + t(a.getParameter(a.MAX_VIEWPORT_DIMS))),
            s.push("webgl red bits:" + a.getParameter(a.RED_BITS)),
            s.push("webgl renderer:" + a.getParameter(a.RENDERER)),
            s.push("webgl shading language version:" + a.getParameter(a.SHADING_LANGUAGE_VERSION)),
            s.push("webgl stencil bits:" + a.getParameter(a.STENCIL_BITS)),
            s.push("webgl vendor:" + a.getParameter(a.VENDOR)),
            s.push("webgl version:" + a.getParameter(a.VERSION));
            try {
                var c = a.getExtension("WEBGL_debug_renderer_info");
                c && (s.push("webgl unmasked vendor:" + a.getParameter(c.UNMASKED_VENDOR_WEBGL)),
                s.push("webgl unmasked renderer:" + a.getParameter(c.UNMASKED_RENDERER_WEBGL)))
            } catch (t) {}
            return a.getShaderPrecisionFormat && l(["FLOAT", "INT"], function(o) {
                l(["VERTEX", "FRAGMENT"], function(r) {
                    l(["HIGH", "MEDIUM", "LOW"], function(i) {
                        l(["precision", "rangeMin", "rangeMax"], function(t) {
                            var e = a.getShaderPrecisionFormat(a[r + "_SHADER"], a[i + "_" + o])[t];
                            "precision" !== t && (t = "precision " + t);
                            var n = ["webgl ", r.toLowerCase(), " shader ", i.toLowerCase(), " ", o.toLowerCase(), " ", t, ":", e].join("");
                            s.push(n)
                        })
                    })
                })
            }),
            F(a),
            s
        }
          , O = function() {
            try {
                var t = U()
                  , e = t.getExtension("WEBGL_debug_renderer_info")
                  , n = t.getParameter(e.UNMASKED_VENDOR_WEBGL) + "~" + t.getParameter(e.UNMASKED_RENDERER_WEBGL);
                return F(t),
                n
            } catch (t) {
                return null
            }
        }
          , C = function() {
            var t = document.createElement("div");
            t.innerHTML = "&nbsp;";
            var e = !(t.className = "adsbox");
            try {
                document.body.appendChild(t),
                e = 0 === document.getElementsByClassName("adsbox")[0].offsetHeight,
                document.body.removeChild(t)
            } catch (t) {
                e = !1
            }
            return e
        }
          , B = function() {
            if (void 0 !== navigator.languages)
                try {
                    if (navigator.languages[0].substr(0, 2) !== navigator.language.substr(0, 2))
                        return !0
                } catch (t) {
                    return !0
                }
            return !1
        }
          , D = function() {
            return window.screen.width < window.screen.availWidth || window.screen.height < window.screen.availHeight
        }
          , k = function() {
            var t, e = navigator.userAgent.toLowerCase(), n = navigator.oscpu, i = navigator.platform.toLowerCase();
            if (t = 0 <= e.indexOf("windows phone") ? "Windows Phone" : 0 <= e.indexOf("windows") || 0 <= e.indexOf("win16") || 0 <= e.indexOf("win32") || 0 <= e.indexOf("win64") || 0 <= e.indexOf("win95") || 0 <= e.indexOf("win98") || 0 <= e.indexOf("winnt") || 0 <= e.indexOf("wow64") ? "Windows" : 0 <= e.indexOf("android") ? "Android" : 0 <= e.indexOf("linux") || 0 <= e.indexOf("cros") || 0 <= e.indexOf("x11") ? "Linux" : 0 <= e.indexOf("iphone") || 0 <= e.indexOf("ipad") || 0 <= e.indexOf("ipod") || 0 <= e.indexOf("crios") || 0 <= e.indexOf("fxios") ? "iOS" : 0 <= e.indexOf("macintosh") || 0 <= e.indexOf("mac_powerpc)") ? "Mac" : "Other",
            ("ontouchstart"in window || 0 < navigator.maxTouchPoints || 0 < navigator.msMaxTouchPoints) && "Windows" !== t && "Windows Phone" !== t && "Android" !== t && "iOS" !== t && "Other" !== t && -1 === e.indexOf("cros"))
                return !0;
            if (void 0 !== n) {
                if (0 <= (n = n.toLowerCase()).indexOf("win") && "Windows" !== t && "Windows Phone" !== t)
                    return !0;
                if (0 <= n.indexOf("linux") && "Linux" !== t && "Android" !== t)
                    return !0;
                if (0 <= n.indexOf("mac") && "Mac" !== t && "iOS" !== t)
                    return !0;
                if ((-1 === n.indexOf("win") && -1 === n.indexOf("linux") && -1 === n.indexOf("mac")) != ("Other" === t))
                    return !0
            }
            return 0 <= i.indexOf("win") && "Windows" !== t && "Windows Phone" !== t || ((0 <= i.indexOf("linux") || 0 <= i.indexOf("android") || 0 <= i.indexOf("pike")) && "Linux" !== t && "Android" !== t || ((0 <= i.indexOf("mac") || 0 <= i.indexOf("ipad") || 0 <= i.indexOf("ipod") || 0 <= i.indexOf("iphone")) && "Mac" !== t && "iOS" !== t || !(0 <= i.indexOf("arm") && "Windows Phone" === t) && (!(0 <= i.indexOf("pike") && 0 <= e.indexOf("opera mini")) && ((i.indexOf("win") < 0 && i.indexOf("linux") < 0 && i.indexOf("mac") < 0 && i.indexOf("iphone") < 0 && i.indexOf("ipad") < 0 && i.indexOf("ipod") < 0) !== ("Other" === t) || void 0 === navigator.plugins && "Windows" !== t && "Windows Phone" !== t))))
        }
          , R = function() {
            var t, e = navigator.userAgent.toLowerCase(), n = navigator.productSub;
            if (0 <= e.indexOf("edge/") || 0 <= e.indexOf("iemobile/"))
                return !1;
            if (0 <= e.indexOf("opera mini"))
                return !1;
            if (("Chrome" === (t = 0 <= e.indexOf("firefox/") ? "Firefox" : 0 <= e.indexOf("opera/") || 0 <= e.indexOf(" opr/") ? "Opera" : 0 <= e.indexOf("chrome/") ? "Chrome" : 0 <= e.indexOf("safari/") ? 0 <= e.indexOf("android 1.") || 0 <= e.indexOf("android 2.") || 0 <= e.indexOf("android 3.") || 0 <= e.indexOf("android 4.") ? "AOSP" : "Safari" : 0 <= e.indexOf("trident/") ? "Internet Explorer" : "Other") || "Safari" === t || "Opera" === t) && "20030107" !== n)
                return !0;
            var i, r = eval.toString().length;
            if (37 === r && "Safari" !== t && "Firefox" !== t && "Other" !== t)
                return !0;
            if (39 === r && "Internet Explorer" !== t && "Other" !== t)
                return !0;
            if (33 === r && "Chrome" !== t && "AOSP" !== t && "Opera" !== t && "Other" !== t)
                return !0;
            try {
                throw "a"
            } catch (t) {
                try {
                    t.toSource(),
                    i = !0
                } catch (t) {
                    i = !1
                }
            }
            return i && "Firefox" !== t && "Other" !== t
        }
          , I = function() {
            var t = document.createElement("canvas");
            return !(!t.getContext || !t.getContext("2d"))
        }
          , N = function() {
            if (!I())
                return !1;
            var t = U()
              , e = !!window.WebGLRenderingContext && !!t;
            return F(t),
            e
        }
          , P = function() {
            return "Microsoft Internet Explorer" === navigator.appName || !("Netscape" !== navigator.appName || !/Trident/.test(navigator.userAgent))
        }
          , M = function() {
            return 2 <= ("msWriteProfilerMark"in window) + ("msLaunchUri"in navigator) + ("msSaveBlob"in navigator)
        }
          , L = function() {
            return void 0 !== window.swfobject
        }
          , V = function() {
            return window.swfobject.hasFlashPlayerVersion("9.0.0")
        }
          , j = function(e, t) {
            var n = "___fp_swf_loaded";
            window[n] = function(t) {
                e(t)
            }
            ;
            var i, r, o = t.fonts.swfContainerId;
            (r = document.createElement("div")).setAttribute("id", i.fonts.swfContainerId),
            document.body.appendChild(r);
            var a = {
                onReady: n
            };
            window.swfobject.embedSWF(t.fonts.swfPath, o, "1", "1", "9.0.0", !1, a, {
                allowScriptAccess: "always",
                menu: "false"
            }, {})
        }
          , U = function() {
            var t = document.createElement("canvas")
              , e = null;
            try {
                e = t.getContext("webgl") || t.getContext("experimental-webgl")
            } catch (t) {}
            return e || (e = null),
            e
        }
          , F = function(t) {
            var e = t.getExtension("WEBGL_lose_context");
            null != e && e.loseContext()
        }
          , _ = [{
            key: "userAgent",
            getData: function(t) {
                t(navigator.userAgent)
            }
        }, {
            key: "webdriver",
            getData: function(t, e) {
                t(null == navigator.webdriver ? e.NOT_AVAILABLE : navigator.webdriver)
            }
        }, {
            key: "language",
            getData: function(t, e) {
                t(navigator.language || navigator.userLanguage || navigator.browserLanguage || navigator.systemLanguage || e.NOT_AVAILABLE)
            }
        }, {
            key: "colorDepth",
            getData: function(t, e) {
                t(window.screen.colorDepth || e.NOT_AVAILABLE)
            }
        }, {
            key: "deviceMemory",
            getData: function(t, e) {
                t(navigator.deviceMemory || e.NOT_AVAILABLE)
            }
        }, {
            key: "pixelRatio",
            getData: function(t, e) {
                t(window.devicePixelRatio || e.NOT_AVAILABLE)
            }
        }, {
            key: "hardwareConcurrency",
            getData: function(t, e) {
                t(w(e))
            }
        }, {
            key: "screenResolution",
            getData: function(t, e) {
                t(i(e))
            }
        }, {
            key: "availableScreenResolution",
            getData: function(t, e) {
                t(r(e))
            }
        }, {
            key: "timezoneOffset",
            getData: function(t) {
                t((new Date).getTimezoneOffset())
            }
        }, {
            key: "timezone",
            getData: function(t, e) {
                window.Intl && window.Intl.DateTimeFormat ? t((new window.Intl.DateTimeFormat).resolvedOptions().timeZone || e.NOT_AVAILABLE) : t(e.NOT_AVAILABLE)
            }
        }, {
            key: "sessionStorage",
            getData: function(t, e) {
                t(y(e))
            }
        }, {
            key: "localStorage",
            getData: function(t, e) {
                t(v(e))
            }
        }, {
            key: "indexedDb",
            getData: function(t, e) {
                t(b(e))
            }
        }, {
            key: "addBehavior",
            getData: function(t) {
                t(!!window.HTMLElement.prototype.addBehavior)
            }
        }, {
            key: "openDatabase",
            getData: function(t) {
                t(!!window.openDatabase)
            }
        }, {
            key: "cpuClass",
            getData: function(t, e) {
                t(T(e))
            }
        }, {
            key: "platform",
            getData: function(t, e) {
                t(A(e))
            }
        }, {
            key: "doNotTrack",
            getData: function(t, e) {
                t(E(e))
            }
        }, {
            key: "plugins",
            getData: function(t, e) {
                P() ? e.plugins.excludeIE ? t(e.EXCLUDED) : t(a(e)) : t(o(e))
            }
        }, {
            key: "canvas",
            getData: function(t, e) {
                I() ? t(x(e)) : t(e.NOT_AVAILABLE)
            }
        }, {
            key: "webgl",
            getData: function(t, e) {
                N() ? t(S()) : t(e.NOT_AVAILABLE)
            }
        }, {
            key: "webglVendorAndRenderer",
            getData: function(t) {
                N() ? t(O()) : t()
            }
        }, {
            key: "adBlock",
            getData: function(t) {
                t(C())
            }
        }, {
            key: "hasLiedLanguages",
            getData: function(t) {
                t(B())
            }
        }, {
            key: "hasLiedResolution",
            getData: function(t) {
                t(D())
            }
        }, {
            key: "hasLiedOs",
            getData: function(t) {
                t(k())
            }
        }, {
            key: "hasLiedBrowser",
            getData: function(t) {
                t(R())
            }
        }, {
            key: "touchSupport",
            getData: function(t) {
                t(e())
            }
        }, {
            key: "fonts",
            getData: function(t, e) {
                var u = ["monospace", "sans-serif", "serif"]
                  , h = ["Andale Mono", "Arial", "Arial Black", "Arial Hebrew", "Arial MT", "Arial Narrow", "Arial Rounded MT Bold", "Arial Unicode MS", "Bitstream Vera Sans Mono", "Book Antiqua", "Bookman Old Style", "Calibri", "Cambria", "Cambria Math", "Century", "Century Gothic", "Century Schoolbook", "Comic Sans", "Comic Sans MS", "Consolas", "Courier", "Courier New", "Geneva", "Georgia", "Helvetica", "Helvetica Neue", "Impact", "Lucida Bright", "Lucida Calligraphy", "Lucida Console", "Lucida Fax", "LUCIDA GRANDE", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter", "Lucida Sans Unicode", "Microsoft Sans Serif", "Monaco", "Monotype Corsiva", "MS Gothic", "MS Outlook", "MS PGothic", "MS Reference Sans Serif", "MS Sans Serif", "MS Serif", "MYRIAD", "MYRIAD PRO", "Palatino", "Palatino Linotype", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Symbol", "Tahoma", "Times", "Times New Roman", "Times New Roman PS", "Trebuchet MS", "Verdana", "Wingdings", "Wingdings 2", "Wingdings 3"];
                e.fonts.extendedJsFonts && (h = h.concat(["Abadi MT Condensed Light", "Academy Engraved LET", "ADOBE CASLON PRO", "Adobe Garamond", "ADOBE GARAMOND PRO", "Agency FB", "Aharoni", "Albertus Extra Bold", "Albertus Medium", "Algerian", "Amazone BT", "American Typewriter", "American Typewriter Condensed", "AmerType Md BT", "Andalus", "Angsana New", "AngsanaUPC", "Antique Olive", "Aparajita", "Apple Chancery", "Apple Color Emoji", "Apple SD Gothic Neo", "Arabic Typesetting", "ARCHER", "ARNO PRO", "Arrus BT", "Aurora Cn BT", "AvantGarde Bk BT", "AvantGarde Md BT", "AVENIR", "Ayuthaya", "Bandy", "Bangla Sangam MN", "Bank Gothic", "BankGothic Md BT", "Baskerville", "Baskerville Old Face", "Batang", "BatangChe", "Bauer Bodoni", "Bauhaus 93", "Bazooka", "Bell MT", "Bembo", "Benguiat Bk BT", "Berlin Sans FB", "Berlin Sans FB Demi", "Bernard MT Condensed", "BernhardFashion BT", "BernhardMod BT", "Big Caslon", "BinnerD", "Blackadder ITC", "BlairMdITC TT", "Bodoni 72", "Bodoni 72 Oldstyle", "Bodoni 72 Smallcaps", "Bodoni MT", "Bodoni MT Black", "Bodoni MT Condensed", "Bodoni MT Poster Compressed", "Bookshelf Symbol 7", "Boulder", "Bradley Hand", "Bradley Hand ITC", "Bremen Bd BT", "Britannic Bold", "Broadway", "Browallia New", "BrowalliaUPC", "Brush Script MT", "Californian FB", "Calisto MT", "Calligrapher", "Candara", "CaslonOpnface BT", "Castellar", "Centaur", "Cezanne", "CG Omega", "CG Times", "Chalkboard", "Chalkboard SE", "Chalkduster", "Charlesworth", "Charter Bd BT", "Charter BT", "Chaucer", "ChelthmITC Bk BT", "Chiller", "Clarendon", "Clarendon Condensed", "CloisterBlack BT", "Cochin", "Colonna MT", "Constantia", "Cooper Black", "Copperplate", "Copperplate Gothic", "Copperplate Gothic Bold", "Copperplate Gothic Light", "CopperplGoth Bd BT", "Corbel", "Cordia New", "CordiaUPC", "Cornerstone", "Coronet", "Cuckoo", "Curlz MT", "DaunPenh", "Dauphin", "David", "DB LCD Temp", "DELICIOUS", "Denmark", "DFKai-SB", "Didot", "DilleniaUPC", "DIN", "DokChampa", "Dotum", "DotumChe", "Ebrima", "Edwardian Script ITC", "Elephant", "English 111 Vivace BT", "Engravers MT", "EngraversGothic BT", "Eras Bold ITC", "Eras Demi ITC", "Eras Light ITC", "Eras Medium ITC", "EucrosiaUPC", "Euphemia", "Euphemia UCAS", "EUROSTILE", "Exotc350 Bd BT", "FangSong", "Felix Titling", "Fixedsys", "FONTIN", "Footlight MT Light", "Forte", "FrankRuehl", "Fransiscan", "Freefrm721 Blk BT", "FreesiaUPC", "Freestyle Script", "French Script MT", "FrnkGothITC Bk BT", "Fruitger", "FRUTIGER", "Futura", "Futura Bk BT", "Futura Lt BT", "Futura Md BT", "Futura ZBlk BT", "FuturaBlack BT", "Gabriola", "Galliard BT", "Gautami", "Geeza Pro", "Geometr231 BT", "Geometr231 Hv BT", "Geometr231 Lt BT", "GeoSlab 703 Lt BT", "GeoSlab 703 XBd BT", "Gigi", "Gill Sans", "Gill Sans MT", "Gill Sans MT Condensed", "Gill Sans MT Ext Condensed Bold", "Gill Sans Ultra Bold", "Gill Sans Ultra Bold Condensed", "Gisha", "Gloucester MT Extra Condensed", "GOTHAM", "GOTHAM BOLD", "Goudy Old Style", "Goudy Stout", "GoudyHandtooled BT", "GoudyOLSt BT", "Gujarati Sangam MN", "Gulim", "GulimChe", "Gungsuh", "GungsuhChe", "Gurmukhi MN", "Haettenschweiler", "Harlow Solid Italic", "Harrington", "Heather", "Heiti SC", "Heiti TC", "HELV", "Herald", "High Tower Text", "Hiragino Kaku Gothic ProN", "Hiragino Mincho ProN", "Hoefler Text", "Humanst 521 Cn BT", "Humanst521 BT", "Humanst521 Lt BT", "Imprint MT Shadow", "Incised901 Bd BT", "Incised901 BT", "Incised901 Lt BT", "INCONSOLATA", "Informal Roman", "Informal011 BT", "INTERSTATE", "IrisUPC", "Iskoola Pota", "JasmineUPC", "Jazz LET", "Jenson", "Jester", "Jokerman", "Juice ITC", "Kabel Bk BT", "Kabel Ult BT", "Kailasa", "KaiTi", "Kalinga", "Kannada Sangam MN", "Kartika", "Kaufmann Bd BT", "Kaufmann BT", "Khmer UI", "KodchiangUPC", "Kokila", "Korinna BT", "Kristen ITC", "Krungthep", "Kunstler Script", "Lao UI", "Latha", "Leelawadee", "Letter Gothic", "Levenim MT", "LilyUPC", "Lithograph", "Lithograph Light", "Long Island", "Lydian BT", "Magneto", "Maiandra GD", "Malayalam Sangam MN", "Malgun Gothic", "Mangal", "Marigold", "Marion", "Marker Felt", "Market", "Marlett", "Matisse ITC", "Matura MT Script Capitals", "Meiryo", "Meiryo UI", "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Tai Le", "Microsoft Uighur", "Microsoft YaHei", "Microsoft Yi Baiti", "MingLiU", "MingLiU_HKSCS", "MingLiU_HKSCS-ExtB", "MingLiU-ExtB", "Minion", "Minion Pro", "Miriam", "Miriam Fixed", "Mistral", "Modern", "Modern No. 20", "Mona Lisa Solid ITC TT", "Mongolian Baiti", "MONO", "MoolBoran", "Mrs Eaves", "MS LineDraw", "MS Mincho", "MS PMincho", "MS Reference Specialty", "MS UI Gothic", "MT Extra", "MUSEO", "MV Boli", "Nadeem", "Narkisim", "NEVIS", "News Gothic", "News GothicMT", "NewsGoth BT", "Niagara Engraved", "Niagara Solid", "Noteworthy", "NSimSun", "Nyala", "OCR A Extended", "Old Century", "Old English Text MT", "Onyx", "Onyx BT", "OPTIMA", "Oriya Sangam MN", "OSAKA", "OzHandicraft BT", "Palace Script MT", "Papyrus", "Parchment", "Party LET", "Pegasus", "Perpetua", "Perpetua Titling MT", "PetitaBold", "Pickwick", "Plantagenet Cherokee", "Playbill", "PMingLiU", "PMingLiU-ExtB", "Poor Richard", "Poster", "PosterBodoni BT", "PRINCETOWN LET", "Pristina", "PTBarnum BT", "Pythagoras", "Raavi", "Rage Italic", "Ravie", "Ribbon131 Bd BT", "Rockwell", "Rockwell Condensed", "Rockwell Extra Bold", "Rod", "Roman", "Sakkal Majalla", "Santa Fe LET", "Savoye LET", "Sceptre", "Script", "Script MT Bold", "SCRIPTINA", "Serifa", "Serifa BT", "Serifa Th BT", "ShelleyVolante BT", "Sherwood", "Shonar Bangla", "Showcard Gothic", "Shruti", "Signboard", "SILKSCREEN", "SimHei", "Simplified Arabic", "Simplified Arabic Fixed", "SimSun", "SimSun-ExtB", "Sinhala Sangam MN", "Sketch Rockwell", "Skia", "Small Fonts", "Snap ITC", "Snell Roundhand", "Socket", "Souvenir Lt BT", "Staccato222 BT", "Steamer", "Stencil", "Storybook", "Styllo", "Subway", "Swis721 BlkEx BT", "Swiss911 XCm BT", "Sylfaen", "Synchro LET", "System", "Tamil Sangam MN", "Technical", "Teletype", "Telugu Sangam MN", "Tempus Sans ITC", "Terminal", "Thonburi", "Traditional Arabic", "Trajan", "TRAJAN PRO", "Tristan", "Tubular", "Tunga", "Tw Cen MT", "Tw Cen MT Condensed", "Tw Cen MT Condensed Extra Bold", "TypoUpright BT", "Unicorn", "Univers", "Univers CE 55 Medium", "Univers Condensed", "Utsaah", "Vagabond", "Vani", "Vijaya", "Viner Hand ITC", "VisualUI", "Vivaldi", "Vladimir Script", "Vrinda", "Westminster", "WHITNEY", "Wide Latin", "ZapfEllipt BT", "ZapfHumnst BT", "ZapfHumnst Dm BT", "Zapfino", "Zurich BlkEx BT", "Zurich Ex BT", "ZWAdobeF"]));
                h = (h = h.concat(e.fonts.userDefinedFonts)).filter(function(t, e) {
                    return h.indexOf(t) === e
                });
                var n = document.getElementsByTagName("body")[0]
                  , r = document.createElement("div")
                  , d = document.createElement("div")
                  , i = {}
                  , o = {}
                  , f = function() {
                    var t = document.createElement("span");
                    return t.style.position = "absolute",
                    t.style.left = "-9999px",
                    t.style.fontSize = "72px",
                    t.style.fontStyle = "normal",
                    t.style.fontWeight = "normal",
                    t.style.letterSpacing = "normal",
                    t.style.lineBreak = "auto",
                    t.style.lineHeight = "normal",
                    t.style.textTransform = "none",
                    t.style.textAlign = "left",
                    t.style.textDecoration = "none",
                    t.style.textShadow = "none",
                    t.style.whiteSpace = "normal",
                    t.style.wordBreak = "normal",
                    t.style.wordSpacing = "normal",
                    t.innerHTML = "mmmmmmmmmmlli",
                    t
                }
                  , a = function(t) {
                    for (var e = !1, n = 0; n < u.length; n++)
                        if (e = t[n].offsetWidth !== i[u[n]] || t[n].offsetHeight !== o[u[n]])
                            return e;
                    return e
                }
                  , s = function() {
                    for (var t = [], e = 0, n = u.length; e < n; e++) {
                        var i = f();
                        i.style.fontFamily = u[e],
                        r.appendChild(i),
                        t.push(i)
                    }
                    return t
                }();
                n.appendChild(r);
                for (var c = 0, l = u.length; c < l; c++)
                    i[u[c]] = s[c].offsetWidth,
                    o[u[c]] = s[c].offsetHeight;
                var p = function() {
                    for (var t, e, n, i = {}, r = 0, o = h.length; r < o; r++) {
                        for (var a = [], s = 0, c = u.length; s < c; s++) {
                            var l = (t = h[r],
                            e = u[s],
                            n = void 0,
                            (n = f()).style.fontFamily = "'" + t + "'," + e,
                            n);
                            d.appendChild(l),
                            a.push(l)
                        }
                        i[h[r]] = a
                    }
                    return i
                }();
                n.appendChild(d);
                for (var g = [], m = 0, y = h.length; m < y; m++)
                    a(p[h[m]]) && g.push(h[m]);
                n.removeChild(d),
                n.removeChild(r),
                t(g)
            },
            pauseBefore: !0
        }, {
            key: "fontsFlash",
            getData: function(e, t) {
                return L() ? V() ? t.fonts.swfPath ? void j(function(t) {
                    e(t)
                }, t) : e("missing options.fonts.swfPath") : e("flash not installed") : e("swf object not loaded")
            },
            pauseBefore: !0
        }, {
            key: "audio",
            getData: function(n, t) {
                var e = t.audio;
                if (e.excludeIOS11 && navigator.userAgent.match(/OS 11.+Version\/11.+Safari/))
                    return n(t.EXCLUDED);
                var i = window.OfflineAudioContext || window.webkitOfflineAudioContext;
                if (null == i)
                    return n(t.NOT_AVAILABLE);
                var r = new i(1,44100,44100)
                  , o = r.createOscillator();
                o.type = "triangle",
                o.frequency.setValueAtTime(1e4, r.currentTime);
                var a = r.createDynamicsCompressor();
                l([["threshold", -50], ["knee", 40], ["ratio", 12], ["reduction", -20], ["attack", 0], ["release", .25]], function(t) {
                    void 0 !== a[t[0]] && "function" == typeof a[t[0]].setValueAtTime && a[t[0]].setValueAtTime(t[1], r.currentTime)
                }),
                o.connect(a),
                a.connect(r.destination),
                o.start(0),
                r.startRendering();
                var s = setTimeout(function() {
                    return console.warn('Audio fingerprint timed out. Please report bug at https://github.com/fingerprintjs/fingerprintjs with your user agent: "' + navigator.userAgent + '".'),
                    r.oncomplete = function() {}
                    ,
                    r = null,
                    n("audioTimeout")
                }, e.timeout);
                r.oncomplete = function(t) {
                    var e;
                    try {
                        clearTimeout(s),
                        e = t.renderedBuffer.getChannelData(0).slice(4500, 5e3).reduce(function(t, e) {
                            return t + Math.abs(e)
                        }, 0).toString(),
                        o.disconnect(),
                        a.disconnect()
                    } catch (t) {
                        return void n(t)
                    }
                    n(e)
                }
            }
        }, {
            key: "enumerateDevices",
            getData: function(e, t) {
                if (!n())
                    return e(t.NOT_AVAILABLE);
                navigator.mediaDevices.enumerateDevices().then(function(t) {
                    e(t.map(function(t) {
                        return "id=" + t.deviceId + ";gid=" + t.groupId + ";" + t.kind + ";" + t.label
                    }))
                }).catch(function(t) {
                    e(t)
                })
            }
        }]
          , H = function(t) {
            throw new Error("'new Fingerprint()' is deprecated, see https://github.com/fingerprintjs/fingerprintjs#upgrade-guide-from-182-to-200")
        };
        return H.get = function(n, i) {
            i ? n || (n = {}) : (i = n,
            n = {}),
            function(t, e) {
                if (null == e)
                    return;
                var n, i;
                for (i in e)
                    null == (n = e[i]) || Object.prototype.hasOwnProperty.call(t, i) || (t[i] = n)
            }(n, t),
            n.components = n.extraComponents.concat(_);
            var r = {
                data: [],
                addPreprocessedComponent: function(t, e) {
                    "function" == typeof n.preprocessor && (e = n.preprocessor(t, e)),
                    r.data.push({
                        key: t,
                        value: e
                    })
                }
            }
              , o = -1
              , a = function(t) {
                if ((o += 1) >= n.components.length)
                    i(r.data);
                else {
                    var e = n.components[o];
                    if (n.excludes[e.key])
                        a(!1);
                    else {
                        if (!t && e.pauseBefore)
                            return o -= 1,
                            void setTimeout(function() {
                                a(!0)
                            }, 1);
                        try {
                            e.getData(function(t) {
                                r.addPreprocessedComponent(e.key, t),
                                a(!1)
                            }, n)
                        } catch (t) {
                            r.addPreprocessedComponent(e.key, String(t)),
                            a(!1)
                        }
                    }
                }
            };
            a(!1)
        }
        ,
        H.getPromise = function(n) {
            return new Promise(function(t, e) {
                H.get(n, t)
            }
            )
        }
        ,
        H.getV18 = function(o, a) {
            return null == a && (a = o,
            o = {}),
            H.get(o, function(t) {
                for (var e = [], n = 0; n < t.length; n++) {
                    var i = t[n];
                    if (i.value === (o.NOT_AVAILABLE || "not available"))
                        e.push({
                            key: i.key,
                            value: "unknown"
                        });
                    else if ("plugins" === i.key)
                        e.push({
                            key: "plugins",
                            value: c(i.value, function(t) {
                                var e = c(t[2], function(t) {
                                    return t.join ? t.join("~") : t
                                }).join(",");
                                return [t[0], t[1], e].join("::")
                            })
                        });
                    else if (-1 !== ["canvas", "webgl"].indexOf(i.key) && Array.isArray(i.value))
                        e.push({
                            key: i.key,
                            value: i.value.join("~")
                        });
                    else if (-1 !== ["sessionStorage", "localStorage", "indexedDb", "addBehavior", "openDatabase"].indexOf(i.key)) {
                        if (!i.value)
                            continue;
                        e.push({
                            key: i.key,
                            value: 1
                        })
                    } else
                        i.value ? e.push(i.value.join ? {
                            key: i.key,
                            value: i.value.join(";")
                        } : i) : e.push({
                            key: i.key,
                            value: i.value
                        })
                }
                var r = s(c(e, function(t) {
                    return t.value
                }).join("~~~"), 31);
                a(r, e)
            })
        }
        ,
        H.x64hash128 = s,
        H.VERSION = "2.1.4",
        H
    })
}
, function(t, e) {
    t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8BAMAAADI0sRBAAAAElBMVEVHcEyPj7V3fp52fZ52fZ52fZ5Xt/B6AAAABXRSTlMABraK6T5p8dIAAABjSURBVDjLY2AYBQMOGE2cBfBIM4eGKuKRZgkNDRLAK41PO9BwfNoZVfFrFxrVDgHCrqHYAEy7KVbZ0GCoNHbNoSHESRMwnIDTSA0XAsEyEjUTyEQEsiCBDEwg+xMoPEYBzQEAYlpTdYl6u9gAAAAASUVORK5CYII="
}
, function(t, e) {
    t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8BAMAAADI0sRBAAAAD1BMVEVHcExSxBpSxBpV1CpSxBqRg39rAAAABHRSTlMAiOYGvfLd/QAAAFFJREFUOMtjYBgFwwsYKgkjOMxCigaoUiIujggBRhcXAQQPJKXi4oQQYHJxUUDwQFIuLi4IARYXFwcEDyQ1Kj0qPSykCWQDApmIQBYcBcMLAACpu0NXK5UQPQAAAABJRU5ErkJggg=="
}
, function(t, e) {
    t.exports = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAR0AAADIBAMAAAAnwChgAAAAIVBMVEVHcEwZ+igZ+igZ+igZ+igZ+igZ+igZ+igZ+igZ+yga+ilF3P5FAAAACnRSTlMAyq2S5ndCXSoTIhVgFQAABDtJREFUeNrtnT1vGkEQhg+OT1e2EkUJlatEosLtVUkTIVcuIyqUpIkriqShIpKLiAqkVKkIISbZX2kLxUFm975mZ3ZepNve+OUBdveem9mLIoTRurh882oWoYxW39yP9Rglz8jsxi+QOLH5N04x8vQe8qwh4tTN/3GOkKe/z7PFwmN+YuExZozz49qNgXqe5FGecyw85jXI1IySp2mw8hzg0V4xDvFof5+nh3kmqnHah3HMDAvPGgzPrWqeayvPlequ2WB9XDYe1dmnY8XR3f3M0fFswPCorqVdMDw/0PEYVTwnVpyVap5LLDwNK85fMDyLCk8WHtV9Yc2K80cVTw8dzy0YnnGFJ8U/6eOpW3G2YHgmFZ79SLCuAWMrzu8KDy6ekZVnoBnH0nPKt7zg8egKFkvP6erUdoUna7TA/BOYnqvwZI5Kzx0VHjQ9B+afvld67rj90wLLIOji6VV67qjxVHouU7Cg6bnKP1V4hP1T58snIP/UvbhfgJ+MYfB8llJDNDwP37lnAfAU8E8dMdVJ03MNMddJ03OJlAum6bm2mAwekfxTTWouJ+q5E6nJnKjn5kKLXZvon6ZCq92U6J8Smd0AWc/1ZTaTZD2XiGy2W2T/NBXZbdP13CHYDQegziVZz1nv5C1Dnhu6f7IuHzczATzG45s31NVzCTsgP3u5tP74uWeepZd/csyknoB6fnrOXmleqOo5x0q84MVTkjcvIH8959jJLRTxUHe6cv6J80Y9S3kYHyAePccHiMk/cVV6cPmnmKkSJuHScwkLoJhNz/EAYiwP4wDEWR7GAYi1eq7v/WK85WF1b9jM5WG+gLir53wBsVfP+QHir57zm+wFysN6HrO9RPVczQOQRPVclw6IqufKXsltyXhOGfJ0qTeDparnbojbTanqOYdIKgKoRfdPpQEV8VMfxcrDSIDk8Lje6pAAdcWWx2FqZ6WZcpaHXZf2U19Fq+dK+ynHpBVxjrL6Zenpn5j9VNdTz3EDki8PK+enApSHldEv9QDVc2W2wv0Q1XPFAYUpDysOKFD3ZlFAoarnitoFNv/Eo1/4/BMPoGB4igEKh6cYoKDdm/n/rBm0ezNfv4zCNrfm6ZfQ3Zt5gIJ3b2YDCt/cmu2npuGbW7P0i0b3ZpafUuneTAek09yaDkipuTXNT2l1b6Y1c6h1b7r1iy1YQjW3Npx+Ss4/kQBJ+qfygIYO/xQMj6PYafNNEY+rlfVMtXvTcdScbvfmPDfOKmieTm6eRQQFKHT3ZgcLj2u10u3ebGXmmQXPkwlIo7k1C9BYIY9jO6jbvdnGwpMOSKu5NQ3QRCmP42pdt3uziYXHDUjz9DAXoCvFPA5AuoerxVh4bMOp/TyhGOlwNRuQ/uOW6lh4HhtOhIct1VEOV7MBYTyLqoZxepj9E8PAs1/FBiB5ove7OC8jmPHh6ebsndir3wFXkAz2i2iqAQAAAABJRU5ErkJggg=="
}
, function(t, e, n) {
    var i, r, o, a, u, s, c, l;
    t.exports = (i = n(0),
    n(15),
    n(16),
    o = (r = i).lib,
    a = o.Base,
    u = o.WordArray,
    s = r.algo,
    c = s.MD5,
    l = s.EvpKDF = a.extend({
        cfg: a.extend({
            keySize: 4,
            hasher: c,
            iterations: 1
        }),
        init: function(t) {
            this.cfg = this.cfg.extend(t)
        },
        compute: function(t, e) {
            for (var n = this.cfg, i = n.hasher.create(), r = u.create(), o = r.words, a = n.keySize, s = n.iterations; o.length < a; ) {
                c && i.update(c);
                var c = i.update(t).finalize(e);
                i.reset();
                for (var l = 1; l < s; l++)
                    c = i.finalize(c),
                    i.reset();
                r.concat(c)
            }
            return r.sigBytes = 4 * a,
            r
        }
    }),
    r.EvpKDF = function(t, e, n) {
        return l.create(n).compute(t, e)
    }
    ,
    i.EvpKDF)
}
, function(t, e, n) {
    var r;
    t.exports = (r = n(0),
    n(13),
    n(14),
    n(9),
    n(17),
    function() {
        var t = r
          , e = t.lib.BlockCipher
          , n = t.algo
          , l = []
          , u = []
          , h = []
          , d = []
          , f = []
          , p = []
          , g = []
          , m = []
          , y = []
          , v = [];
        !function() {
            for (var t = [], e = 0; e < 256; e++)
                t[e] = e < 128 ? e << 1 : e << 1 ^ 283;
            var n = 0
              , i = 0;
            for (e = 0; e < 256; e++) {
                var r = i ^ i << 1 ^ i << 2 ^ i << 3 ^ i << 4;
                r = r >>> 8 ^ 255 & r ^ 99,
                l[n] = r;
                var o = t[u[r] = n]
                  , a = t[o]
                  , s = t[a]
                  , c = 257 * t[r] ^ 16843008 * r;
                h[n] = c << 24 | c >>> 8,
                d[n] = c << 16 | c >>> 16,
                f[n] = c << 8 | c >>> 24,
                p[n] = c,
                c = 16843009 * s ^ 65537 * a ^ 257 * o ^ 16843008 * n,
                g[r] = c << 24 | c >>> 8,
                m[r] = c << 16 | c >>> 16,
                y[r] = c << 8 | c >>> 24,
                v[r] = c,
                n ? (n = o ^ t[t[t[s ^ o]]],
                i ^= t[t[i]]) : n = i = 1
            }
        }();
        var b = [0, 1, 2, 4, 8, 16, 32, 64, 128, 27, 54]
          , i = n.AES = e.extend({
            _doReset: function() {
                if (!this._nRounds || this._keyPriorReset !== this._key) {
                    for (var t = this._keyPriorReset = this._key, e = t.words, n = t.sigBytes / 4, i = 4 * ((this._nRounds = n + 6) + 1), r = this._keySchedule = [], o = 0; o < i; o++)
                        if (o < n)
                            r[o] = e[o];
                        else {
                            var a = r[o - 1];
                            o % n ? 6 < n && o % n == 4 && (a = l[a >>> 24] << 24 | l[a >>> 16 & 255] << 16 | l[a >>> 8 & 255] << 8 | l[255 & a]) : (a = l[(a = a << 8 | a >>> 24) >>> 24] << 24 | l[a >>> 16 & 255] << 16 | l[a >>> 8 & 255] << 8 | l[255 & a],
                            a ^= b[o / n | 0] << 24),
                            r[o] = r[o - n] ^ a
                        }
                    for (var s = this._invKeySchedule = [], c = 0; c < i; c++)
                        o = i - c,
                        a = c % 4 ? r[o] : r[o - 4],
                        s[c] = c < 4 || o <= 4 ? a : g[l[a >>> 24]] ^ m[l[a >>> 16 & 255]] ^ y[l[a >>> 8 & 255]] ^ v[l[255 & a]]
                }
            },
            encryptBlock: function(t, e) {
                this._doCryptBlock(t, e, this._keySchedule, h, d, f, p, l)
            },
            decryptBlock: function(t, e) {
                var n = t[e + 1];
                t[e + 1] = t[e + 3],
                t[e + 3] = n,
                this._doCryptBlock(t, e, this._invKeySchedule, g, m, y, v, u),
                n = t[e + 1],
                t[e + 1] = t[e + 3],
                t[e + 3] = n
            },
            _doCryptBlock: function(t, e, n, i, r, o, a, s) {
                for (var c = this._nRounds, l = t[e] ^ n[0], u = t[e + 1] ^ n[1], h = t[e + 2] ^ n[2], d = t[e + 3] ^ n[3], f = 4, p = 1; p < c; p++) {
                    var g = i[l >>> 24] ^ r[u >>> 16 & 255] ^ o[h >>> 8 & 255] ^ a[255 & d] ^ n[f++]
                      , m = i[u >>> 24] ^ r[h >>> 16 & 255] ^ o[d >>> 8 & 255] ^ a[255 & l] ^ n[f++]
                      , y = i[h >>> 24] ^ r[d >>> 16 & 255] ^ o[l >>> 8 & 255] ^ a[255 & u] ^ n[f++]
                      , v = i[d >>> 24] ^ r[l >>> 16 & 255] ^ o[u >>> 8 & 255] ^ a[255 & h] ^ n[f++];
                    l = g,
                    u = m,
                    h = y,
                    d = v
                }
                g = (s[l >>> 24] << 24 | s[u >>> 16 & 255] << 16 | s[h >>> 8 & 255] << 8 | s[255 & d]) ^ n[f++],
                m = (s[u >>> 24] << 24 | s[h >>> 16 & 255] << 16 | s[d >>> 8 & 255] << 8 | s[255 & l]) ^ n[f++],
                y = (s[h >>> 24] << 24 | s[d >>> 16 & 255] << 16 | s[l >>> 8 & 255] << 8 | s[255 & u]) ^ n[f++],
                v = (s[d >>> 24] << 24 | s[l >>> 16 & 255] << 16 | s[u >>> 8 & 255] << 8 | s[255 & h]) ^ n[f++],
                t[e] = g,
                t[e + 1] = m,
                t[e + 2] = y,
                t[e + 3] = v
            },
            keySize: 8
        });
        t.AES = e._createHelper(i)
    }(),
    r.AES)
}
, function(t, e, n) {
    !function(t) {
        "use strict";
        var e = "0123456789abcdefghijklmnopqrstuvwxyz";
        function c(t) {
            return e.charAt(t)
        }
        function n(t, e) {
            return t & e
        }
        function l(t, e) {
            return t | e
        }
        function i(t, e) {
            return t ^ e
        }
        function r(t, e) {
            return t & ~e
        }
        function o(t) {
            if (0 == t)
                return -1;
            var e = 0;
            return 0 == (65535 & t) && (t >>= 16,
            e += 16),
            0 == (255 & t) && (t >>= 8,
            e += 8),
            0 == (15 & t) && (t >>= 4,
            e += 4),
            0 == (3 & t) && (t >>= 2,
            e += 2),
            0 == (1 & t) && ++e,
            e
        }
        function a(t) {
            for (var e = 0; 0 != t; )
                t &= t - 1,
                ++e;
            return e
        }
        var s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        function u(t) {
            var e, n, i = "";
            for (e = 0; e + 3 <= t.length; e += 3)
                n = parseInt(t.substring(e, e + 3), 16),
                i += s.charAt(n >> 6) + s.charAt(63 & n);
            for (e + 1 == t.length ? (n = parseInt(t.substring(e, e + 1), 16),
            i += s.charAt(n << 2)) : e + 2 == t.length && (n = parseInt(t.substring(e, e + 2), 16),
            i += s.charAt(n >> 2) + s.charAt((3 & n) << 4)); 0 < (3 & i.length); )
                i += "=";
            return i
        }
        function h(t) {
            var e, n = "", i = 0, r = 0;
            for (e = 0; e < t.length && "=" != t.charAt(e); ++e) {
                var o = s.indexOf(t.charAt(e));
                o < 0 || (i = 0 == i ? (n += c(o >> 2),
                r = 3 & o,
                1) : 1 == i ? (n += c(r << 2 | o >> 4),
                r = 15 & o,
                2) : 2 == i ? (n += c(r),
                n += c(o >> 2),
                r = 3 & o,
                3) : (n += c(r << 2 | o >> 4),
                n += c(15 & o),
                0))
            }
            return 1 == i && (n += c(r << 2)),
            n
        }
        var d, f, p = function(t, e) {
            return (p = Object.setPrototypeOf || {
                __proto__: []
            }instanceof Array && function(t, e) {
                t.__proto__ = e
            }
            || function(t, e) {
                for (var n in e)
                    e.hasOwnProperty(n) && (t[n] = e[n])
            }
            )(t, e)
        }, g = {
            decode: function(t) {
                var e;
                if (void 0 === d) {
                    var n = "0123456789ABCDEF"
                      , i = " \f\n\r\t \u2028\u2029";
                    for (d = {},
                    e = 0; e < 16; ++e)
                        d[n.charAt(e)] = e;
                    for (n = n.toLowerCase(),
                    e = 10; e < 16; ++e)
                        d[n.charAt(e)] = e;
                    for (e = 0; e < i.length; ++e)
                        d[i.charAt(e)] = -1
                }
                var r = []
                  , o = 0
                  , a = 0;
                for (e = 0; e < t.length; ++e) {
                    var s = t.charAt(e);
                    if ("=" == s)
                        break;
                    if (-1 != (s = d[s])) {
                        if (void 0 === s)
                            throw new Error("Illegal character at offset " + e);
                        o |= s,
                        2 <= ++a ? (r[r.length] = o,
                        a = o = 0) : o <<= 4
                    }
                }
                if (a)
                    throw new Error("Hex encoding incomplete: 4 bits missing");
                return r
            }
        }, m = {
            decode: function(t) {
                var e;
                if (void 0 === f) {
                    var n = "= \f\n\r\t \u2028\u2029";
                    for (f = Object.create(null),
                    e = 0; e < 64; ++e)
                        f["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(e)] = e;
                    for (e = 0; e < n.length; ++e)
                        f[n.charAt(e)] = -1
                }
                var i = []
                  , r = 0
                  , o = 0;
                for (e = 0; e < t.length; ++e) {
                    var a = t.charAt(e);
                    if ("=" == a)
                        break;
                    if (-1 != (a = f[a])) {
                        if (void 0 === a)
                            throw new Error("Illegal character at offset " + e);
                        r |= a,
                        4 <= ++o ? (i[i.length] = r >> 16,
                        i[i.length] = r >> 8 & 255,
                        i[i.length] = 255 & r,
                        o = r = 0) : r <<= 6
                    }
                }
                switch (o) {
                case 1:
                    throw new Error("Base64 encoding incomplete: at least 2 bits missing");
                case 2:
                    i[i.length] = r >> 10;
                    break;
                case 3:
                    i[i.length] = r >> 16,
                    i[i.length] = r >> 8 & 255
                }
                return i
            },
            re: /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
            unarmor: function(t) {
                var e = m.re.exec(t);
                if (e)
                    if (e[1])
                        t = e[1];
                    else {
                        if (!e[2])
                            throw new Error("RegExp out of sync");
                        t = e[2]
                    }
                return m.decode(t)
            }
        }, y = 1e13, v = function() {
            function t(t) {
                this.buf = [+t || 0]
            }
            return t.prototype.mulAdd = function(t, e) {
                var n, i, r = this.buf, o = r.length;
                for (n = 0; n < o; ++n)
                    (i = r[n] * t + e) < y ? e = 0 : i -= (e = 0 | i / y) * y,
                    r[n] = i;
                0 < e && (r[n] = e)
            }
            ,
            t.prototype.sub = function(t) {
                var e, n, i = this.buf, r = i.length;
                for (e = 0; e < r; ++e)
                    n = i[e] - t,
                    t = n < 0 ? (n += y,
                    1) : 0,
                    i[e] = n;
                for (; 0 === i[i.length - 1]; )
                    i.pop()
            }
            ,
            t.prototype.toString = function(t) {
                if (10 != (t || 10))
                    throw new Error("only base 10 is supported");
                for (var e = this.buf, n = e[e.length - 1].toString(), i = e.length - 2; 0 <= i; --i)
                    n += (y + e[i]).toString().substring(1);
                return n
            }
            ,
            t.prototype.valueOf = function() {
                for (var t = this.buf, e = 0, n = t.length - 1; 0 <= n; --n)
                    e = e * y + t[n];
                return e
            }
            ,
            t.prototype.simplify = function() {
                var t = this.buf;
                return 1 == t.length ? t[0] : this
            }
            ,
            t
        }(), b = "…", w = /^(\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/, T = /^(\d\d\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/;
        function A(t, e) {
            return t.length > e && (t = t.substring(0, e) + b),
            t
        }
        var E, x = function() {
            function n(t, e) {
                this.hexDigits = "0123456789ABCDEF",
                this.pos = t instanceof n ? (this.enc = t.enc,
                t.pos) : (this.enc = t,
                e)
            }
            return n.prototype.get = function(t) {
                if (void 0 === t && (t = this.pos++),
                t >= this.enc.length)
                    throw new Error("Requesting byte offset " + t + " on a stream of length " + this.enc.length);
                return "string" == typeof this.enc ? this.enc.charCodeAt(t) : this.enc[t]
            }
            ,
            n.prototype.hexByte = function(t) {
                return this.hexDigits.charAt(t >> 4 & 15) + this.hexDigits.charAt(15 & t)
            }
            ,
            n.prototype.hexDump = function(t, e, n) {
                for (var i = "", r = t; r < e; ++r)
                    if (i += this.hexByte(this.get(r)),
                    !0 !== n)
                        switch (15 & r) {
                        case 7:
                            i += "  ";
                            break;
                        case 15:
                            i += "\n";
                            break;
                        default:
                            i += " "
                        }
                return i
            }
            ,
            n.prototype.isASCII = function(t, e) {
                for (var n = t; n < e; ++n) {
                    var i = this.get(n);
                    if (i < 32 || 176 < i)
                        return !1
                }
                return !0
            }
            ,
            n.prototype.parseStringISO = function(t, e) {
                for (var n = "", i = t; i < e; ++i)
                    n += String.fromCharCode(this.get(i));
                return n
            }
            ,
            n.prototype.parseStringUTF = function(t, e) {
                for (var n = "", i = t; i < e; ) {
                    var r = this.get(i++);
                    n += r < 128 ? String.fromCharCode(r) : 191 < r && r < 224 ? String.fromCharCode((31 & r) << 6 | 63 & this.get(i++)) : String.fromCharCode((15 & r) << 12 | (63 & this.get(i++)) << 6 | 63 & this.get(i++))
                }
                return n
            }
            ,
            n.prototype.parseStringBMP = function(t, e) {
                for (var n, i, r = "", o = t; o < e; )
                    n = this.get(o++),
                    i = this.get(o++),
                    r += String.fromCharCode(n << 8 | i);
                return r
            }
            ,
            n.prototype.parseTime = function(t, e, n) {
                var i = this.parseStringISO(t, e)
                  , r = (n ? w : T).exec(i);
                return r ? (n && (r[1] = +r[1],
                r[1] += +r[1] < 70 ? 2e3 : 1900),
                i = r[1] + "-" + r[2] + "-" + r[3] + " " + r[4],
                r[5] && (i += ":" + r[5],
                r[6] && (i += ":" + r[6],
                r[7] && (i += "." + r[7]))),
                r[8] && (i += " UTC",
                "Z" != r[8] && (i += r[8],
                r[9] && (i += ":" + r[9]))),
                i) : "Unrecognized time: " + i
            }
            ,
            n.prototype.parseInteger = function(t, e) {
                for (var n, i = this.get(t), r = 127 < i, o = r ? 255 : 0, a = ""; i == o && ++t < e; )
                    i = this.get(t);
                if (0 == (n = e - t))
                    return r ? -1 : 0;
                if (4 < n) {
                    for (a = i,
                    n <<= 3; 0 == (128 & (+a ^ o)); )
                        a = +a << 1,
                        --n;
                    a = "(" + n + " bit)\n"
                }
                r && (i -= 256);
                for (var s = new v(i), c = t + 1; c < e; ++c)
                    s.mulAdd(256, this.get(c));
                return a + s.toString()
            }
            ,
            n.prototype.parseBitString = function(t, e, n) {
                for (var i = this.get(t), r = (e - t - 1 << 3) - i, o = "(" + r + " bit)\n", a = "", s = t + 1; s < e; ++s) {
                    for (var c = this.get(s), l = s == e - 1 ? i : 0, u = 7; l <= u; --u)
                        a += c >> u & 1 ? "1" : "0";
                    if (a.length > n)
                        return o + A(a, n)
                }
                return o + a
            }
            ,
            n.prototype.parseOctetString = function(t, e, n) {
                if (this.isASCII(t, e))
                    return A(this.parseStringISO(t, e), n);
                var i = e - t
                  , r = "(" + i + " byte)\n";
                (n /= 2) < i && (e = t + n);
                for (var o = t; o < e; ++o)
                    r += this.hexByte(this.get(o));
                return n < i && (r += b),
                r
            }
            ,
            n.prototype.parseOID = function(t, e, n) {
                for (var i = "", r = new v, o = 0, a = t; a < e; ++a) {
                    var s = this.get(a);
                    if (r.mulAdd(128, 127 & s),
                    o += 7,
                    !(128 & s)) {
                        if ("" === i)
                            if ((r = r.simplify())instanceof v)
                                r.sub(80),
                                i = "2." + r.toString();
                            else {
                                var c = r < 80 ? r < 40 ? 0 : 1 : 2;
                                i = c + "." + (r - 40 * c)
                            }
                        else
                            i += "." + r.toString();
                        if (i.length > n)
                            return A(i, n);
                        r = new v,
                        o = 0
                    }
                }
                return 0 < o && (i += ".incomplete"),
                i
            }
            ,
            n
        }(), S = function() {
            function u(t, e, n, i, r) {
                if (!(i instanceof O))
                    throw new Error("Invalid tag value.");
                this.stream = t,
                this.header = e,
                this.length = n,
                this.tag = i,
                this.sub = r
            }
            return u.prototype.typeName = function() {
                switch (this.tag.tagClass) {
                case 0:
                    switch (this.tag.tagNumber) {
                    case 0:
                        return "EOC";
                    case 1:
                        return "BOOLEAN";
                    case 2:
                        return "INTEGER";
                    case 3:
                        return "BIT_STRING";
                    case 4:
                        return "OCTET_STRING";
                    case 5:
                        return "NULL";
                    case 6:
                        return "OBJECT_IDENTIFIER";
                    case 7:
                        return "ObjectDescriptor";
                    case 8:
                        return "EXTERNAL";
                    case 9:
                        return "REAL";
                    case 10:
                        return "ENUMERATED";
                    case 11:
                        return "EMBEDDED_PDV";
                    case 12:
                        return "UTF8String";
                    case 16:
                        return "SEQUENCE";
                    case 17:
                        return "SET";
                    case 18:
                        return "NumericString";
                    case 19:
                        return "PrintableString";
                    case 20:
                        return "TeletexString";
                    case 21:
                        return "VideotexString";
                    case 22:
                        return "IA5String";
                    case 23:
                        return "UTCTime";
                    case 24:
                        return "GeneralizedTime";
                    case 25:
                        return "GraphicString";
                    case 26:
                        return "VisibleString";
                    case 27:
                        return "GeneralString";
                    case 28:
                        return "UniversalString";
                    case 30:
                        return "BMPString"
                    }
                    return "Universal_" + this.tag.tagNumber.toString();
                case 1:
                    return "Application_" + this.tag.tagNumber.toString();
                case 2:
                    return "[" + this.tag.tagNumber.toString() + "]";
                case 3:
                    return "Private_" + this.tag.tagNumber.toString()
                }
            }
            ,
            u.prototype.content = function(t) {
                if (void 0 === this.tag)
                    return null;
                void 0 === t && (t = 1 / 0);
                var e = this.posContent()
                  , n = Math.abs(this.length);
                if (!this.tag.isUniversal())
                    return null !== this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + n, t);
                switch (this.tag.tagNumber) {
                case 1:
                    return 0 === this.stream.get(e) ? "false" : "true";
                case 2:
                    return this.stream.parseInteger(e, e + n);
                case 3:
                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(e, e + n, t);
                case 4:
                    return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + n, t);
                case 6:
                    return this.stream.parseOID(e, e + n, t);
                case 16:
                case 17:
                    return null !== this.sub ? "(" + this.sub.length + " elem)" : "(no elem)";
                case 12:
                    return A(this.stream.parseStringUTF(e, e + n), t);
                case 18:
                case 19:
                case 20:
                case 21:
                case 22:
                case 26:
                    return A(this.stream.parseStringISO(e, e + n), t);
                case 30:
                    return A(this.stream.parseStringBMP(e, e + n), t);
                case 23:
                case 24:
                    return this.stream.parseTime(e, e + n, 23 == this.tag.tagNumber)
                }
                return null
            }
            ,
            u.prototype.toString = function() {
                return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
            }
            ,
            u.prototype.toPrettyString = function(t) {
                void 0 === t && (t = "");
                var e = t + this.typeName() + " @" + this.stream.pos;
                if (0 <= this.length && (e += "+"),
                e += this.length,
                this.tag.tagConstructed ? e += " (constructed)" : !this.tag.isUniversal() || 3 != this.tag.tagNumber && 4 != this.tag.tagNumber || null === this.sub || (e += " (encapsulates)"),
                e += "\n",
                null !== this.sub) {
                    t += "  ";
                    for (var n = 0, i = this.sub.length; n < i; ++n)
                        e += this.sub[n].toPrettyString(t)
                }
                return e
            }
            ,
            u.prototype.posStart = function() {
                return this.stream.pos
            }
            ,
            u.prototype.posContent = function() {
                return this.stream.pos + this.header
            }
            ,
            u.prototype.posEnd = function() {
                return this.stream.pos + this.header + Math.abs(this.length)
            }
            ,
            u.prototype.toHexString = function() {
                return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
            }
            ,
            u.decodeLength = function(t) {
                var e = t.get()
                  , n = 127 & e;
                if (n == e)
                    return n;
                if (6 < n)
                    throw new Error("Length over 48 bits not supported at position " + (t.pos - 1));
                if (0 === n)
                    return null;
                for (var i = e = 0; i < n; ++i)
                    e = 256 * e + t.get();
                return e
            }
            ,
            u.prototype.getHexStringValue = function() {
                var t = this.toHexString()
                  , e = 2 * this.header
                  , n = 2 * this.length;
                return t.substr(e, n)
            }
            ,
            u.decode = function(t) {
                var i;
                i = t instanceof x ? t : new x(t,0);
                var e = new x(i)
                  , n = new O(i)
                  , r = u.decodeLength(i)
                  , o = i.pos
                  , a = o - e.pos
                  , s = null
                  , c = function() {
                    var t = [];
                    if (null !== r) {
                        for (var e = o + r; i.pos < e; )
                            t[t.length] = u.decode(i);
                        if (i.pos != e)
                            throw new Error("Content size is not correct for container starting at offset " + o)
                    } else
                        try {
                            for (; ; ) {
                                var n = u.decode(i);
                                if (n.tag.isEOC())
                                    break;
                                t[t.length] = n
                            }
                            r = o - i.pos
                        } catch (t) {
                            throw new Error("Exception while decoding undefined length content: " + t)
                        }
                    return t
                };
                if (n.tagConstructed)
                    s = c();
                else if (n.isUniversal() && (3 == n.tagNumber || 4 == n.tagNumber))
                    try {
                        if (3 == n.tagNumber && 0 != i.get())
                            throw new Error("BIT STRINGs with unused bits cannot encapsulate.");
                        s = c();
                        for (var l = 0; l < s.length; ++l)
                            if (s[l].tag.isEOC())
                                throw new Error("EOC is not supposed to be actual content.")
                    } catch (t) {
                        s = null
                    }
                if (null === s) {
                    if (null === r)
                        throw new Error("We can't skip over an invalid tag with undefined length at offset " + o);
                    i.pos = o + Math.abs(r)
                }
                return new u(e,a,r,n,s)
            }
            ,
            u
        }(), O = function() {
            function t(t) {
                var e = t.get();
                if (this.tagClass = e >> 6,
                this.tagConstructed = 0 != (32 & e),
                this.tagNumber = 31 & e,
                31 == this.tagNumber) {
                    for (var n = new v; e = t.get(),
                    n.mulAdd(128, 127 & e),
                    128 & e; )
                        ;
                    this.tagNumber = n.simplify()
                }
            }
            return t.prototype.isUniversal = function() {
                return 0 === this.tagClass
            }
            ,
            t.prototype.isEOC = function() {
                return 0 === this.tagClass && 0 === this.tagNumber
            }
            ,
            t
        }(), C = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997], B = (1 << 26) / C[C.length - 1], D = function() {
            function b(t, e, n) {
                null != t && ("number" == typeof t ? this.fromNumber(t, e, n) : null == e && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, e))
            }
            return b.prototype.toString = function(t) {
                if (this.s < 0)
                    return "-" + this.negate().toString(t);
                var e;
                if (16 == t)
                    e = 4;
                else if (8 == t)
                    e = 3;
                else if (2 == t)
                    e = 1;
                else if (32 == t)
                    e = 5;
                else {
                    if (4 != t)
                        return this.toRadix(t);
                    e = 2
                }
                var n, i = (1 << e) - 1, r = !1, o = "", a = this.t, s = this.DB - a * this.DB % e;
                if (0 < a--)
                    for (s < this.DB && 0 < (n = this[a] >> s) && (r = !0,
                    o = c(n)); 0 <= a; )
                        s < e ? (n = (this[a] & (1 << s) - 1) << e - s,
                        n |= this[--a] >> (s += this.DB - e)) : (n = this[a] >> (s -= e) & i,
                        s <= 0 && (s += this.DB,
                        --a)),
                        0 < n && (r = !0),
                        r && (o += c(n));
                return r ? o : "0"
            }
            ,
            b.prototype.negate = function() {
                var t = P();
                return b.ZERO.subTo(this, t),
                t
            }
            ,
            b.prototype.abs = function() {
                return this.s < 0 ? this.negate() : this
            }
            ,
            b.prototype.compareTo = function(t) {
                var e = this.s - t.s;
                if (0 != e)
                    return e;
                var n = this.t;
                if (0 != (e = n - t.t))
                    return this.s < 0 ? -e : e;
                for (; 0 <= --n; )
                    if (0 != (e = this[n] - t[n]))
                        return e;
                return 0
            }
            ,
            b.prototype.bitLength = function() {
                return this.t <= 0 ? 0 : this.DB * (this.t - 1) + _(this[this.t - 1] ^ this.s & this.DM)
            }
            ,
            b.prototype.mod = function(t) {
                var e = P();
                return this.abs().divRemTo(t, null, e),
                this.s < 0 && 0 < e.compareTo(b.ZERO) && t.subTo(e, e),
                e
            }
            ,
            b.prototype.modPowInt = function(t, e) {
                var n;
                return n = t < 256 || e.isEven() ? new R(e) : new I(e),
                this.exp(t, n)
            }
            ,
            b.prototype.clone = function() {
                var t = P();
                return this.copyTo(t),
                t
            }
            ,
            b.prototype.intValue = function() {
                if (this.s < 0) {
                    if (1 == this.t)
                        return this[0] - this.DV;
                    if (0 == this.t)
                        return -1
                } else {
                    if (1 == this.t)
                        return this[0];
                    if (0 == this.t)
                        return 0
                }
                return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
            }
            ,
            b.prototype.byteValue = function() {
                return 0 == this.t ? this.s : this[0] << 24 >> 24
            }
            ,
            b.prototype.shortValue = function() {
                return 0 == this.t ? this.s : this[0] << 16 >> 16
            }
            ,
            b.prototype.signum = function() {
                return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
            }
            ,
            b.prototype.toByteArray = function() {
                var t = this.t
                  , e = [];
                e[0] = this.s;
                var n, i = this.DB - t * this.DB % 8, r = 0;
                if (0 < t--)
                    for (i < this.DB && (n = this[t] >> i) != (this.s & this.DM) >> i && (e[r++] = n | this.s << this.DB - i); 0 <= t; )
                        i < 8 ? (n = (this[t] & (1 << i) - 1) << 8 - i,
                        n |= this[--t] >> (i += this.DB - 8)) : (n = this[t] >> (i -= 8) & 255,
                        i <= 0 && (i += this.DB,
                        --t)),
                        0 != (128 & n) && (n |= -256),
                        0 == r && (128 & this.s) != (128 & n) && ++r,
                        (0 < r || n != this.s) && (e[r++] = n);
                return e
            }
            ,
            b.prototype.equals = function(t) {
                return 0 == this.compareTo(t)
            }
            ,
            b.prototype.min = function(t) {
                return this.compareTo(t) < 0 ? this : t
            }
            ,
            b.prototype.max = function(t) {
                return 0 < this.compareTo(t) ? this : t
            }
            ,
            b.prototype.and = function(t) {
                var e = P();
                return this.bitwiseTo(t, n, e),
                e
            }
            ,
            b.prototype.or = function(t) {
                var e = P();
                return this.bitwiseTo(t, l, e),
                e
            }
            ,
            b.prototype.xor = function(t) {
                var e = P();
                return this.bitwiseTo(t, i, e),
                e
            }
            ,
            b.prototype.andNot = function(t) {
                var e = P();
                return this.bitwiseTo(t, r, e),
                e
            }
            ,
            b.prototype.not = function() {
                for (var t = P(), e = 0; e < this.t; ++e)
                    t[e] = this.DM & ~this[e];
                return t.t = this.t,
                t.s = ~this.s,
                t
            }
            ,
            b.prototype.shiftLeft = function(t) {
                var e = P();
                return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
                e
            }
            ,
            b.prototype.shiftRight = function(t) {
                var e = P();
                return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
                e
            }
            ,
            b.prototype.getLowestSetBit = function() {
                for (var t = 0; t < this.t; ++t)
                    if (0 != this[t])
                        return t * this.DB + o(this[t]);
                return this.s < 0 ? this.t * this.DB : -1
            }
            ,
            b.prototype.bitCount = function() {
                for (var t = 0, e = this.s & this.DM, n = 0; n < this.t; ++n)
                    t += a(this[n] ^ e);
                return t
            }
            ,
            b.prototype.testBit = function(t) {
                var e = Math.floor(t / this.DB);
                return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
            }
            ,
            b.prototype.setBit = function(t) {
                return this.changeBit(t, l)
            }
            ,
            b.prototype.clearBit = function(t) {
                return this.changeBit(t, r)
            }
            ,
            b.prototype.flipBit = function(t) {
                return this.changeBit(t, i)
            }
            ,
            b.prototype.add = function(t) {
                var e = P();
                return this.addTo(t, e),
                e
            }
            ,
            b.prototype.subtract = function(t) {
                var e = P();
                return this.subTo(t, e),
                e
            }
            ,
            b.prototype.multiply = function(t) {
                var e = P();
                return this.multiplyTo(t, e),
                e
            }
            ,
            b.prototype.divide = function(t) {
                var e = P();
                return this.divRemTo(t, e, null),
                e
            }
            ,
            b.prototype.remainder = function(t) {
                var e = P();
                return this.divRemTo(t, null, e),
                e
            }
            ,
            b.prototype.divideAndRemainder = function(t) {
                var e = P()
                  , n = P();
                return this.divRemTo(t, e, n),
                [e, n]
            }
            ,
            b.prototype.modPow = function(t, e) {
                var n, i, r = t.bitLength(), o = F(1);
                if (r <= 0)
                    return o;
                n = r < 18 ? 1 : r < 48 ? 3 : r < 144 ? 4 : r < 768 ? 5 : 6,
                i = r < 8 ? new R(e) : e.isEven() ? new N(e) : new I(e);
                var a = []
                  , s = 3
                  , c = n - 1
                  , l = (1 << n) - 1;
                if (a[1] = i.convert(this),
                1 < n) {
                    var u = P();
                    for (i.sqrTo(a[1], u); s <= l; )
                        a[s] = P(),
                        i.mulTo(u, a[s - 2], a[s]),
                        s += 2
                }
                var h, d, f = t.t - 1, p = !0, g = P();
                for (r = _(t[f]) - 1; 0 <= f; ) {
                    for (c <= r ? h = t[f] >> r - c & l : (h = (t[f] & (1 << r + 1) - 1) << c - r,
                    0 < f && (h |= t[f - 1] >> this.DB + r - c)),
                    s = n; 0 == (1 & h); )
                        h >>= 1,
                        --s;
                    if ((r -= s) < 0 && (r += this.DB,
                    --f),
                    p)
                        a[h].copyTo(o),
                        p = !1;
                    else {
                        for (; 1 < s; )
                            i.sqrTo(o, g),
                            i.sqrTo(g, o),
                            s -= 2;
                        0 < s ? i.sqrTo(o, g) : (d = o,
                        o = g,
                        g = d),
                        i.mulTo(g, a[h], o)
                    }
                    for (; 0 <= f && 0 == (t[f] & 1 << r); )
                        i.sqrTo(o, g),
                        d = o,
                        o = g,
                        g = d,
                        --r < 0 && (r = this.DB - 1,
                        --f)
                }
                return i.revert(o)
            }
            ,
            b.prototype.modInverse = function(t) {
                var e = t.isEven();
                if (this.isEven() && e || 0 == t.signum())
                    return b.ZERO;
                for (var n = t.clone(), i = this.clone(), r = F(1), o = F(0), a = F(0), s = F(1); 0 != n.signum(); ) {
                    for (; n.isEven(); )
                        n.rShiftTo(1, n),
                        e ? (r.isEven() && o.isEven() || (r.addTo(this, r),
                        o.subTo(t, o)),
                        r.rShiftTo(1, r)) : o.isEven() || o.subTo(t, o),
                        o.rShiftTo(1, o);
                    for (; i.isEven(); )
                        i.rShiftTo(1, i),
                        e ? (a.isEven() && s.isEven() || (a.addTo(this, a),
                        s.subTo(t, s)),
                        a.rShiftTo(1, a)) : s.isEven() || s.subTo(t, s),
                        s.rShiftTo(1, s);
                    0 <= n.compareTo(i) ? (n.subTo(i, n),
                    e && r.subTo(a, r),
                    o.subTo(s, o)) : (i.subTo(n, i),
                    e && a.subTo(r, a),
                    s.subTo(o, s))
                }
                return 0 != i.compareTo(b.ONE) ? b.ZERO : 0 <= s.compareTo(t) ? s.subtract(t) : s.signum() < 0 ? (s.addTo(t, s),
                s.signum() < 0 ? s.add(t) : s) : s
            }
            ,
            b.prototype.pow = function(t) {
                return this.exp(t, new k)
            }
            ,
            b.prototype.gcd = function(t) {
                var e = this.s < 0 ? this.negate() : this.clone()
                  , n = t.s < 0 ? t.negate() : t.clone();
                if (e.compareTo(n) < 0) {
                    var i = e;
                    e = n,
                    n = i
                }
                var r = e.getLowestSetBit()
                  , o = n.getLowestSetBit();
                if (o < 0)
                    return e;
                for (r < o && (o = r),
                0 < o && (e.rShiftTo(o, e),
                n.rShiftTo(o, n)); 0 < e.signum(); )
                    0 < (r = e.getLowestSetBit()) && e.rShiftTo(r, e),
                    0 < (r = n.getLowestSetBit()) && n.rShiftTo(r, n),
                    0 <= e.compareTo(n) ? (e.subTo(n, e),
                    e.rShiftTo(1, e)) : (n.subTo(e, n),
                    n.rShiftTo(1, n));
                return 0 < o && n.lShiftTo(o, n),
                n
            }
            ,
            b.prototype.isProbablePrime = function(t) {
                var e, n = this.abs();
                if (1 == n.t && n[0] <= C[C.length - 1]) {
                    for (e = 0; e < C.length; ++e)
                        if (n[0] == C[e])
                            return !0;
                    return !1
                }
                if (n.isEven())
                    return !1;
                for (e = 1; e < C.length; ) {
                    for (var i = C[e], r = e + 1; r < C.length && i < B; )
                        i *= C[r++];
                    for (i = n.modInt(i); e < r; )
                        if (i % C[e++] == 0)
                            return !1
                }
                return n.millerRabin(t)
            }
            ,
            b.prototype.copyTo = function(t) {
                for (var e = this.t - 1; 0 <= e; --e)
                    t[e] = this[e];
                t.t = this.t,
                t.s = this.s
            }
            ,
            b.prototype.fromInt = function(t) {
                this.t = 1,
                this.s = t < 0 ? -1 : 0,
                0 < t ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
            }
            ,
            b.prototype.fromString = function(t, e) {
                var n;
                if (16 == e)
                    n = 4;
                else if (8 == e)
                    n = 3;
                else if (256 == e)
                    n = 8;
                else if (2 == e)
                    n = 1;
                else if (32 == e)
                    n = 5;
                else {
                    if (4 != e)
                        return void this.fromRadix(t, e);
                    n = 2
                }
                this.t = 0,
                this.s = 0;
                for (var i = t.length, r = !1, o = 0; 0 <= --i; ) {
                    var a = 8 == n ? 255 & +t[i] : U(t, i);
                    a < 0 ? "-" == t.charAt(i) && (r = !0) : (r = !1,
                    0 == o ? this[this.t++] = a : o + n > this.DB ? (this[this.t - 1] |= (a & (1 << this.DB - o) - 1) << o,
                    this[this.t++] = a >> this.DB - o) : this[this.t - 1] |= a << o,
                    (o += n) >= this.DB && (o -= this.DB))
                }
                8 == n && 0 != (128 & +t[0]) && (this.s = -1,
                0 < o && (this[this.t - 1] |= (1 << this.DB - o) - 1 << o)),
                this.clamp(),
                r && b.ZERO.subTo(this, this)
            }
            ,
            b.prototype.clamp = function() {
                for (var t = this.s & this.DM; 0 < this.t && this[this.t - 1] == t; )
                    --this.t
            }
            ,
            b.prototype.dlShiftTo = function(t, e) {
                var n;
                for (n = this.t - 1; 0 <= n; --n)
                    e[n + t] = this[n];
                for (n = t - 1; 0 <= n; --n)
                    e[n] = 0;
                e.t = this.t + t,
                e.s = this.s
            }
            ,
            b.prototype.drShiftTo = function(t, e) {
                for (var n = t; n < this.t; ++n)
                    e[n - t] = this[n];
                e.t = Math.max(this.t - t, 0),
                e.s = this.s
            }
            ,
            b.prototype.lShiftTo = function(t, e) {
                for (var n = t % this.DB, i = this.DB - n, r = (1 << i) - 1, o = Math.floor(t / this.DB), a = this.s << n & this.DM, s = this.t - 1; 0 <= s; --s)
                    e[s + o + 1] = this[s] >> i | a,
                    a = (this[s] & r) << n;
                for (var s = o - 1; 0 <= s; --s)
                    e[s] = 0;
                e[o] = a,
                e.t = this.t + o + 1,
                e.s = this.s,
                e.clamp()
            }
            ,
            b.prototype.rShiftTo = function(t, e) {
                e.s = this.s;
                var n = Math.floor(t / this.DB);
                if (n >= this.t)
                    e.t = 0;
                else {
                    var i = t % this.DB
                      , r = this.DB - i
                      , o = (1 << i) - 1;
                    e[0] = this[n] >> i;
                    for (var a = n + 1; a < this.t; ++a)
                        e[a - n - 1] |= (this[a] & o) << r,
                        e[a - n] = this[a] >> i;
                    0 < i && (e[this.t - n - 1] |= (this.s & o) << r),
                    e.t = this.t - n,
                    e.clamp()
                }
            }
            ,
            b.prototype.subTo = function(t, e) {
                for (var n = 0, i = 0, r = Math.min(t.t, this.t); n < r; )
                    i += this[n] - t[n],
                    e[n++] = i & this.DM,
                    i >>= this.DB;
                if (t.t < this.t) {
                    for (i -= t.s; n < this.t; )
                        i += this[n],
                        e[n++] = i & this.DM,
                        i >>= this.DB;
                    i += this.s
                } else {
                    for (i += this.s; n < t.t; )
                        i -= t[n],
                        e[n++] = i & this.DM,
                        i >>= this.DB;
                    i -= t.s
                }
                e.s = i < 0 ? -1 : 0,
                i < -1 ? e[n++] = this.DV + i : 0 < i && (e[n++] = i),
                e.t = n,
                e.clamp()
            }
            ,
            b.prototype.multiplyTo = function(t, e) {
                var n = this.abs()
                  , i = t.abs()
                  , r = n.t;
                for (e.t = r + i.t; 0 <= --r; )
                    e[r] = 0;
                for (r = 0; r < i.t; ++r)
                    e[r + n.t] = n.am(0, i[r], e, r, 0, n.t);
                e.s = 0,
                e.clamp(),
                this.s != t.s && b.ZERO.subTo(e, e)
            }
            ,
            b.prototype.squareTo = function(t) {
                for (var e = this.abs(), n = t.t = 2 * e.t; 0 <= --n; )
                    t[n] = 0;
                for (n = 0; n < e.t - 1; ++n) {
                    var i = e.am(n, e[n], t, 2 * n, 0, 1);
                    (t[n + e.t] += e.am(n + 1, 2 * e[n], t, 2 * n + 1, i, e.t - n - 1)) >= e.DV && (t[n + e.t] -= e.DV,
                    t[n + e.t + 1] = 1)
                }
                0 < t.t && (t[t.t - 1] += e.am(n, e[n], t, 2 * n, 0, 1)),
                t.s = 0,
                t.clamp()
            }
            ,
            b.prototype.divRemTo = function(t, e, n) {
                var i = t.abs();
                if (!(i.t <= 0)) {
                    var r = this.abs();
                    if (r.t < i.t)
                        return null != e && e.fromInt(0),
                        void (null != n && this.copyTo(n));
                    null == n && (n = P());
                    var o = P()
                      , a = this.s
                      , s = t.s
                      , c = this.DB - _(i[i.t - 1]);
                    0 < c ? (i.lShiftTo(c, o),
                    r.lShiftTo(c, n)) : (i.copyTo(o),
                    r.copyTo(n));
                    var l = o.t
                      , u = o[l - 1];
                    if (0 != u) {
                        var h = u * (1 << this.F1) + (1 < l ? o[l - 2] >> this.F2 : 0)
                          , d = this.FV / h
                          , f = (1 << this.F1) / h
                          , p = 1 << this.F2
                          , g = n.t
                          , m = g - l
                          , y = null == e ? P() : e;
                        for (o.dlShiftTo(m, y),
                        0 <= n.compareTo(y) && (n[n.t++] = 1,
                        n.subTo(y, n)),
                        b.ONE.dlShiftTo(l, y),
                        y.subTo(o, o); o.t < l; )
                            o[o.t++] = 0;
                        for (; 0 <= --m; ) {
                            var v = n[--g] == u ? this.DM : Math.floor(n[g] * d + (n[g - 1] + p) * f);
                            if ((n[g] += o.am(0, v, n, m, 0, l)) < v)
                                for (o.dlShiftTo(m, y),
                                n.subTo(y, n); n[g] < --v; )
                                    n.subTo(y, n)
                        }
                        null != e && (n.drShiftTo(l, e),
                        a != s && b.ZERO.subTo(e, e)),
                        n.t = l,
                        n.clamp(),
                        0 < c && n.rShiftTo(c, n),
                        a < 0 && b.ZERO.subTo(n, n)
                    }
                }
            }
            ,
            b.prototype.invDigit = function() {
                if (this.t < 1)
                    return 0;
                var t = this[0];
                if (0 == (1 & t))
                    return 0;
                var e = 3 & t;
                return 0 < (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) ? this.DV - e : -e
            }
            ,
            b.prototype.isEven = function() {
                return 0 == (0 < this.t ? 1 & this[0] : this.s)
            }
            ,
            b.prototype.exp = function(t, e) {
                if (4294967295 < t || t < 1)
                    return b.ONE;
                var n = P()
                  , i = P()
                  , r = e.convert(this)
                  , o = _(t) - 1;
                for (r.copyTo(n); 0 <= --o; )
                    if (e.sqrTo(n, i),
                    0 < (t & 1 << o))
                        e.mulTo(i, r, n);
                    else {
                        var a = n;
                        n = i,
                        i = a
                    }
                return e.revert(n)
            }
            ,
            b.prototype.chunkSize = function(t) {
                return Math.floor(Math.LN2 * this.DB / Math.log(t))
            }
            ,
            b.prototype.toRadix = function(t) {
                if (null == t && (t = 10),
                0 == this.signum() || t < 2 || 36 < t)
                    return "0";
                var e = this.chunkSize(t)
                  , n = Math.pow(t, e)
                  , i = F(n)
                  , r = P()
                  , o = P()
                  , a = "";
                for (this.divRemTo(i, r, o); 0 < r.signum(); )
                    a = (n + o.intValue()).toString(t).substr(1) + a,
                    r.divRemTo(i, r, o);
                return o.intValue().toString(t) + a
            }
            ,
            b.prototype.fromRadix = function(t, e) {
                this.fromInt(0),
                null == e && (e = 10);
                for (var n = this.chunkSize(e), i = Math.pow(e, n), r = !1, o = 0, a = 0, s = 0; s < t.length; ++s) {
                    var c = U(t, s);
                    c < 0 ? "-" == t.charAt(s) && 0 == this.signum() && (r = !0) : (a = e * a + c,
                    ++o >= n && (this.dMultiply(i),
                    this.dAddOffset(a, 0),
                    a = o = 0))
                }
                0 < o && (this.dMultiply(Math.pow(e, o)),
                this.dAddOffset(a, 0)),
                r && b.ZERO.subTo(this, this)
            }
            ,
            b.prototype.fromNumber = function(t, e, n) {
                if ("number" == typeof e)
                    if (t < 2)
                        this.fromInt(1);
                    else
                        for (this.fromNumber(t, n),
                        this.testBit(t - 1) || this.bitwiseTo(b.ONE.shiftLeft(t - 1), l, this),
                        this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(e); )
                            this.dAddOffset(2, 0),
                            this.bitLength() > t && this.subTo(b.ONE.shiftLeft(t - 1), this);
                else {
                    var i = []
                      , r = 7 & t;
                    i.length = 1 + (t >> 3),
                    e.nextBytes(i),
                    0 < r ? i[0] &= (1 << r) - 1 : i[0] = 0,
                    this.fromString(i, 256)
                }
            }
            ,
            b.prototype.bitwiseTo = function(t, e, n) {
                var i, r, o = Math.min(t.t, this.t);
                for (i = 0; i < o; ++i)
                    n[i] = e(this[i], t[i]);
                if (t.t < this.t) {
                    for (r = t.s & this.DM,
                    i = o; i < this.t; ++i)
                        n[i] = e(this[i], r);
                    n.t = this.t
                } else {
                    for (r = this.s & this.DM,
                    i = o; i < t.t; ++i)
                        n[i] = e(r, t[i]);
                    n.t = t.t
                }
                n.s = e(this.s, t.s),
                n.clamp()
            }
            ,
            b.prototype.changeBit = function(t, e) {
                var n = b.ONE.shiftLeft(t);
                return this.bitwiseTo(n, e, n),
                n
            }
            ,
            b.prototype.addTo = function(t, e) {
                for (var n = 0, i = 0, r = Math.min(t.t, this.t); n < r; )
                    i += this[n] + t[n],
                    e[n++] = i & this.DM,
                    i >>= this.DB;
                if (t.t < this.t) {
                    for (i += t.s; n < this.t; )
                        i += this[n],
                        e[n++] = i & this.DM,
                        i >>= this.DB;
                    i += this.s
                } else {
                    for (i += this.s; n < t.t; )
                        i += t[n],
                        e[n++] = i & this.DM,
                        i >>= this.DB;
                    i += t.s
                }
                e.s = i < 0 ? -1 : 0,
                0 < i ? e[n++] = i : i < -1 && (e[n++] = this.DV + i),
                e.t = n,
                e.clamp()
            }
            ,
            b.prototype.dMultiply = function(t) {
                this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
                ++this.t,
                this.clamp()
            }
            ,
            b.prototype.dAddOffset = function(t, e) {
                if (0 != t) {
                    for (; this.t <= e; )
                        this[this.t++] = 0;
                    for (this[e] += t; this[e] >= this.DV; )
                        this[e] -= this.DV,
                        ++e >= this.t && (this[this.t++] = 0),
                        ++this[e]
                }
            }
            ,
            b.prototype.multiplyLowerTo = function(t, e, n) {
                var i = Math.min(this.t + t.t, e);
                for (n.s = 0,
                n.t = i; 0 < i; )
                    n[--i] = 0;
                for (var r = n.t - this.t; i < r; ++i)
                    n[i + this.t] = this.am(0, t[i], n, i, 0, this.t);
                for (var r = Math.min(t.t, e); i < r; ++i)
                    this.am(0, t[i], n, i, 0, e - i);
                n.clamp()
            }
            ,
            b.prototype.multiplyUpperTo = function(t, e, n) {
                --e;
                var i = n.t = this.t + t.t - e;
                for (n.s = 0; 0 <= --i; )
                    n[i] = 0;
                for (i = Math.max(e - this.t, 0); i < t.t; ++i)
                    n[this.t + i - e] = this.am(e - i, t[i], n, 0, 0, this.t + i - e);
                n.clamp(),
                n.drShiftTo(1, n)
            }
            ,
            b.prototype.modInt = function(t) {
                if (t <= 0)
                    return 0;
                var e = this.DV % t
                  , n = this.s < 0 ? t - 1 : 0;
                if (0 < this.t)
                    if (0 == e)
                        n = this[0] % t;
                    else
                        for (var i = this.t - 1; 0 <= i; --i)
                            n = (e * n + this[i]) % t;
                return n
            }
            ,
            b.prototype.millerRabin = function(t) {
                var e = this.subtract(b.ONE)
                  , n = e.getLowestSetBit();
                if (n <= 0)
                    return !1;
                var i = e.shiftRight(n);
                C.length < (t = t + 1 >> 1) && (t = C.length);
                for (var r = P(), o = 0; o < t; ++o) {
                    r.fromInt(C[Math.floor(Math.random() * C.length)]);
                    var a = r.modPow(i, this);
                    if (0 != a.compareTo(b.ONE) && 0 != a.compareTo(e)) {
                        for (var s = 1; s++ < n && 0 != a.compareTo(e); )
                            if (0 == (a = a.modPowInt(2, this)).compareTo(b.ONE))
                                return !1;
                        if (0 != a.compareTo(e))
                            return !1
                    }
                }
                return !0
            }
            ,
            b.prototype.square = function() {
                var t = P();
                return this.squareTo(t),
                t
            }
            ,
            b.prototype.gcda = function(t, e) {
                var n = this.s < 0 ? this.negate() : this.clone()
                  , i = t.s < 0 ? t.negate() : t.clone();
                if (n.compareTo(i) < 0) {
                    var r = n;
                    n = i,
                    i = r
                }
                var o = n.getLowestSetBit()
                  , a = i.getLowestSetBit();
                if (a < 0)
                    e(n);
                else {
                    o < a && (a = o),
                    0 < a && (n.rShiftTo(a, n),
                    i.rShiftTo(a, i));
                    var s = function() {
                        0 < (o = n.getLowestSetBit()) && n.rShiftTo(o, n),
                        0 < (o = i.getLowestSetBit()) && i.rShiftTo(o, i),
                        0 <= n.compareTo(i) ? (n.subTo(i, n),
                        n.rShiftTo(1, n)) : (i.subTo(n, i),
                        i.rShiftTo(1, i)),
                        0 < n.signum() ? setTimeout(s, 0) : (0 < a && i.lShiftTo(a, i),
                        setTimeout(function() {
                            e(i)
                        }, 0))
                    };
                    setTimeout(s, 10)
                }
            }
            ,
            b.prototype.fromNumberAsync = function(t, e, n, i) {
                if ("number" == typeof e)
                    if (t < 2)
                        this.fromInt(1);
                    else {
                        this.fromNumber(t, n),
                        this.testBit(t - 1) || this.bitwiseTo(b.ONE.shiftLeft(t - 1), l, this),
                        this.isEven() && this.dAddOffset(1, 0);
                        var r = this
                          , o = function() {
                            r.dAddOffset(2, 0),
                            r.bitLength() > t && r.subTo(b.ONE.shiftLeft(t - 1), r),
                            r.isProbablePrime(e) ? setTimeout(function() {
                                i()
                            }, 0) : setTimeout(o, 0)
                        };
                        setTimeout(o, 0)
                    }
                else {
                    var a = []
                      , s = 7 & t;
                    a.length = 1 + (t >> 3),
                    e.nextBytes(a),
                    0 < s ? a[0] &= (1 << s) - 1 : a[0] = 0,
                    this.fromString(a, 256)
                }
            }
            ,
            b
        }(), k = function() {
            function t() {}
            return t.prototype.convert = function(t) {
                return t
            }
            ,
            t.prototype.revert = function(t) {
                return t
            }
            ,
            t.prototype.mulTo = function(t, e, n) {
                t.multiplyTo(e, n)
            }
            ,
            t.prototype.sqrTo = function(t, e) {
                t.squareTo(e)
            }
            ,
            t
        }(), R = function() {
            function t(t) {
                this.m = t
            }
            return t.prototype.convert = function(t) {
                return t.s < 0 || 0 <= t.compareTo(this.m) ? t.mod(this.m) : t
            }
            ,
            t.prototype.revert = function(t) {
                return t
            }
            ,
            t.prototype.reduce = function(t) {
                t.divRemTo(this.m, null, t)
            }
            ,
            t.prototype.mulTo = function(t, e, n) {
                t.multiplyTo(e, n),
                this.reduce(n)
            }
            ,
            t.prototype.sqrTo = function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
            ,
            t
        }(), I = function() {
            function t(t) {
                this.m = t,
                this.mp = t.invDigit(),
                this.mpl = 32767 & this.mp,
                this.mph = this.mp >> 15,
                this.um = (1 << t.DB - 15) - 1,
                this.mt2 = 2 * t.t
            }
            return t.prototype.convert = function(t) {
                var e = P();
                return t.abs().dlShiftTo(this.m.t, e),
                e.divRemTo(this.m, null, e),
                t.s < 0 && 0 < e.compareTo(D.ZERO) && this.m.subTo(e, e),
                e
            }
            ,
            t.prototype.revert = function(t) {
                var e = P();
                return t.copyTo(e),
                this.reduce(e),
                e
            }
            ,
            t.prototype.reduce = function(t) {
                for (; t.t <= this.mt2; )
                    t[t.t++] = 0;
                for (var e = 0; e < this.m.t; ++e) {
                    var n = 32767 & t[e]
                      , i = n * this.mpl + ((n * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
                    for (n = e + this.m.t,
                    t[n] += this.m.am(0, i, t, e, 0, this.m.t); t[n] >= t.DV; )
                        t[n] -= t.DV,
                        t[++n]++
                }
                t.clamp(),
                t.drShiftTo(this.m.t, t),
                0 <= t.compareTo(this.m) && t.subTo(this.m, t)
            }
            ,
            t.prototype.mulTo = function(t, e, n) {
                t.multiplyTo(e, n),
                this.reduce(n)
            }
            ,
            t.prototype.sqrTo = function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
            ,
            t
        }(), N = function() {
            function t(t) {
                this.m = t,
                this.r2 = P(),
                this.q3 = P(),
                D.ONE.dlShiftTo(2 * t.t, this.r2),
                this.mu = this.r2.divide(t)
            }
            return t.prototype.convert = function(t) {
                if (t.s < 0 || t.t > 2 * this.m.t)
                    return t.mod(this.m);
                if (t.compareTo(this.m) < 0)
                    return t;
                var e = P();
                return t.copyTo(e),
                this.reduce(e),
                e
            }
            ,
            t.prototype.revert = function(t) {
                return t
            }
            ,
            t.prototype.reduce = function(t) {
                for (t.drShiftTo(this.m.t - 1, this.r2),
                t.t > this.m.t + 1 && (t.t = this.m.t + 1,
                t.clamp()),
                this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
                this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); t.compareTo(this.r2) < 0; )
                    t.dAddOffset(1, this.m.t + 1);
                for (t.subTo(this.r2, t); 0 <= t.compareTo(this.m); )
                    t.subTo(this.m, t)
            }
            ,
            t.prototype.mulTo = function(t, e, n) {
                t.multiplyTo(e, n),
                this.reduce(n)
            }
            ,
            t.prototype.sqrTo = function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
            ,
            t
        }();
        function P() {
            return new D(null)
        }
        function M(t, e) {
            return new D(t,e)
        }
        E = "Microsoft Internet Explorer" == navigator.appName ? (D.prototype.am = function(t, e, n, i, r, o) {
            for (var a = 32767 & e, s = e >> 15; 0 <= --o; ) {
                var c = 32767 & this[t]
                  , l = this[t++] >> 15
                  , u = s * c + l * a;
                c = a * c + ((32767 & u) << 15) + n[i] + (1073741823 & r),
                r = (c >>> 30) + (u >>> 15) + s * l + (r >>> 30),
                n[i++] = 1073741823 & c
            }
            return r
        }
        ,
        30) : "Netscape" != navigator.appName ? (D.prototype.am = function(t, e, n, i, r, o) {
            for (; 0 <= --o; ) {
                var a = e * this[t++] + n[i] + r;
                r = Math.floor(a / 67108864),
                n[i++] = 67108863 & a
            }
            return r
        }
        ,
        26) : (D.prototype.am = function(t, e, n, i, r, o) {
            for (var a = 16383 & e, s = e >> 14; 0 <= --o; ) {
                var c = 16383 & this[t]
                  , l = this[t++] >> 14
                  , u = s * c + l * a;
                c = a * c + ((16383 & u) << 14) + n[i] + r,
                r = (c >> 28) + (u >> 14) + s * l,
                n[i++] = 268435455 & c
            }
            return r
        }
        ,
        28),
        D.prototype.DB = E,
        D.prototype.DM = (1 << E) - 1,
        D.prototype.DV = 1 << E,
        D.prototype.FV = Math.pow(2, 52),
        D.prototype.F1 = 52 - E,
        D.prototype.F2 = 2 * E - 52;
        var L, V, j = [];
        for (L = "0".charCodeAt(0),
        V = 0; V <= 9; ++V)
            j[L++] = V;
        for (L = "a".charCodeAt(0),
        V = 10; V < 36; ++V)
            j[L++] = V;
        for (L = "A".charCodeAt(0),
        V = 10; V < 36; ++V)
            j[L++] = V;
        function U(t, e) {
            var n = j[t.charCodeAt(e)];
            return null == n ? -1 : n
        }
        function F(t) {
            var e = P();
            return e.fromInt(t),
            e
        }
        function _(t) {
            var e, n = 1;
            return 0 != (e = t >>> 16) && (t = e,
            n += 16),
            0 != (e = t >> 8) && (t = e,
            n += 8),
            0 != (e = t >> 4) && (t = e,
            n += 4),
            0 != (e = t >> 2) && (t = e,
            n += 2),
            0 != (e = t >> 1) && (t = e,
            n += 1),
            n
        }
        D.ZERO = F(0),
        D.ONE = F(1);
        var H, X, z = function() {
            function t() {
                this.i = 0,
                this.j = 0,
                this.S = []
            }
            return t.prototype.init = function(t) {
                var e, n, i;
                for (e = 0; e < 256; ++e)
                    this.S[e] = e;
                for (e = n = 0; e < 256; ++e)
                    n = n + this.S[e] + t[e % t.length] & 255,
                    i = this.S[e],
                    this.S[e] = this.S[n],
                    this.S[n] = i;
                this.i = 0,
                this.j = 0
            }
            ,
            t.prototype.next = function() {
                var t;
                return this.i = this.i + 1 & 255,
                this.j = this.j + this.S[this.i] & 255,
                t = this.S[this.i],
                this.S[this.i] = this.S[this.j],
                this.S[this.j] = t,
                this.S[t + this.S[this.i] & 255]
            }
            ,
            t
        }(), W = 256, q = null;
        if (null == q) {
            q = [];
            var G = void (X = 0);
            if (window.crypto && window.crypto.getRandomValues) {
                var K = new Uint32Array(256);
                for (window.crypto.getRandomValues(K),
                G = 0; G < K.length; ++G)
                    q[X++] = 255 & K[G]
            }
            var J = function(t) {
                if (this.count = this.count || 0,
                256 <= this.count || W <= X)
                    window.removeEventListener ? window.removeEventListener("mousemove", J, !1) : window.detachEvent && window.detachEvent("onmousemove", J);
                else
                    try {
                        var e = t.x + t.y;
                        q[X++] = 255 & e,
                        this.count += 1
                    } catch (t) {}
            };
            window.addEventListener ? window.addEventListener("mousemove", J, !1) : window.attachEvent && window.attachEvent("onmousemove", J)
        }
        function Y() {
            if (null == H) {
                for (H = new z; X < W; ) {
                    var t = Math.floor(65536 * Math.random());
                    q[X++] = 255 & t
                }
                for (H.init(q),
                X = 0; X < q.length; ++X)
                    q[X] = 0;
                X = 0
            }
            return H.next()
        }
        var Q = function() {
            function t() {}
            return t.prototype.nextBytes = function(t) {
                for (var e = 0; e < t.length; ++e)
                    t[e] = Y()
            }
            ,
            t
        }()
          , Z = function() {
            function t() {
                this.n = null,
                this.e = 0,
                this.d = null,
                this.p = null,
                this.q = null,
                this.dmp1 = null,
                this.dmq1 = null,
                this.coeff = null
            }
            return t.prototype.doPublic = function(t) {
                return t.modPowInt(this.e, this.n)
            }
            ,
            t.prototype.doPrivate = function(t) {
                if (null == this.p || null == this.q)
                    return t.modPow(this.d, this.n);
                for (var e = t.mod(this.p).modPow(this.dmp1, this.p), n = t.mod(this.q).modPow(this.dmq1, this.q); e.compareTo(n) < 0; )
                    e = e.add(this.p);
                return e.subtract(n).multiply(this.coeff).mod(this.p).multiply(this.q).add(n)
            }
            ,
            t.prototype.setPublic = function(t, e) {
                null != t && null != e && 0 < t.length && 0 < e.length ? (this.n = M(t, 16),
                this.e = parseInt(e, 16)) : console.error("Invalid RSA public key")
            }
            ,
            t.prototype.encrypt = function(t) {
                var e = function(t, e) {
                    if (e < t.length + 11)
                        return console.error("Message too long for RSA"),
                        null;
                    for (var n = [], i = t.length - 1; 0 <= i && 0 < e; ) {
                        var r = t.charCodeAt(i--);
                        n[--e] = r < 128 ? r : 127 < r && r < 2048 ? (n[--e] = 63 & r | 128,
                        r >> 6 | 192) : (n[--e] = 63 & r | 128,
                        n[--e] = r >> 6 & 63 | 128,
                        r >> 12 | 224)
                    }
                    n[--e] = 0;
                    for (var o = new Q, a = []; 2 < e; ) {
                        for (a[0] = 0; 0 == a[0]; )
                            o.nextBytes(a);
                        n[--e] = a[0]
                    }
                    return n[--e] = 2,
                    n[--e] = 0,
                    new D(n)
                }(t, this.n.bitLength() + 7 >> 3);
                if (null == e)
                    return null;
                var n = this.doPublic(e);
                if (null == n)
                    return null;
                var i = n.toString(16);
                return 0 == (1 & i.length) ? i : "0" + i
            }
            ,
            t.prototype.setPrivate = function(t, e, n) {
                null != t && null != e && 0 < t.length && 0 < e.length ? (this.n = M(t, 16),
                this.e = parseInt(e, 16),
                this.d = M(n, 16)) : console.error("Invalid RSA private key")
            }
            ,
            t.prototype.setPrivateEx = function(t, e, n, i, r, o, a, s) {
                null != t && null != e && 0 < t.length && 0 < e.length ? (this.n = M(t, 16),
                this.e = parseInt(e, 16),
                this.d = M(n, 16),
                this.p = M(i, 16),
                this.q = M(r, 16),
                this.dmp1 = M(o, 16),
                this.dmq1 = M(a, 16),
                this.coeff = M(s, 16)) : console.error("Invalid RSA private key")
            }
            ,
            t.prototype.generate = function(t, e) {
                var n = new Q
                  , i = t >> 1;
                this.e = parseInt(e, 16);
                for (var r = new D(e,16); ; ) {
                    for (; this.p = new D(t - i,1,n),
                    0 != this.p.subtract(D.ONE).gcd(r).compareTo(D.ONE) || !this.p.isProbablePrime(10); )
                        ;
                    for (; this.q = new D(i,1,n),
                    0 != this.q.subtract(D.ONE).gcd(r).compareTo(D.ONE) || !this.q.isProbablePrime(10); )
                        ;
                    if (this.p.compareTo(this.q) <= 0) {
                        var o = this.p;
                        this.p = this.q,
                        this.q = o
                    }
                    var a = this.p.subtract(D.ONE)
                      , s = this.q.subtract(D.ONE)
                      , c = a.multiply(s);
                    if (0 == c.gcd(r).compareTo(D.ONE)) {
                        this.n = this.p.multiply(this.q),
                        this.d = r.modInverse(c),
                        this.dmp1 = this.d.mod(a),
                        this.dmq1 = this.d.mod(s),
                        this.coeff = this.q.modInverse(this.p);
                        break
                    }
                }
            }
            ,
            t.prototype.decrypt = function(t) {
                var e = M(t, 16)
                  , n = this.doPrivate(e);
                return null == n ? null : function(t, e) {
                    for (var n = t.toByteArray(), i = 0; i < n.length && 0 == n[i]; )
                        ++i;
                    if (n.length - i != e - 1 || 2 != n[i])
                        return null;
                    for (++i; 0 != n[i]; )
                        if (++i >= n.length)
                            return null;
                    for (var r = ""; ++i < n.length; ) {
                        var o = 255 & n[i];
                        o < 128 ? r += String.fromCharCode(o) : 191 < o && o < 224 ? (r += String.fromCharCode((31 & o) << 6 | 63 & n[i + 1]),
                        ++i) : (r += String.fromCharCode((15 & o) << 12 | (63 & n[i + 1]) << 6 | 63 & n[i + 2]),
                        i += 2)
                    }
                    return r
                }(n, this.n.bitLength() + 7 >> 3)
            }
            ,
            t.prototype.generateAsync = function(t, e, r) {
                var o = new Q
                  , a = t >> 1;
                this.e = parseInt(e, 16);
                var s = new D(e,16)
                  , c = this
                  , l = function() {
                    var e = function() {
                        if (c.p.compareTo(c.q) <= 0) {
                            var t = c.p;
                            c.p = c.q,
                            c.q = t
                        }
                        var e = c.p.subtract(D.ONE)
                          , n = c.q.subtract(D.ONE)
                          , i = e.multiply(n);
                        0 == i.gcd(s).compareTo(D.ONE) ? (c.n = c.p.multiply(c.q),
                        c.d = s.modInverse(i),
                        c.dmp1 = c.d.mod(e),
                        c.dmq1 = c.d.mod(n),
                        c.coeff = c.q.modInverse(c.p),
                        setTimeout(function() {
                            r()
                        }, 0)) : setTimeout(l, 0)
                    }
                      , n = function() {
                        c.q = P(),
                        c.q.fromNumberAsync(a, 1, o, function() {
                            c.q.subtract(D.ONE).gcda(s, function(t) {
                                0 == t.compareTo(D.ONE) && c.q.isProbablePrime(10) ? setTimeout(e, 0) : setTimeout(n, 0)
                            })
                        })
                    }
                      , i = function() {
                        c.p = P(),
                        c.p.fromNumberAsync(t - a, 1, o, function() {
                            c.p.subtract(D.ONE).gcda(s, function(t) {
                                0 == t.compareTo(D.ONE) && c.p.isProbablePrime(10) ? setTimeout(n, 0) : setTimeout(i, 0)
                            })
                        })
                    };
                    setTimeout(i, 0)
                };
                setTimeout(l, 0)
            }
            ,
            t.prototype.sign = function(t, e, n) {
                var i = $[n] || ""
                  , r = i + e(t).toString()
                  , o = function(t, e) {
                    if (e < t.length + 22)
                        return console.error("Message too long for RSA"),
                        null;
                    for (var n = e - t.length - 6, i = "", r = 0; r < n; r += 2)
                        i += "ff";
                    return M("0001" + i + "00" + t, 16)
                }(r, this.n.bitLength() / 4);
                if (null == o)
                    return null;
                var a = this.doPrivate(o);
                if (null == a)
                    return null;
                var s = a.toString(16);
                return 0 == (1 & s.length) ? s : "0" + s
            }
            ,
            t.prototype.verify = function(t, e, n) {
                var i = M(e, 16)
                  , r = this.doPublic(i);
                if (null == r)
                    return null;
                var o = r.toString(16).replace(/^1f+00/, "")
                  , a = function(t) {
                    for (var e in $)
                        if ($.hasOwnProperty(e)) {
                            var n = $[e]
                              , i = n.length;
                            if (t.substr(0, i) == n)
                                return t.substr(i)
                        }
                    return t
                }(o);
                return a == n(t).toString()
            }
            ,
            t
        }()
          , $ = {
            md2: "3020300c06082a864886f70d020205000410",
            md5: "3020300c06082a864886f70d020505000410",
            sha1: "3021300906052b0e03021a05000414",
            sha224: "302d300d06096086480165030402040500041c",
            sha256: "3031300d060960864801650304020105000420",
            sha384: "3041300d060960864801650304020205000430",
            sha512: "3051300d060960864801650304020305000440",
            ripemd160: "3021300906052b2403020105000414"
        }
          , tt = {};
        tt.lang = {
            extend: function(t, e, n) {
                if (!e || !t)
                    throw new Error("YAHOO.lang.extend failed, please check that all dependencies are included.");
                var i = function() {};
                if (i.prototype = e.prototype,
                t.prototype = new i,
                (t.prototype.constructor = t).superclass = e.prototype,
                e.prototype.constructor == Object.prototype.constructor && (e.prototype.constructor = e),
                n) {
                    var r;
                    for (r in n)
                        t.prototype[r] = n[r];
                    var o = function() {}
                      , a = ["toString", "valueOf"];
                    try {
                        /MSIE/.test(navigator.userAgent) && (o = function(t, e) {
                            for (r = 0; r < a.length; r += 1) {
                                var n = a[r]
                                  , i = e[n];
                                "function" == typeof i && i != Object.prototype[n] && (t[n] = i)
                            }
                        }
                        )
                    } catch (t) {}
                    o(t.prototype, n)
                }
            }
        };
        var et = {};
        void 0 !== et.asn1 && et.asn1 || (et.asn1 = {}),
        et.asn1.ASN1Util = new function() {
            this.integerToByteHex = function(t) {
                var e = t.toString(16);
                return e.length % 2 == 1 && (e = "0" + e),
                e
            }
            ,
            this.bigIntToMinTwosComplementsHex = function(t) {
                var e = t.toString(16);
                if ("-" != e.substr(0, 1))
                    e.length % 2 == 1 ? e = "0" + e : e.match(/^[0-7]/) || (e = "00" + e);
                else {
                    var n = e.substr(1)
                      , i = n.length;
                    i % 2 == 1 ? i += 1 : e.match(/^[0-7]/) || (i += 2);
                    for (var r = "", o = 0; o < i; o++)
                        r += "f";
                    var a = new D(r,16)
                      , s = a.xor(t).add(D.ONE);
                    e = s.toString(16).replace(/^-/, "")
                }
                return e
            }
            ,
            this.getPEMStringFromHex = function(t, e) {
                return hextopem(t, e)
            }
            ,
            this.newObject = function(t) {
                var e = et
                  , n = e.asn1
                  , i = n.DERBoolean
                  , r = n.DERInteger
                  , o = n.DERBitString
                  , a = n.DEROctetString
                  , s = n.DERNull
                  , c = n.DERObjectIdentifier
                  , l = n.DEREnumerated
                  , u = n.DERUTF8String
                  , h = n.DERNumericString
                  , d = n.DERPrintableString
                  , f = n.DERTeletexString
                  , p = n.DERIA5String
                  , g = n.DERUTCTime
                  , m = n.DERGeneralizedTime
                  , y = n.DERSequence
                  , v = n.DERSet
                  , b = n.DERTaggedObject
                  , w = n.ASN1Util.newObject
                  , T = Object.keys(t);
                if (1 != T.length)
                    throw "key of param shall be only one.";
                var A = T[0];
                if (-1 == ":bool:int:bitstr:octstr:null:oid:enum:utf8str:numstr:prnstr:telstr:ia5str:utctime:gentime:seq:set:tag:".indexOf(":" + A + ":"))
                    throw "undefined key: " + A;
                if ("bool" == A)
                    return new i(t[A]);
                if ("int" == A)
                    return new r(t[A]);
                if ("bitstr" == A)
                    return new o(t[A]);
                if ("octstr" == A)
                    return new a(t[A]);
                if ("null" == A)
                    return new s(t[A]);
                if ("oid" == A)
                    return new c(t[A]);
                if ("enum" == A)
                    return new l(t[A]);
                if ("utf8str" == A)
                    return new u(t[A]);
                if ("numstr" == A)
                    return new h(t[A]);
                if ("prnstr" == A)
                    return new d(t[A]);
                if ("telstr" == A)
                    return new f(t[A]);
                if ("ia5str" == A)
                    return new p(t[A]);
                if ("utctime" == A)
                    return new g(t[A]);
                if ("gentime" == A)
                    return new m(t[A]);
                if ("seq" == A) {
                    for (var E = t[A], x = [], S = 0; S < E.length; S++) {
                        var O = w(E[S]);
                        x.push(O)
                    }
                    return new y({
                        array: x
                    })
                }
                if ("set" == A) {
                    for (var E = t[A], x = [], S = 0; S < E.length; S++) {
                        var O = w(E[S]);
                        x.push(O)
                    }
                    return new v({
                        array: x
                    })
                }
                if ("tag" == A) {
                    var C = t[A];
                    if ("[object Array]" === Object.prototype.toString.call(C) && 3 == C.length) {
                        var B = w(C[2]);
                        return new b({
                            tag: C[0],
                            explicit: C[1],
                            obj: B
                        })
                    }
                    var D = {};
                    if (void 0 !== C.explicit && (D.explicit = C.explicit),
                    void 0 !== C.tag && (D.tag = C.tag),
                    void 0 === C.obj)
                        throw "obj shall be specified for 'tag'.";
                    return D.obj = w(C.obj),
                    new b(D)
                }
            }
            ,
            this.jsonToASN1HEX = function(t) {
                var e = this.newObject(t);
                return e.getEncodedHex()
            }
        }
        ,
        et.asn1.ASN1Util.oidHexToInt = function(t) {
            for (var e = "", n = parseInt(t.substr(0, 2), 16), i = Math.floor(n / 40), r = n % 40, e = i + "." + r, o = "", a = 2; a < t.length; a += 2) {
                var s = parseInt(t.substr(a, 2), 16)
                  , c = ("00000000" + s.toString(2)).slice(-8);
                if (o += c.substr(1, 7),
                "0" == c.substr(0, 1)) {
                    var l = new D(o,2);
                    e = e + "." + l.toString(10),
                    o = ""
                }
            }
            return e
        }
        ,
        et.asn1.ASN1Util.oidIntToHex = function(t) {
            var c = function(t) {
                var e = t.toString(16);
                return 1 == e.length && (e = "0" + e),
                e
            }
              , e = function(t) {
                var e = ""
                  , n = new D(t,10)
                  , i = n.toString(2)
                  , r = 7 - i.length % 7;
                7 == r && (r = 0);
                for (var o = "", a = 0; a < r; a++)
                    o += "0";
                i = o + i;
                for (var a = 0; a < i.length - 1; a += 7) {
                    var s = i.substr(a, 7);
                    a != i.length - 7 && (s = "1" + s),
                    e += c(parseInt(s, 2))
                }
                return e
            };
            if (!t.match(/^[0-9.]+$/))
                throw "malformed oid string: " + t;
            var n = ""
              , i = t.split(".")
              , r = 40 * parseInt(i[0]) + parseInt(i[1]);
            n += c(r),
            i.splice(0, 2);
            for (var o = 0; o < i.length; o++)
                n += e(i[o]);
            return n
        }
        ,
        et.asn1.ASN1Object = function() {
            this.getLengthHexFromValue = function() {
                if (void 0 === this.hV || null == this.hV)
                    throw "this.hV is null or undefined.";
                if (this.hV.length % 2 == 1)
                    throw "value hex must be even length: n=" + "".length + ",v=" + this.hV;
                var t = this.hV.length / 2
                  , e = t.toString(16);
                if (e.length % 2 == 1 && (e = "0" + e),
                t < 128)
                    return e;
                var n = e.length / 2;
                if (15 < n)
                    throw "ASN.1 length too long to represent by 8x: n = " + t.toString(16);
                var i = 128 + n;
                return i.toString(16) + e
            }
            ,
            this.getEncodedHex = function() {
                return (null == this.hTLV || this.isModified) && (this.hV = this.getFreshValueHex(),
                this.hL = this.getLengthHexFromValue(),
                this.hTLV = this.hT + this.hL + this.hV,
                this.isModified = !1),
                this.hTLV
            }
            ,
            this.getValueHex = function() {
                return this.getEncodedHex(),
                this.hV
            }
            ,
            this.getFreshValueHex = function() {
                return ""
            }
        }
        ,
        et.asn1.DERAbstractString = function(t) {
            et.asn1.DERAbstractString.superclass.constructor.call(this),
            this.getString = function() {
                return this.s
            }
            ,
            this.setString = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = t,
                this.hV = stohex(this.s)
            }
            ,
            this.setStringHex = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = null,
                this.hV = t
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            void 0 !== t && ("string" == typeof t ? this.setString(t) : void 0 !== t.str ? this.setString(t.str) : void 0 !== t.hex && this.setStringHex(t.hex))
        }
        ,
        tt.lang.extend(et.asn1.DERAbstractString, et.asn1.ASN1Object),
        et.asn1.DERAbstractTime = function(t) {
            et.asn1.DERAbstractTime.superclass.constructor.call(this),
            this.localDateToUTC = function(t) {
                utc = t.getTime() + 6e4 * t.getTimezoneOffset();
                var e = new Date(utc);
                return e
            }
            ,
            this.formatDate = function(t, e, n) {
                var i = this.zeroPadding
                  , r = this.localDateToUTC(t)
                  , o = String(r.getFullYear());
                "utc" == e && (o = o.substr(2, 2));
                var a = i(String(r.getMonth() + 1), 2)
                  , s = i(String(r.getDate()), 2)
                  , c = i(String(r.getHours()), 2)
                  , l = i(String(r.getMinutes()), 2)
                  , u = i(String(r.getSeconds()), 2)
                  , h = o + a + s + c + l + u;
                if (!0 === n) {
                    var d = r.getMilliseconds();
                    if (0 != d) {
                        var f = i(String(d), 3);
                        f = f.replace(/[0]+$/, ""),
                        h = h + "." + f
                    }
                }
                return h + "Z"
            }
            ,
            this.zeroPadding = function(t, e) {
                return t.length >= e ? t : new Array(e - t.length + 1).join("0") + t
            }
            ,
            this.getString = function() {
                return this.s
            }
            ,
            this.setString = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = t,
                this.hV = stohex(t)
            }
            ,
            this.setByDateValue = function(t, e, n, i, r, o) {
                var a = new Date(Date.UTC(t, e - 1, n, i, r, o, 0));
                this.setByDate(a)
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
        }
        ,
        tt.lang.extend(et.asn1.DERAbstractTime, et.asn1.ASN1Object),
        et.asn1.DERAbstractStructured = function(t) {
            et.asn1.DERAbstractString.superclass.constructor.call(this),
            this.setByASN1ObjectArray = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.asn1Array = t
            }
            ,
            this.appendASN1Object = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.asn1Array.push(t)
            }
            ,
            this.asn1Array = new Array,
            void 0 !== t && void 0 !== t.array && (this.asn1Array = t.array)
        }
        ,
        tt.lang.extend(et.asn1.DERAbstractStructured, et.asn1.ASN1Object),
        et.asn1.DERBoolean = function() {
            et.asn1.DERBoolean.superclass.constructor.call(this),
            this.hT = "01",
            this.hTLV = "0101ff"
        }
        ,
        tt.lang.extend(et.asn1.DERBoolean, et.asn1.ASN1Object),
        et.asn1.DERInteger = function(t) {
            et.asn1.DERInteger.superclass.constructor.call(this),
            this.hT = "02",
            this.setByBigInteger = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.hV = et.asn1.ASN1Util.bigIntToMinTwosComplementsHex(t)
            }
            ,
            this.setByInteger = function(t) {
                var e = new D(String(t),10);
                this.setByBigInteger(e)
            }
            ,
            this.setValueHex = function(t) {
                this.hV = t
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            void 0 !== t && (void 0 !== t.bigint ? this.setByBigInteger(t.bigint) : void 0 !== t.int ? this.setByInteger(t.int) : "number" == typeof t ? this.setByInteger(t) : void 0 !== t.hex && this.setValueHex(t.hex))
        }
        ,
        tt.lang.extend(et.asn1.DERInteger, et.asn1.ASN1Object),
        et.asn1.DERBitString = function(t) {
            if (void 0 !== t && void 0 !== t.obj) {
                var e = et.asn1.ASN1Util.newObject(t.obj);
                t.hex = "00" + e.getEncodedHex()
            }
            et.asn1.DERBitString.superclass.constructor.call(this),
            this.hT = "03",
            this.setHexValueIncludingUnusedBits = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.hV = t
            }
            ,
            this.setUnusedBitsAndHexValue = function(t, e) {
                if (t < 0 || 7 < t)
                    throw "unused bits shall be from 0 to 7: u = " + t;
                var n = "0" + t;
                this.hTLV = null,
                this.isModified = !0,
                this.hV = n + e
            }
            ,
            this.setByBinaryString = function(t) {
                var e = 8 - (t = t.replace(/0+$/, "")).length % 8;
                8 == e && (e = 0);
                for (var n = 0; n <= e; n++)
                    t += "0";
                for (var i = "", n = 0; n < t.length - 1; n += 8) {
                    var r = t.substr(n, 8)
                      , o = parseInt(r, 2).toString(16);
                    1 == o.length && (o = "0" + o),
                    i += o
                }
                this.hTLV = null,
                this.isModified = !0,
                this.hV = "0" + e + i
            }
            ,
            this.setByBooleanArray = function(t) {
                for (var e = "", n = 0; n < t.length; n++)
                    1 == t[n] ? e += "1" : e += "0";
                this.setByBinaryString(e)
            }
            ,
            this.newFalseArray = function(t) {
                for (var e = new Array(t), n = 0; n < t; n++)
                    e[n] = !1;
                return e
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            void 0 !== t && ("string" == typeof t && t.toLowerCase().match(/^[0-9a-f]+$/) ? this.setHexValueIncludingUnusedBits(t) : void 0 !== t.hex ? this.setHexValueIncludingUnusedBits(t.hex) : void 0 !== t.bin ? this.setByBinaryString(t.bin) : void 0 !== t.array && this.setByBooleanArray(t.array))
        }
        ,
        tt.lang.extend(et.asn1.DERBitString, et.asn1.ASN1Object),
        et.asn1.DEROctetString = function(t) {
            if (void 0 !== t && void 0 !== t.obj) {
                var e = et.asn1.ASN1Util.newObject(t.obj);
                t.hex = e.getEncodedHex()
            }
            et.asn1.DEROctetString.superclass.constructor.call(this, t),
            this.hT = "04"
        }
        ,
        tt.lang.extend(et.asn1.DEROctetString, et.asn1.DERAbstractString),
        et.asn1.DERNull = function() {
            et.asn1.DERNull.superclass.constructor.call(this),
            this.hT = "05",
            this.hTLV = "0500"
        }
        ,
        tt.lang.extend(et.asn1.DERNull, et.asn1.ASN1Object),
        et.asn1.DERObjectIdentifier = function(t) {
            var c = function(t) {
                var e = t.toString(16);
                return 1 == e.length && (e = "0" + e),
                e
            }
              , o = function(t) {
                var e = ""
                  , n = new D(t,10)
                  , i = n.toString(2)
                  , r = 7 - i.length % 7;
                7 == r && (r = 0);
                for (var o = "", a = 0; a < r; a++)
                    o += "0";
                i = o + i;
                for (var a = 0; a < i.length - 1; a += 7) {
                    var s = i.substr(a, 7);
                    a != i.length - 7 && (s = "1" + s),
                    e += c(parseInt(s, 2))
                }
                return e
            };
            et.asn1.DERObjectIdentifier.superclass.constructor.call(this),
            this.hT = "06",
            this.setValueHex = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.s = null,
                this.hV = t
            }
            ,
            this.setValueOidString = function(t) {
                if (!t.match(/^[0-9.]+$/))
                    throw "malformed oid string: " + t;
                var e = ""
                  , n = t.split(".")
                  , i = 40 * parseInt(n[0]) + parseInt(n[1]);
                e += c(i),
                n.splice(0, 2);
                for (var r = 0; r < n.length; r++)
                    e += o(n[r]);
                this.hTLV = null,
                this.isModified = !0,
                this.s = null,
                this.hV = e
            }
            ,
            this.setValueName = function(t) {
                var e = et.asn1.x509.OID.name2oid(t);
                if ("" === e)
                    throw "DERObjectIdentifier oidName undefined: " + t;
                this.setValueOidString(e)
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            void 0 !== t && ("string" == typeof t ? t.match(/^[0-2].[0-9.]+$/) ? this.setValueOidString(t) : this.setValueName(t) : void 0 !== t.oid ? this.setValueOidString(t.oid) : void 0 !== t.hex ? this.setValueHex(t.hex) : void 0 !== t.name && this.setValueName(t.name))
        }
        ,
        tt.lang.extend(et.asn1.DERObjectIdentifier, et.asn1.ASN1Object),
        et.asn1.DEREnumerated = function(t) {
            et.asn1.DEREnumerated.superclass.constructor.call(this),
            this.hT = "0a",
            this.setByBigInteger = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.hV = et.asn1.ASN1Util.bigIntToMinTwosComplementsHex(t)
            }
            ,
            this.setByInteger = function(t) {
                var e = new D(String(t),10);
                this.setByBigInteger(e)
            }
            ,
            this.setValueHex = function(t) {
                this.hV = t
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            void 0 !== t && (void 0 !== t.int ? this.setByInteger(t.int) : "number" == typeof t ? this.setByInteger(t) : void 0 !== t.hex && this.setValueHex(t.hex))
        }
        ,
        tt.lang.extend(et.asn1.DEREnumerated, et.asn1.ASN1Object),
        et.asn1.DERUTF8String = function(t) {
            et.asn1.DERUTF8String.superclass.constructor.call(this, t),
            this.hT = "0c"
        }
        ,
        tt.lang.extend(et.asn1.DERUTF8String, et.asn1.DERAbstractString),
        et.asn1.DERNumericString = function(t) {
            et.asn1.DERNumericString.superclass.constructor.call(this, t),
            this.hT = "12"
        }
        ,
        tt.lang.extend(et.asn1.DERNumericString, et.asn1.DERAbstractString),
        et.asn1.DERPrintableString = function(t) {
            et.asn1.DERPrintableString.superclass.constructor.call(this, t),
            this.hT = "13"
        }
        ,
        tt.lang.extend(et.asn1.DERPrintableString, et.asn1.DERAbstractString),
        et.asn1.DERTeletexString = function(t) {
            et.asn1.DERTeletexString.superclass.constructor.call(this, t),
            this.hT = "14"
        }
        ,
        tt.lang.extend(et.asn1.DERTeletexString, et.asn1.DERAbstractString),
        et.asn1.DERIA5String = function(t) {
            et.asn1.DERIA5String.superclass.constructor.call(this, t),
            this.hT = "16"
        }
        ,
        tt.lang.extend(et.asn1.DERIA5String, et.asn1.DERAbstractString),
        et.asn1.DERUTCTime = function(t) {
            et.asn1.DERUTCTime.superclass.constructor.call(this, t),
            this.hT = "17",
            this.setByDate = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.date = t,
                this.s = this.formatDate(this.date, "utc"),
                this.hV = stohex(this.s)
            }
            ,
            this.getFreshValueHex = function() {
                return void 0 === this.date && void 0 === this.s && (this.date = new Date,
                this.s = this.formatDate(this.date, "utc"),
                this.hV = stohex(this.s)),
                this.hV
            }
            ,
            void 0 !== t && (void 0 !== t.str ? this.setString(t.str) : "string" == typeof t && t.match(/^[0-9]{12}Z$/) ? this.setString(t) : void 0 !== t.hex ? this.setStringHex(t.hex) : void 0 !== t.date && this.setByDate(t.date))
        }
        ,
        tt.lang.extend(et.asn1.DERUTCTime, et.asn1.DERAbstractTime),
        et.asn1.DERGeneralizedTime = function(t) {
            et.asn1.DERGeneralizedTime.superclass.constructor.call(this, t),
            this.hT = "18",
            this.withMillis = !1,
            this.setByDate = function(t) {
                this.hTLV = null,
                this.isModified = !0,
                this.date = t,
                this.s = this.formatDate(this.date, "gen", this.withMillis),
                this.hV = stohex(this.s)
            }
            ,
            this.getFreshValueHex = function() {
                return void 0 === this.date && void 0 === this.s && (this.date = new Date,
                this.s = this.formatDate(this.date, "gen", this.withMillis),
                this.hV = stohex(this.s)),
                this.hV
            }
            ,
            void 0 !== t && (void 0 !== t.str ? this.setString(t.str) : "string" == typeof t && t.match(/^[0-9]{14}Z$/) ? this.setString(t) : void 0 !== t.hex ? this.setStringHex(t.hex) : void 0 !== t.date && this.setByDate(t.date),
            !0 === t.millis && (this.withMillis = !0))
        }
        ,
        tt.lang.extend(et.asn1.DERGeneralizedTime, et.asn1.DERAbstractTime),
        et.asn1.DERSequence = function(t) {
            et.asn1.DERSequence.superclass.constructor.call(this, t),
            this.hT = "30",
            this.getFreshValueHex = function() {
                for (var t = "", e = 0; e < this.asn1Array.length; e++) {
                    var n = this.asn1Array[e];
                    t += n.getEncodedHex()
                }
                return this.hV = t,
                this.hV
            }
        }
        ,
        tt.lang.extend(et.asn1.DERSequence, et.asn1.DERAbstractStructured),
        et.asn1.DERSet = function(t) {
            et.asn1.DERSet.superclass.constructor.call(this, t),
            this.hT = "31",
            this.sortFlag = !0,
            this.getFreshValueHex = function() {
                for (var t = new Array, e = 0; e < this.asn1Array.length; e++) {
                    var n = this.asn1Array[e];
                    t.push(n.getEncodedHex())
                }
                return 1 == this.sortFlag && t.sort(),
                this.hV = t.join(""),
                this.hV
            }
            ,
            void 0 !== t && void 0 !== t.sortflag && 0 == t.sortflag && (this.sortFlag = !1)
        }
        ,
        tt.lang.extend(et.asn1.DERSet, et.asn1.DERAbstractStructured),
        et.asn1.DERTaggedObject = function(t) {
            et.asn1.DERTaggedObject.superclass.constructor.call(this),
            this.hT = "a0",
            this.hV = "",
            this.isExplicit = !0,
            this.asn1Object = null,
            this.setASN1Object = function(t, e, n) {
                this.hT = e,
                this.isExplicit = t,
                this.asn1Object = n,
                this.isExplicit ? (this.hV = this.asn1Object.getEncodedHex(),
                this.hTLV = null,
                this.isModified = !0) : (this.hV = null,
                this.hTLV = n.getEncodedHex(),
                this.hTLV = this.hTLV.replace(/^../, e),
                this.isModified = !1)
            }
            ,
            this.getFreshValueHex = function() {
                return this.hV
            }
            ,
            void 0 !== t && (void 0 !== t.tag && (this.hT = t.tag),
            void 0 !== t.explicit && (this.isExplicit = t.explicit),
            void 0 !== t.obj && (this.asn1Object = t.obj,
            this.setASN1Object(this.isExplicit, this.hT, this.asn1Object)))
        }
        ,
        tt.lang.extend(et.asn1.DERTaggedObject, et.asn1.ASN1Object);
        var nt = function(n) {
            function i(t) {
                var e = n.call(this) || this;
                return t && ("string" == typeof t ? e.parseKey(t) : (i.hasPrivateKeyProperty(t) || i.hasPublicKeyProperty(t)) && e.parsePropertiesFrom(t)),
                e
            }
            return function(t, e) {
                function n() {
                    this.constructor = t
                }
                p(t, e),
                t.prototype = null === e ? Object.create(e) : (n.prototype = e.prototype,
                new n)
            }(i, n),
            i.prototype.parseKey = function(t) {
                try {
                    var e = 0
                      , n = 0
                      , i = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/.test(t) ? g.decode(t) : m.unarmor(t)
                      , r = S.decode(i);
                    if (3 === r.sub.length && (r = r.sub[2].sub[0]),
                    9 === r.sub.length) {
                        e = r.sub[1].getHexStringValue(),
                        this.n = M(e, 16),
                        n = r.sub[2].getHexStringValue(),
                        this.e = parseInt(n, 16);
                        var o = r.sub[3].getHexStringValue();
                        this.d = M(o, 16);
                        var a = r.sub[4].getHexStringValue();
                        this.p = M(a, 16);
                        var s = r.sub[5].getHexStringValue();
                        this.q = M(s, 16);
                        var c = r.sub[6].getHexStringValue();
                        this.dmp1 = M(c, 16);
                        var l = r.sub[7].getHexStringValue();
                        this.dmq1 = M(l, 16);
                        var u = r.sub[8].getHexStringValue();
                        this.coeff = M(u, 16)
                    } else {
                        if (2 !== r.sub.length)
                            return !1;
                        var h = r.sub[1]
                          , d = h.sub[0];
                        e = d.sub[0].getHexStringValue(),
                        this.n = M(e, 16),
                        n = d.sub[1].getHexStringValue(),
                        this.e = parseInt(n, 16)
                    }
                    return !0
                } catch (t) {
                    return !1
                }
            }
            ,
            i.prototype.getPrivateBaseKey = function() {
                var t = {
                    array: [new et.asn1.DERInteger({
                        int: 0
                    }), new et.asn1.DERInteger({
                        bigint: this.n
                    }), new et.asn1.DERInteger({
                        int: this.e
                    }), new et.asn1.DERInteger({
                        bigint: this.d
                    }), new et.asn1.DERInteger({
                        bigint: this.p
                    }), new et.asn1.DERInteger({
                        bigint: this.q
                    }), new et.asn1.DERInteger({
                        bigint: this.dmp1
                    }), new et.asn1.DERInteger({
                        bigint: this.dmq1
                    }), new et.asn1.DERInteger({
                        bigint: this.coeff
                    })]
                }
                  , e = new et.asn1.DERSequence(t);
                return e.getEncodedHex()
            }
            ,
            i.prototype.getPrivateBaseKeyB64 = function() {
                return u(this.getPrivateBaseKey())
            }
            ,
            i.prototype.getPublicBaseKey = function() {
                var t = new et.asn1.DERSequence({
                    array: [new et.asn1.DERObjectIdentifier({
                        oid: "1.2.840.113549.1.1.1"
                    }), new et.asn1.DERNull]
                })
                  , e = new et.asn1.DERSequence({
                    array: [new et.asn1.DERInteger({
                        bigint: this.n
                    }), new et.asn1.DERInteger({
                        int: this.e
                    })]
                })
                  , n = new et.asn1.DERBitString({
                    hex: "00" + e.getEncodedHex()
                })
                  , i = new et.asn1.DERSequence({
                    array: [t, n]
                });
                return i.getEncodedHex()
            }
            ,
            i.prototype.getPublicBaseKeyB64 = function() {
                return u(this.getPublicBaseKey())
            }
            ,
            i.wordwrap = function(t, e) {
                if (e = e || 64,
                !t)
                    return t;
                var n = "(.{1," + e + "})( +|$\n?)|(.{1," + e + "})";
                return t.match(RegExp(n, "g")).join("\n")
            }
            ,
            i.prototype.getPrivateKey = function() {
                var t = "-----BEGIN RSA PRIVATE KEY-----\n";
                return t += i.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
                t += "-----END RSA PRIVATE KEY-----"
            }
            ,
            i.prototype.getPublicKey = function() {
                var t = "-----BEGIN PUBLIC KEY-----\n";
                return t += i.wordwrap(this.getPublicBaseKeyB64()) + "\n",
                t += "-----END PUBLIC KEY-----"
            }
            ,
            i.hasPublicKeyProperty = function(t) {
                return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e")
            }
            ,
            i.hasPrivateKeyProperty = function(t) {
                return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e") && t.hasOwnProperty("d") && t.hasOwnProperty("p") && t.hasOwnProperty("q") && t.hasOwnProperty("dmp1") && t.hasOwnProperty("dmq1") && t.hasOwnProperty("coeff")
            }
            ,
            i.prototype.parsePropertiesFrom = function(t) {
                this.n = t.n,
                this.e = t.e,
                t.hasOwnProperty("d") && (this.d = t.d,
                this.p = t.p,
                this.q = t.q,
                this.dmp1 = t.dmp1,
                this.dmq1 = t.dmq1,
                this.coeff = t.coeff)
            }
            ,
            i
        }(Z)
          , it = function() {
            function t(t) {
                t = t || {},
                this.default_key_size = parseInt(t.default_key_size, 10) || 1024,
                this.default_public_exponent = t.default_public_exponent || "010001",
                this.log = t.log || !1,
                this.key = null
            }
            return t.prototype.setKey = function(t) {
                this.log && this.key && console.warn("A key was already set, overriding existing."),
                this.key = new nt(t)
            }
            ,
            t.prototype.setPrivateKey = function(t) {
                this.setKey(t)
            }
            ,
            t.prototype.setPublicKey = function(t) {
                this.setKey(t)
            }
            ,
            t.prototype.decrypt = function(t) {
                try {
                    return this.getKey().decrypt(h(t))
                } catch (t) {
                    return !1
                }
            }
            ,
            t.prototype.encrypt = function(t) {
                try {
                    return u(this.getKey().encrypt(t))
                } catch (t) {
                    return !1
                }
            }
            ,
            t.prototype.sign = function(t, e, n) {
                try {
                    return u(this.getKey().sign(t, e, n))
                } catch (t) {
                    return !1
                }
            }
            ,
            t.prototype.verify = function(t, e, n) {
                try {
                    return this.getKey().verify(t, h(e), n)
                } catch (t) {
                    return !1
                }
            }
            ,
            t.prototype.getKey = function(t) {
                if (!this.key) {
                    if (this.key = new nt,
                    t && "[object Function]" === {}.toString.call(t))
                        return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, t);
                    this.key.generate(this.default_key_size, this.default_public_exponent)
                }
                return this.key
            }
            ,
            t.prototype.getPrivateKey = function() {
                return this.getKey().getPrivateKey()
            }
            ,
            t.prototype.getPrivateKeyB64 = function() {
                return this.getKey().getPrivateBaseKeyB64()
            }
            ,
            t.prototype.getPublicKey = function() {
                return this.getKey().getPublicKey()
            }
            ,
            t.prototype.getPublicKeyB64 = function() {
                return this.getKey().getPublicBaseKeyB64()
            }
            ,
            t.version = "3.0.0-rc.1",
            t
        }();
        window.JSEncrypt = it,
        t.JSEncrypt = it,
        t.default = it,
        Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }(e)
}
, function(t, e, n) {
    t.exports = n(25)
}
, function(t, e, n) {
    var i, r, c;
    t.exports = (i = n(0),
    c = (r = i).lib.WordArray,
    r.enc.Base64 = {
        stringify: function(t) {
            var e = t.words
              , n = t.sigBytes
              , i = this._map;
            t.clamp();
            for (var r = [], o = 0; o < n; o += 3)
                for (var a = (e[o >>> 2] >>> 24 - o % 4 * 8 & 255) << 16 | (e[o + 1 >>> 2] >>> 24 - (o + 1) % 4 * 8 & 255) << 8 | e[o + 2 >>> 2] >>> 24 - (o + 2) % 4 * 8 & 255, s = 0; s < 4 && o + .75 * s < n; s++)
                    r.push(i.charAt(a >>> 6 * (3 - s) & 63));
            var c = i.charAt(64);
            if (c)
                for (; r.length % 4; )
                    r.push(c);
            return r.join("")
        },
        parse: function(t) {
            var e = t.length
              , n = this._map
              , i = this._reverseMap;
            if (!i) {
                i = this._reverseMap = [];
                for (var r = 0; r < n.length; r++)
                    i[n.charCodeAt(r)] = r
            }
            var o = n.charAt(64);
            if (o) {
                var a = t.indexOf(o);
                -1 !== a && (e = a)
            }
            return function(t, e, n) {
                for (var i = [], r = 0, o = 0; o < e; o++)
                    if (o % 4) {
                        var a = n[t.charCodeAt(o - 1)] << o % 4 * 2
                          , s = n[t.charCodeAt(o)] >>> 6 - o % 4 * 2;
                        i[r >>> 2] |= (a | s) << 24 - r % 4 * 8,
                        r++
                    }
                return c.create(i, r)
            }(t, e, i)
        },
        _map: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    },
    i.enc.Base64)
}
, function(t, e, n) {
    var a;
    t.exports = (a = n(0),
    function(u) {
        var t = a
          , e = t.lib
          , n = e.WordArray
          , i = e.Hasher
          , r = t.algo
          , O = [];
        !function() {
            for (var t = 0; t < 64; t++)
                O[t] = 4294967296 * u.abs(u.sin(t + 1)) | 0
        }();
        var o = r.MD5 = i.extend({
            _doReset: function() {
                this._hash = new n.init([1732584193, 4023233417, 2562383102, 271733878])
            },
            _doProcessBlock: function(t, e) {
                for (var n = 0; n < 16; n++) {
                    var i = e + n
                      , r = t[i];
                    t[i] = 16711935 & (r << 8 | r >>> 24) | 4278255360 & (r << 24 | r >>> 8)
                }
                var o = this._hash.words
                  , a = t[e + 0]
                  , s = t[e + 1]
                  , c = t[e + 2]
                  , l = t[e + 3]
                  , u = t[e + 4]
                  , h = t[e + 5]
                  , d = t[e + 6]
                  , f = t[e + 7]
                  , p = t[e + 8]
                  , g = t[e + 9]
                  , m = t[e + 10]
                  , y = t[e + 11]
                  , v = t[e + 12]
                  , b = t[e + 13]
                  , w = t[e + 14]
                  , T = t[e + 15]
                  , A = o[0]
                  , E = o[1]
                  , x = o[2]
                  , S = o[3];
                E = k(E = k(E = k(E = k(E = D(E = D(E = D(E = D(E = B(E = B(E = B(E = B(E = C(E = C(E = C(E = C(E, x = C(x, S = C(S, A = C(A, E, x, S, a, 7, O[0]), E, x, s, 12, O[1]), A, E, c, 17, O[2]), S, A, l, 22, O[3]), x = C(x, S = C(S, A = C(A, E, x, S, u, 7, O[4]), E, x, h, 12, O[5]), A, E, d, 17, O[6]), S, A, f, 22, O[7]), x = C(x, S = C(S, A = C(A, E, x, S, p, 7, O[8]), E, x, g, 12, O[9]), A, E, m, 17, O[10]), S, A, y, 22, O[11]), x = C(x, S = C(S, A = C(A, E, x, S, v, 7, O[12]), E, x, b, 12, O[13]), A, E, w, 17, O[14]), S, A, T, 22, O[15]), x = B(x, S = B(S, A = B(A, E, x, S, s, 5, O[16]), E, x, d, 9, O[17]), A, E, y, 14, O[18]), S, A, a, 20, O[19]), x = B(x, S = B(S, A = B(A, E, x, S, h, 5, O[20]), E, x, m, 9, O[21]), A, E, T, 14, O[22]), S, A, u, 20, O[23]), x = B(x, S = B(S, A = B(A, E, x, S, g, 5, O[24]), E, x, w, 9, O[25]), A, E, l, 14, O[26]), S, A, p, 20, O[27]), x = B(x, S = B(S, A = B(A, E, x, S, b, 5, O[28]), E, x, c, 9, O[29]), A, E, f, 14, O[30]), S, A, v, 20, O[31]), x = D(x, S = D(S, A = D(A, E, x, S, h, 4, O[32]), E, x, p, 11, O[33]), A, E, y, 16, O[34]), S, A, w, 23, O[35]), x = D(x, S = D(S, A = D(A, E, x, S, s, 4, O[36]), E, x, u, 11, O[37]), A, E, f, 16, O[38]), S, A, m, 23, O[39]), x = D(x, S = D(S, A = D(A, E, x, S, b, 4, O[40]), E, x, a, 11, O[41]), A, E, l, 16, O[42]), S, A, d, 23, O[43]), x = D(x, S = D(S, A = D(A, E, x, S, g, 4, O[44]), E, x, v, 11, O[45]), A, E, T, 16, O[46]), S, A, c, 23, O[47]), x = k(x, S = k(S, A = k(A, E, x, S, a, 6, O[48]), E, x, f, 10, O[49]), A, E, w, 15, O[50]), S, A, h, 21, O[51]), x = k(x, S = k(S, A = k(A, E, x, S, v, 6, O[52]), E, x, l, 10, O[53]), A, E, m, 15, O[54]), S, A, s, 21, O[55]), x = k(x, S = k(S, A = k(A, E, x, S, p, 6, O[56]), E, x, T, 10, O[57]), A, E, d, 15, O[58]), S, A, b, 21, O[59]), x = k(x, S = k(S, A = k(A, E, x, S, u, 6, O[60]), E, x, y, 10, O[61]), A, E, c, 15, O[62]), S, A, g, 21, O[63]),
                o[0] = o[0] + A | 0,
                o[1] = o[1] + E | 0,
                o[2] = o[2] + x | 0,
                o[3] = o[3] + S | 0
            },
            _doFinalize: function() {
                var t = this._data
                  , e = t.words
                  , n = 8 * this._nDataBytes
                  , i = 8 * t.sigBytes;
                e[i >>> 5] |= 128 << 24 - i % 32;
                var r = u.floor(n / 4294967296)
                  , o = n;
                e[15 + (i + 64 >>> 9 << 4)] = 16711935 & (r << 8 | r >>> 24) | 4278255360 & (r << 24 | r >>> 8),
                e[14 + (i + 64 >>> 9 << 4)] = 16711935 & (o << 8 | o >>> 24) | 4278255360 & (o << 24 | o >>> 8),
                t.sigBytes = 4 * (e.length + 1),
                this._process();
                for (var a = this._hash, s = a.words, c = 0; c < 4; c++) {
                    var l = s[c];
                    s[c] = 16711935 & (l << 8 | l >>> 24) | 4278255360 & (l << 24 | l >>> 8)
                }
                return a
            },
            clone: function() {
                var t = i.clone.call(this);
                return t._hash = this._hash.clone(),
                t
            }
        });
        function C(t, e, n, i, r, o, a) {
            var s = t + (e & n | ~e & i) + r + a;
            return (s << o | s >>> 32 - o) + e
        }
        function B(t, e, n, i, r, o, a) {
            var s = t + (e & i | n & ~i) + r + a;
            return (s << o | s >>> 32 - o) + e
        }
        function D(t, e, n, i, r, o, a) {
            var s = t + (e ^ n ^ i) + r + a;
            return (s << o | s >>> 32 - o) + e
        }
        function k(t, e, n, i, r, o, a) {
            var s = t + (n ^ (e | ~i)) + r + a;
            return (s << o | s >>> 32 - o) + e
        }
        t.MD5 = i._createHelper(o),
        t.HmacMD5 = i._createHmacHelper(o)
    }(Math),
    a.MD5)
}
, function(t, e, n) {
    var i, r, o, a, s, c, h, l;
    t.exports = (i = n(0),
    o = (r = i).lib,
    a = o.WordArray,
    s = o.Hasher,
    c = r.algo,
    h = [],
    l = c.SHA1 = s.extend({
        _doReset: function() {
            this._hash = new a.init([1732584193, 4023233417, 2562383102, 271733878, 3285377520])
        },
        _doProcessBlock: function(t, e) {
            for (var n = this._hash.words, i = n[0], r = n[1], o = n[2], a = n[3], s = n[4], c = 0; c < 80; c++) {
                if (c < 16)
                    h[c] = 0 | t[e + c];
                else {
                    var l = h[c - 3] ^ h[c - 8] ^ h[c - 14] ^ h[c - 16];
                    h[c] = l << 1 | l >>> 31
                }
                var u = (i << 5 | i >>> 27) + s + h[c];
                u += c < 20 ? 1518500249 + (r & o | ~r & a) : c < 40 ? 1859775393 + (r ^ o ^ a) : c < 60 ? (r & o | r & a | o & a) - 1894007588 : (r ^ o ^ a) - 899497514,
                s = a,
                a = o,
                o = r << 30 | r >>> 2,
                r = i,
                i = u
            }
            n[0] = n[0] + i | 0,
            n[1] = n[1] + r | 0,
            n[2] = n[2] + o | 0,
            n[3] = n[3] + a | 0,
            n[4] = n[4] + s | 0
        },
        _doFinalize: function() {
            var t = this._data
              , e = t.words
              , n = 8 * this._nDataBytes
              , i = 8 * t.sigBytes;
            return e[i >>> 5] |= 128 << 24 - i % 32,
            e[14 + (i + 64 >>> 9 << 4)] = Math.floor(n / 4294967296),
            e[15 + (i + 64 >>> 9 << 4)] = n,
            t.sigBytes = 4 * e.length,
            this._process(),
            this._hash
        },
        clone: function() {
            var t = s.clone.call(this);
            return t._hash = this._hash.clone(),
            t
        }
    }),
    r.SHA1 = s._createHelper(l),
    r.HmacSHA1 = s._createHmacHelper(l),
    i.SHA1)
}
, function(t, e, n) {
    var i, r, o, a, s, l, c;
    t.exports = (i = n(0),
    o = (r = i).lib,
    a = o.Base,
    s = r.enc,
    l = s.Utf8,
    c = r.algo,
    void (c.HMAC = a.extend({
        init: function(t, e) {
            t = this._hasher = new t.init,
            "string" == typeof e && (e = l.parse(e));
            var n = t.blockSize
              , i = 4 * n;
            e.sigBytes > i && (e = t.finalize(e)),
            e.clamp();
            for (var r = this._oKey = e.clone(), o = this._iKey = e.clone(), a = r.words, s = o.words, c = 0; c < n; c++)
                a[c] ^= 1549556828,
                s[c] ^= 909522486;
            r.sigBytes = o.sigBytes = i,
            this.reset()
        },
        reset: function() {
            var t = this._hasher;
            t.reset(),
            t.update(this._iKey)
        },
        update: function(t) {
            return this._hasher.update(t),
            this
        },
        finalize: function(t) {
            var e = this._hasher
              , n = e.finalize(t);
            e.reset();
            var i = e.finalize(this._oKey.clone().concat(n));
            return i
        }
    })))
}
, function(t, e, n) {
    var i, r, o, a, c, s, l, u, h, d, f, p, g, m, y, v, b, w, T, A, E, x, S;
    t.exports = (i = n(0),
    n(9),
    void (i.lib.Cipher || (o = (r = i).lib,
    a = o.Base,
    c = o.WordArray,
    s = o.BufferedBlockAlgorithm,
    (l = r.enc).Utf8,
    u = l.Base64,
    h = r.algo,
    d = h.EvpKDF,
    f = o.Cipher = s.extend({
        cfg: a.extend(),
        createEncryptor: function(t, e) {
            return this.create(this._ENC_XFORM_MODE, t, e)
        },
        createDecryptor: function(t, e) {
            return this.create(this._DEC_XFORM_MODE, t, e)
        },
        init: function(t, e, n) {
            this.cfg = this.cfg.extend(n),
            this._xformMode = t,
            this._key = e,
            this.reset()
        },
        reset: function() {
            s.reset.call(this),
            this._doReset()
        },
        process: function(t) {
            return this._append(t),
            this._process()
        },
        finalize: function(t) {
            t && this._append(t);
            var e = this._doFinalize();
            return e
        },
        keySize: 4,
        ivSize: 4,
        _ENC_XFORM_MODE: 1,
        _DEC_XFORM_MODE: 2,
        _createHelper: function() {
            function r(t) {
                return "string" == typeof t ? S : A
            }
            return function(i) {
                window.entry = {
                    encrypt: function(t, e, n) {
                        return r(e).encrypt(i, t, e, n)
                    },
                    decrypt: function(t, e, n) {
                        return r(e).decrypt(i, t, e, n)
                    }
                }
                return window.entry
            }
        }()
    }),
    o.StreamCipher = f.extend({
        _doFinalize: function() {
            var t = this._process(!0);
            return t
        },
        blockSize: 1
    }),
    p = r.mode = {},
    g = o.BlockCipherMode = a.extend({
        createEncryptor: function(t, e) {
            return this.Encryptor.create(t, e)
        },
        createDecryptor: function(t, e) {
            return this.Decryptor.create(t, e)
        },
        init: function(t, e) {
            this._cipher = t,
            this._iv = e
        }
    }),
    m = p.CBC = function() {
        var t = g.extend();
        function o(t, e, n) {
            var i = this._iv;
            if (i) {
                var r = i;
                this._iv = void 0
            } else
                var r = this._prevBlock;
            for (var o = 0; o < n; o++)
                t[e + o] ^= r[o]
        }
        return t.Encryptor = t.extend({
            processBlock: function(t, e) {
                var n = this._cipher
                  , i = n.blockSize;
                o.call(this, t, e, i),
                n.encryptBlock(t, e),
                this._prevBlock = t.slice(e, e + i)
            }
        }),
        t.Decryptor = t.extend({
            processBlock: function(t, e) {
                var n = this._cipher
                  , i = n.blockSize
                  , r = t.slice(e, e + i);
                n.decryptBlock(t, e),
                o.call(this, t, e, i),
                this._prevBlock = r
            }
        }),
        t
    }(),
    y = r.pad = {},
    v = y.Pkcs7 = {
        pad: function(t, e) {
            for (var n = 4 * e, i = n - t.sigBytes % n, r = i << 24 | i << 16 | i << 8 | i, o = [], a = 0; a < i; a += 4)
                o.push(r);
            var s = c.create(o, i);
            t.concat(s)
        },
        unpad: function(t) {
            var e = 255 & t.words[t.sigBytes - 1 >>> 2];
            t.sigBytes -= e
        }
    },
    o.BlockCipher = f.extend({
        cfg: f.cfg.extend({
            mode: m,
            padding: v
        }),
        reset: function() {
            f.reset.call(this);
            var t = this.cfg
              , e = t.iv
              , n = t.mode;
            if (this._xformMode == this._ENC_XFORM_MODE)
                var i = n.createEncryptor;
            else {
                var i = n.createDecryptor;
                this._minBufferSize = 1
            }
            this._mode && this._mode.__creator == i ? this._mode.init(this, e && e.words) : (this._mode = i.call(n, this, e && e.words),
            this._mode.__creator = i)
        },
        _doProcessBlock: function(t, e) {
            this._mode.processBlock(t, e)
        },
        _doFinalize: function() {
            var t = this.cfg.padding;
            if (this._xformMode == this._ENC_XFORM_MODE) {
                t.pad(this._data, this.blockSize);
                var e = this._process(!0)
            } else {
                var e = this._process(!0);
                t.unpad(e)
            }
            return e
        },
        blockSize: 4
    }),
    b = o.CipherParams = a.extend({
        init: function(t) {
            this.mixIn(t)
        },
        toString: function(t) {
            return (t || this.formatter).stringify(this)
        }
    }),
    w = r.format = {},
    T = w.OpenSSL = {
        stringify: function(t) {
            var e = t.ciphertext
              , n = t.salt;
            if (n)
                var i = c.create([1398893684, 1701076831]).concat(n).concat(e);
            else
                var i = e;
            return i.toString(u)
        },
        parse: function(t) {
            var e = u.parse(t)
              , n = e.words;
            if (1398893684 == n[0] && 1701076831 == n[1]) {
                var i = c.create(n.slice(2, 4));
                n.splice(0, 4),
                e.sigBytes -= 16
            }
            return b.create({
                ciphertext: e,
                salt: i
            })
        }
    },
    A = o.SerializableCipher = a.extend({
        cfg: a.extend({
            format: T
        }),
        encrypt: function(t, e, n, i) {
            i = this.cfg.extend(i);
            var r = t.createEncryptor(n, i)
              , o = r.finalize(e)
              , a = r.cfg;
            return b.create({
                ciphertext: o,
                key: n,
                iv: a.iv,
                algorithm: t,
                mode: a.mode,
                padding: a.padding,
                blockSize: t.blockSize,
                formatter: i.format
            })
        },
        decrypt: function(t, e, n, i) {
            i = this.cfg.extend(i),
            e = this._parse(e, i.format);
            var r = t.createDecryptor(n, i).finalize(e.ciphertext);
            return r
        },
        _parse: function(t, e) {
            return "string" == typeof t ? e.parse(t, this) : t
        }
    }),
    E = r.kdf = {},
    x = E.OpenSSL = {
        execute: function(t, e, n, i) {
            i || (i = c.random(8));
            var r = d.create({
                keySize: e + n
            }).compute(t, i)
              , o = c.create(r.words.slice(e), 4 * n);
            return r.sigBytes = 4 * e,
            b.create({
                key: r,
                iv: o,
                salt: i
            })
        }
    },
    S = o.PasswordBasedCipher = A.extend({
        cfg: A.cfg.extend({
            kdf: x
        }),
        encrypt: function(t, e, n, i) {
            var r = (i = this.cfg.extend(i)).kdf.execute(n, t.keySize, t.ivSize);
            i.iv = r.iv;
            var o = A.encrypt.call(this, t, e, r.key, i);
            return o.mixIn(r),
            o
        },
        decrypt: function(t, e, n, i) {
            i = this.cfg.extend(i),
            e = this._parse(e, i.format);
            var r = i.kdf.execute(n, t.keySize, t.ivSize, e.salt);
            i.iv = r.iv;
            var o = A.decrypt.call(this, t, e, r.key, i);
            return o
        }
    }))))
}
, function(e, t) {
    (function(t) {
        e.exports = t
    }
    ).call(this, {})
}
, function(t, e) {
    t.exports = "data:image/png;base64,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"
}
, function(t, e, n) {
    var i = n(21);
    "string" == typeof i && (i = [[t.i, i, ""]]);
    var r = {
        hmr: !0,
        transform: void 0,
        insertInto: void 0
    };
    n(23)(i, r);
    i.locals && (t.exports = i.locals)
}
, function(t, e, n) {
    (t.exports = n(22)(!1)).push([t.i, '.yp-riddler {\n  color: black;\n}\n.yp-riddler .yp-riddler-winbox {\n  margin: 100px auto 0 auto;\n  border-radius: 2px;\n}\n.yp-riddler .yp-riddler-win {\n  -webkit-touch-callout: none;\n  /* iOS Safari */\n  -webkit-user-select: none;\n  /* Chrome/Safari/Opera */\n  -khtml-user-select: none;\n  /* Konqueror */\n  -moz-user-select: none;\n  /* Firefox */\n  -ms-user-select: none;\n  /* Internet Explorer/Edge */\n  user-select: none;\n  -moz-box-sizing: content-box;\n  -webkit-box-sizing: content-box;\n  box-sizing: content-box;\n  background-color: white;\n  padding: 10px;\n}\n.yp-riddler .yp-riddler-tip-text-container {\n  text-align: left;\n}\n.yp-riddler .yp-riddler-tip-text-container > * {\n  vertical-align: middle;\n}\n.yp-riddler .yp-riddler-tip-text-container span {\n  color: black;\n}\n.yp-riddler .yp-riddler-tip-text-container img {\n  width: 24%;\n  margin-left: 5px;\n}\n.yp-riddler .yp-riddler-click-img-container {\n  position: relative;\n}\n.yp-riddler .yp-riddler-click-img-container .yp-riddler-power-img {\n  height: 18px;\n  position: absolute;\n  bottom: 8px;\n  right: 8px;\n}\n.yp-riddler .yp-riddler-click-position {\n  width: 32px;\n  height: 32px;\n  background-position: center;\n  background-repeat: no-repeat;\n  background-size: 100%;\n  position: absolute;\n  background-color: rgba(83, 159, 254, 0.8);\n  box-sizing: border-box;\n  box-shadow: 0 0 10px black;\n  border-radius: 50%;\n  text-align: center;\n  line-height: 26px;\n  border: 3px solid white;\n  color: #fff;\n}\n.yp-riddler .yp-riddler-slide-img-container {\n  position: relative;\n}\n.yp-riddler .yp-riddler-slide-img-container > .yp-riddler-slider-bg,\n.yp-riddler .yp-riddler-slide-img-container .yp-riddler-slider-front {\n  display: block;\n}\n.yp-riddler .yp-riddler-slide-img-container .yp-riddler-slider-front {\n  position: absolute;\n  top: 0;\n  left: 0;\n  height: 100%;\n  width: auto;\n}\n.yp-riddler .yp-riddler-slide-img-container .yp-riddler-power-img {\n  height: 18px;\n  position: absolute;\n  bottom: 8px;\n  right: 8px;\n}\n.yp-riddler .yp-riddler-slider-area {\n  margin-top: 10px;\n  background: #E6E7EB;\n  line-height: 40px;\n  height: 40px;\n  text-align: center;\n  position: relative;\n  font-weight: 300;\n  font-size: 5px;\n  cursor: default;\n  user-select: none;\n  text-shadow: none;\n  border-radius: 2px;\n}\n.yp-riddler .yp-riddler-slider-area .yp-riddler-slider-tip-default {\n  white-space: nowrap;\n  overflow: hidden;\n  padding-left: 40px;\n  font-size: 12px;\n  color: #88949d;\n}\n.yp-riddler .yp-riddler-slider-area .yp-riddler-slider-btn {\n  height: 40px;\n  width: 40px;\n  position: absolute;\n  top: 0;\n  background-color: #FFFFFF;\n  box-sizing: border-box;\n  cursor: move;\n  border-radius: 2px;\n  box-shadow: 0px 0px 4px 0px rgba(0, 0, 0, 0.2);\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n@keyframes gogogo {\n  from {\n    padding-left: -5px;\n  }\n  to {\n    padding-left: 5px;\n  }\n}\n.yp-riddler .yp-riddler-slider-area .yp-riddler-slider-btn .yp-riddler-slider-btn-sign {\n  width: 16px;\n  pointer-events: none;\n}\n.yp-riddler .yp-riddler-slider-area .yp-riddler-slider-btn .yp-riddler-slider-btn-mask {\n  position: absolute;\n  width: 40px;\n  height: 40px;\n  animation: myfirst 2s;\n  -moz-animation: myfirst 2s;\n  /* Firefox */\n  -webkit-animation: myfirst 2s;\n  /* Safari 和 Chrome */\n  -o-animation: myfirst 2s;\n  top: 0;\n  background: #fff;\n  left: 0;\n}\n@keyframes myfirst {\n  0% {\n    left: 0;\n    width: 40px;\n  }\n  100% {\n    left: 40px;\n    width: 0px;\n  }\n}\n@-moz-keyframes myfirst {\n  /* Firefox */\n  0% {\n    left: 0;\n    width: 40px;\n  }\n  100% {\n    left: 40px;\n    width: 0px;\n  }\n}\n@-webkit-keyframes myfirst {\n  /* Safari 和 Chrome */\n  0% {\n    left: 0;\n    width: 40px;\n  }\n  100% {\n    left: 40px;\n    width: 0px;\n  }\n}\n@-o-keyframes myfirst {\n  /* Opera */\n  0% {\n    left: 0;\n    width: 40px;\n  }\n  100% {\n    left: 40px;\n    width: 0px;\n  }\n}\n.yp-riddler .yp-riddler-slider-area .yp-riddler-slider-trajectory {\n  height: inherit;\n  position: absolute;\n  top: 0;\n  left: 0;\n  background-color: #EAEFFF;\n  border-radius: 2px;\n}\n.yp-riddler.yp-flat .yp-riddler-win-masker {\n  margin: 0;\n}\n.yp-riddler.yp-flat .yp-riddler-winbox {\n  border: 1px solid #eeeeee;\n  margin: 0;\n}\n.yp-riddler.yp-float .yp-riddler-winbox {\n  border: none;\n  box-shadow: 0 0 5px grey;\n}\n.yp-riddler.yp-float .yp-riddler-win-masker {\n  z-index: 3;\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  padding-bottom: 50px;\n  display: none;\n}\n.yp-riddler.yp-float .yp-riddler-win {\n  margin: 0;\n}\n.yp-riddler.yp-external .yp-riddler-winbox {\n  border: none;\n  box-shadow: 0 0 5px grey;\n  -webkit-animation-name: fadeIn;\n  /*动画名称*/\n  -webkit-animation-duration: 500ms;\n  /*动画持续时间*/\n  -webkit-animation-iteration-count: 1;\n  /*动画次数*/\n  -webkit-animation-delay: 0s;\n  /*延迟时间*/\n}\n.yp-riddler.yp-external .yp-riddler-win-masker {\n  position: absolute;\n  bottom: 0;\n  left: 0;\n  padding-bottom: 50px;\n  display: none;\n}\n.yp-riddler.yp-external .yp-riddler-win {\n  margin: 0;\n}\n.yp-riddler.yp-dialog .yp-riddler-win-masker {\n  cursor: auto;\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  bottom: auto;\n  height: 100%;\n  background-color: rgba(0, 0, 0, 0.6);\n  z-index: 999;\n}\n.yp-riddler .yp-riddler-refresh {\n  pointer-events: auto;\n  display: block;\n  width: 18px;\n  height: 18px;\n  position: absolute;\n  top: 10px;\n  right: 10px;\n  transition: 200ms;\n  cursor: pointer;\n  transition: all 500ms ease-in-out;\n}\n.yp-riddler .yp-riddler-win-masker {\n  background: rgba(0, 0, 0, 0);\n  display: none;\n}\n.yp-riddler .yp-riddler-result-alert-success {\n  width: 100%;\n  height: 24px;\n  line-height: 24px;\n  text-align: center;\n  position: absolute;\n  bottom: 0px;\n  background-color: #52c41a;\n  color: #fff;\n  font-size: 12px;\n  font-family: PingFangSC-Regular;\n  transition: height 0.4s ease-out, opacity 0.2s ease-in, visibility 0.2s ease-in;\n}\n.yp-riddler .yp-riddler-result-alert-error {\n  width: 100%;\n  line-height: 24px;\n  text-align: center;\n  position: absolute;\n  bottom: 0px;\n  background-color: #fee8ea;\n  color: #f5222d;\n  font-size: 12px;\n  font-family: PingFangSC-Regular;\n  transition: height 0.4s ease-out, opacity 0.2s ease-in, visibility 0.2s ease-in;\n}\n.yp-riddler.yp-riddler-button {\n  position: relative;\n  line-height: 40px;\n  height: 40px;\n  cursor: pointer;\n  font-family: "PingFang SC", "Microsoft yahei", "Helvetica Neue", "Helvetica", "Arial", sans-serif;\n  user-select: none;\n  text-align: center;\n  width: 100%;\n  outline: none;\n  text-decoration: none;\n  border: 1px solid #D9D9D9;\n  background-color: #F7F9FA;\n  border-radius: 2px;\n  font-size: 14px;\n  color: #757575;\n}\n.yp-riddler.yp-riddler-button:hover {\n  font-size: 14px;\n  color: #1792FA;\n}\n.yp-riddler.yp-riddler-button .yp-riddler-button_logo {\n  display: inline-block;\n  width: 25px;\n  height: 25px;\n  box-sizing: border-box;\n  transition: 200ms;\n  margin-right: 10px;\n  line-height: 25px;\n  position: relative;\n  top: 6.5px;\n}\n.yp-riddler.yp-riddler-button .yp-riddler-button_logo .yp-riddler-btn_a {\n  width: 100%;\n  height: 100%;\n  background: #145cff;\n  border-radius: 100px;\n  opacity: 0.5;\n  box-shadow: 0 0 6px grey;\n}\n.yp-riddler.yp-riddler-button .yp-riddler-button_logo .yp-riddler-btn_b {\n  width: 17px;\n  height: 17px;\n  background: #145cff;\n  border-radius: 100px;\n  opacity: 0.5;\n  position: absolute;\n  top: 4px;\n  left: 4px;\n}\n.yp-riddler.yp-riddler-button:hover .yp-riddler-button_logo {\n  padding: 4px;\n}\n.yp-riddler .yp-riddler-button-sucButton_logo {\n  display: inline-block;\n  width: 19px;\n  vertical-align: middle;\n  background: #26C267;\n  border-radius: 50%;\n  box-shadow: #26C267 0px 0px 10px;\n  padding: 5px;\n}\n.yp-riddler .yp-riddler-button-sucButton_text {\n  display: inline-block;\n  margin: 0 0 0 10px;\n  color: #26C267;\n}\n@-webkit-keyframes fadeIn {\n  0% {\n    opacity: 0;\n    /*初始状态 透明度为0*/\n  }\n  50% {\n    opacity: 0;\n    /*中间状态 透明度为0*/\n  }\n  100% {\n    opacity: 1;\n    /*结尾状态 透明度为1*/\n  }\n}\n', ""])
}
, function(t, e) {
    t.exports = function(n) {
        var a = [];
        return a.toString = function() {
            return this.map(function(t) {
                var e = function(t, e) {
                    var n = t[1] || ""
                      , i = t[3];
                    if (!i)
                        return n;
                    if (e && "function" == typeof btoa) {
                        var r = (a = i,
                        "/*# sourceMappingURL=data:application/json;charset=utf-8;base64," + btoa(unescape(encodeURIComponent(JSON.stringify(a)))) + " */")
                          , o = i.sources.map(function(t) {
                            return "/*# sourceURL=" + i.sourceRoot + t + " */"
                        });
                        return [n].concat(o).concat([r]).join("\n")
                    }
                    var a;
                    return [n].join("\n")
                }(t, n);
                return t[2] ? "@media " + t[2] + "{" + e + "}" : e
            }).join("")
        }
        ,
        a.i = function(t, e) {
            "string" == typeof t && (t = [[null, t, ""]]);
            for (var n = {}, i = 0; i < this.length; i++) {
                var r = this[i][0];
                "number" == typeof r && (n[r] = !0)
            }
            for (i = 0; i < t.length; i++) {
                var o = t[i];
                "number" == typeof o[0] && n[o[0]] || (e && !o[2] ? o[2] = e : e && (o[2] = "(" + o[2] + ") and (" + e + ")"),
                a.push(o))
            }
        }
        ,
        a
    }
}
, function(t, e, i) {
    var n, r, o, c = {}, l = (n = function() {
        return window && document && document.all && !window.atob
    }
    ,
    function() {
        return void 0 === r && (r = n.apply(this, arguments)),
        r
    }
    ), a = (o = {},
    function(t, e) {
        if ("function" == typeof t)
            return t();
        if (void 0 === o[t]) {
            var n = function(t, e) {
                return e ? e.querySelector(t) : document.querySelector(t)
            }
            .call(this, t, e);
            if (window.HTMLIFrameElement )
                try {
                    n = n.contentDocument.head
                } catch (t) {
                    n = null
                }
            o[t] = n
        }
        return o[t]
    }
    ), u = null, h = 0, s = [], d = i(24);
    function f(t, e) {
        for (var n = 0; n < t.length; n++) {
            var i = t[n]
              , r = c[i.id];
            if (r) {
                r.refs++;
                for (var o = 0; o < r.parts.length; o++)
                    r.parts[o](i.parts[o]);
                for (; o < i.parts.length; o++)
                    r.parts.push(b(i.parts[o], e))
            } else {
                var a = [];
                for (o = 0; o < i.parts.length; o++)
                    a.push(b(i.parts[o], e));
                c[i.id] = {
                    id: i.id,
                    refs: 1,
                    parts: a
                }
            }
        }
    }
    function p(t, e) {
        for (var n = [], i = {}, r = 0; r < t.length; r++) {
            var o = t[r]
              , a = e.base ? o[0] + e.base : o[0]
              , s = {
                css: o[1],
                media: o[2],
                sourceMap: o[3]
            };
            i[a] ? i[a].parts.push(s) : n.push(i[a] = {
                id: a,
                parts: [s]
            })
        }
        return n
    }
    function g(t, e) {
        /*
        var n = a(t.insertInto);
        if (!n)
            throw new Error("Couldn't find a style target. This probably means that the value for the 'insertInto' parameter is invalid.");
        var i = s[s.length - 1];
        if ("top" === t.insertAt)
            i ? i.nextSibling ? n.insertBefore(e, i.nextSibling) : n.appendChild(e) : n.insertBefore(e, n.firstChild),
            s.push(e);
        else if ("bottom" === t.insertAt)
            n.appendChild(e);
        else {
            if ("object" != typeof t.insertAt || !t.insertAt.before)
                throw new Error("[Style Loader]\n\n Invalid value for parameter 'insertAt' ('options.insertAt') found.\n Must be 'top', 'bottom', or Object.\n (https://github.com/webpack-contrib/style-loader#insertat)\n");
            var r = a(t.insertAt.before, n);
            n.insertBefore(e, r)
        }*/
    }
    function m(t) {
        if (null === t.parentNode)
            return !1;
        t.parentNode.removeChild(t);
        var e = s.indexOf(t);
        0 <= e && s.splice(e, 1)
    }
    function y(t) {
        var e = document.createElement("style");
        if (void 0 === t.attrs.type && (t.attrs.type = "text/css"),
        void 0 === t.attrs.nonce) {
            var n = function() {
                0;
                return i.nc
            }();
            n && (t.attrs.nonce = n)
        }
        return v(e, t.attrs),
        g(t, e),
        e
    }
    function v(e, n) {
        Object.keys(n).forEach(function(t) {
            e.setAttribute(t, n[t])
        })
    }
    function b(e, t) {
        var n, i, r, o, a, s;
        if (t.transform && e.css) {
            if (!(o = "function" == typeof t.transform ? t.transform(e.css) : t.transform.default(e.css)))
                return function() {}
                ;
            e.css = o
        }
        if (t.singleton) {
            var c = h++;
            n = u || (u = y(t)),
            i = A.bind(null, n, c, !1),
            r = A.bind(null, n, c, !0)
        } else
            r = e.sourceMap && "function" == typeof URL && "function" == typeof URL.createObjectURL && "function" == typeof URL.revokeObjectURL && "function" == typeof Blob && "function" == typeof btoa ? (a = t,
            s = document.createElement("link"),
            void 0 === a.attrs.type && (a.attrs.type = "text/css"),
            a.attrs.rel = "stylesheet",
            v(s, a.attrs),
            g(a, s),
            i = function(t, e, n) {
                var i = n.css
                  , r = n.sourceMap
                  , o = void 0 === e.convertToAbsoluteUrls && r;
                (e.convertToAbsoluteUrls || o) && (i = d(i));
                r && (i += "\n/*# sourceMappingURL=data:application/json;base64," + btoa(unescape(encodeURIComponent(JSON.stringify(r)))) + " */");
                var a = new Blob([i],{
                    type: "text/css"
                })
                  , s = t.href;
                t.href = URL.createObjectURL(a),
                s && URL.revokeObjectURL(s)
            }
            .bind(null, n = s, t),
            function() {
                m(n),
                n.href && URL.revokeObjectURL(n.href)
            }
            ) : (n = y(t),
            i = function(t, e) {
                var n = e.css
                  , i = e.media;
                i && t.setAttribute("media", i);
                if (t.styleSheet)
                    t.styleSheet.cssText = n;
                else {
                    for (; t.firstChild; ) break;
                        /*t.removeChild(t.firstChild);
                    t.appendChild(document.createTextNode(n))*/
                }
            }
            .bind(null, n),
            function() {
                m(n)
            }
            );
        return i(e),
        function(t) {
            if (t) {
                if (t.css === e.css && t.media === e.media && t.sourceMap === e.sourceMap)
                    return;
                i(e = t)
            } else
                r()
        }
    }
    t.exports = function(t, a) {
        if ("undefined" != typeof DEBUG && DEBUG && "object" != typeof document)
            throw new Error("The style-loader cannot be used in a non-browser environment");
        (a = a || {}).attrs = "object" == typeof a.attrs ? a.attrs : {},
        a.singleton || "boolean" == typeof a.singleton || (a.singleton = l()),
        a.insertInto || (a.insertInto = "head"),
        a.insertAt || (a.insertAt = "bottom");
        var s = p(t, a);
        return f(s, a),
        function(t) {
            for (var e = [], n = 0; n < s.length; n++) {
                var i = s[n];
                (r = c[i.id]).refs--,
                e.push(r)
            }
            t && f(p(t, a), a);
            for (n = 0; n < e.length; n++) {
                var r;
                if (0 === (r = e[n]).refs) {
                    for (var o = 0; o < r.parts.length; o++)
                        r.parts[o]();
                    delete c[r.id]
                }
            }
        }
    }
    ;
    var w, T = (w = [],
    function(t, e) {
        return w[t] = e,
        w.filter(Boolean).join("\n")
    }
    );
    function A(t, e, n, i) {
        var r = n ? "" : i.css;
        if (t.styleSheet)
            t.styleSheet.cssText = T(e, r);
        else {
            var o = document.createTextNode(r)
              , a = t.childNodes;
            a[e] && t.removeChild(a[e]),
            a.length ? t.insertBefore(o, a[e]) : t.appendChild(o)
        }
    }
}
, function(t, e) {
    t.exports = function(t) {
        var e = "undefined" != typeof window && window.location;
        if (!e)
            throw new Error("fixUrls requires window.location");
        if (!t || "string" != typeof t)
            return t;
        var r = e.protocol + "//" + e.host
          , o = r + e.pathname.replace(/\/[^\/]*$/, "/");
        return t.replace(/url\s*\(((?:[^)(]|\((?:[^)(]+|\([^)(]*\))*\))*)\)/gi, function(t, e) {
            var n, i = e.trim().replace(/^"(.*)"$/, function(t, e) {
                return e
            }).replace(/^'(.*)'$/, function(t, e) {
                return e
            });
            return /^(#|data:|http:\/\/|https:\/\/|file:\/\/\/|\s*$)/i.test(i) ? t : (n = 0 === i.indexOf("//") ? i : 0 === i.indexOf("/") ? r + i : o + i.replace(/^\.\//, ""),
            "url(" + JSON.stringify(n) + ")")
        })
    }
}
, function(t, e, n) {
    "use strict";
    function l(t, e) {
        return window.YP_RIDDLER_RESOURCE_LANG[e][t]
    }
    function i() {
        var t = navigator.userAgent;
        return {
            trident: -1 < t.indexOf("Trident"),
            presto: -1 < t.indexOf("Presto"),
            webKit: -1 < t.indexOf("AppleWebKit"),
            gecko: -1 < t.indexOf("Gecko") && -1 == t.indexOf("KHTML"),
            mobile: !!t.match(/AppleWebKit.*Mobile.*/),
            ios: !!t.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/),
            mac: t.match("Macintosh"),
            android: -1 < t.indexOf("Android") || -1 < t.indexOf("Adr"),
            iPhone: -1 < t.indexOf("iPhone"),
            iPad: -1 < t.indexOf("iPad"),
            fireFox: -1 < t.indexOf("Firefox"),
            webApp: -1 == t.indexOf("Safari"),
            weixin: -1 < t.indexOf("MicroMessenger"),
            qq: " qq" == t.match(/\sQQ/i)
        }
    }
    n.r(e);
    var r = {
        YPcaptcha_01: "请点击按钮开始验证",
        YPcaptcha_02: "请按顺序点击:",
        YPcaptcha_03: "向右拖动滑块填充拼图",
        YPcaptcha_04: "验证失败，请重试",
        YPcaptcha_05: "验证成功!"
    }
      , o = {
        "zh-cn": r,
        en: {
            YPcaptcha_01: "Click here to verify",
            YPcaptcha_02: "Select in this order:",
            YPcaptcha_03: "Drag to verify",
            YPcaptcha_04: "Sorry, please try again.",
            YPcaptcha_05: "I am not a robot!"
        }
    }
      , S = "dialog"
      , a = "flat"
      , s = "external"
      , c = -1
      , u = 0
      , h = 1
      , d = 2
      , f = 3
      , p = {
        href: "",
        enText: "Powered by YunPian's CAPTCHA",
        chText: "由云片行为验证提供技术支持"
    };
    function g(t, e) {
        for (var n = 0; n < e.length; n++) {
            var i = e[n];
            i.enumerable = i.enumerable || !1,
            i.configurable = !0,
            "value"in i && (i.writable = !0),
            Object.defineProperty(t, i.key, i)
        }
    }
    var m = function() {
        function d(t, e, n, i, r, o, a, s, c, l, u, h) {
            !function(t, e) {
                if (!(t instanceof e))
                    throw new TypeError("Cannot call a class as a function")
            }(this, d),
            this.captchaId = s,
            this.winWidth = a,
            this.onSuccess = t,
            this.onError = e,
            this.onFail = n,
            this.CONTAINER = i,
            this.jsonpRequest = r,
            this.getCaptcha = o,
            this.waterMark = c,
            this.lang = l,
            this.logoOptions = u || function(r) {
                for (var t = 1; t < arguments.length; t++) {
                    var o = null != arguments[t] ? arguments[t] : {}
                      , e = Object.keys(o);
                    "function" == typeof Object.getOwnPropertySymbols && (e = e.concat(Object.getOwnPropertySymbols(o).filter(function(t) {
                        return Object.getOwnPropertyDescriptor(o, t).enumerable
                    }))),
                    e.forEach(function(t) {
                        var e, n, i;
                        e = r,
                        i = o[n = t],
                        n in e ? Object.defineProperty(e, n, {
                            value: i,
                            enumerable: !0,
                            configurable: !0,
                            writable: !0
                        }) : e[n] = i
                    })
                }
                return r
            }({}, p),
            this.mode = h
        }
        var t, e, n;
        return t = d,
        (e = [{
            key: "render",
            value: function(t) {
                throw new Error("not implement")
            }
        }, {
            key: "verify",
            value: function() {
                throw new Error("not implement")
            }
        }, {
            key: "destroy",
            value: function() {
                var t = this.CONTAINER.getElementsByClassName("yp-riddler-winbox")[0];
                t && t.parentNode.removeChild(t)
            }
        }, {
            key: "makeWin",
            value: function() {
                var t = this.CONTAINER.getElementsByClassName("yp-riddler-win-masker")[0]
                  , e = document.createElement("div")
                  , n = document.createElement("div");
                return n.className = "yp-riddler-winbox",
                n.style.width = this.winWidth + "px",
                "flat" === this.mode && (n.style.width = this.winWidth - 2 + "px"),
                e.className = "yp-riddler-win",
                e.style.width = this.winWidth - 26 + "px",
                "flat" === this.mode && (e.style.padding = "12px"),
                n.appendChild(e),
                t.appendChild(n),
                e.addEventListener(window.EventObj.click, function(t) {
                    t.stopPropagation(),
                    t.preventDefault()
                }),
                e
            }
        }]) && g(t.prototype, e),
        n && g(t, n),
        d
    }();
    function y(t) {
        return (y = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(t) {
            return typeof t
        }
        : function(t) {
            return t && "function" == typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
        }
        )(t)
    }
    function v(t) {
        return function(t) {
            if (Array.isArray(t)) {
                for (var e = 0, n = new Array(t.length); e < t.length; e++)
                    n[e] = t[e];
                return n
            }
        }(t) || function(t) {
            if (Symbol.iterator in Object(t) || "[object Arguments]" === Object.prototype.toString.call(t))
                return Array.from(t)
        }(t) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance")
        }()
    }
    function b(t, e) {
        for (var n = 0; n < e.length; n++) {
            var i = e[n];
            i.enumerable = i.enumerable || !1,
            i.configurable = !0,
            "value"in i && (i.writable = !0),
            Object.defineProperty(t, i.key, i)
        }
    }
    function w(t, e) {
        return !e || "object" !== y(e) && "function" != typeof e ? function(t) {
            if (void 0 !== t)
                return t;
            throw new ReferenceError("this hasn't been initialised - super() hasn't been called")
        }(t) : e
    }
    function T(t) {
        return (T = Object.setPrototypeOf ? Object.getPrototypeOf : function(t) {
            return t.__proto__ || Object.getPrototypeOf(t)
        }
        )(t)
    }
    function A(t, e) {
        return (A = Object.setPrototypeOf || function(t, e) {
            return t.__proto__ = e,
            t
        }
        )(t, e)
    }
    var E = n(1)
      , x = n(2)
      , O = n(3)
      , C = function(t) {
        function o() {
            var t, e;
            !function(t, e) {
                if (!(t instanceof e))
                    throw new TypeError("Cannot call a class as a function")
            }(this, o);
            for (var n = arguments.length, i = new Array(n), r = 0; r < n; r++)
                i[r] = arguments[r];
            return (e = w(this, (t = T(o)).call.apply(t, [this].concat(i)))).position = [],
            e.clickAmount = 0,
            e.captchaImgTag = null,
            e.charactersImgTag = null,
            e.deg = 0,
            e.imgWidth = e.winWidth - 26,
            e.verifyResultTag = null,
            e
        }
        var e, n, i;
        return function(t, e) {
            if ("function" != typeof e && null !== e)
                throw new TypeError("Super expression must either be null or a function");
            t.prototype = Object.create(e && e.prototype, {
                constructor: {
                    value: t,
                    writable: !0,
                    configurable: !0
                }
            }),
            e && A(t, e)
        }(o, m),
        e = o,
        (n = [{
            key: "render",
            value: function(t) {
                var e = t.clickAmount
                  , n = t.captchaImage
                  , i = t.wordsImage;
                this.CONTAINER.getElementsByClassName("yp-riddler-win").length || this.createWin(),
                this.position = [],
                this.cleanClickSign(),
                this.clickAmount = e,
                this.captchaImgTag.src = n,
                this.charactersImgTag.src = i
            }
        }, {
            key: "verify",
            value: function() {
                var e = this
                  , t = window.getComputedStyle(this.captchaImgTag, null)
                  , n = parseInt(t.width)
                  , i = parseInt(t.height)
                  , r = this.position.map(function(t) {
                    return [t[0] / n, t[1] / i]
                });
                this.jsonpRequest("/jsonp/captcha/verify", {
                    points: r
                }, function(t) {
                    if (t.code)
                        return e.cleanClickSign(),
                        void e.onFail(t.code, t.msg);
                    e.showVerifyResult("success", l("YPcaptcha_05", e.lang), !0),
                    e.onSuccess({
                        token: t.data.token,
                        authenticate: t.data.authenticate
                    })
                }, this.onFail)
            }
        }, {
            key: "showVerifyResult",
            value: function(t, e, n) {
                var i = this;
                if (this.verifyResultTag.className = "yp-riddler-result yp-riddler-result-alert-".concat(t),
                this.verifyResultTag.innerHTML = e,
                this.verifyResultTag.style.height = "24px",
                n)
                    var r = setTimeout(function() {
                        i.hiddenVerifyResult(),
                        clearTimeout(r)
                    }, 2e3)
            }
        }, {
            key: "hiddenVerifyResult",
            value: function() {
                this.verifyResultTag.style.height = "0px",
                this.verifyResultTag.innerHTML = ""
            }
        }, {
            key: "cleanClickSign",
            value: function() {
                for (var t = this.CONTAINER.getElementsByClassName("yp-riddler-click-position"); t.length; ) {
                    var e = t[0];
                    e.parentNode.removeChild(e)
                }
                this.position = []
            }
        }, {
            key: "addClickSign",
            value: function(t, e) {
                var n = this
                  , i = this.CONTAINER.getElementsByClassName("yp-riddler-click-img-container")[0]
                  , r = i.getBoundingClientRect();
                if (r.x && r.y ? (t -= r.x,
                e -= r.y) : (t -= r.left,
                e -= r.top),
                this.position.length < this.clickAmount) {
                    this.position.push([t, e]);
                    var o = document.createElement("div");
                    o.className = "yp-riddler-click-position",
                    o.style.top = e - 16 + "px",
                    o.style.left = t - 16 + "px";
                    var a = document.createElement("div");
                    a.className = "yp-riddler-click-position-index",
                    a.innerHTML = this.position.length,
                    a.addEventListener(window.EventObj.click, function(t) {
                        (t.stopPropagation(),
                        t.preventDefault(),
                        t.cancelBubble = !0,
                        parseInt(o.childNodes[0].innerHTML) < n.position.length) ? (v(n.CONTAINER.getElementsByClassName("yp-riddler-click-position")).forEach(function(t) {
                            i.removeChild(t)
                        }),
                        n.position = []) : (i.removeChild(o),
                        n.position.pop())
                    }),
                    o.appendChild(a),
                    i.appendChild(o),
                    this.position.length === this.clickAmount && this.verify()
                }
            }
        }, {
            key: "createWin",
            value: function() {
                var i = this
                  , t = this.makeWin()
                  , e = document.createElement("div");
                e.className = "yp-riddler-click-img-container",
                e.style.height = this.winWidth / 2 + "px",
                e.addEventListener(window.EventObj.click, function(t) {
                    var e = null
                      , n = null;
                    e = "touchmove" === window.EventObj.move ? (n = t.targetTouches[0].clientX,
                    t.targetTouches[0].clientY) : (n = t.clientX,
                    t.clientY),
                    i.addClickSign(n, e)
                });
                var n = document.createElement("img");
                if (n.className = "yp-riddler-click-img",
                n.style.width = this.imgWidth + "px",
                n.style.height = this.winWidth / 2 + "px",
                n.style.backgroundColor = "#c7c7c7",
                this.captchaImgTag = n,
                e.appendChild(n),
                t.appendChild(e),
                this.waterMark) {
                    var r = document.createElement("img");
                    r.className = "yp-riddler-power-img",
                    r.src = "en" === this.lang ? x : O,
                    e.appendChild(r)
                }
                var o = document.createElement("div");
                o.className = "yp-riddler-tip-text-container";
                var a = document.createElement("span");
                a.innerHTML = l("YPcaptcha_02", this.lang),
                o.appendChild(a);
                var s = document.createElement("img");
                this.charactersImgTag = s,
                o.appendChild(s),
                this.verifyResultTag = document.createElement("div"),
                this.verifyResultTag.className = "yp-riddler-result",
                e.appendChild(this.verifyResultTag),
                t.appendChild(o);
                var c = document.createElement("img");
                c.src = E,
                c.className = "yp-riddler-refresh",
                c.addEventListener(window.EventObj.click, function(t) {
                    t.stopPropagation(),
                    t.preventDefault(),
                    i.cleanClickSign(),
                    i.deg += 360,
                    c.style.transform = "rotate(".concat(i.deg, "deg)"),
                    i.showVerifyResult("", "", !1),
                    i.getCaptcha()
                }),
                e.appendChild(c)
            }
        }]) && b(e.prototype, n),
        i && b(e, i),
        o
    }();
    function B(t) {
        return (B = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(t) {
            return typeof t
        }
        : function(t) {
            return t && "function" == typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
        }
        )(t)
    }
    function D(t) {
        return function(t) {
            if (Array.isArray(t)) {
                for (var e = 0, n = new Array(t.length); e < t.length; e++)
                    n[e] = t[e];
                return n
            }
        }(t) || function(t) {
            if (Symbol.iterator in Object(t) || "[object Arguments]" === Object.prototype.toString.call(t))
                return Array.from(t)
        }(t) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance")
        }()
    }
    function k(t, e) {
        for (var n = 0; n < e.length; n++) {
            var i = e[n];
            i.enumerable = i.enumerable || !1,
            i.configurable = !0,
            "value"in i && (i.writable = !0),
            Object.defineProperty(t, i.key, i)
        }
    }
    function R(t, e) {
        return !e || "object" !== B(e) && "function" != typeof e ? function(t) {
            if (void 0 !== t)
                return t;
            throw new ReferenceError("this hasn't been initialised - super() hasn't been called")
        }(t) : e
    }
    function I(t) {
        return (I = Object.setPrototypeOf ? Object.getPrototypeOf : function(t) {
            return t.__proto__ || Object.getPrototypeOf(t)
        }
        )(t)
    }
    function N(t, e) {
        return (N = Object.setPrototypeOf || function(t, e) {
            return t.__proto__ = e,
            t
        }
        )(t, e)
    }
    var P = n(1)
      , M = n(6)
      , L = n(7)
      , V = n(3)
      , j = n(2)
      , U = n(8)
      , F = function(t) {
        function o() {
            var t, e;
            !function(t, e) {
                if (!(t instanceof e))
                    throw new TypeError("Cannot call a class as a function")
            }(this, o);
            for (var n = arguments.length, i = new Array(n), r = 0; r < n; r++)
                i[r] = arguments[r];
            return (e = R(this, (t = I(o)).call.apply(t, [this].concat(i)))).position = [],
            e.bgTag = null,
            e.alertImgTag = null,
            e.trajectoryTag = null,
            e.rawX = 0,
            e.rawTimestamp = 0,
            e.offsetX = 0,
            e.alertTextTag = null,
            e.btnTag = null,
            e.isDraging = !1,
            e.MAX_OFFSET = 0,
            e.MAX_POINTS_AMOUNT = 50,
            e.disabled = !1,
            e.curErrorIndex = 0,
            e.MAX_ERROR = 3,
            e.mouseDown = !1,
            e.proption = 0,
            e.deg = 0,
            e.imgWidth = e.winWidth - 26,
            e.verifyResultTag = null,
            e
        }
        var e, n, i;
        return function(t, e) {
            if ("function" != typeof e && null !== e)
                throw new TypeError("Super expression must either be null or a function");
            t.prototype = Object.create(e && e.prototype, {
                constructor: {
                    value: t,
                    writable: !0,
                    configurable: !0
                }
            }),
            e && N(t, e)
        }(o, m),
        e = o,
        (n = [{
            key: "render",
            value: function(t) {
                var e = t.sliderWidth
                  , n = void 0 === e ? 0 : e
                  , i = t.width
                  , r = void 0 === i ? 1 : i
                  , o = t.bg
                  , a = void 0 === o ? "" : o
                  , s = t.front
                  , c = void 0 === s ? "" : s
                  , l = this.CONTAINER.getElementsByClassName("yp-riddler-win");
                l && !l.length && (this.proption = (n / r).toFixed(2),
                this.createWin()),
                this.bgTag.src = a,
                this.alertImgTag.src = c,
                this.alertImgTag.ondragstart = function() {
                    return !1
                }
                ,
                this.disabled = !1,
                this.resetPosition()
            }
        }, {
            key: "resetPosition",
            value: function() {
                this.position = [],
                this.rawX = 0,
                this.offsetX = 0,
                this.trajectoryTag.style.width = "0px",
                this.moveModule(),
                this.hiddenVerifyResult(),
                this.showTip(l("YPcaptcha_03", this.lang))
            }
        }, {
            key: "verify",
            value: function() {
                var e = this
                  , t = window.getComputedStyle(this.bgTag, null)
                  , n = parseInt(t.width)
                  , i = this.reducePoints()
                  , r = (this.imgWidth - this.alertImgTag.width) * (this.offsetX / (this.imgWidth - 42)) / n;
                this.jsonpRequest("/jsonp/captcha/verify", {
                    points: i,
                    distanceX: r
                }, function(t) {
                    if (t.code)
                        return e.resetPosition(),
                        e.disabled = !0,
                        e.curErrorIndex++,
                        void (e.curErrorIndex < e.MAX_ERROR ? (e.showVerifyResult("error", l("YPcaptcha_04", e.lang)),
                        setTimeout(function() {
                            e.disabled = !1,
                            setTimeout(function() {
                                return e.onFail(t.code, t.msg, !0)
                            }, 0)
                        }, 500)) : (e.disabled = !1,
                        e.curErrorIndex = 0,
                        setTimeout(function() {
                            return e.onFail(t.code, t.msg, !1)
                        }, 0)));
                    e.curErrorIndex = 0,
                    e.showVerifyResult("success", l("YPcaptcha_05", e.lang), !1),
                    e.onSuccess({
                        token: t.data.token,
                        authenticate: t.data.authenticate
                    })
                }, this.onFail)
            }
        }, {
            key: "showTip",
            value: function(t) {
                this.alertTextTag.innerHTML = t,
                this.alertTextTag.className = "yp-riddler-slider-tip-default"
            }
        }, {
            key: "showVerifyResult",
            value: function(t, e) {
                var n = this
                  , i = !(2 < arguments.length && void 0 !== arguments[2]) || arguments[2];
                if ("success" === t) {
                    this.trajectoryTag.style.background = "#E5F6DD",
                    this.CONTAINER.querySelector(".yp-riddler-slider-btn-sign").src = U;
                    var r = document.createElement("div");
                    r.className = "yp-riddler-slider-btn-mask",
                    this.CONTAINER.querySelector(".yp-riddler-slider-btn").appendChild(r);
                    var o = setTimeout(function() {
                        var t = n.CONTAINER.querySelector(".yp-riddler-slider-btn");
                        t && t.removeChild(r),
                        clearTimeout(o)
                    }, 2e3)
                }
                if (this.verifyResultTag.className = "yp-riddler-result yp-riddler-result-alert-".concat(t),
                this.verifyResultTag.innerHTML = e,
                this.verifyResultTag.style.height = "24px",
                i)
                    var a = setTimeout(function() {
                        n.hiddenVerifyResult(),
                        clearTimeout(a)
                    }, 2e3)
            }
        }, {
            key: "createRightDom",
            value: function(t) {
                var e = document.createElement("img");
                e.className = "yp-riddler-slider-btn-sign",
                e.src = M,
                t.appendChild(e)
            }
        }, {
            key: "hiddenVerifyResult",
            value: function() {
                this.verifyResultTag.style.height = "0px",
                this.verifyResultTag.innerHTML = "",
                this.CONTAINER.querySelector(".yp-riddler-slider-btn-sign").src = M
            }
        }, {
            key: "moveModule",
            value: function() {
                this.trajectoryTag.style.width = "".concat(this.offsetX, "px"),
                this.btnTag.style.left = "".concat(this.offsetX, "px"),
                this.alertImgTag.style.left = (this.imgWidth - this.alertImgTag.width) * (this.offsetX / (this.imgWidth - 40)) + "px"
            }
        }, {
            key: "reducePoints",
            value: function() {
                var t = D(this.position);
                if (t.length <= this.MAX_POINTS_AMOUNT)
                    return t;
                var e = [t[0]]
                  , n = t[t.length - 1]
                  , i = Math.floor(t.length / this.MAX_POINTS_AMOUNT);
                if (i < 2)
                    return t;
                for (var r = 1; r < t.length - 2; r += i)
                    e.push(t[r]);
                return e.push(n),
                e
            }
        }, {
            key: "createWin",
            value: function() {
                var e = this
                  , t = this.makeWin()
                  , n = document.createElement("div");
                if (n.className = "yp-riddler-slide-img-container",
                n.style.width = this.imgWidth + "px",
                t.appendChild(n),
                this.waterMark) {
                    var i = document.createElement("img");
                    i.className = "yp-riddler-power-img",
                    i.src = "en" === this.lang ? j : V,
                    n.appendChild(i)
                }
                this.bgTag = document.createElement("img"),
                this.bgTag.className = "yp-riddler-slider-bg",
                this.bgTag.style.width = this.imgWidth + "px",
                this.bgTag.style.height = this.imgWidth / 2 + "px",
                this.bgTag.style.backgroundColor = "#c7c7c7",
                this.alertImgTag = document.createElement("img"),
                this.alertImgTag.className = "yp-riddler-slider-front",
                this.verifyResultTag = document.createElement("div"),
                this.verifyResultTag.className = "yp-riddler-result",
                n.appendChild(this.bgTag),
                n.appendChild(this.alertImgTag),
                n.appendChild(this.verifyResultTag);
                var r = document.createElement("img");
                r.src = P,
                r.addEventListener(window.EventObj.click, function(t) {
                    t.stopPropagation(),
                    t.preventDefault(),
                    e.deg += 360,
                    r.style.transform = "rotate(".concat(e.deg, "deg)"),
                    e.resetPosition(),
                    e.getCaptcha()
                }),
                r.className = "yp-riddler-refresh",
                n.appendChild(r);
                var o = document.createElement("div");
                o.className = "yp-riddler-slider-area",
                t.appendChild(o),
                this.trajectoryTag = document.createElement("div"),
                this.trajectoryTag.className = "yp-riddler-slider-trajectory",
                o.appendChild(this.trajectoryTag),
                this.alertTextTag = document.createElement("div"),
                o.appendChild(this.alertTextTag);
                var a = document.createElement("div");
                a.className = "yp-riddler-slider-btn",
                this.createRightDom(a),
                o.appendChild(a),
                this.btnTag = a,
                this.registerDragEvent()
            }
        }, {
            key: "registerDragEvent",
            value: function() {
                var r = this;
                this.alertImgTag.addEventListener(window.EventObj.down, function(t) {
                    if (!r.offsetX && !r.disabled) {
                        var e = 0;
                        e = "touchmove" === window.EventObj.move ? t.targetTouches[0].pageX : t.pageX,
                        r.mouseDown = !0,
                        r.isDraging = !0,
                        r.rawX = e,
                        r.rawTimestamp = Date.now(),
                        r.showTip(""),
                        r.MAX_OFFSET = r.imgWidth - 40,
                        r.trajectoryTag.style.width = (r.proption - .125) * r.imgWidth / 2 + "px"
                    }
                }),
                this.btnTag.addEventListener(window.EventObj.down, function(t) {
                    if (!r.offsetX && !r.disabled) {
                        r.CONTAINER.querySelector(".yp-riddler-slider-btn-sign").src = L;
                        var e = 0;
                        e = "touchmove" === window.EventObj.move ? t.targetTouches[0].pageX : t.pageX,
                        r.mouseDown = !0,
                        r.isDraging = !0,
                        r.rawX = e,
                        r.rawTimestamp = Date.now(),
                        r.showTip(""),
                        r.MAX_OFFSET = r.imgWidth - 40,
                        r.trajectoryTag.style.width = (r.proption - .125) * r.imgWidth / 2 + "px"
                    }
                }),
                document.addEventListener(window.EventObj.up, function() {
                    r.mouseDown && (r.CONTAINER.querySelector(".yp-riddler-slider-btn-sign").src = M,
                    r.isDraging = !1,
                    r.mouseDown = !1,
                    r.verify())
                }),
                this.CONTAINER.addEventListener(window.EventObj.up, function() {
                    r.mouseDown && (r.CONTAINER.querySelector(".yp-riddler-slider-btn-sign").src = M,
                    r.isDraging = !1,
                    r.mouseDown = !1,
                    r.verify())
                }),
                this.CONTAINER.addEventListener(window.EventObj.move, function(t) {
                    var e = 0
                      , n = 0;
                    if (n = "touchmove" === window.EventObj.move ? (t.preventDefault(),
                    e = t.targetTouches[0].pageX,
                    t.targetTouches[0].pageY) : (e = t.pageX,
                    t.pageY),
                    r.isDraging) {
                        r.offsetX = e - r.rawX,
                        r.offsetX < 0 ? r.offsetX = 0 : r.offsetX > r.MAX_OFFSET && (r.offsetX = r.MAX_OFFSET);
                        var i = [parseInt(e.toFixed(2)), parseInt(n.toFixed(2)), Date.now() - r.rawTimestamp];
                        r.position.push(i),
                        r.moveModule()
                    }
                }),
                this.CONTAINER.getElementsByClassName("yp-riddler-win")[0].addEventListener("mouserleave", function() {
                    r.isDraging && (r.isDraging = !1,
                    r.resetPosition())
                })
            }
        }]) && k(e.prototype, n),
        i && k(e, i),
        o
    }();
    function _(t) {
        return (_ = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(t) {
            return typeof t
        }
        : function(t) {
            return t && "function" == typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
        }
        )(t)
    }
    function H(t) {
        return function(t) {
            if (Array.isArray(t)) {
                for (var e = 0, n = new Array(t.length); e < t.length; e++)
                    n[e] = t[e];
                return n
            }
        }(t) || function(t) {
            if (Symbol.iterator in Object(t) || "[object Arguments]" === Object.prototype.toString.call(t))
                return Array.from(t)
        }(t) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance")
        }()
    }
    function X(t, e) {
        for (var n = 0; n < e.length; n++) {
            var i = e[n];
            i.enumerable = i.enumerable || !1,
            i.configurable = !0,
            "value"in i && (i.writable = !0),
            Object.defineProperty(t, i.key, i)
        }
    }
    function z(t, e) {
        return !e || "object" !== _(e) && "function" != typeof e ? function(t) {
            if (void 0 !== t)
                return t;
            throw new ReferenceError("this hasn't been initialised - super() hasn't been called")
        }(t) : e
    }
    function W(t) {
        return (W = Object.setPrototypeOf ? Object.getPrototypeOf : function(t) {
            return t.__proto__ || Object.getPrototypeOf(t)
        }
        )(t)
    }
    function q(t, e) {
        return (q = Object.setPrototypeOf || function(t, e) {
            return t.__proto__ = e,
            t
        }
        )(t, e)
    }
    var G = n(1)
      , K = n(6)
      , J = n(7)
      , Y = n(3)
      , Q = n(2)
      , Z = n(8)
      , $ = function(t) {
        function o() {
            var t, e;
            !function(t, e) {
                if (!(t instanceof e))
                    throw new TypeError("Cannot call a class as a function")
            }(this, o);
            for (var n = arguments.length, i = new Array(n), r = 0; r < n; r++)
                i[r] = arguments[r];
            return (e = z(this, (t = W(o)).call.apply(t, [this].concat(i)))).position = [],
            e.bgTag = null,
            e.alertImgTag = null,
            e.trajectoryTag = null,
            e.rawX = 0,
            e.rawTimestamp = 0,
            e.offsetX = 0,
            e.alertTextTag = null,
            e.btnTag = null,
            e.maskerTag = null,
            e.isDraging = !1,
            e.MAX_OFFSET = 0,
            e.MAX_POINTS_AMOUNT = 50,
            e.disabled = !1,
            e.curErrorIndex = 0,
            e.MAX_ERROR = 3,
            e.mouseDown = !1,
            e.proption = 0,
            e.deg = 0,
            e
        }
        var e, n, i;
        return function(t, e) {
            if ("function" != typeof e && null !== e)
                throw new TypeError("Super expression must either be null or a function");
            t.prototype = Object.create(e && e.prototype, {
                constructor: {
                    value: t,
                    writable: !0,
                    configurable: !0
                }
            }),
            e && q(t, e)
        }(o, m),
        e = o,
        (n = [{
            key: "render",
            value: function(t) {
                var e = t.sliderWidth
                  , n = void 0 === e ? 0 : e
                  , i = t.width
                  , r = void 0 === i ? 1 : i
                  , o = t.bg
                  , a = void 0 === o ? "" : o
                  , s = t.front
                  , c = void 0 === s ? "" : s
                  , l = this.CONTAINER.getElementsByClassName("yp-riddler-win");
                l && !l.length && (this.proption = (n / r).toFixed(2),
                this.createWin()),
                this.bgTag.src = a,
                this.alertImgTag.src = c,
                this.disabled = !1,
                this.resetPosition()
            }
        }, {
            key: "resetPosition",
            value: function() {
                this.position = [],
                this.rawX = 0,
                this.offsetX = 0,
                this.trajectoryTag.style.width = "0px",
                this.maskerTag.style.display = "none",
                this.moveModule(),
                this.showVerifyResult("", "", !1),
                this.showTip(l("YPcaptcha_03", this.lang))
            }
        }, {
            key: "verify",
            value: function() {
                var e = this
                  , t = window.getComputedStyle(this.bgTag, null)
                  , n = parseInt(t.width)
                  , i = this.reducePoints()
                  , r = this.offsetX / n;
                this.jsonpRequest("/jsonp/captcha/verify", {
                    points: i,
                    distanceX: r
                }, function(t) {
                    if (t.code)
                        return e.resetPosition(),
                        e.showTip(l("YPcaptcha_04", e.lang), "error"),
                        e.disabled = !0,
                        e.curErrorIndex++,
                        void (e.curErrorIndex < e.MAX_ERROR ? setTimeout(function() {
                            e.showTip(l("YPcaptcha_03", e.lang)),
                            e.disabled = !1,
                            setTimeout(function() {
                                return e.onFail(t.code, t.msg, !0)
                            }, 0)
                        }, 500) : (e.curErrorIndex = 0,
                        setTimeout(function() {
                            return e.onFail(t.code, t.msg, !1)
                        }, 0)));
                    e.curErrorIndex = 0,
                    e.showVerifyResult("success", l("YPcaptcha_05", e.lang), !0),
                    e.onSuccess({
                        token: t.data.token,
                        authenticate: t.data.authenticate
                    })
                }, this.onFail)
            }
        }, {
            key: "showTip",
            value: function(t) {
                var e = 1 < arguments.length && void 0 !== arguments[1] && arguments[1];
                this.alertTextTag.innerHTML = t,
                this.alertTextTag.className = "yp-riddler-slider-tip-" + (e ? "error" : "default")
            }
        }, {
            key: "showVerifyResult",
            value: function(t, e, n) {
                var i = this.CONTAINER.getElementsByClassName("yp-riddler-slide-img-container");
                if (n) {
                    if (i && i.length) {
                        var r = document.createElement("div");
                        r.className = "yp-riddler-result yp-riddler-result-alert-".concat(t),
                        r.innerHTML = e,
                        i[0].appendChild(r)
                    }
                    if ("success" === t) {
                        this.trajectoryTag.style.background = "#E5F6DD",
                        document.querySelector(".yp-riddler-slider-btn-sign").src = Z;
                        var o = document.createElement("div");
                        o.className = "yp-riddler-slider-btn-mask",
                        document.querySelector(".yp-riddler-slider-btn").appendChild(o);
                        var a = setTimeout(function() {
                            var t = document.querySelector(".yp-riddler-slider-btn");
                            t && t.removeChild(o),
                            clearTimeout(a)
                        }, 2e3)
                    }
                } else {
                    var s = this.CONTAINER.getElementsByClassName("yp-riddler-result")[0];
                    s && i[0].removeChild(s)
                }
            }
        }, {
            key: "moveModule",
            value: function() {
                this.trajectoryTag.style.width = "".concat(this.offsetX, "px"),
                this.alertImgTag.style.left = "".concat(this.offsetX, "px"),
                this.btnTag.style.left = "".concat(this.offsetX, "px")
            }
        }, {
            key: "reducePoints",
            value: function() {
                var t = H(this.position);
                if (t.length <= this.MAX_POINTS_AMOUNT)
                    return t;
                var e = [t[0]]
                  , n = t[t.length - 1]
                  , i = Math.floor(t.length / this.MAX_POINTS_AMOUNT);
                if (i < 2)
                    return t;
                for (var r = 1; r < t.length - 2; r += i)
                    e.push(t[r]);
                return e.push(n),
                e
            }
        }, {
            key: "externalSlide",
            value: function() {
                var t = this.CONTAINER.getElementsByClassName("yp-riddler")[0]
                  , e = document.createElement("div");
                e.className = "yp-riddler-slider-area",
                e.style.height = this.winWidth / 8 + "px",
                e.style.width = this.winWidth + "px",
                e.style.lineHeight = this.winWidth / 8 + "px",
                t.appendChild(e);
                var n = document.createElement("div");
                n.className = "yp-riddler-slider-btn",
                n.style.width = this.winWidth / 6 + "px";
                var i = document.createElement("span");
                i.className = "yp-riddler-slider-tip-default",
                i.innerHTML = l("YPcaptcha_03", this.lang),
                e.appendChild(i);
                var r = document.createElement("img");
                r.className = "yp-riddler-slider-btn-sign",
                r.src = K,
                n.appendChild(r),
                e.appendChild(n)
            }
        }, {
            key: "createWin",
            value: function() {
                var e = this
                  , t = this.makeWin();
                t.style.width = this.winWidth + "px",
                t.style.padding = "0px";
                var n = document.createElement("div");
                if (n.className = "yp-riddler-slide-img-container",
                n.style.width = this.winWidth + "px",
                t.appendChild(n),
                this.waterMark) {
                    var i = document.createElement("img");
                    i.className = "yp-riddler-power-img",
                    i.src = "en" === this.lang ? Q : Y,
                    n.appendChild(i)
                }
                this.bgTag = document.createElement("img"),
                this.bgTag.className = "yp-riddler-slider-bg",
                this.bgTag.style.width = this.winWidth + "px",
                this.bgTag.style.height = this.winWidth / 2 + "px",
                this.bgTag.style.backgroundColor = "#c7c7c7",
                this.alertImgTag = document.createElement("img"),
                this.alertImgTag.className = "yp-riddler-slider-front",
                this.externalSlide(),
                n.appendChild(this.bgTag),
                n.appendChild(this.alertImgTag);
                var r = document.createElement("img");
                r.src = G,
                r.addEventListener(window.EventObj.click, function(t) {
                    t.stopPropagation(),
                    t.preventDefault(),
                    e.deg += 360,
                    r.style.transform = "rotate(".concat(e.deg, "deg)"),
                    e.resetPosition(),
                    e.getCaptcha()
                }),
                r.className = "yp-riddler-refresh",
                n.appendChild(r);
                var o = this.CONTAINER.getElementsByClassName("yp-riddler-slider-area")[0];
                this.alertTextTag = this.CONTAINER.getElementsByClassName("yp-riddler-slider-tip-default")[0],
                this.alertTextTag.style.paddingLeft = "40px",
                this.alertTextTag.style.fontSize = "14px",
                this.trajectoryTag = document.createElement("div"),
                this.trajectoryTag.className = "yp-riddler-slider-trajectory",
                o.appendChild(this.trajectoryTag),
                this.maskerTag = this.CONTAINER.getElementsByClassName("yp-riddler-win-masker")[0],
                this.maskerTag.style.display = "none",
                this.btnTag = this.CONTAINER.getElementsByClassName("yp-riddler-slider-btn")[0],
                this.maskerTag.style.paddingBottom = this.btnTag.offsetHeight + 10 + "px",
                this.registerDragEvent()
            }
        }, {
            key: "registerDragEvent",
            value: function() {
                var c = this;
                this.btnTag.addEventListener(window.EventObj.down, function(t) {
                    if (!c.offsetX && !c.disabled) {
                        document.querySelector(".yp-riddler-slider-btn-sign").src = J,
                        c.maskerTag.style.display = "block";
                        var e = 0;
                        e = "touchmove" === window.EventObj.move ? t.targetTouches[0].pageX : t.pageX,
                        c.mouseDown = !0,
                        c.isDraging = !0,
                        c.rawX = e,
                        c.rawTimestamp = Date.now(),
                        c.showTip("");
                        var n = window.getComputedStyle(c.btnTag.parentNode, null)
                          , i = window.getComputedStyle(c.btnTag, null)
                          , r = c.CONTAINER.getElementsByClassName("yp-riddler-slider-front")[0].offsetWidth
                          , o = parseInt(n.width)
                          , a = o - r
                          , s = o - parseInt(i.width);
                        s < (c.MAX_OFFSET = a) && (c.MAX_OFFSET = s),
                        c.trajectoryTag.style.marginLeft = "0px",
                        c.trajectoryTag.style.width = (c.proption - .125) * (c.winWidth - 20) / 2 + "px"
                    }
                }),
                this.CONTAINER.addEventListener(window.EventObj.up, function() {
                    c.mouseDown && (document.querySelector(".yp-riddler-slider-btn-sign").src = K,
                    c.isDraging = !1,
                    c.mouseDown = !1,
                    c.maskerTag.style.display = "none",
                    c.verify())
                }),
                this.CONTAINER.addEventListener(window.EventObj.move, function(t) {
                    var e = 0
                      , n = 0;
                    if (n = "touchmove" === window.EventObj.move ? (t.preventDefault(),
                    e = t.targetTouches[0].pageX,
                    t.targetTouches[0].pageY) : (e = t.pageX,
                    t.pageY),
                    c.isDraging) {
                        c.offsetX = e - c.rawX,
                        c.offsetX < 0 ? c.offsetX = 0 : c.offsetX > c.MAX_OFFSET && (c.offsetX = c.MAX_OFFSET);
                        var i = [parseInt(e.toFixed(2)), parseInt(n.toFixed(2)), Date.now() - c.rawTimestamp];
                        c.position.push(i),
                        c.moveModule()
                    }
                }),
                this.CONTAINER.getElementsByClassName("yp-riddler-win-masker")[0].addEventListener("mouseleave", function() {
                    c.isDraging && (c.isDraging = !1,
                    c.resetPosition())
                })
            }
        }]) && X(e.prototype, n),
        i && X(e, i),
        o
    }();
    function tt(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = null != arguments[t] ? arguments[t] : {}
              , i = Object.keys(n);
            "function" == typeof Object.getOwnPropertySymbols && (i = i.concat(Object.getOwnPropertySymbols(n).filter(function(t) {
                return Object.getOwnPropertyDescriptor(n, t).enumerable
            }))),
            i.forEach(function(t) {
                et(e, t, n[t])
            })
        }
        return e
    }
    function et(t, e, n) {
        return e in t ? Object.defineProperty(t, e, {
            value: n,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : t[e] = n,
        t
    }
    function nt(t, e) {
        return function(t) {
            if (Array.isArray(t))
                return t
        }(t) || function(t, e) {
            var n = []
              , i = !0
              , r = !1
              , o = void 0;
            try {
                for (var a, s = t[Symbol.iterator](); !(i = (a = s.next()).done) && (n.push(a.value),
                !e || n.length !== e); i = !0)
                    ;
            } catch (t) {
                r = !0,
                o = t
            } finally {
                try {
                    i || null == s.return || s.return()
                } finally {
                    if (r)
                        throw o
                }
            }
            return n
        }(t, e) || function() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance")
        }()
    }
    function it(t, e, n) {
        return (it = function() {
            if ("undefined" == typeof Reflect || !Reflect.construct)
                return !1;
            if (Reflect.construct.sham)
                return !1;
            if ("function" == typeof Proxy)
                return !0;
            try {
                return Date.prototype.toString.call(Reflect.construct(Date, [], function() {})),
                !0
            } catch (t) {
                return !1
            }
        }() ? Reflect.construct : function(t, e, n) {
            var i = [null];
            i.push.apply(i, e);
            var r = new (Function.bind.apply(t, i));
            return n && rt(r, n.prototype),
            r
        }
        ).apply(null, arguments)
    }
    function rt(t, e) {
        return (rt = Object.setPrototypeOf || function(t, e) {
            return t.__proto__ = e,
            t
        }
        )(t, e)
    }
    function ot(t, e) {
        for (var n = 0; n < e.length; n++) {
            var i = e[n];
            i.enumerable = i.enumerable || !1,
            i.configurable = !0,
            "value"in i && (i.writable = !0),
            Object.defineProperty(t, i.key, i)
        }
    }
    function at(t, e, n) {
        return e && ot(t.prototype, e),
        n && ot(t, n),
        t
    }
    var st = function() {
        function e(t) {
            !function(t, e) {
                if (!(t instanceof e))
                    throw new TypeError("Cannot call a class as a function")
            }(this, e),
            this.pool = {},
            this.expired = 1e3 * t
        }
        return at(e, null, [{
            key: "Instance",
            value: function() {
                if (!this._instance) {
                    for (var t = arguments.length, e = new Array(t), n = 0; n < t; n++)
                        e[n] = arguments[n];
                    this._instance = it(this, e)
                }
                return this._instance
            }
        }]),
        at(e, [{
            key: "makeScriptId",
            value: function(t) {
                return "jsonp_".concat(t)
            }
        }, {
            key: "preAdd",
            value: function() {
                for (var t; (t = Math.random().toString(32).replace("0.", ""))in this.pool; )
                    ;
                return this.pool[t] = {
                    ts: 1 / 0
                },
                t
            }
        }, {
            key: "add",
            value: function(t, e, n) {
                var i = 3 < arguments.length && void 0 !== arguments[3] ? arguments[3] : null;
                this.pool[t] = {
                    ts: Date.now(),
                    cb: n,
                    failCb: i
                };
                var r = document.createElement("script");
                r.src = e,
                r.id = this.makeScriptId(t),
                document.head.appendChild(r)
            }
        }, {
            key: "removeCallback",
            value: function(t) {
                if (t in this.pool) {
                    var e = this.pool[t];
                    delete this.pool[t];
                    var n = document.getElementById(this.makeScriptId(t));
                    return n.parentNode.removeChild(n),
                    e
                }
            }
        }, {
            key: "checkExpired",
            value: function() {
                var t = !0
                  , e = !1
                  , n = void 0;
                try {
                    for (var i, r = function(t) {
                        t || (t = {});
                        var e = Object.keys(t)
                          , n = e.length
                          , i = new Array(n);
                        for (; n--; )
                            i[n] = [e[n], t[e[n]]];
                        return i
                    }(this.pool)[Symbol.iterator](); !(t = (i = r.next()).done); t = !0) {
                        var o = nt(i.value, 2)
                          , a = o[0]
                          , s = o[1].ts;
                        if (Date.now() > s + this.expired) {
                            var c = tt({}, this.removeCallback(a), {
                                msg: "request timeout",
                                code: 408
                            });
                            c.failCb && c.failCb(c)
                        }
                    }
                } catch (t) {
                    e = !0,
                    n = t
                } finally {
                    try {
                        t || null == r.return || r.return()
                    } finally {
                        if (e)
                            throw n
                    }
                }
            }
        }, {
            key: "invoke",
            value: function(t, e) {
                var n = this.pool[t];
                n ? (this.removeCallback(t),
                n.cb(e)) : console.warn("cb[".concat(t, "] is expired"))
            }
        }]),
        e

    }();
    window.pre=new st
    // window.preAdd =st.Instance(10)

    var ct = n(10)
      , lt = n.n(ct)
      , ut = n(4)
      , ht = n.n(ut)
      , dt = n(11)
      , ft = n.n(dt)
      , pt = n(5)
      , gt = n.n(pt)
      , mt = {};
    function yt(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = null != arguments[t] ? arguments[t] : {}
              , i = Object.keys(n);
            "function" == typeof Object.getOwnPropertySymbols && (i = i.concat(Object.getOwnPropertySymbols(n).filter(function(t) {
                return Object.getOwnPropertyDescriptor(n, t).enumerable
            }))),
            i.forEach(function(t) {
                vt(e, t, n[t])
            })
        }
        return e
    }
    function vt(t, e, n) {
        return e in t ? Object.defineProperty(t, e, {
            value: n,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : t[e] = n,
        t
    }
    function bt(t, e) {
        for (var n = 0; n < e.length; n++) {
            var i = e[n];
            i.enumerable = i.enumerable || !1,
            i.configurable = !0,
            "value"in i && (i.writable = !0),
            Object.defineProperty(t, i.key, i)
        }
    }
    window.getRandomStr = mt.getRandomStr = function(t) {
        for (var e = ""; e.length < t; )
            e += Math.random().toString(36).substr(2);
        return e = e.slice(0, t)
    }
    ,
    mt.getBrowserInfo = function() {
        var t = []
          , e = {
            userAgent: navigator.userAgent,
            language: navigator.language,
            hardware_concurrency: navigator.hardwareConcurrency,
            resolution: [window.screen.width, window.screen.height],
            navigator_platform: navigator.platform
        };
        for (var n in e)
            e.hasOwnProperty(n) && t.push({
                key: n,
                value: e[n]
            });
        return t
    }
    ,
    mt.createUUid = function() {
        var n = (new Date).getTime();
        return window.performance && "function" == typeof window.performance.now && (n += window.performance.now()),
        "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(t) {
            var e = (n + 16 * Math.random()) % 16 | 0;
            return n = Math.floor(n / 16),
            ("x" === t ? e : 3 & e | 8).toString(16)
        })
    }
    ,
    mt.cookie = {
        get: function() {
            for (var t = (0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : "") + "=", e = document.cookie.split(";"), n = 0; n < e.length; n++) {
                for (var i = e[n]; " " === i.charAt(0); )
                    i = i.substring(1, i.length);
                if (0 === i.indexOf(t))
                    return decodeURIComponent(i.substring(t.length, i.length))
            }
            return null
        },
        set: function(t, e, n, i, r) {
            var o = ""
              , a = ""
              , s = "";
            if (i) {
                var c = document.location.hostname.match(/[a-z0-9][a-z0-9\-]+\.[a-z\.]{2,6}$/i)
                  , l = c ? c[0] : "";
                o = l ? "; domain=." + l : ""
            }
            if (n) {
                var u = new Date;
                u.setTime(u.getTime() + 24 * n * 60 * 60 * 1e3),
                a = "; expires=" + u.toGMTString()
            }
            r && (s = "; secure");
            var h = "".concat(t, "=").concat(encodeURIComponent(e)).concat(a, "; path=/").concat(o).concat(s);
            return document.cookie = h
        },
        parse: function(t) {
            return JSON.parse(mt.cookie.get(t) || null)
        },
        remove: function(t, e) {
            mt.cookie.set(t, "", -1, e)
        }
    };
    var wt = n(19)
      , Tt = "";
    document.currentScript && document.currentScript.src && (Tt = document.currentScript.src);
    var At = function() {
        function x(t) {
            var e = t.config
              , n = void 0 === e ? {} : e
              , i = t.container
              , r = t.additions
              , o = t.nativeInfo
              , a = t.langPack
              , s = t.onError
              , c = t.onSuccess
              , l = t.onFail
              , u = t.onExit
              , h = t.beforeStart
              , d = t.afterStart
              , f = t.expired
              , p = t.jsonpField
              , g = t.hosts
              , m = t.appId
              , y = t.noButton
              , v = t.mode
              , b = t.winWidth
              , w = t.lang
              , T = t.mobile
              , A = t.username
              , E = t.version;
            !function(t, e) {
                if (!(t instanceof e))
                    throw new TypeError("Cannot call a class as a function")
            }(this, x),
            this.mode = n.mode || v || S,
            this.winWidth = n.winWidth || b,
            this.APP_ID = n.appId || m,
            this.version = E || "v1",
            this.EXPIRED = n.expired || f || 30,
            this.JSONP_FIELD = p || "ypjsonp",
            this.RSA_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDnOWe/gs033L/2/xR3oi6SLAMPBY5VledUqqH6dbCNOdrGX4xW+1x6NUfvmwpHRBA2C7xWDDvOIldTl0rMtERTDy9homrVqEcW6/TY+dSVFL3e2Yg2sVaehHv7FhmATkgfC2FcXt8Wvm99QpKRSrGKpcFYJwOj2F8hJh+rTG0IPQIDAQAB-----END PUBLIC KEY-----",
            this.HOSTS = n.hosts || g || "https://captcha.yunpian.com",
            this.NO_BUTTON = n.noButton || y,
            this.CONTAINER = i.dom || i,
            this.lang = n.lang || w || "zh-cn",
            this.langPack = n.langPack || a,
            this.additions = r || {},
            this.additions.username = this.additions.username || A || T,
            this.beforeStart = h || function(t) {
                return t()
            }
            ,
            this.afterStart = d || function() {}
            ,
            this.onSuccess = c || function() {}
            ,
            this.onError = s || function() {}
            ,
            this.onFail = l || function(t, e, n) {
                console.warn("验证失败:", e, "code:", t),
                n()
            }
            ,
            this.onExit = u || function() {}
            ,
            this.fingerprint = null,
            this.browserInfo = null,
            this.token = null,
            this.cbManager = st.Instance(this.EXPIRED),
            this.validator = null,
            this.masker = null,
            this.hasModeBuildDone = !1,
            this.scrollTop = null,
            this.waterMark = !0,
            this.logoOptions = {},
            this.drawIndex = 0,
            this.nativeInfo = o || null,
            this.init()
        }
        var t, e, n;
        return t = x,
        (e = [{
            key: "rsaEncrypt",
            value: function(t) {
                var e = new ft.a;
                return e.setPublicKey('-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDnOWe/gs033L/2/xR3oi6SLAMPBY5VledUqqH6dbCNOdrGX4xW+1x6NUfvmwpHRBA2C7xWDDvOIldTl0rMtERTDy9homrVqEcW6/TY+dSVFL3e2Yg2sVaehHv7FhmATkgfC2FcXt8Wvm99QpKRSrGKpcFYJwOj2F8hJh+rTG0IPQIDAQAB-----END PUBLIC KEY-----'),
                e.encrypt(t)
            }
        }, {
            key: "encrypt",
            value: function(t) {
                t = JSON.stringify(t);
                var e = mt.getRandomStr(16)
                  , n = mt.getRandomStr(16);
                return {
                    i: lt.a.encrypt(t, ht.a.parse(e), {
                        iv: ht.a.parse(n)
                    }).toString(),
                    k: this.rsaEncrypt(e + n)
                }
            }
        }, {
            key: "jsonpRequest",
            value: function(t, e, n) {
                var i = 3 < arguments.length && void 0 !== arguments[3] ? arguments[3] : null
                  , r = this.cbManager.preAdd()
                  , o = location.origin;
                e.fp = this.fingerprint,
                e.address = o,
                e.yp_riddler_id = mt.cookie.get("yp_riddler_id") || "";
                var a = this.encrypt(e);
                t = "".concat(this.HOSTS, "/").concat(this.version).concat(t, "?cb=").concat(r, "&i=").concat(encodeURIComponent(a.i), "&k=").concat(encodeURIComponent(a.k)),
                this.token && (t += "&token=".concat(this.token)),
                this.APP_ID && (t += "&captchaId=".concat(this.APP_ID)),
                this.cbManager.add(r, t, n, i)
            }
        }, {
            key: "injectButton",
            value: function(t) {
                if (!this.NO_BUTTON) {
                    var e = document.createElement("div");
                    e.className = "yp-riddler-button_logo";
                    var n = document.createElement("div");
                    n.className = "yp-riddler-btn_a",
                    e.appendChild(n),
                    (n = document.createElement("div")).className = "yp-riddler-btn_b",
                    e.appendChild(n);
                    var i = document.createElement("span");
                    i.className = "yp-riddler-button_text",
                    i.innerHTML = l("YPcaptcha_01", this.lang),
                    t.appendChild(e),
                    t.appendChild(i)
                }
            }
        }, {
            key: "injectSuccessBtn",
            value: function(t) {
                if (!this.NO_BUTTON && t) {
                    this.isVerifySuccess = !0;
                    var e = this.CONTAINER.getElementsByClassName("yp-riddler-button")[0];
                    if (e) {
                        var n = this.CONTAINER.getElementsByClassName("yp-riddler-button_logo")[0]
                          , i = this.CONTAINER.getElementsByClassName("yp-riddler-button_text")[0];
                        e.removeChild(n),
                        e.removeChild(i);
                        var r = document.createElement("img");
                        r.className = "yp-riddler-button-sucButton_logo",
                        r.src = wt;
                        var o = document.createElement("p");
                        return o.className = "yp-riddler-button-sucButton_text",
                        o.innerText = l("YPcaptcha_05", this.lang),
                        e.setAttribute("style", "background: #EEFFF5; border: 1px solid #26C267"),
                        e.appendChild(r),
                        e.appendChild(o),
                        e
                    }
                }
                return null
            }
        }, {
            key: "externalSlide",
            value: function(t) {
                var e = document.createElement("div");
                e.className = "yp-riddler-slider-area",
                e.style.height = this.winWidth / 8 + "px",
                e.style.width = this.winWidth + "px",
                e.style.lineHeight = this.winWidth / 8 + "px",
                t.appendChild(e);
                var n = document.createElement("div");
                n.className = "yp-riddler-slider-btn",
                n.style.width = this.winWidth / 6 + "px";
                var i = document.createElement("span");
                i.className = "yp-riddler-slider-tip-default",
                i.innerHTML = l("YPcaptcha_03", this.lang),
                e.appendChild(i);
                var r = document.createElement("span");
                r.className = "yp-riddler-slider-btn-sign",
                r.innerHTML = ">&nbsp;>",
                n.appendChild(r),
                e.appendChild(n)
            }
        }, {
            key: "buildDialogMode",
            value: function(t) {
                var e = this;
                this.CONTAINER.addEventListener("click", function(t) {
                    if (!e.isVerifySuccess) {
                        t.stopPropagation();
                        e.beforeStart(function() {
                            e.getCaptcha(),
                            e.hasModeBuildDone = !0
                        }),
                        i().ios && window.scrollTo(e.scrollTop, 0)
                    }
                }),
                this.injectButton(t)
            }
        }, {
            key: "buildFloatMode",
            value: function(n) {
                var i = this;
                this.CONTAINER.addEventListener("mouseenter", function() {
                    var t = n.getElementsByClassName("yp-riddler-win-masker")[0]
                      , e = i.NO_BUTTON ? i.CONTAINER : n;
                    t.style.paddingBottom = e.clientHeight + 10 + "px";
                    i.beforeStart(function() {
                        i.validator || i.hasModeBuildDone ? i.showUI(null, !1) : (i.getCaptcha(),
                        i.hasModeBuildDone = !0)
                    });
                    i.CONTAINER.addEventListener("mouseleave", function t() {
                        i.hideUI(!1),
                        i.CONTAINER.removeEventListener("mouseleave", t)
                    })
                }),
                this.injectButton(n)
            }
        }, {
            key: "buildFlatMode",
            value: function(t) {
                var e = this;
                this.beforeStart(function() {
                    e.getCaptcha(),
                    e.hasModeBuildDone = !0
                })
            }
        }, {
            key: "buildExternalMode",
            value: function(t) {
                var e = this;
                this.beforeStart(function() {
                    e.getCaptcha(),
                    e.hasModeBuildDone = !0
                })
            }
        }, {
            key: "retWidth",
            value: function() {
                var t = new RegExp(/^\d+%$/);
                if (this.winWidth) {
                    if (t.test(this.winWidth)) {
                        var e = document.body.clientWidth
                          , n = this.winWidth.replace("%", "") / 100;
                        this.winWidth = n * e
                    }
                    this.winWidth = this.winWidth < 230 ? 230 : this.winWidth
                } else
                    this.winWidth = 500
            }
        }, {
            key: "loadLang",
            value: function() {
                window.YP_RIDDLER_RESOURCE_LANG = yt({}, window.YP_RIDDLER_RESOURCE_LANG);
                var t = yt({}, r);
                if (this.langPack && "{}" !== JSON.stringify(this.langPack))
                    return window.YP_RIDDLER_RESOURCE_LANG.other = yt({}, t, this.langPack),
                    void (this.lang = "other");
                this.lang ? window.YP_RIDDLER_RESOURCE_LANG[this.lang] = o[this.lang] : window.YP_RIDDLER_RESOURCE_LANG[this.lang] = o["zh-cn"]
            }
        }, {
            key: "createPublicCpts",
            value: function(r) {
                var o = this;
                gt.a.get({
                    NOT_AVAILABLE: "not available",
                    ERROR: "error",
                    EXCLUDED: "excluded"
                }, function(t) {
                    var e = t.map(function(t) {
                        return t.value
                    });
                    o.fingerprint = gt.a.x64hash128(e.join(""), 31),
                    o.browserInfo = mt.getBrowserInfo();
                    var n = o["build".concat(o.mode[0].toUpperCase() + o.mode.slice(1), "Mode")];
                    n && n.call(o, r);
                    var i = document.createElement("div");
                    i.className = "yp-riddler-win-masker " + o.mode,
                    o.mode === S && i.addEventListener("click", function(t) {
                        t.stopPropagation(),
                        "touchstart" !== window.EventObj.click && t.preventDefault(),
                        o.validator && (o.hideUI(),
                        o.onExit())
                    }),
                    r.appendChild(i),
                    o.masker = i
                })
            }
        }, {
            key: "showUI",
            value: function(t) {
                var e = !(1 < arguments.length && void 0 !== arguments[1]) || arguments[1];
                this.masker.style.display = "block",
                e && this.validator.render(t)
            }
        }, {
            key: "hideUI",
            value: function() {
                var t = this
                  , e = !(0 < arguments.length && void 0 !== arguments[0]) || arguments[0];
                setTimeout(function() {
                    t.masker.style.display = "none",
                    e && t.validator.destroy()
                }, 500)
            }
        }, {
            key: "getCaptcha",
            value: function() {
                var r = this;
                this.jsonpRequest("/jsonp/captcha/get", {
                    browserInfo: this.browserInfo.filter(function(t) {
                        if ("webql" !== t.key && "canvas" !== t.key)
                            return t
                    }),
                    nativeInfo: this.nativeInfo,
                    additions: this.additions,
                    options: {
                        sdk: Tt,
                        sdkBuildVersion: "1.5.0(2021111001)",
                        hosts: this.HOSTS
                    }
                }, function(t) {
                    var e;
                    if (t.code)
                        r.onError && r.onError(t);
                    else if (t.data.type !== d) {
                        r.mode === s && 1 === t.data.type && (t.data.type = -1);
                        var n = (e = {},
                        vt(e, u, C),
                        vt(e, h, F),
                        vt(e, c, $),
                        vt(e, f, C),
                        e)[t.data.type];
                        r.token = t.data.token,
                        r.logoOptions = yt({}, t.data.logoOptions),
                        r.waterMark = t.data.logoOptions.status;
                        var i = function() {
                            r.validator = new n(function(t) {
                                r.onSuccess(t, function() {
                                    return r.hideUI()
                                }, function() {
                                    var t = 0 < arguments.length && void 0 !== arguments[0] && arguments[0];
                                    return r.injectSuccessBtn(t)
                                }),
                                r.token = null
                            }
                            ,function() {
                                r.onError.apply(r, arguments),
                                r.token = null
                            }
                            ,function(t, e, n) {
                                n || (r.getCaptcha(),
                                r.token = null),
                                r.onFail(t, e, function() {})
                            }
                            ,r.CONTAINER,function() {
                                r.jsonpRequest.apply(r, arguments)
                            }
                            ,function() {
                                return r.getCaptcha()
                            }
                            ,r.winWidth,r.APP_ID,r.waterMark,r.lang,r.logoOptions,r.mode)
                        };
                        r.validator ? r.validator instanceof n || (r.hideUI(),
                        i()) : i(),
                        r.showUI(t.data),
                        0 === r.drawIndex && setTimeout(function() {
                            r.drawIndex++,
                            r.afterStart()
                        }, 0)
                    } else
                        r.onSuccess(t.data, function() {}, function() {
                            var t = 0 < arguments.length && void 0 !== arguments[0] && arguments[0];
                            return r.injectSuccessBtn(t)
                        })
                }, this.onError)
            }
        }, {
            key: "setCookie",
            value: function() {
                var t = mt.createUUid();
                mt.cookie.set("yp_riddler_id", t, 356)
            }
        }, {
            key: "init",
            value: function() {
                var e = this;
                this.loadLang(),
                this.retWidth(),
                mt.cookie.get("yp_riddler_id") || this.setCookie(),
                this.scrollTop = document.documentElement.scrollTop,
                this.CONTAINER.getElementsByClassName("yp-riddler")[0] && (this.CONTAINER.innerHTML = ""),
                setInterval(function() {
                    e.cbManager.checkExpired()
                }, 500);
                window[this.JSONP_FIELD] = function(t) {
                    window[e.JSONP_FIELD].ret = null,
                    e.cbManager.invoke(t.cb, t)
                }
                ;
                var t = document.createElement("div");
                t.className = "yp-riddler yp-".concat(this.mode, " ").concat(this.mode === a || this.NO_BUTTON || this.mode === s ? "" : "yp-riddler-button"),
                this.CONTAINER.appendChild(t),
                "static" === window.getComputedStyle(this.CONTAINER, null).position && (this.CONTAINER.style.position = "relative"),
                this.createPublicCpts(t)
            }
        }]) && bt(t.prototype, e),
        n && bt(t, n),
        x,
        window.rsa = e[0].value
    }();
    n(20);
    window.YpRiddler = At;
    var Et = {
        down: "mousedown",
        up: "mouseup",
        move: "mousemove",
        click: "click"
    }
      , xt = i();
    "ontouchend"in document && (Et = {
        down: "touchstart",
        up: "touchend",
        move: "touchmove",
        click: "touchstart"
    }),
    xt.mobile && "ontouchstart"in document.documentElement == !0 && (Et = {
        down: "touchstart",
        up: "touchend",
        move: "touchmove",
        click: "touchstart"
    }),
    xt.mac && "ontouchstart"in document.documentElement == !0 && (Et = {
        down: "touchstart",
        up: "touchend",
        move: "touchmove",
        click: "touchstart"
    }),
    xt.iPad && "ontouchstart"in document.documentElement == !1 && (Et = {
        down: "mousedown",
        up: "mouseup",
        move: "mousemove",
        click: "click"
    }),
    xt.weixin && xt.mobile && (Et = {
        down: "touchstart",
        up: "touchend",
        move: "touchmove",
        click: "touchstart"
    }),
    xt.fireFox && -1 < navigator.userAgent.indexOf("Mobile") && (Et = {
        down: "touchstart",
        up: "touchend",
        move: "touchmove",
        click: "touchstart"
    }),
    window.EventObj = Et
}
]);

function get_image(){
    var e = window.getRandomStr(16);
    var n = window.getRandomStr(16);

    fp_=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    false,
    "zh-CN",
    24,
    8,
    8,
    [
    1920,
    1080
    ],
    [
    1920,
    1080
    ],
    -480,
    "Asia/Shanghai",
    true,
    true,
    true,
    false,
    false,
    "not available",
    "Win32",
    [
    [
        "PDF Viewer",
        "Portable Document Format",
        [
            [
                "application/pdf",
                "pdf"
            ],
            [
                "text/pdf",
                "pdf"
            ]
        ]
    ],
    [
        "Chrome PDF Viewer",
        "Portable Document Format",
        [
            [
                "application/pdf",
                "pdf"
            ],
            [
                "text/pdf",
                "pdf"
            ]
        ]
    ],
    [
        "Chromium PDF Viewer",
        "Portable Document Format",
        [
            [
                "application/pdf",
                "pdf"
            ],
            [
                "text/pdf",
                "pdf"
            ]
        ]
    ],
    [
        "Microsoft Edge PDF Viewer",
        "Portable Document Format",
        [
            [
                "application/pdf",
                "pdf"
            ],
            [
                "text/pdf",
                "pdf"
            ]
        ]
    ],
    [
        "WebKit built-in PDF",
        "Portable Document Format",
        [
            [
                "application/pdf",
                "pdf"
            ],
            [
                "text/pdf",
                "pdf"
            ]
        ]
    ]
    ],
    [
    "canvas winding:yes",
    "canvas fp:data:image/png;base64,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+MvJw+9uXgjcmi37IyTJ+cPvBlyxAgoooIACCiiggAIKKKCAAgoooIACCiiggAIKKKCAAgpszgIRoB8O/HH4IcwBPgZcny39BuA1w+8mOq44nkI8jRiXHwEf/QasmjG87uopYEteQ5LEI3EooIACCiiggAIKKKCAAgoooIACCiiggAIKKKCAAgoooIACw0YgAvTJwOJhs+JsoZcVu843tC97CTBleN3EhquNpxBPIx831sMJ34G5Hxg+d3Yt8AamkCTxSBwKKKCAAgoooIACCiiggAIKKKCAAgoooIACCiiggAIKKKDAsBFIYqUp6Qpg/PBY9UmtKfOlnS51F2DB8LiJDVe5MzC/k8U/BrzjRPjnJcPizrY8lZVPfyeZMCwW6yIVUEABBRRQQAEFFFBAAQUUUEABBRRQQAEFFFBAAQUUUECBEoE8QF809Au4FwLHAH/v8gG+E/jJcH287wB+3M3i3/oy+MUPgKlD+g5fPZPFf7o12X5IL9LFKaCAAgoooIACCiiggAIKKKCAAgoooIACCiiggAIKKKCAAp0I5AH6MmCroSt0K/B24JFul3gRcMrQvYnuV3YhcHIPi//YTvDNn7bu+z5zyN7luVvw1OnPJJOG7AJdmAIKKKCAAgoooIACCiiggAIKKKCAAgoooIACCiiggAIKKNCFQOyBPgZYNXSFbgDeDKzucYlzgD17PGqIHnB/a/n8jArWds0YeNsvgcMrOHjwDynextiEpOcHNvjL84oKKKCAAgoooIACCiiggAIKKKCAAgoooIACCiiggAIKKKBAlwIRoB8E/GtoGv0eeH22S3ulY2/gvkoPHirHbd1afb60F4t5LIEdfwsc1YuTBv7QvYB72y7zwoTktoG/oldQQAEFFFBAAQUUUEABBRRQQAEFFFBAAQUUUEABBRRQQAEFqicQAfpxwHerN2W1ZorK89f2KjyPK38a+Fq1ljBY84wFYov3ib244NMJbPWHIVWJ/ingq2238L6E5Kpe3I2HKqCAAgoooIACCiiggAIKKKCAAgoooIACCiiggAIKKKCAAhtdIAL0r7f2R//ERl9JhwXEnuevrKhte/m648yDh9bNVLaanxS3ea/s6Lajbh0DB/9lyOyJfsv6lZyTkHyyN7fisQoooIACCiiggAIKKKCAAgoooIACCiiggAIKKKCAAgoooMDGFogAPfqk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AAECBAgQIECAAAECBAgQIECAQEkBBXpJXbMJECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAoBoBBXo1qxKUAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBEoKKNBL6ppNgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAtUIKNCrWZWgBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFBSQIFeUtdsAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEKhGQIFezaoEJUCAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAIGSAgr0krpmEyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEA1Agr0alYlKAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiUFFCgl9Q1mwABAgQIECBAgAABAgQI43LJWQAABcNJREFUECBAgAABAgQIECBAgAABAgSqEVCgV7MqQQkQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECgpIACvaSu2QQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQjYACvZpVCUqAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECJQUU6CV1zSZAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBagQU6NWsSlACBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQKCmgQC+pazYBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIVCOgQK9mVYISIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQEkBBXpJXbMJECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAoBoBBXo1qxKUAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBEoKKNBL6ppNgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAtUIKNCrWZWgBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFBSQIFeUtdsAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEKhGQIFezaoEJUCAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAIGSAgr0krpmEyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEA1Agr0alYlKAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiUFFCgl9Q1mwABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgSqEVCgV7MqQQkQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECgpIACvaSu2QQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQjYACvZpVCUqAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECJQUU6CV1zSZAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBagQU6NWsSlACBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQKCmgQC+pazYBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIVCOgQK9mVYISIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQEkBBXpJXbMJECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAoBoBBXo1qxKUAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBEoKKNBL6ppNgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAtUIKNCrWZWgBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIFBSQIFeUtdsAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEKhGQIFezaoEJUCAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAIGSAgr0krpmEyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEA1Agr0alYlKAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiUFFCgl9Q1mwABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgSqEVCgV7MqQQkQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECgpIACvaSu2QQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBQjYACvZpVCUqAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECJQUU6CV1zSZAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBagQU6NWsSlACBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQKCnwX/Ky2W08OxQgAAAAAElFTkSuQmCC"
    ],
    [
    "data:image/png;base64,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",
    "extensions:ANGLE_instanced_arrays;EXT_blend_minmax;EXT_clip_control;EXT_color_buffer_half_float;EXT_depth_clamp;EXT_disjoint_timer_query;EXT_float_blend;EXT_frag_depth;EXT_polygon_offset_clamp;EXT_shader_texture_lod;EXT_texture_compression_bptc;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;EXT_texture_mirror_clamp_to_edge;EXT_sRGB;KHR_parallel_shader_compile;OES_element_index_uint;OES_fbo_render_mipmap;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_blend_func_extended;WEBGL_color_buffer_float;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_debug_shaders;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context;WEBGL_multi_draw;WEBGL_polygon_mode",
    "webgl aliased line width range:[1, 1]",
    "webgl aliased point size range:[1, 1024]",
    "webgl alpha bits:8",
    "webgl antialiasing:yes",
    "webgl blue bits:8",
    "webgl depth bits:24",
    "webgl green bits:8",
    "webgl max anisotropy:16",
    "webgl max combined texture image units:32",
    "webgl max cube map texture size:16384",
    "webgl max fragment uniform vectors:1024",
    "webgl max render buffer size:16384",
    "webgl max texture image units:16",
    "webgl max texture size:16384",
    "webgl max varying vectors:30",
    "webgl max vertex attribs:16",
    "webgl max vertex texture image units:16",
    "webgl max vertex uniform vectors:4096",
    "webgl max viewport dims:[32767, 32767]",
    "webgl red bits:8",
    "webgl renderer:WebKit WebGL",
    "webgl shading language version:WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
    "webgl stencil bits:0",
    "webgl vendor:WebKit",
    "webgl version:WebGL 1.0 (OpenGL ES 2.0 Chromium)",
    "webgl unmasked vendor:Google Inc. (Intel)",
    "webgl unmasked renderer:ANGLE (Intel, Intel(R) UHD Graphics (0x00009BA4) Direct3D11 vs_5_0 ps_5_0, D3D11)",
    "webgl vertex shader high float precision:23",
    "webgl vertex shader high float precision rangeMin:127",
    "webgl vertex shader high float precision rangeMax:127",
    "webgl vertex shader medium float precision:23",
    "webgl vertex shader medium float precision rangeMin:127",
    "webgl vertex shader medium float precision rangeMax:127",
    "webgl vertex shader low float precision:23",
    "webgl vertex shader low float precision rangeMin:127",
    "webgl vertex shader low float precision rangeMax:127",
    "webgl fragment shader high float precision:23",
    "webgl fragment shader high float precision rangeMin:127",
    "webgl fragment shader high float precision rangeMax:127",
    "webgl fragment shader medium float precision:23",
    "webgl fragment shader medium float precision rangeMin:127",
    "webgl fragment shader medium float precision rangeMax:127",
    "webgl fragment shader low float precision:23",
    "webgl fragment shader low float precision rangeMin:127",
    "webgl fragment shader low float precision rangeMax:127",
    "webgl vertex shader high int precision:0",
    "webgl vertex shader high int precision rangeMin:31",
    "webgl vertex shader high int precision rangeMax:30",
    "webgl vertex shader medium int precision:0",
    "webgl vertex shader medium int precision rangeMin:31",
    "webgl vertex shader medium int precision rangeMax:30",
    "webgl vertex shader low int precision:0",
    "webgl vertex shader low int precision rangeMin:31",
    "webgl vertex shader low int precision rangeMax:30",
    "webgl fragment shader high int precision:0",
    "webgl fragment shader high int precision rangeMin:31",
    "webgl fragment shader high int precision rangeMax:30",
    "webgl fragment shader medium int precision:0",
    "webgl fragment shader medium int precision rangeMin:31",
    "webgl fragment shader medium int precision rangeMax:30",
    "webgl fragment shader low int precision:0",
    "webgl fragment shader low int precision rangeMin:31",
    "webgl fragment shader low int precision rangeMax:30"
    ],
    "Google Inc. (Intel)~ANGLE (Intel, Intel(R) UHD Graphics (0x00009BA4) Direct3D11 vs_5_0 ps_5_0, D3D11)",
    false,
    false,
    false,
    false,
    [
    0,
    false,
    false
    ],
    [
    "Arial",
    "Arial Black",
    "Arial Narrow",
    "Book Antiqua",
    "Bookman Old Style",
    "Calibri",
    "Cambria",
    "Cambria Math",
    "Century",
    "Century Gothic",
    "Century Schoolbook",
    "Comic Sans MS",
    "Consolas",
    "Courier",
    "Courier New",
    "Georgia",
    "Helvetica",
    "Impact",
    "Lucida Bright",
    "Lucida Calligraphy",
    "Lucida Console",
    "Lucida Fax",
    "Lucida Handwriting",
    "Lucida Sans",
    "Lucida Sans Typewriter",
    "Lucida Sans Unicode",
    "Microsoft Sans Serif",
    "Monotype Corsiva",
    "MS Gothic",
    "MS PGothic",
    "MS Reference Sans Serif",
    "MS Sans Serif",
    "MS Serif",
    "Palatino Linotype",
    "Segoe Print",
    "Segoe Script",
    "Segoe UI",
    "Segoe UI Light",
    "Segoe UI Semibold",
    "Segoe UI Symbol",
    "Tahoma",
    "Times",
    "Times New Roman",
    "Trebuchet MS",
    "Verdana",
    "Wingdings",
    "Wingdings 2",
    "Wingdings 3"
    ],
    "124.04347527516074"
    ]
    finger=window.x64hash128(fp_.join(""), 31)
    var cb = window.pre.preAdd()
    var ival = window.entry.encrypt('{"browserInfo":[{"key":"userAgent","value":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"},{"key":"language","value":"zh-CN"},{"key":"hardware_concurrency","value":8},{"key":"resolution","value":[720,1280]},{"key":"navigator_platform","value":"Win32"}],"nativeInfo":null,"additions":{},"options":{"sdk":"https://www.yunpian.com/static/official/js/libs/riddler-sdk-0.2.2.js","sdkBuildVersion":"1.5.0(2021111001)","hosts":"https://captcha.yunpian.com"},"fp":"6acf5ac395ebcee4f0e555de99d9f4fe","address":"https://www.yunpian.com","yp_riddler_id":"e3457c98-caa3-48db-92bb-68faca693518"}',window.parse(e), {
    iv: window.parse(n)
    }).toString()
    var kval = window.rsa(e + n)
    return [cb,ival,kval]

}
// var arr=get_image()
// console.log(arr)
function vertify(x){
    trace=[
    [
        1112,
        1971,
        56
    ],
    [
        1115,
        1972,
        58
    ],
    [
        1116,
        1972,
        62
    ],
    [
        1117,
        1972,
        63
    ],
    [
        1118,
        1972,
        65
    ],
    [
        1119,
        1972,
        66
    ],
    [
        1120,
        1972,
        68
    ],
    [
        1121,
        1972,
        69
    ],
    [
        1122,
        1972,
        70
    ],
    [
        1123,
        1972,
        71
    ],
    [
        1124,
        1972,
        72
    ],
    [
        1125,
        1972,
        73
    ],
    [
        1127,
        1972,
        75
    ],
    [
        1128,
        1972,
        76
    ],
    [
        1129,
        1972,
        78
    ],
    [
        1131,
        1972,
        79
    ],
    [
        1134,
        1972,
        81
    ],
    [
        1135,
        1972,
        84
    ],
    [
        1137,
        1972,
        85
    ],
    [
        1139,
        1972,
        87
    ],
    [
        1140,
        1972,
        90
    ],
    [
        1143,
        1972,
        91
    ],
    [
        1145,
        1972,
        93
    ],
    [
        1146,
        1972,
        95
    ],
    [
        1147,
        1972,
        97
    ],
    [
        1150,
        1972,
        98
    ],
    [
        1151,
        1972,
        99
    ],
    [
        1153,
        1972,
        102
    ],
    [
        1156,
        1972,
        104
    ],
    [
        1157,
        1972,
        105
    ],
    [
        1158,
        1972,
        106
    ],
    [
        1160,
        1972,
        107
    ],
    [
        1161,
        1972,
        108
    ],
    [
        1162,
        1972,
        109
    ],
    [
        1166,
        1973,
        112
    ],
    [
        1167,
        1973,
        113
    ],
    [
        1168,
        1973,
        115
    ],
    [
        1171,
        1973,
        116
    ],
    [
        1174,
        1973,
        118
    ],
    [
        1175,
        1973,
        120
    ],
    [
        1178,
        1973,
        122
    ],
    [
        1180,
        1973,
        123
    ],
    [
        1184,
        1973,
        125
    ],
    [
        1187,
        1973,
        129
    ],
    [
        1188,
        1973,
        130
    ],
    [
        1189,
        1973,
        131
    ],
    [
        1190,
        1973,
        132
    ],
    [
        1191,
        1973,
        134
    ],
    [
        1193,
        1973,
        135
    ],
    [
        1194,
        1973,
        137
    ],
    [
        1195,
        1973,
        138
    ],
    [
        1198,
        1973,
        141
    ],
    [
        1199,
        1973,
        144
    ],
    [
        1200,
        1973,
        147
    ]
]
    var distanceX=245*(x/262)/304
    var ik={
    "points": trace,
    "distanceX":distanceX,
    "fp": "dcb2d6ab8c60db1c8b6a99ecad52aa03",
    "address": "https://www.yunpian.com",
    "yp_riddler_id": "e3457c98-caa3-48db-92bb-68faca693518"
}
    var e = window.getRandomStr(16);
    var n = window.getRandomStr(16);
    var cb = window.pre.preAdd()
    var ival = window.entry.encrypt(JSON.stringify(ik),window.parse(e), {
    iv: window.parse(n)
    }).toString()
    var kval = window.rsa(e + n)
    return [cb,ival,kval]
}
arr=vertify(166)
console.log(arr)
