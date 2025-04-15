import execjs
rrr=execjs.compile(open('password加密.js','r',encoding='utf-8').read()).call('getkey','123331s',1726125984887)
# js里输出异常 wtdebug可以  py也可以   !!!!!window=global就可以了
print(rrr)