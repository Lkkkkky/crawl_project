const babel =require('@babel/core')
var code ='var aaaaa=1'
const result = babel.transform(code,{ast:true})
console.log(result.ast)