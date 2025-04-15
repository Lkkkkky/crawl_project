function watch(obj,name){
    return new Proxy(obj,{
        get(target,p,receiver){
            if(p==="Math"||p==="isNaN"||p==="encodeURI"||p==="Uint8Array"||p.toString().indexOf("Symbol(Symbol.")!=-1){
                let val =Reflect.get(...arguments);
                return val
            }else{
                let val =Reflect.get(...arguments);
                console.log(`取值:`,name,`.`,p,`=>`,val);
                return val
            }
        },
        set(target,p,value,receiver){
            let val =Reflect.get(...arguments);
            console.log(`设置值:`,name,`.`,p,val,`=>`,value);
            return Reflect.set(...arguments)
        }
    })
}

window=global

delete __filename
delete __dirname
delete global
delete Buffer
window.Request=function (){}
window.top=window
window.self=window
// window.chrome={
//     "app": {
//         "isInstalled": false,
//         "InstallState": {
//             "DISABLED": "disabled",
//             "INSTALLED": "installed",
//             "NOT_INSTALLED": "not_installed"
//         },
//         "RunningState": {
//             "CANNOT_RUN": "cannot_run",
//             "READY_TO_RUN": "ready_to_run",
//             "RUNNING": "running"
//         }
//     }
// }
// window.sessionStorage=watch({
//     removeItem:function (){},
//     getItem:function (){},
//     setItem:function (){}},'window.sessionStorage')
// window.indexedDB=watch({},'window.indexedDB')
// window.name='$_YWTU=jJn9h0RU3Iflt5f5Si7dFM5UgfNfS9LItrzMHHzGEwg&$_YVTX=WG&vdFm='
window.addEventListener=function(){
    console.log(arguments)
}
// window.XMLHttpRequest=function(){
//     console.log(arguments)
// }
document={}
document.cookie=''
// document.body=null

document. createElement=function (x){
        console.log('document. createElement创建标签===>',x)
        if (x==='div') {
            return watch({
                getElementsByTagName: function (i) {
                    console.log('document. createElement(div).getElementsByTagName',i)
                     if (i == 'i') {
                        return watch({}, 'document.createElement(div).getElementsByTagName(i)')
                    }
                    return watch({}, 'document.createElement(div).getElementsByTagName')

                },
                innerHTML: ''

            }, 'document.createElement("div")')
        }

        else {
            return []
        }
    }
document.getElementsByTagName=function (x){
                console.log('document.getElementsByTagName获取标签===>',x)
    if(x==='script'){
        return [
            {
                getAttribute: function (x) {
                    console.log('script__0.getAttribute====>', x)
                    if (x === 'r') {
                        return 'm'
                    }

                },
                parentElement: {
                    removeChild: function (x) {
                        console.log('script__0.removeChild',x)

                    }
                }
            },
                {

                    getAttribute: function (x) {
                        console.log('script__1.getAttribute====>', x)
                        if (x === 'r') {
                            return 'm'
                        }
                    },
                    parentElement:{
                        removeChild: function (x) {
                            console.log('script__0.removeChild',x)

                        }
                    }
                }
        ]
    }
    if(x==='meta'){
        return {
            0:watch({ getAttribute:function (x){
                    console.log('meta__0.getAttribute===>',x)
                    if (x==='r'){
                        return 'm'
                    }
                    // 草拟吗的陷阱  居然不是陷阱
                }
            },'meta__0'),
            1:watch({
                getAttribute:function (x){
                    console.log('meta__1.getAttribute===>',x)
                    if (x==='r'){
                        return 'm'
                    }
                    // 草拟吗的陷阱  居然不是陷阱
                },
                parentNode: watch({
                    removeChild:function (){}
                },'meta__1.parentNode')
                , content:'9wk1AGzCfXaJAoLL3aujh8Ak5CeS4ThVdGDFY4vUNCbw0tvzdDZzQ6VMXdSmTXzB'
                    // '&&content&&'
                    //     '9wk1AGzCfXaJAoLL3aujh8Ak5CeS4ThVdGDFY4vUNCbw0tvzdDZzQ6VMXdSmTXzB'
            },'meta__1'),
            length:2
        }
    }
     if(x==='base'){
        return []
    }
                return watch({},'document.getElementsByTagName')

            }
// document.appendChild=function (x){console.log('document.appendChild',x)}
// document. removeChild=function (x){console.log('document.removeChild',x)}
document. getElementById=function (x){
    console.log('document.getElementById',x)
    if(x==='root-hammerhead-shadow-ui')
        return null
}
document. visibilityState='visible'
document. documentElement=watch({},'document. documentElement')
document. all=watch({},'document. all')
location={
"ancestorOrigins": {},
"href": "https://www.nmpa.gov.cn/",
"origin": "https://www.nmpa.gov.cn",
"protocol": "https:",
"host": "www.nmpa.gov.cn",
"hostname": "www.nmpa.gov.cn",
"port": "",
"pathname": "/",
"search": "",
"hash": ""
}
navigator={
    userAgent:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    // webkitPersistentStorage:function(x){
    //     console.log('webkitPersistentStorage=====>',x)
    //     return watch({},'navigator.webkitPersistentStorage')
    // },
    languages:["zh-CN"],
    // getBattery:function(x){
    //      console.log('getBattery=====>',x)
    //     return watch({},'navigator.getBattery')
    // },
    connection:{
        downlink: 10,
        effectiveType: "4g",
        onchange: null,
        rtt: 50,
        saveData: false
    },
    webdriver:false,
    platform:'Win32',
    mimeTypes:{
    "0": {},
    "1": {}
}
}
history={}
screen={}
// localStorage={
//     removeItem:function (){},
//     getItem:function (){},
//     setItem:function (){}
//
// }
setTimeout=function(){}
setInterval=function (){}
window=watch(window,'window')
document=watch(document,'document')
location=watch(location,'location')
navigator=watch(navigator,'navigator')
history=watch(history,'history')
screen=watch(screen,'screen')
// localStorage=watch(localStorage,'localStorage')
require('./ts_code')
// '$$ts$$'



require('./func_code')
function get_cookie(){
    return document.cookie
}
get_cookie()