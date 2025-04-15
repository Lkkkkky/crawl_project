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
window = global 

//环境补在这里

document={}
location={}
navigator={}
history={}
screen={}

proxyObjs = ['window', 'document', 'location', 'navigator', 'history', 'screen']
getEnvs(proxyObjs);