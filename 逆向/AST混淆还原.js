const parser = require("@babel/parser");
const traverse = require("@babel/traverse").default;
const types = require("@babel/types");
const generator = require("@babel/generator").default;
// jscode输入要还原的js
jscode = `
`;
const transform_literal = {
    StringLiteral({node})
    {
        if (node.extra && /\\[ux]/gi.test(node.extra.raw)) {
            node.extra = undefined;
        }
    },
}
let _ast = parser.parse(jscode);
traverse(_ast, transform_literal);
let code = generator(_ast).code;
console.log(code);
