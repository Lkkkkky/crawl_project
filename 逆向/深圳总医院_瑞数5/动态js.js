window=globalThis;
meta={
    length:2,
    1:watch({
        content:'&&content&&',
        parentNode: watch({
            removeChild:function (){}
        },'meta_1_parentNode')
    },'meta_1')
}
delete __filename;
delete __dirname;
setInterval=function(){}
scrtpt={
    getAttribute:function (){}
}
document={
    createElement(tag_name){
        console.log('创建标签--->',tag_name)
        return watch({
            getElementsByTagName:function()
            {
                return []
            }


        },`document.createElement(${tag_name})`)

    },
    getElementsByTagName:function (tag_name){
        console.log('获取元素名---->',tag_name);
        if (tag_name==='meta'){
            return watch(meta,'document.getElementsByTagName("mate")')
        }
        if (tag_name==='base'){
            return []
        }
        if (tag_name==='script'){
            return [watch(scrtpt,'document.getElementsByTagName("script")')]
        }
    },
    getElementById:function (id){
        console.log('获取元素名---->',id);
        // if (id==='meta'){
        //     return watch(meta,'document.getElementsByTagName("mate")')
        // }
    },
    documentElement:watch({
        style:{},
        attachEvent:function (){},
        addEventListener:function (){}},'documentElement'),
    attachEvent:function (){},
    addEventListener:function (){},
    cookie:''


}
attachEvent=function (){}
addEventListener=function (){}
indexedDB=function (){}


Storage=function (){}
localStorage={}
sessionStorage={}
Object.setPrototypeOf(localStorage,Storage.prototype)
Object.setPrototypeOf(sessionStorage,Storage.prototype)

navigator={
    userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    platform:'Win32',
    webdriver:false
}
location={
    "ancestorOrigins": {},
    "href": "https://sugh.szu.edu.cn/Html/News/Columns/540/Index.html",
    "origin": "https://sugh.szu.edu.cn",
    "protocol": "https:",
    "host": "sugh.szu.edu.cn",
    "hostname": "sugh.szu.edu.cn",
    "port": "",
    "pathname": "/Html/News/Columns/540/Index.html",
    "search": "",
    "hash": ""
}
window=watch(window,'window')
document=watch(document,'document')
location=watch(location,'location')
navigator=watch(navigator,'navigator')
localStorage=watch(localStorage,'localStorage')
sessionStorage=watch(sessionStorage,'sessionStorage')
Jing3={}
Storage.prototype.getItem=function (key){
    return Jing3[key]
}
Storage.prototype.setItem=function (key,value){
    Jing3[key]=value
}
Storage.prototype.removeItem=function (key){
    delete  Jing3[key]
}

top=window
self=window
'$$ts$$'
'$$jscode$$'
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
function get_cookie()
{
    return document.cookie
}