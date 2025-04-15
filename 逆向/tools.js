// from hashlib import sha256
// from lxml import etree

//--------------------webpack自吐-----------------------
window.c=c; //c是加载器
window.res="";
window.flag=false;
c=function (r){
    if(flag){
        window.res=window.res+`"${r.toString()}"`+":"+(e[r]+"")+",";
    }
    return window.c(r)
}


//--------------------WASM模拟调用------------------------
// import  pywasm
// runtime=pywasm.load(./Wasm.wasm)
// sign=runtime.exec('funcname',[arg1,arg2])


// --------------------时间格式输出为------------------------
// Tue Sep 19 2017 08:00:00 GMT+0800 (中国标准时间)
const moment = require('moment-timezone'); // 使用moment-timezone库处理时区
const dateString = new Date(trace[trace.length-1]['t'])
// 将ISO格式的日期转换为Date对象
const dateObj = moment(dateString, 'YYYY-MM-DDTHH:mm:ss.000Z').toDate();
// 设置为中国标准时间（Asia/Shanghai）
moment.tz.setDefault('Asia/Shanghai');
// 格式化日期为当地时间
const formattedDate = moment(dateObj).format('ddd MMM D YYYY H:mm:ss').concat(' GMT+0800 (中国标准时间)');


// --------------------保护函数------------------------
!function(){
    const $toString=Function.prototype.toString;
    const symbol=Symbol();
    const myToString=function (){
        return typeof this ==='function'  && this[symbol] || $toString.call(this)
    }
    function set_native(func,key,value){
        Object.defineProperty(func,key,{
            enumerable:false,
            configurable:true,
            writable:true,
            value:value
        });
    }
    delete Function.prototype.toString;
    set_native(Function.prototype,'toString',myToString);
    set_native(Function.prototype.toString,symbol,'function toString(){ [native code] }');
    globalThis.setNative =function (func,funcname){
        set_native(func,symbol,`function ${funcname || func.name || ''}() { [native code] }`)
    }
}();

//--------------------proxy代理------------------------
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

//----------------------hook--------------------------
(function() {
    var cookietemp="";
    Object.defineProperty(document, 'cookie', {
        set: function(val) {
            // alert('Hook 到 Set 方法')


            cookietemp = val;
            debugger;
            console.log('Set 方法 Hook 捕获到数据 -> ', val);
            return val;
        },
        get:function()
        {
            return cookietemp;
        }
    })
})();
//----------------------绑定原型链--------------------------
Storage=function (){}
localStorage={}
sessionStorage={}
Object.setPrototypeOf(localStorage,Storage.prototype)
Object.setPrototypeOf(sessionStorage,Storage.prototype)
//----------------------绑定原型链--------------------------
Navigator.prototype.plugins=[]
navigator={}
navigator.__proto__=Navigator.prototype
for (var prototype_ in Navigator.prototype){
    navigator[prototype_]=Navigator.prototype[prototype_];
    Navigator.prototype.__defineGetter__(prototype_,function(){
        throw new TypeError('Illegal constructor');
    });
}

//----------------------MySQL数据库交互--------------------------
import pymysql
from pyreadline3.release import authors
from wx.lib.masked import value
con=pymysql.connect( user='data', password="data",host='47.236.198.227',database='data',)
con.connect()
cursur=con.cursor()
cursur.execute('select * from song_list')
r=cursur.fetchall()
print(r)
sql=('insert into song_list (歌曲名,时长,作者,专辑) value (%s,%s,%s,%s)')
name='aaa'
time='4:30'
author='小青'
album='终于'
cursur.execute(sql,(name,time,author,album))
con.commit()


//----------------------Redis数据库交互--------------------------
import redis  //导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库
conn=redis.ConnectionPool(host='localhost',db=0, password='jing33333', port=6379, decode_responses=True)
conn=redis.Redis(host='47.236.198.227', port=6379,db=0, password='jing33333', charset='utf-8')
r=conn.get('jing3')
r=conn.get('jing3')
print(r)

r = redis.Redis(host='47.236.198.227', port=6379,password='jing33333',decode_responses=True)  //host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set('jing3333', '7777')  // key是"jing3333" value是"7777" 将键值对存入redis缓存
print(r['name'])
print(r.get('jing3'))  //取出键name对应的值
