
// window 部分
window = {};
window.top = window;
window.self = window;
XMLHttpRequest = function () {};
window.process = undefined;
window.requestAnimationFrame = function () {}
window.fetch = function () {
};
window.isSecureContext = true;
window.BluetoothUUID = function () {
};
window.ActiveXObject = undefined;
window.onwheelx = {
    "_Ax": "0X21"
};
window.innerWidth = 1136;
window.innerHeight = 924;
window.screenTop = 0;
window.screenLeft = 0;
window.outerWidth = 1152;
window.outerHeight = 1020;
window.availWidth = 1920;
window.availHeight = 1040;
window.screenX = 0
window.screenY = 0
window.pageYOffset = 0
window.pageYOffset = 0
window.chrome = {
    "app": {
        "isInstalled": false,
        "InstallState": {
            "DISABLED": "disabled",
            "INSTALLED": "installed",
            "NOT_INSTALLED": "not_installed"
        },
        "RunningState": {
            "CANNOT_RUN": "cannot_run",
            "READY_TO_RUN": "ready_to_run",
            "RUNNING": "running"
        }
    }
};
window.locationbar = {};
window.external = {};
window.devicePixelRatio = 1;
window.ontouchstart = undefined;
// body
body = {
    className: "",
    clientHeight: '920',
    clientLeft: 0,
    clientTop: 0,
    clientWidth: '1920',
    contentEditable: "inherit",
    appendChild: function (res) { // 将一个元素作为子元素添加到 <body> 元素的末尾
        debugger;
        return {};
    },
    removeChild: function (res) {
    },
}
// document 部分
document = {
    documentElement: {
        hidden: false,
        id: "",
        isConnected: true,
        isContentEditable: false,
        clientWidth: 931,
        clientHeight: 931,
    },
    createElement: function (val) {
        if (val === 'div') {
            return div
        }
        if (val === 'form') {
            return {}
        }
        if (val === 'a') {
            return {}
        }
        if (val === "span") {
            return {}
        }
        ;
        if (val === "canvas") {
            return '[object HTMLCanvasElement]'
        }

    },
    createEvent: function () {
    },
    addEventListener: function () {
    }
};
document.body = body;
document.fonts = {
    check: function (val) {
        return true;
    }
}
document.all = body;
document.onreadystatechange = null;
// navigator 部分
navigator = {
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    platform: 'Win32',
    vendorSubs: new Date().getTime()
};
Navigator = function () {
}
Object.assign(Navigator.prototype, {
    "vendorSub": "",
    "productSub": "20030107",
    "vendor": "Google Inc.",
    "maxTouchPoints": 0,
    "pdfViewerEnabled": true,
    "hardwareConcurrency": 8,
    "cookieEnabled": true,
    "appCodeName": "Mozilla",
    "appName": "Netscape",
    "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "platform": "MacIntel",
    "product": "Gecko",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "language": "zh-CN",
    "languages": [
        "zh-CN"
    ],
    "onLine": true,
    "webdriver": false,
    [Symbol.toStringTag]: '[object Navigator]',
    webkitPersistentStorage: function () {
    },
    mimeTypes: {
        length: 2,
        0: {type: 'application/pdf'},
        1: {type: 'text/pdf'},
    },
    connection: {},
    plugins: {
        0: {name: 'PDF Viewer'},
        1: {name: 'Chrome PDF Viewer'},
        2: {name: 'Chromium PDF Viewer'},
        3: {name: 'Microsoft Edge PDF Viewer'},
        4: {name: 'WebKit built-in PDF'},
        length: 5
    },
    vibrate: function () {
    },
    getBattery: function () {
        return '[object Promise]'
    },
    bluetooth: {},
    storage: {},
});
Object.setPrototypeOf(navigator, Navigator.prototype);
// location部分
location = {
    "ancestorOrigins": {},
    "href": "https://buyin.jinritemai.com/dashboard/merch-picking-library?pre_universal_page_params_id=&universal_page_params_id=7689ccb6-3649-44ca-831f-0f42467ae950",
    "origin": "https://buyin.jinritemai.com",
    "protocol": "https:",
    "host": "buyin.jinritemai.com",
    "hostname": "buyin.jinritemai.com",
    "port": "",
    "pathname": "/dashboard/merch-picking-library",
    "search": "?pre_universal_page_params_id=&universal_page_params_id=7689ccb6-3649-44ca-831f-0f42467ae950",
    "hash": ""
}
// localStorage
Storage = function Storage() {
    return Object.throwError("TypeError", "Illegal constructor")
}
Object.defineProperty(Storage.prototype, "length", {
    configurable: true, enumerable: true, get: function () {
        return Object.dispatch(this, Storage.prototype, "Storage", "length_get", arguments)
    }, set: undefined
});
Object.defineProperty(Storage.prototype, "clear", {
    configurable: true,
    enumerable: true,
    writable: true,
    value: function () {
        return Object.dispatch(this, Storage.prototype, "Storage", "clear", arguments)
    }
});
Object.defineProperty(Storage.prototype, "getItem", {
    configurable: true,
    enumerable: true,
    writable: true,
    value: function () {
        return Object.dispatch(this, Storage.prototype, "Storage", "getItem", arguments)
    }
});
Object.defineProperty(Storage.prototype, "key", {
    configurable: true,
    enumerable: true,
    writable: true,
    value: function () {
        return Object.dispatch(this, Storage.prototype, "Storage", "key", arguments)
    }
});
Object.defineProperty(Storage.prototype, "removeItem", {
    configurable: true,
    enumerable: true,
    writable: true,
    value: function () {
        return Object.dispatch(this, Storage.prototype, "Storage", "removeItem", arguments)
    }
});
Object.defineProperty(Storage.prototype, "setItem", {
    configurable: true,
    enumerable: true,
    writable: true,
    value: function () {
        return Object.dispatch(this, Storage.prototype, "Storage", "setItem", arguments)
    }
});
// localStorage对象
localStorage = {}
Object.setPrototypeOf(localStorage, Storage.prototype);
// sessionStorage对象
sessionStorage = {}
Object.setPrototypeOf(sessionStorage, Storage.prototype);
//screen 部分
screen = {
    availHeight: 1040,
    availLeft: 0,
    availTop: 0,
    availWidth: 2560,
    colorDepth: 24,
    height: 1080,
    isExtended: false,
    onchange: null,
    orientation: {angle: 0, type: 'landscape-primary', onchange: null},
    pixelDepth: 24,
    width: 2560
};
Screen = function Screen() {
};
screen.__proto__ = Screen.prototype;
window.screen = screen;
window.Screen = Screen;
// image 部分
Image = {
    width: '',
    height: '',
    naturalWidth: '',
    naturalHeigth: '',
    addEventListener: function (res) {
        debugger;
    },
    removeEventListener: function (res) {
        debugger;
    },
    hasAttribute: function (res) {
        debugger;
    },
    getAttribute: function (res) {
        debugger;
    },
    setAttribute: function (res) {
        debugger;
    },
    removeAttribute: function (res) {
        debugger;
    },
    toString: function (res) {
        debugger;
    },
};
window.Image = function () {
    return Image;
}
//  其他的功能 =============================================================
Function.prototype.toString = function () {
    return `function ${this.name}() { [native code] }`
};
// 插件功能相关
!function () {
    // 函数native化
    !function () {
        // 拿原始toString()函数暂存起来
        const $toString = Function.prototype.toString;
        const symbol = Symbol();
        const myToString = function toString() {
            return typeof this === 'function' && this[symbol] || $toString.call(this);
        }
        function set_native(func, obj, value) {
            Object.defineProperty(func, obj, {
                enumerable: false,
                configurable: true,
                writable: true,
                value: value
            });
        }
        delete Function.prototype.toString;
        set_native(Function.prototype, "toString", myToString)
        set_native(Function.prototype.toString, symbol, "myToString", 'function toString() { [native code] }');
        globalThis.setNative = function (func, funcName) {
            set_native(func, symbol, `function ${funcName || func.name || ''}() { [native code] }`)
        }
    }()
}();


const _setTimeout = function (a, b) {
        return setTimeout(a)
    },
    setTimeout = function () {

    };
setInterval = function () {};

setNative(document.documentElement, "document.documentElement")
setNative(document.createElement, "document.createElement")
setNative(document.createEvent, "document.createEvent")
setNative(document.fonts.check, "check")
setNative(setTimeout, "setTimeout")
setNative(setInterval, "setInterval")