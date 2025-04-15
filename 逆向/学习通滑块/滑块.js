const CryptoJS = require('crypto-js')
var timestamp = function get_timestamp() {
    return Math.round(new Date())
}()
function get_uuid() {
    for (var _0x55977e = [], _0x12474f = '0123456789abcdef', _0x33c6e8 = 0x0; _0x33c6e8 < 0x24; _0x33c6e8++)
        _0x55977e[_0x33c6e8] = _0x12474f['substr'](Math['floor'](0x10 * Math['random']()), 0x1);
    return _0x55977e[0xe] = '4',
        _0x55977e[0x13] = _0x12474f['substr'](0x3 & _0x55977e[0x13] | 0x8, 0x1),
        _0x55977e[0x8] = _0x55977e[0xd] = _0x55977e[0x12] = _0x55977e[0x17] = '-',
        _0x55977e['join']('');
}

function get_captchaKey() {
    capkey = CryptoJS.MD5(timestamp + get_uuid())
    return capkey.toString()
}
rrr=get_captchaKey()
console.log(rrr)

// _0x4e0309 时间戳
function get_token(capkey) {
    token = CryptoJS.MD5(timestamp + 'qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv' + 'slide' + capkey) + ':' + (parseInt(timestamp) + 300000)
    return token.toString()
}
function get_iv(){
    iv=CryptoJS.MD5('qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv' + 'slide' + Date['now']() + get_uuid())
    return iv.toString()
//    Date['now']()
}

