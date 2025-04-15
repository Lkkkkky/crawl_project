window = global;
delete global;
var iii = 0;
function myProxy(obj,name){
    return new Proxy(obj,{
        get(target, propKey, receiver){ //拦截对象属性的读取，比如proxy.foo和proxy['foo']。
            let temp = Reflect.get(target,propKey,receiver);
            iii++;
            console.log(`[${iii}]${name} -> get ${propKey.toString()} return -> ${temp}`);
            if(typeof temp == 'object') {
                temp = myProxy(temp,name + " => " + propKey)
            }
            return temp;
        },
        set(target, propKey, value, receiver){ //拦截对象属性的设置，比如proxy.foo = v或proxy['foo'] = v，返回一个布尔值。
            const temp = Reflect.set(target,propKey,value,receiver);
            iii++;
            console.log(`[${iii}]${name} -> set ${propKey} value -> ${value}`);
            return temp;
        },
        has(target, propKey){ //拦截propKey in proxy的操作，返回一个布尔值。
            const temp = Reflect.has(target,propKey);
            iii++;
            console.log(`[${iii}]${name} -> has ${propKey.toString()}`);
            return temp;
        },
        deleteProperty(target, propKey){ //拦截delete proxy[propKey]的操作，返回一个布尔值。
            const temp = Reflect.deleteProperty(target,propKey);
            iii++;
            console.log(`[${iii}]${name} -> deleteProperty ${propKey}`);
            return temp;
        },
        ownKeys(target){ //拦截Object.getOwnPropertyNames(proxy)、Object.getOwnPropertySymbols(proxy)、Object.keys(proxy)、for...in循环，返回一个数组。该方法返回目标对象所有自身的属性的属性名，而Object.keys()的返回结果仅包括目标对象自身的可遍历属性。
            const temp = Reflect.ownKeys(target);
            iii++;
            console.log(`[${iii}]${name} -> ownKeys ${temp}`);
            return temp;
        },
        getOwnPropertyDescriptor(target, propKey){ //拦截Object.getOwnPropertyDescriptor(proxy, propKey)，返回属性的描述对象。
            const temp = Reflect.getOwnPropertyDescriptor(target,propKey);
            return temp;
        },
        defineProperty(target, propKey, propDesc){ //拦截Object.defineProperty(proxy, propKey, propDesc）、Object.defineProperties(proxy, propDescs)，返回一个布尔值。
            const temp = Reflect.defineProperty(target,propKey,propDesc);
            return temp;
        },
        preventExtensions(target){ //拦截Object.preventExtensions(proxy)，返回一个布尔值。
            const temp = Reflect.preventExtensions(target);
            return temp;
        },
        getPrototypeOf(target){ //拦截Object.getPrototypeOf(proxy)，返回一个对象。
            const temp = Reflect.getPrototypeOf(target);
            return temp;
        },
        isExtensible(target){ //拦截Object.isExtensible(proxy)，返回一个布尔值。
            const temp = Reflect.isExtensible(target);
            return temp;
        },
        setPrototypeOf(target, proto){ //拦截Object.setPrototypeOf(proxy, proto)，返回一个布尔值。如果目标对象是函数，那么还有两种额外操作可以拦截。
            const temp = Reflect.setPrototypeOf(target,proto);
            return temp;
        },
        apply(target, object, args){ //拦截 Proxy 实例作为函数调用的操作，比如proxy(...args)、proxy.call(object, ...args)、proxy.apply(...)。
            const temp = Reflect.apply(target, object, args);
            return temp;
        },
        construct(target, args){ //拦截 Proxy 实例作为构造函数调用的操作，比如new proxy(...args)。
            const temp = Reflect.construct(target, args);
            return temp;
        }
    })
};

/**
 * 如果代码中使用 this 关键字绕过代理器对window的代理  使代理器脱钩
 * 可以使用此方法 将this关键字指向的global对象强制指向window
 */
require("./env")
// window = myProxy(window,"window")
require("./bdms")
/* V 1.0.1.1 */

function get_ab(params, ua) {
    // params : 请求url的参数
    // ua:navigator.userAgent
    let ab = window.bdms.init._v[2].p[42].apply(null, [0, 1, 14, params, {}, ua]);
    return ab
}
function get_ab_(params, ua,pre) {
    //pre = '{"scene":"PCSquareSearch","size":30,"search_text":"'+pre+'","cursor":0,"extra":{"new_session_strategy":"1","search_id":"","session_id":""},"filters":{}}'
    pre = '{"operate_type":1,"content":"小黄车有优惠哦","comment_id":"7401072886221886464"}'
    // params : 请求url的参数
    // ua:navigator.userAgent
    console.log(params, pre, ua)
    let ab = window.bdms.init._v[2].p[42].apply(null, [0, 1, 0, params, pre, ua]);
    return ab
}
function fp() {
    var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split("")
        , t = e.length
        , n = (new Date).getTime().toString(36)
        , o = [];
    o[8] = o[13] = o[18] = o[23] = "_",
        o[14] = "4";
    for (var r = 0, i = void 0; r < 36; r++) {
        o[r] || (i = 0 | Math.random() * t,
            o[r] = e[19 == r ? 3 & i | 8 : i])
    }
    return "verify_" + n + "_" + o.join("")
}
fp_  = fp()

passs = 'page=1&page_size=20&product_type=0&filter=false&verifyFp=verify_m11zk0ef_NCLQZwsB_Ti7q_4t7P_8ccj_l0OppE4YnNEb&fp=verify_m11zk0ef_NCLQZwsB_Ti7q_4t7P_8ccj_l0OppE4YnNEb&msToken='
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"
pre = "3687484156155134071"
//ab = get_ab_(passs, ua,pre)
ab = get_ab_(passs, ua)
console.log(ab.length);
console.log(ab);

