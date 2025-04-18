var JSEncryptExports = {};
window=global;
navigator={};
// ASN1=function c(a, b, c, d, e) {
//     this.stream = a,
//         this.header = b,
//         this.length = c,
//         this.tag = d,
//         this.sub = e
// }
!(function(exports) {
        function BigInteger(a, b, c) {
            null != a && ("number" == typeof a ? this.fromNumber(a, b, c) : null == b && "string" != typeof a ? this.fromString(a, 256) : this.fromString(a, b))
        }
        function nbi() {
            return new BigInteger(null)
        }
        function am1(a, b, c, d, e, f) {
            for (; --f >= 0; ) {
                var g = b * this[a++] + c[d] + e;
                e = Math.floor(g / 67108864),
                    c[d++] = 67108863 & g
            }
            return e
        }
        function am2(a, b, c, d, e, f) {
            for (var g = 32767 & b, h = b >> 15; --f >= 0; ) {
                var i = 32767 & this[a]
                    , j = this[a++] >> 15
                    , k = h * i + j * g;
                i = g * i + ((32767 & k) << 15) + c[d] + (1073741823 & e),
                    e = (i >>> 30) + (k >>> 15) + h * j + (e >>> 30),
                    c[d++] = 1073741823 & i
            }
            return e
        }
        function am3(a, b, c, d, e, f) {
            for (var g = 16383 & b, h = b >> 14; --f >= 0; ) {
                var i = 16383 & this[a]
                    , j = this[a++] >> 14
                    , k = h * i + j * g;
                i = g * i + ((16383 & k) << 14) + c[d] + e,
                    e = (i >> 28) + (k >> 14) + h * j,
                    c[d++] = 268435455 & i
            }
            return e
        }
        function int2char(a) {
            return BI_RM.charAt(a)
        }
        function intAt(a, b) {
            var c = BI_RC[a.charCodeAt(b)];
            return null == c ? -1 : c
        }
        function bnpCopyTo(a) {
            for (var b = this.t - 1; b >= 0; --b)
                a[b] = this[b];
            a.t = this.t,
                a.s = this.s
        }
        function bnpFromInt(a) {
            this.t = 1,
                this.s = 0 > a ? -1 : 0,
                a > 0 ? this[0] = a : -1 > a ? this[0] = a + DV : this.t = 0
        }
        function nbv(a) {
            var b = nbi();
            return b.fromInt(a),
                b
        }
        function bnpFromString(a, b) {
            var c;
            if (16 == b)
                c = 4;
            else if (8 == b)
                c = 3;
            else if (256 == b)
                c = 8;
            else if (2 == b)
                c = 1;
            else if (32 == b)
                c = 5;
            else {
                if (4 != b)
                    return void this.fromRadix(a, b);
                c = 2
            }
            this.t = 0,
                this.s = 0;
            for (var d = a.length, e = !1, f = 0; --d >= 0; ) {
                var g = 8 == c ? 255 & a[d] : intAt(a, d);
                0 > g ? "-" == a.charAt(d) && (e = !0) : (e = !1,
                    0 == f ? this[this.t++] = g : f + c > this.DB ? (this[this.t - 1] |= (g & (1 << this.DB - f) - 1) << f,
                        this[this.t++] = g >> this.DB - f) : this[this.t - 1] |= g << f,
                    f += c,
                f >= this.DB && (f -= this.DB))
            }
            8 == c && 0 != (128 & a[0]) && (this.s = -1,
            f > 0 && (this[this.t - 1] |= (1 << this.DB - f) - 1 << f)),
                this.clamp(),
            e && BigInteger.ZERO.subTo(this, this)
        }
        function bnpClamp() {
            for (var a = this.s & this.DM; this.t > 0 && this[this.t - 1] == a; )
                --this.t
        }
        function bnToString(a) {
            if (this.s < 0)
                return "-" + this.negate().toString(a);
            var b;
            if (16 == a)
                b = 4;
            else if (8 == a)
                b = 3;
            else if (2 == a)
                b = 1;
            else if (32 == a)
                b = 5;
            else {
                if (4 != a)
                    return this.toRadix(a);
                b = 2
            }
            var c, d = (1 << b) - 1, e = !1, f = "", g = this.t, h = this.DB - g * this.DB % b;
            if (g-- > 0)
                for (h < this.DB && (c = this[g] >> h) > 0 && (e = !0,
                    f = int2char(c)); g >= 0; )
                    b > h ? (c = (this[g] & (1 << h) - 1) << b - h,
                        c |= this[--g] >> (h += this.DB - b)) : (c = this[g] >> (h -= b) & d,
                    0 >= h && (h += this.DB,
                        --g)),
                    c > 0 && (e = !0),
                    e && (f += int2char(c));
            return e ? f : "0"
        }
        function bnNegate() {
            var a = nbi();
            return BigInteger.ZERO.subTo(this, a),
                a
        }
        function bnAbs() {
            return this.s < 0 ? this.negate() : this
        }
        function bnCompareTo(a) {
            var b = this.s - a.s;
            if (0 != b)
                return b;
            var c = this.t;
            if (b = c - a.t,
            0 != b)
                return this.s < 0 ? -b : b;
            for (; --c >= 0; )
                if (0 != (b = this[c] - a[c]))
                    return b;
            return 0
        }
        function nbits(a) {
            var b, c = 1;
            return 0 != (b = a >>> 16) && (a = b,
                c += 16),
            0 != (b = a >> 8) && (a = b,
                c += 8),
            0 != (b = a >> 4) && (a = b,
                c += 4),
            0 != (b = a >> 2) && (a = b,
                c += 2),
            0 != (b = a >> 1) && (a = b,
                c += 1),
                c
        }
        function bnBitLength() {
            return this.t <= 0 ? 0 : this.DB * (this.t - 1) + nbits(this[this.t - 1] ^ this.s & this.DM)
        }
        function bnpDLShiftTo(a, b) {
            var c;
            for (c = this.t - 1; c >= 0; --c)
                b[c + a] = this[c];
            for (c = a - 1; c >= 0; --c)
                b[c] = 0;
            b.t = this.t + a,
                b.s = this.s
        }
        function bnpDRShiftTo(a, b) {
            for (var c = a; c < this.t; ++c)
                b[c - a] = this[c];
            b.t = Math.max(this.t - a, 0),
                b.s = this.s
        }
        function bnpLShiftTo(a, b) {
            var c, d = a % this.DB, e = this.DB - d, f = (1 << e) - 1, g = Math.floor(a / this.DB), h = this.s << d & this.DM;
            for (c = this.t - 1; c >= 0; --c)
                b[c + g + 1] = this[c] >> e | h,
                    h = (this[c] & f) << d;
            for (c = g - 1; c >= 0; --c)
                b[c] = 0;
            b[g] = h,
                b.t = this.t + g + 1,
                b.s = this.s,
                b.clamp()
        }
        function bnpRShiftTo(a, b) {
            b.s = this.s;
            var c = Math.floor(a / this.DB);
            if (c >= this.t)
                return void (b.t = 0);
            var d = a % this.DB
                , e = this.DB - d
                , f = (1 << d) - 1;
            b[0] = this[c] >> d;
            for (var g = c + 1; g < this.t; ++g)
                b[g - c - 1] |= (this[g] & f) << e,
                    b[g - c] = this[g] >> d;
            d > 0 && (b[this.t - c - 1] |= (this.s & f) << e),
                b.t = this.t - c,
                b.clamp()
        }
        function bnpSubTo(a, b) {
            for (var c = 0, d = 0, e = Math.min(a.t, this.t); e > c; )
                d += this[c] - a[c],
                    b[c++] = d & this.DM,
                    d >>= this.DB;
            if (a.t < this.t) {
                for (d -= a.s; c < this.t; )
                    d += this[c],
                        b[c++] = d & this.DM,
                        d >>= this.DB;
                d += this.s
            } else {
                for (d += this.s; c < a.t; )
                    d -= a[c],
                        b[c++] = d & this.DM,
                        d >>= this.DB;
                d -= a.s
            }
            b.s = 0 > d ? -1 : 0,
                -1 > d ? b[c++] = this.DV + d : d > 0 && (b[c++] = d),
                b.t = c,
                b.clamp()
        }
        function bnpMultiplyTo(a, b) {
            var c = this.abs()
                , d = a.abs()
                , e = c.t;
            for (b.t = e + d.t; --e >= 0; )
                b[e] = 0;
            for (e = 0; e < d.t; ++e)
                b[e + c.t] = c.am(0, d[e], b, e, 0, c.t);
            b.s = 0,
                b.clamp(),
            this.s != a.s && BigInteger.ZERO.subTo(b, b)
        }
        function bnpSquareTo(a) {
            for (var b = this.abs(), c = a.t = 2 * b.t; --c >= 0; )
                a[c] = 0;
            for (c = 0; c < b.t - 1; ++c) {
                var d = b.am(c, b[c], a, 2 * c, 0, 1);
                (a[c + b.t] += b.am(c + 1, 2 * b[c], a, 2 * c + 1, d, b.t - c - 1)) >= b.DV && (a[c + b.t] -= b.DV,
                    a[c + b.t + 1] = 1)
            }
            a.t > 0 && (a[a.t - 1] += b.am(c, b[c], a, 2 * c, 0, 1)),
                a.s = 0,
                a.clamp()
        }
        function bnpDivRemTo(a, b, c) {
            var d = a.abs();
            if (!(d.t <= 0)) {
                var e = this.abs();
                if (e.t < d.t)
                    return null != b && b.fromInt(0),
                        void (null != c && this.copyTo(c));
                null == c && (c = nbi());
                var f = nbi()
                    , g = this.s
                    , h = a.s
                    , i = this.DB - nbits(d[d.t - 1]);
                i > 0 ? (d.lShiftTo(i, f),
                    e.lShiftTo(i, c)) : (d.copyTo(f),
                    e.copyTo(c));
                var j = f.t
                    , k = f[j - 1];
                if (0 != k) {
                    var l = k * (1 << this.F1) + (j > 1 ? f[j - 2] >> this.F2 : 0)
                        , m = this.FV / l
                        , n = (1 << this.F1) / l
                        , o = 1 << this.F2
                        , p = c.t
                        , q = p - j
                        , r = null == b ? nbi() : b;
                    for (f.dlShiftTo(q, r),
                         c.compareTo(r) >= 0 && (c[c.t++] = 1,
                             c.subTo(r, c)),
                             BigInteger.ONE.dlShiftTo(j, r),
                             r.subTo(f, f); f.t < j; )
                        f[f.t++] = 0;
                    for (; --q >= 0; ) {
                        var s = c[--p] == k ? this.DM : Math.floor(c[p] * m + (c[p - 1] + o) * n);
                        if ((c[p] += f.am(0, s, c, q, 0, j)) < s)
                            for (f.dlShiftTo(q, r),
                                     c.subTo(r, c); c[p] < --s; )
                                c.subTo(r, c)
                    }
                    null != b && (c.drShiftTo(j, b),
                    g != h && BigInteger.ZERO.subTo(b, b)),
                        c.t = j,
                        c.clamp(),
                    i > 0 && c.rShiftTo(i, c),
                    0 > g && BigInteger.ZERO.subTo(c, c)
                }
            }
        }
        function bnMod(a) {
            var b = nbi();
            return this.abs().divRemTo(a, null, b),
            this.s < 0 && b.compareTo(BigInteger.ZERO) > 0 && a.subTo(b, b),
                b
        }
        function Classic(a) {
            this.m = a
        }
        function cConvert(a) {
            return a.s < 0 || a.compareTo(this.m) >= 0 ? a.mod(this.m) : a
        }
        function cRevert(a) {
            return a
        }
        function cReduce(a) {
            a.divRemTo(this.m, null, a)
        }
        function cMulTo(a, b, c) {
            a.multiplyTo(b, c),
                this.reduce(c)
        }
        function cSqrTo(a, b) {
            a.squareTo(b),
                this.reduce(b)
        }
        function bnpInvDigit() {
            if (this.t < 1)
                return 0;
            var a = this[0];
            if (0 == (1 & a))
                return 0;
            var b = 3 & a;
            return b = b * (2 - (15 & a) * b) & 15,
                b = b * (2 - (255 & a) * b) & 255,
                b = b * (2 - ((65535 & a) * b & 65535)) & 65535,
                b = b * (2 - a * b % this.DV) % this.DV,
                b > 0 ? this.DV - b : -b
        }
        function Montgomery(a) {
            this.m = a,
                this.mp = a.invDigit(),
                this.mpl = 32767 & this.mp,
                this.mph = this.mp >> 15,
                this.um = (1 << a.DB - 15) - 1,
                this.mt2 = 2 * a.t
        }
        function montConvert(a) {
            var b = nbi();
            return a.abs().dlShiftTo(this.m.t, b),
                b.divRemTo(this.m, null, b),
            a.s < 0 && b.compareTo(BigInteger.ZERO) > 0 && this.m.subTo(b, b),
                b
        }
        function montRevert(a) {
            var b = nbi();
            return a.copyTo(b),
                this.reduce(b),
                b
        }
        function montReduce(a) {
            for (; a.t <= this.mt2; )
                a[a.t++] = 0;
            for (var b = 0; b < this.m.t; ++b) {
                var c = 32767 & a[b]
                    , d = c * this.mpl + ((c * this.mph + (a[b] >> 15) * this.mpl & this.um) << 15) & a.DM;
                for (c = b + this.m.t,
                         a[c] += this.m.am(0, d, a, b, 0, this.m.t); a[c] >= a.DV; )
                    a[c] -= a.DV,
                        a[++c]++
            }
            a.clamp(),
                a.drShiftTo(this.m.t, a),
            a.compareTo(this.m) >= 0 && a.subTo(this.m, a)
        }
        function montSqrTo(a, b) {
            a.squareTo(b),
                this.reduce(b)
        }
        function montMulTo(a, b, c) {
            a.multiplyTo(b, c),
                this.reduce(c)
        }
        function bnpIsEven() {
            return 0 == (this.t > 0 ? 1 & this[0] : this.s)
        }
        function bnpExp(a, b) {
            if (a > 4294967295 || 1 > a)
                return BigInteger.ONE;
            var c = nbi()
                , d = nbi()
                , e = b.convert(this)
                , f = nbits(a) - 1;
            for (e.copyTo(c); --f >= 0; )
                if (b.sqrTo(c, d),
                (a & 1 << f) > 0)
                    b.mulTo(d, e, c);
                else {
                    var g = c;
                    c = d,
                        d = g
                }
            return b.revert(c)
        }
        function bnModPowInt(a, b) {
            var c;
            return c = 256 > a || b.isEven() ? new Classic(b) : new Montgomery(b),
                this.exp(a, c)
        }
        function bnClone() {
            var a = nbi();
            return this.copyTo(a),
                a
        }
        function bnIntValue() {
            if (this.s < 0) {
                if (1 == this.t)
                    return this[0] - this.DV;
                if (0 == this.t)
                    return -1
            } else {
                if (1 == this.t)
                    return this[0];
                if (0 == this.t)
                    return 0
            }
            return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
        }
        function bnByteValue() {
            return 0 == this.t ? this.s : this[0] << 24 >> 24
        }
        function bnShortValue() {
            return 0 == this.t ? this.s : this[0] << 16 >> 16
        }
        function bnpChunkSize(a) {
            return Math.floor(Math.LN2 * this.DB / Math.log(a))
        }
        function bnSigNum() {
            return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
        }
        function bnpToRadix(a) {
            if (null == a && (a = 10),
            0 == this.signum() || 2 > a || a > 36)
                return "0";
            var b = this.chunkSize(a)
                , c = Math.pow(a, b)
                , d = nbv(c)
                , e = nbi()
                , f = nbi()
                , g = "";
            for (this.divRemTo(d, e, f); e.signum() > 0; )
                g = (c + f.intValue()).toString(a).substr(1) + g,
                    e.divRemTo(d, e, f);
            return f.intValue().toString(a) + g
        }
        function bnpFromRadix(a, b) {
            this.fromInt(0),
            null == b && (b = 10);
            for (var c = this.chunkSize(b), d = Math.pow(b, c), e = !1, f = 0, g = 0, h = 0; h < a.length; ++h) {
                var i = intAt(a, h);
                0 > i ? "-" == a.charAt(h) && 0 == this.signum() && (e = !0) : (g = b * g + i,
                ++f >= c && (this.dMultiply(d),
                    this.dAddOffset(g, 0),
                    f = 0,
                    g = 0))
            }
            f > 0 && (this.dMultiply(Math.pow(b, f)),
                this.dAddOffset(g, 0)),
            e && BigInteger.ZERO.subTo(this, this)
        }
        function bnpFromNumber(a, b, c) {
            if ("number" == typeof b)
                if (2 > a)
                    this.fromInt(1);
                else
                    for (this.fromNumber(a, c),
                         this.testBit(a - 1) || this.bitwiseTo(BigInteger.ONE.shiftLeft(a - 1), op_or, this),
                         this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(b); )
                        this.dAddOffset(2, 0),
                        this.bitLength() > a && this.subTo(BigInteger.ONE.shiftLeft(a - 1), this);
            else {
                var d = new Array
                    , e = 7 & a;
                d.length = (a >> 3) + 1,
                    b.nextBytes(d),
                    e > 0 ? d[0] &= (1 << e) - 1 : d[0] = 0,
                    this.fromString(d, 256)
            }
        }
        function bnToByteArray() {
            var a = this.t
                , b = new Array;
            b[0] = this.s;
            var c, d = this.DB - a * this.DB % 8, e = 0;
            if (a-- > 0)
                for (d < this.DB && (c = this[a] >> d) != (this.s & this.DM) >> d && (b[e++] = c | this.s << this.DB - d); a >= 0; )
                    8 > d ? (c = (this[a] & (1 << d) - 1) << 8 - d,
                        c |= this[--a] >> (d += this.DB - 8)) : (c = this[a] >> (d -= 8) & 255,
                    0 >= d && (d += this.DB,
                        --a)),
                    0 != (128 & c) && (c |= -256),
                    0 == e && (128 & this.s) != (128 & c) && ++e,
                    (e > 0 || c != this.s) && (b[e++] = c);
            return b
        }
        function bnEquals(a) {
            return 0 == this.compareTo(a)
        }
        function bnMin(a) {
            return this.compareTo(a) < 0 ? this : a
        }
        function bnMax(a) {
            return this.compareTo(a) > 0 ? this : a
        }
        function bnpBitwiseTo(a, b, c) {
            var d, e, f = Math.min(a.t, this.t);
            for (d = 0; f > d; ++d)
                c[d] = b(this[d], a[d]);
            if (a.t < this.t) {
                for (e = a.s & this.DM,
                         d = f; d < this.t; ++d)
                    c[d] = b(this[d], e);
                c.t = this.t
            } else {
                for (e = this.s & this.DM,
                         d = f; d < a.t; ++d)
                    c[d] = b(e, a[d]);
                c.t = a.t
            }
            c.s = b(this.s, a.s),
                c.clamp()
        }
        function op_and(a, b) {
            return a & b
        }
        function bnAnd(a) {
            var b = nbi();
            return this.bitwiseTo(a, op_and, b),
                b
        }
        function op_or(a, b) {
            return a | b
        }
        function bnOr(a) {
            var b = nbi();
            return this.bitwiseTo(a, op_or, b),
                b
        }
        function op_xor(a, b) {
            return a ^ b
        }
        function bnXor(a) {
            var b = nbi();
            return this.bitwiseTo(a, op_xor, b),
                b
        }
        function op_andnot(a, b) {
            return a & ~b
        }
        function bnAndNot(a) {
            var b = nbi();
            return this.bitwiseTo(a, op_andnot, b),
                b
        }
        function bnNot() {
            for (var a = nbi(), b = 0; b < this.t; ++b)
                a[b] = this.DM & ~this[b];
            return a.t = this.t,
                a.s = ~this.s,
                a
        }
        function bnShiftLeft(a) {
            var b = nbi();
            return 0 > a ? this.rShiftTo(-a, b) : this.lShiftTo(a, b),
                b
        }
        function bnShiftRight(a) {
            var b = nbi();
            return 0 > a ? this.lShiftTo(-a, b) : this.rShiftTo(a, b),
                b
        }
        function lbit(a) {
            if (0 == a)
                return -1;
            var b = 0;
            return 0 == (65535 & a) && (a >>= 16,
                b += 16),
            0 == (255 & a) && (a >>= 8,
                b += 8),
            0 == (15 & a) && (a >>= 4,
                b += 4),
            0 == (3 & a) && (a >>= 2,
                b += 2),
            0 == (1 & a) && ++b,
                b
        }
        function bnGetLowestSetBit() {
            for (var a = 0; a < this.t; ++a)
                if (0 != this[a])
                    return a * this.DB + lbit(this[a]);
            return this.s < 0 ? this.t * this.DB : -1
        }
        function cbit(a) {
            for (var b = 0; 0 != a; )
                a &= a - 1,
                    ++b;
            return b
        }
        function bnBitCount() {
            for (var a = 0, b = this.s & this.DM, c = 0; c < this.t; ++c)
                a += cbit(this[c] ^ b);
            return a
        }
        function bnTestBit(a) {
            var b = Math.floor(a / this.DB);
            return b >= this.t ? 0 != this.s : 0 != (this[b] & 1 << a % this.DB)
        }
        function bnpChangeBit(a, b) {
            var c = BigInteger.ONE.shiftLeft(a);
            return this.bitwiseTo(c, b, c),
                c
        }
        function bnSetBit(a) {
            return this.changeBit(a, op_or)
        }
        function bnClearBit(a) {
            return this.changeBit(a, op_andnot)
        }
        function bnFlipBit(a) {
            return this.changeBit(a, op_xor)
        }
        function bnpAddTo(a, b) {
            for (var c = 0, d = 0, e = Math.min(a.t, this.t); e > c; )
                d += this[c] + a[c],
                    b[c++] = d & this.DM,
                    d >>= this.DB;
            if (a.t < this.t) {
                for (d += a.s; c < this.t; )
                    d += this[c],
                        b[c++] = d & this.DM,
                        d >>= this.DB;
                d += this.s
            } else {
                for (d += this.s; c < a.t; )
                    d += a[c],
                        b[c++] = d & this.DM,
                        d >>= this.DB;
                d += a.s
            }
            b.s = 0 > d ? -1 : 0,
                d > 0 ? b[c++] = d : -1 > d && (b[c++] = this.DV + d),
                b.t = c,
                b.clamp()
        }
        function bnAdd(a) {
            var b = nbi();
            return this.addTo(a, b),
                b
        }
        function bnSubtract(a) {
            var b = nbi();
            return this.subTo(a, b),
                b
        }
        function bnMultiply(a) {
            var b = nbi();
            return this.multiplyTo(a, b),
                b
        }
        function bnSquare() {
            var a = nbi();
            return this.squareTo(a),
                a
        }
        function bnDivide(a) {
            var b = nbi();
            return this.divRemTo(a, b, null),
                b
        }
        function bnRemainder(a) {
            var b = nbi();
            return this.divRemTo(a, null, b),
                b
        }
        function bnDivideAndRemainder(a) {
            var b = nbi()
                , c = nbi();
            return this.divRemTo(a, b, c),
                new Array(b,c)
        }
        function bnpDMultiply(a) {
            this[this.t] = this.am(0, a - 1, this, 0, 0, this.t),
                ++this.t,
                this.clamp()
        }
        function bnpDAddOffset(a, b) {
            if (0 != a) {
                for (; this.t <= b; )
                    this[this.t++] = 0;
                for (this[b] += a; this[b] >= this.DV; )
                    this[b] -= this.DV,
                    ++b >= this.t && (this[this.t++] = 0),
                        ++this[b]
            }
        }
        function NullExp() {}
        function nNop(a) {
            return a
        }
        function nMulTo(a, b, c) {
            a.multiplyTo(b, c)
        }
        function nSqrTo(a, b) {
            a.squareTo(b)
        }
        function bnPow(a) {
            return this.exp(a, new NullExp)
        }
        function bnpMultiplyLowerTo(a, b, c) {
            var d = Math.min(this.t + a.t, b);
            for (c.s = 0,
                     c.t = d; d > 0; )
                c[--d] = 0;
            var e;
            for (e = c.t - this.t; e > d; ++d)
                c[d + this.t] = this.am(0, a[d], c, d, 0, this.t);
            for (e = Math.min(a.t, b); e > d; ++d)
                this.am(0, a[d], c, d, 0, b - d);
            c.clamp()
        }
        function bnpMultiplyUpperTo(a, b, c) {
            --b;
            var d = c.t = this.t + a.t - b;
            for (c.s = 0; --d >= 0; )
                c[d] = 0;
            for (d = Math.max(b - this.t, 0); d < a.t; ++d)
                c[this.t + d - b] = this.am(b - d, a[d], c, 0, 0, this.t + d - b);
            c.clamp(),
                c.drShiftTo(1, c)
        }
        function Barrett(a) {
            this.r2 = nbi(),
                this.q3 = nbi(),
                BigInteger.ONE.dlShiftTo(2 * a.t, this.r2),
                this.mu = this.r2.divide(a),
                this.m = a
        }
        function barrettConvert(a) {
            if (a.s < 0 || a.t > 2 * this.m.t)
                return a.mod(this.m);
            if (a.compareTo(this.m) < 0)
                return a;
            var b = nbi();
            return a.copyTo(b),
                this.reduce(b),
                b
        }
        function barrettRevert(a) {
            return a
        }
        function barrettReduce(a) {
            for (a.drShiftTo(this.m.t - 1, this.r2),
                 a.t > this.m.t + 1 && (a.t = this.m.t + 1,
                     a.clamp()),
                     this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
                     this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); a.compareTo(this.r2) < 0; )
                a.dAddOffset(1, this.m.t + 1);
            for (a.subTo(this.r2, a); a.compareTo(this.m) >= 0; )
                a.subTo(this.m, a)
        }
        function barrettSqrTo(a, b) {
            a.squareTo(b),
                this.reduce(b)
        }
        function barrettMulTo(a, b, c) {
            a.multiplyTo(b, c),
                this.reduce(c)
        }
        function bnModPow(a, b) {
            var c, d, e = a.bitLength(), f = nbv(1);
            if (0 >= e)
                return f;
            c = 18 > e ? 1 : 48 > e ? 3 : 144 > e ? 4 : 768 > e ? 5 : 6,
                d = 8 > e ? new Classic(b) : b.isEven() ? new Barrett(b) : new Montgomery(b);
            var g = new Array
                , h = 3
                , i = c - 1
                , j = (1 << c) - 1;
            if (g[1] = d.convert(this),
            c > 1) {
                var k = nbi();
                for (d.sqrTo(g[1], k); j >= h; )
                    g[h] = nbi(),
                        d.mulTo(k, g[h - 2], g[h]),
                        h += 2
            }
            var l, m, n = a.t - 1, o = !0, p = nbi();
            for (e = nbits(a[n]) - 1; n >= 0; ) {
                for (e >= i ? l = a[n] >> e - i & j : (l = (a[n] & (1 << e + 1) - 1) << i - e,
                n > 0 && (l |= a[n - 1] >> this.DB + e - i)),
                         h = c; 0 == (1 & l); )
                    l >>= 1,
                        --h;
                if ((e -= h) < 0 && (e += this.DB,
                    --n),
                    o)
                    g[l].copyTo(f),
                        o = !1;
                else {
                    for (; h > 1; )
                        d.sqrTo(f, p),
                            d.sqrTo(p, f),
                            h -= 2;
                    h > 0 ? d.sqrTo(f, p) : (m = f,
                        f = p,
                        p = m),
                        d.mulTo(p, g[l], f)
                }
                for (; n >= 0 && 0 == (a[n] & 1 << e); )
                    d.sqrTo(f, p),
                        m = f,
                        f = p,
                        p = m,
                    --e < 0 && (e = this.DB - 1,
                        --n)
            }
            return d.revert(f)
        }
        function bnGCD(a) {
            var b = this.s < 0 ? this.negate() : this.clone()
                , c = a.s < 0 ? a.negate() : a.clone();
            if (b.compareTo(c) < 0) {
                var d = b;
                b = c,
                    c = d
            }
            var e = b.getLowestSetBit()
                , f = c.getLowestSetBit();
            if (0 > f)
                return b;
            for (f > e && (f = e),
                 f > 0 && (b.rShiftTo(f, b),
                     c.rShiftTo(f, c)); b.signum() > 0; )
                (e = b.getLowestSetBit()) > 0 && b.rShiftTo(e, b),
                (e = c.getLowestSetBit()) > 0 && c.rShiftTo(e, c),
                    b.compareTo(c) >= 0 ? (b.subTo(c, b),
                        b.rShiftTo(1, b)) : (c.subTo(b, c),
                        c.rShiftTo(1, c));
            return f > 0 && c.lShiftTo(f, c),
                c
        }
        function bnpModInt(a) {
            if (0 >= a)
                return 0;
            var b = this.DV % a
                , c = this.s < 0 ? a - 1 : 0;
            if (this.t > 0)
                if (0 == b)
                    c = this[0] % a;
                else
                    for (var d = this.t - 1; d >= 0; --d)
                        c = (b * c + this[d]) % a;
            return c
        }
        function bnModInverse(a) {
            var b = a.isEven();
            if (this.isEven() && b || 0 == a.signum())
                return BigInteger.ZERO;
            for (var c = a.clone(), d = this.clone(), e = nbv(1), f = nbv(0), g = nbv(0), h = nbv(1); 0 != c.signum(); ) {
                for (; c.isEven(); )
                    c.rShiftTo(1, c),
                        b ? (e.isEven() && f.isEven() || (e.addTo(this, e),
                            f.subTo(a, f)),
                            e.rShiftTo(1, e)) : f.isEven() || f.subTo(a, f),
                        f.rShiftTo(1, f);
                for (; d.isEven(); )
                    d.rShiftTo(1, d),
                        b ? (g.isEven() && h.isEven() || (g.addTo(this, g),
                            h.subTo(a, h)),
                            g.rShiftTo(1, g)) : h.isEven() || h.subTo(a, h),
                        h.rShiftTo(1, h);
                c.compareTo(d) >= 0 ? (c.subTo(d, c),
                b && e.subTo(g, e),
                    f.subTo(h, f)) : (d.subTo(c, d),
                b && g.subTo(e, g),
                    h.subTo(f, h))
            }
            return 0 != d.compareTo(BigInteger.ONE) ? BigInteger.ZERO : h.compareTo(a) >= 0 ? h.subtract(a) : h.signum() < 0 ? (h.addTo(a, h),
                h.signum() < 0 ? h.add(a) : h) : h
        }
        function bnIsProbablePrime(a) {
            var b, c = this.abs();
            if (1 == c.t && c[0] <= lowprimes[lowprimes.length - 1]) {
                for (b = 0; b < lowprimes.length; ++b)
                    if (c[0] == lowprimes[b])
                        return !0;
                return !1
            }
            if (c.isEven())
                return !1;
            for (b = 1; b < lowprimes.length; ) {
                for (var d = lowprimes[b], e = b + 1; e < lowprimes.length && lplim > d; )
                    d *= lowprimes[e++];
                for (d = c.modInt(d); e > b; )
                    if (d % lowprimes[b++] == 0)
                        return !1
            }
            return c.millerRabin(a)
        }
        function bnpMillerRabin(a) {
            var b = this.subtract(BigInteger.ONE)
                , c = b.getLowestSetBit();
            if (0 >= c)
                return !1;
            var d = b.shiftRight(c);
            a = a + 1 >> 1,
            a > lowprimes.length && (a = lowprimes.length);
            for (var e = nbi(), f = 0; a > f; ++f) {
                e.fromInt(lowprimes[Math.floor(Math.random() * lowprimes.length)]);
                var g = e.modPow(d, this);
                if (0 != g.compareTo(BigInteger.ONE) && 0 != g.compareTo(b)) {
                    for (var h = 1; h++ < c && 0 != g.compareTo(b); )
                        if (g = g.modPowInt(2, this),
                        0 == g.compareTo(BigInteger.ONE))
                            return !1;
                    if (0 != g.compareTo(b))
                        return !1
                }
            }
            return !0
        }
        function Arcfour() {
            this.i = 0,
                this.j = 0,
                this.S = new Array
        }
        function ARC4init(a) {
            var b, c, d;
            for (b = 0; 256 > b; ++b)
                this.S[b] = b;
            for (c = 0,
                     b = 0; 256 > b; ++b)
                c = c + this.S[b] + a[b % a.length] & 255,
                    d = this.S[b],
                    this.S[b] = this.S[c],
                    this.S[c] = d;
            this.i = 0,
                this.j = 0
        }
        function ARC4next() {
            var a;
            return this.i = this.i + 1 & 255,
                this.j = this.j + this.S[this.i] & 255,
                a = this.S[this.i],
                this.S[this.i] = this.S[this.j],
                this.S[this.j] = a,
                this.S[a + this.S[this.i] & 255]
        }
        function prng_newstate() {
            return new Arcfour
        }
        function rng_get_byte() {
            if (null == rng_state) {
                for (rng_state = prng_newstate(); rng_psize > rng_pptr; ) {
                    var a = Math.floor(65536 * Math.random());
                    rng_pool[rng_pptr++] = 255 & a
                }
                for (rng_state.init(rng_pool),
                         rng_pptr = 0; rng_pptr < rng_pool.length; ++rng_pptr)
                    rng_pool[rng_pptr] = 0;
                rng_pptr = 0
            }
            return rng_state.next()
        }
        function rng_get_bytes(a) {
            var b;
            for (b = 0; b < a.length; ++b)
                a[b] = rng_get_byte()
        }
        function SecureRandom() {}
        function parseBigInt(a, b) {
            return new BigInteger(a,b)
        }
        function linebrk(a, b) {
            for (var c = "", d = 0; d + b < a.length; )
                c += a.substring(d, d + b) + "\n",
                    d += b;
            return c + a.substring(d, a.length)
        }
        function byte2Hex(a) {
            return 16 > a ? "0" + a.toString(16) : a.toString(16)
        }
        function pkcs1pad2(a, b) {
            if (b < a.length + 11)
                return console.error("Message too long for RSA"),
                    null;
            for (var c = new Array, d = a.length - 1; d >= 0 && b > 0; ) {
                var e = a.charCodeAt(d--);
                128 > e ? c[--b] = e : e > 127 && 2048 > e ? (c[--b] = 63 & e | 128,
                    c[--b] = e >> 6 | 192) : (c[--b] = 63 & e | 128,
                    c[--b] = e >> 6 & 63 | 128,
                    c[--b] = e >> 12 | 224)
            }
            c[--b] = 0;
            for (var f = new SecureRandom, g = new Array; b > 2; ) {
                for (g[0] = 0; 0 == g[0]; )
                    f.nextBytes(g);
                c[--b] = g[0]
            }
            return c[--b] = 2,
                c[--b] = 0,
                new BigInteger(c)
        }
        function RSAKey() {
            this.n = null,
                this.e = 0,
                this.d = null,
                this.p = null,
                this.q = null,
                this.dmp1 = null,
                this.dmq1 = null,
                this.coeff = null
        }
        function RSASetPublic(a, b) {
            null != a && null != b && a.length > 0 && b.length > 0 ? (this.n = parseBigInt(a, 16),
                this.e = parseInt(b, 16)) : console.error("Invalid RSA public key")
        }
        function RSADoPublic(a) {
            return a.modPowInt(this.e, this.n)
        }
        function RSAEncrypt(a) {
            var b = pkcs1pad2(a, this.n.bitLength() + 7 >> 3);
            if (null == b)
                return null;
            var c = this.doPublic(b);
            if (null == c)
                return null;
            var d = c.toString(16);
            return 0 == (1 & d.length) ? d : "0" + d
        }
        function pkcs1unpad2(a, b) {
            for (var c = a.toByteArray(), d = 0; d < c.length && 0 == c[d]; )
                ++d;
            if (c.length - d != b - 1 || 2 != c[d])
                return null;
            for (++d; 0 != c[d]; )
                if (++d >= c.length)
                    return null;
            for (var e = ""; ++d < c.length; ) {
                var f = 255 & c[d];
                128 > f ? e += String.fromCharCode(f) : f > 191 && 224 > f ? (e += String.fromCharCode((31 & f) << 6 | 63 & c[d + 1]),
                    ++d) : (e += String.fromCharCode((15 & f) << 12 | (63 & c[d + 1]) << 6 | 63 & c[d + 2]),
                    d += 2)
            }
            return e
        }
        function RSASetPrivate(a, b, c) {
            null != a && null != b && a.length > 0 && b.length > 0 ? (this.n = parseBigInt(a, 16),
                this.e = parseInt(b, 16),
                this.d = parseBigInt(c, 16)) : console.error("Invalid RSA private key")
        }
        function RSASetPrivateEx(a, b, c, d, e, f, g, h) {
            null != a && null != b && a.length > 0 && b.length > 0 ? (this.n = parseBigInt(a, 16),
                this.e = parseInt(b, 16),
                this.d = parseBigInt(c, 16),
                this.p = parseBigInt(d, 16),
                this.q = parseBigInt(e, 16),
                this.dmp1 = parseBigInt(f, 16),
                this.dmq1 = parseBigInt(g, 16),
                this.coeff = parseBigInt(h, 16)) : console.error("Invalid RSA private key")
        }
        function RSAGenerate(a, b) {
            var c = new SecureRandom
                , d = a >> 1;
            this.e = parseInt(b, 16);
            for (var e = new BigInteger(b,16); ; ) {
                for (; this.p = new BigInteger(a - d,1,c),
                       0 != this.p.subtract(BigInteger.ONE).gcd(e).compareTo(BigInteger.ONE) || !this.p.isProbablePrime(10); )
                    ;
                for (; this.q = new BigInteger(d,1,c),
                       0 != this.q.subtract(BigInteger.ONE).gcd(e).compareTo(BigInteger.ONE) || !this.q.isProbablePrime(10); )
                    ;
                if (this.p.compareTo(this.q) <= 0) {
                    var f = this.p;
                    this.p = this.q,
                        this.q = f
                }
                var g = this.p.subtract(BigInteger.ONE)
                    , h = this.q.subtract(BigInteger.ONE)
                    , i = g.multiply(h);
                if (0 == i.gcd(e).compareTo(BigInteger.ONE)) {
                    this.n = this.p.multiply(this.q),
                        this.d = e.modInverse(i),
                        this.dmp1 = this.d.mod(g),
                        this.dmq1 = this.d.mod(h),
                        this.coeff = this.q.modInverse(this.p);
                    break
                }
            }
        }
        function RSADoPrivate(a) {
            if (null == this.p || null == this.q)
                return a.modPow(this.d, this.n);
            for (var b = a.mod(this.p).modPow(this.dmp1, this.p), c = a.mod(this.q).modPow(this.dmq1, this.q); b.compareTo(c) < 0; )
                b = b.add(this.p);
            return b.subtract(c).multiply(this.coeff).mod(this.p).multiply(this.q).add(c)
        }
        function RSADecrypt(a) {
            var b = parseBigInt(a, 16)
                , c = this.doPrivate(b);
            return null == c ? null : pkcs1unpad2(c, this.n.bitLength() + 7 >> 3)
        }
        function hex2b64(a) {
            var b, c, d = "";
            for (b = 0; b + 3 <= a.length; b += 3)
                c = parseInt(a.substring(b, b + 3), 16),
                    d += b64map.charAt(c >> 6) + b64map.charAt(63 & c);
            for (b + 1 == a.length ? (c = parseInt(a.substring(b, b + 1), 16),
                d += b64map.charAt(c << 2)) : b + 2 == a.length && (c = parseInt(a.substring(b, b + 2), 16),
                d += b64map.charAt(c >> 2) + b64map.charAt((3 & c) << 4)); (3 & d.length) > 0; )
                d += b64pad;
            return d
        }
        function b64tohex(a) {
            var b, c, d = "", e = 0;
            for (b = 0; b < a.length && a.charAt(b) != b64pad; ++b)
                v = b64map.indexOf(a.charAt(b)),
                v < 0 || (0 == e ? (d += int2char(v >> 2),
                    c = 3 & v,
                    e = 1) : 1 == e ? (d += int2char(c << 2 | v >> 4),
                    c = 15 & v,
                    e = 2) : 2 == e ? (d += int2char(c),
                    d += int2char(v >> 2),
                    c = 3 & v,
                    e = 3) : (d += int2char(c << 2 | v >> 4),
                    d += int2char(15 & v),
                    e = 0));
            return 1 == e && (d += int2char(c << 2)),
                d
        }
        function b64toBA(a) {
            var b, c = b64tohex(a), d = new Array;
            for (b = 0; 2 * b < c.length; ++b)
                d[b] = parseInt(c.substring(2 * b, 2 * b + 2), 16);
            return d
        }
        var dbits, canary = 0xdeadbeefcafe, j_lm = 15715070 == (16777215 & canary);
        j_lm && "Microsoft Internet Explorer" == navigator.appName ? (BigInteger.prototype.am = am2,
            dbits = 30) : j_lm && "Netscape" != navigator.appName ? (BigInteger.prototype.am = am1,
            dbits = 26) : (BigInteger.prototype.am = am3,
            dbits = 28),
            BigInteger.prototype.DB = dbits,
            BigInteger.prototype.DM = (1 << dbits) - 1,
            BigInteger.prototype.DV = 1 << dbits;
        var BI_FP = 52;
        BigInteger.prototype.FV = Math.pow(2, BI_FP),
            BigInteger.prototype.F1 = BI_FP - dbits,
            BigInteger.prototype.F2 = 2 * dbits - BI_FP;
        var BI_RM = "0123456789abcdefghijklmnopqrstuvwxyz", BI_RC = new Array, rr, vv;
        for (rr = "0".charCodeAt(0),
                 vv = 0; 9 >= vv; ++vv)
            BI_RC[rr++] = vv;
        for (rr = "a".charCodeAt(0),
                 vv = 10; 36 > vv; ++vv)
            BI_RC[rr++] = vv;
        for (rr = "A".charCodeAt(0),
                 vv = 10; 36 > vv; ++vv)
            BI_RC[rr++] = vv;
        Classic.prototype.convert = cConvert,
            Classic.prototype.revert = cRevert,
            Classic.prototype.reduce = cReduce,
            Classic.prototype.mulTo = cMulTo,
            Classic.prototype.sqrTo = cSqrTo,
            Montgomery.prototype.convert = montConvert,
            Montgomery.prototype.revert = montRevert,
            Montgomery.prototype.reduce = montReduce,
            Montgomery.prototype.mulTo = montMulTo,
            Montgomery.prototype.sqrTo = montSqrTo,
            BigInteger.prototype.copyTo = bnpCopyTo,
            BigInteger.prototype.fromInt = bnpFromInt,
            BigInteger.prototype.fromString = bnpFromString,
            BigInteger.prototype.clamp = bnpClamp,
            BigInteger.prototype.dlShiftTo = bnpDLShiftTo,
            BigInteger.prototype.drShiftTo = bnpDRShiftTo,
            BigInteger.prototype.lShiftTo = bnpLShiftTo,
            BigInteger.prototype.rShiftTo = bnpRShiftTo,
            BigInteger.prototype.subTo = bnpSubTo,
            BigInteger.prototype.multiplyTo = bnpMultiplyTo,
            BigInteger.prototype.squareTo = bnpSquareTo,
            BigInteger.prototype.divRemTo = bnpDivRemTo,
            BigInteger.prototype.invDigit = bnpInvDigit,
            BigInteger.prototype.isEven = bnpIsEven,
            BigInteger.prototype.exp = bnpExp,
            BigInteger.prototype.toString = bnToString,
            BigInteger.prototype.negate = bnNegate,
            BigInteger.prototype.abs = bnAbs,
            BigInteger.prototype.compareTo = bnCompareTo,
            BigInteger.prototype.bitLength = bnBitLength,
            BigInteger.prototype.mod = bnMod,
            BigInteger.prototype.modPowInt = bnModPowInt,
            BigInteger.ZERO = nbv(0),
            BigInteger.ONE = nbv(1),
            NullExp.prototype.convert = nNop,
            NullExp.prototype.revert = nNop,
            NullExp.prototype.mulTo = nMulTo,
            NullExp.prototype.sqrTo = nSqrTo,
            Barrett.prototype.convert = barrettConvert,
            Barrett.prototype.revert = barrettRevert,
            Barrett.prototype.reduce = barrettReduce,
            Barrett.prototype.mulTo = barrettMulTo,
            Barrett.prototype.sqrTo = barrettSqrTo;
        var lowprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
            , lplim = (1 << 26) / lowprimes[lowprimes.length - 1];
        BigInteger.prototype.chunkSize = bnpChunkSize,
            BigInteger.prototype.toRadix = bnpToRadix,
            BigInteger.prototype.fromRadix = bnpFromRadix,
            BigInteger.prototype.fromNumber = bnpFromNumber,
            BigInteger.prototype.bitwiseTo = bnpBitwiseTo,
            BigInteger.prototype.changeBit = bnpChangeBit,
            BigInteger.prototype.addTo = bnpAddTo,
            BigInteger.prototype.dMultiply = bnpDMultiply,
            BigInteger.prototype.dAddOffset = bnpDAddOffset,
            BigInteger.prototype.multiplyLowerTo = bnpMultiplyLowerTo,
            BigInteger.prototype.multiplyUpperTo = bnpMultiplyUpperTo,
            BigInteger.prototype.modInt = bnpModInt,
            BigInteger.prototype.millerRabin = bnpMillerRabin,
            BigInteger.prototype.clone = bnClone,
            BigInteger.prototype.intValue = bnIntValue,
            BigInteger.prototype.byteValue = bnByteValue,
            BigInteger.prototype.shortValue = bnShortValue,
            BigInteger.prototype.signum = bnSigNum,
            BigInteger.prototype.toByteArray = bnToByteArray,
            BigInteger.prototype.equals = bnEquals,
            BigInteger.prototype.min = bnMin,
            BigInteger.prototype.max = bnMax,
            BigInteger.prototype.and = bnAnd,
            BigInteger.prototype.or = bnOr,
            BigInteger.prototype.xor = bnXor,
            BigInteger.prototype.andNot = bnAndNot,
            BigInteger.prototype.not = bnNot,
            BigInteger.prototype.shiftLeft = bnShiftLeft,
            BigInteger.prototype.shiftRight = bnShiftRight,
            BigInteger.prototype.getLowestSetBit = bnGetLowestSetBit,
            BigInteger.prototype.bitCount = bnBitCount,
            BigInteger.prototype.testBit = bnTestBit,
            BigInteger.prototype.setBit = bnSetBit,
            BigInteger.prototype.clearBit = bnClearBit,
            BigInteger.prototype.flipBit = bnFlipBit,
            BigInteger.prototype.add = bnAdd,
            BigInteger.prototype.subtract = bnSubtract,
            BigInteger.prototype.multiply = bnMultiply,
            BigInteger.prototype.divide = bnDivide,
            BigInteger.prototype.remainder = bnRemainder,
            BigInteger.prototype.divideAndRemainder = bnDivideAndRemainder,
            BigInteger.prototype.modPow = bnModPow,
            BigInteger.prototype.modInverse = bnModInverse,
            BigInteger.prototype.pow = bnPow,
            BigInteger.prototype.gcd = bnGCD,
            BigInteger.prototype.isProbablePrime = bnIsProbablePrime,
            BigInteger.prototype.square = bnSquare,
            Arcfour.prototype.init = ARC4init,
            Arcfour.prototype.next = ARC4next;
        var rng_psize = 256, rng_state, rng_pool, rng_pptr;
        if (null == rng_pool) {
            rng_pool = new Array,
                rng_pptr = 0;
            var t;
            if (window.crypto && window.crypto.getRandomValues) {
                var z = new Uint32Array(256);
                for (window.crypto.getRandomValues(z),
                         t = 0; t < z.length; ++t)
                    rng_pool[rng_pptr++] = 255 & z[t]
            }
            var onMouseMoveListener = function(a) {
                if (this.count = this.count || 0,
                this.count >= 256 || rng_pptr >= rng_psize)
                    return void (window.removeEventListener ? window.removeEventListener("mousemove", onMouseMoveListener) : window.detachEvent && window.detachEvent("onmousemove", onMouseMoveListener));
                this.count += 1;
                var b = a.x + a.y;
                rng_pool[rng_pptr++] = 255 & b
            };
            window.addEventListener ? window.addEventListener("mousemove", onMouseMoveListener) : window.attachEvent && window.attachEvent("onmousemove", onMouseMoveListener)
        }
        SecureRandom.prototype.nextBytes = rng_get_bytes,
            RSAKey.prototype.doPublic = RSADoPublic,
            RSAKey.prototype.setPublic = RSASetPublic,
            RSAKey.prototype.encrypt = RSAEncrypt,
            RSAKey.prototype.doPrivate = RSADoPrivate,
            RSAKey.prototype.setPrivate = RSASetPrivate,
            RSAKey.prototype.setPrivateEx = RSASetPrivateEx,
            RSAKey.prototype.generate = RSAGenerate,
            RSAKey.prototype.decrypt = RSADecrypt,
            function() {
                var a = function(a, b, c) {
                    var d = new SecureRandom
                        , e = a >> 1;
                    this.e = parseInt(b, 16);
                    var f = new BigInteger(b,16)
                        , g = this
                        , h = function() {
                        var b = function() {
                            if (g.p.compareTo(g.q) <= 0) {
                                var a = g.p;
                                g.p = g.q,
                                    g.q = a
                            }
                            var b = g.p.subtract(BigInteger.ONE)
                                , d = g.q.subtract(BigInteger.ONE)
                                , e = b.multiply(d);
                            0 == e.gcd(f).compareTo(BigInteger.ONE) ? (g.n = g.p.multiply(g.q),
                                g.d = f.modInverse(e),
                                g.dmp1 = g.d.mod(b),
                                g.dmq1 = g.d.mod(d),
                                g.coeff = g.q.modInverse(g.p),
                                setTimeout(function() {
                                    c()
                                }, 0)) : setTimeout(h, 0)
                        }
                            , i = function() {
                            g.q = nbi(),
                                g.q.fromNumberAsync(e, 1, d, function() {
                                    g.q.subtract(BigInteger.ONE).gcda(f, function(a) {
                                        0 == a.compareTo(BigInteger.ONE) && g.q.isProbablePrime(10) ? setTimeout(b, 0) : setTimeout(i, 0)
                                    })
                                })
                        }
                            , j = function() {
                            g.p = nbi(),
                                g.p.fromNumberAsync(a - e, 1, d, function() {
                                    g.p.subtract(BigInteger.ONE).gcda(f, function(a) {
                                        0 == a.compareTo(BigInteger.ONE) && g.p.isProbablePrime(10) ? setTimeout(i, 0) : setTimeout(j, 0)
                                    })
                                })
                        };
                        setTimeout(j, 0)
                    };
                    setTimeout(h, 0)
                };
                RSAKey.prototype.generateAsync = a;
                var b = function(a, b) {
                    var c = this.s < 0 ? this.negate() : this.clone()
                        , d = a.s < 0 ? a.negate() : a.clone();
                    if (c.compareTo(d) < 0) {
                        var e = c;
                        c = d,
                            d = e
                    }
                    var f = c.getLowestSetBit()
                        , g = d.getLowestSetBit();
                    if (0 > g)
                        return void b(c);
                    g > f && (g = f),
                    g > 0 && (c.rShiftTo(g, c),
                        d.rShiftTo(g, d));
                    var h = function() {
                        (f = c.getLowestSetBit()) > 0 && c.rShiftTo(f, c),
                        (f = d.getLowestSetBit()) > 0 && d.rShiftTo(f, d),
                            c.compareTo(d) >= 0 ? (c.subTo(d, c),
                                c.rShiftTo(1, c)) : (d.subTo(c, d),
                                d.rShiftTo(1, d)),
                            c.signum() > 0 ? setTimeout(h, 0) : (g > 0 && d.lShiftTo(g, d),
                                setTimeout(function() {
                                    b(d)
                                }, 0))
                    };
                    setTimeout(h, 10)
                };
                BigInteger.prototype.gcda = b;
                var c = function(a, b, c, d) {
                    if ("number" == typeof b)
                        if (2 > a)
                            this.fromInt(1);
                        else {
                            this.fromNumber(a, c),
                            this.testBit(a - 1) || this.bitwiseTo(BigInteger.ONE.shiftLeft(a - 1), op_or, this),
                            this.isEven() && this.dAddOffset(1, 0);
                            var e = this
                                , f = function() {
                                e.dAddOffset(2, 0),
                                e.bitLength() > a && e.subTo(BigInteger.ONE.shiftLeft(a - 1), e),
                                    e.isProbablePrime(b) ? setTimeout(function() {
                                        d()
                                    }, 0) : setTimeout(f, 0)
                            };
                            setTimeout(f, 0)
                        }
                    else {
                        var g = new Array
                            , h = 7 & a;
                        g.length = (a >> 3) + 1,
                            b.nextBytes(g),
                            h > 0 ? g[0] &= (1 << h) - 1 : g[0] = 0,
                            this.fromString(g, 256)
                    }
                };
                BigInteger.prototype.fromNumberAsync = c
            }();
        var b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            , b64pad = "="
            , JSX = JSX || {};
        JSX.env = JSX.env || {};
        var L = JSX
            , OP = Object.prototype
            , FUNCTION_TOSTRING = "[object Function]"
            , ADD = ["toString", "valueOf"];
        JSX.env.parseUA = function(a) {
            var b, c = function(a) {
                var b = 0;
                return parseFloat(a.replace(/\./g, function() {
                    return 1 == b++ ? "" : "."
                }))
            }, d = navigator, e = {
                ie: 0,
                opera: 0,
                gecko: 0,
                webkit: 0,
                chrome: 0,
                mobile: null,
                air: 0,
                ipad: 0,
                iphone: 0,
                ipod: 0,
                ios: null,
                android: 0,
                webos: 0,
                caja: d && d.cajaVersion,
                secure: !1,
                os: null
            }, f = a || navigator && navigator.userAgent, g = window && window.location, h = g && g.href;
            return e.secure = h && 0 === h.toLowerCase().indexOf("https"),
            f && (/windows|win32/i.test(f) ? e.os = "windows" : /macintosh/i.test(f) ? e.os = "macintosh" : /rhino/i.test(f) && (e.os = "rhino"),
            /KHTML/.test(f) && (e.webkit = 1),
                b = f.match(/AppleWebKit\/([^\s]*)/),
            b && b[1] && (e.webkit = c(b[1]),
                / Mobile\//.test(f) ? (e.mobile = "Apple",
                    b = f.match(/OS ([^\s]*)/),
                b && b[1] && (b = c(b[1].replace("_", "."))),
                    e.ios = b,
                    e.ipad = e.ipod = e.iphone = 0,
                    b = f.match(/iPad|iPod|iPhone/),
                b && b[0] && (e[b[0].toLowerCase()] = e.ios)) : (b = f.match(/NokiaN[^\/]*|Android \d\.\d|webOS\/\d\.\d/),
                b && (e.mobile = b[0]),
                /webOS/.test(f) && (e.mobile = "WebOS",
                    b = f.match(/webOS\/([^\s]*);/),
                b && b[1] && (e.webos = c(b[1]))),
                / Android/.test(f) && (e.mobile = "Android",
                    b = f.match(/Android ([^\s]*);/),
                b && b[1] && (e.android = c(b[1])))),
                b = f.match(/Chrome\/([^\s]*)/),
                b && b[1] ? e.chrome = c(b[1]) : (b = f.match(/AdobeAIR\/([^\s]*)/),
                b && (e.air = b[0]))),
            e.webkit || (b = f.match(/Opera[\s\/]([^\s]*)/),
                b && b[1] ? (e.opera = c(b[1]),
                    b = f.match(/Version\/([^\s]*)/),
                b && b[1] && (e.opera = c(b[1])),
                    b = f.match(/Opera Mini[^;]*/),
                b && (e.mobile = b[0])) : (b = f.match(/MSIE\s([^;]*)/),
                    b && b[1] ? e.ie = c(b[1]) : (b = f.match(/Gecko\/([^\s]*)/),
                    b && (e.gecko = 1,
                        b = f.match(/rv:([^\s\)]*)/),
                    b && b[1] && (e.gecko = c(b[1]))))))),
                e
        }
            ,
            JSX.env.ua = JSX.env.parseUA(),
            JSX.isFunction = function(a) {
                return "function" == typeof a || OP.toString.apply(a) === FUNCTION_TOSTRING
            }
            ,
            JSX._IEEnumFix = JSX.env.ua.ie ? function(a, b) {
                    var c, d, e;
                    for (c = 0; c < ADD.length; c += 1)
                        d = ADD[c],
                            e = b[d],
                        L.isFunction(e) && e != OP[d] && (a[d] = e)
                }
                : function() {}
            ,
            JSX.extend = function(a, b, c) {
                if (!b || !a)
                    throw new Error("extend failed, please check that all dependencies are included.");
                var d, e = function() {};
                if (e.prototype = b.prototype,
                    a.prototype = new e,
                    a.prototype.constructor = a,
                    a.superclass = b.prototype,
                b.prototype.constructor == OP.constructor && (b.prototype.constructor = b),
                    c) {
                    for (d in c)
                        L.hasOwnProperty(c, d) && (a.prototype[d] = c[d]);
                    L._IEEnumFix(a.prototype, c)
                }
            }
            ,
        "undefined" != typeof KJUR && KJUR || (KJUR = {}),
        "undefined" != typeof KJUR.asn1 && KJUR.asn1 || (KJUR.asn1 = {}),
            KJUR.asn1.ASN1Util = new function() {
                this.integerToByteHex = function(a) {
                    var b = a.toString(16);
                    return b.length % 2 == 1 && (b = "0" + b),
                        b
                }
                    ,
                    this.bigIntToMinTwosComplementsHex = function(a) {
                        var b = a.toString(16);
                        if ("-" != b.substr(0, 1))
                            b.length % 2 == 1 ? b = "0" + b : b.match(/^[0-7]/) || (b = "00" + b);
                        else {
                            var c = b.substr(1)
                                , d = c.length;
                            d % 2 == 1 ? d += 1 : b.match(/^[0-7]/) || (d += 2);
                            for (var e = "", f = 0; d > f; f++)
                                e += "f";
                            var g = new BigInteger(e,16)
                                , h = g.xor(a).add(BigInteger.ONE);
                            b = h.toString(16).replace(/^-/, "")
                        }
                        return b
                    }
                    ,
                    this.getPEMStringFromHex = function(a, b) {
                        var c = CryptoJS.enc.Hex.parse(a)
                            , d = CryptoJS.enc.Base64.stringify(c)
                            , e = d.replace(/(.{64})/g, "$1\r\n");
                        return e = e.replace(/\r\n$/, ""),
                        "-----BEGIN " + b + "-----\r\n" + e + "\r\n-----END " + b + "-----\r\n"
                    }
            }
            ,
            KJUR.asn1.ASN1Object = function() {
                var a = "";
                this.getLengthHexFromValue = function() {
                    if ("undefined" == typeof this.hV || null == this.hV)
                        throw "this.hV is null or undefined.";
                    if (this.hV.length % 2 == 1)
                        throw "value hex must be even length: n=" + a.length + ",v=" + this.hV;
                    var b = this.hV.length / 2
                        , c = b.toString(16);
                    if (c.length % 2 == 1 && (c = "0" + c),
                    128 > b)
                        return c;
                    var d = c.length / 2;
                    if (d > 15)
                        throw "ASN.1 length too long to represent by 8x: n = " + b.toString(16);
                    var e = 128 + d;
                    return e.toString(16) + c
                }
                    ,
                    this.getEncodedHex = function() {
                        return (null == this.hTLV || this.isModified) && (this.hV = this.getFreshValueHex(),
                            this.hL = this.getLengthHexFromValue(),
                            this.hTLV = this.hT + this.hL + this.hV,
                            this.isModified = !1),
                            this.hTLV
                    }
                    ,
                    this.getValueHex = function() {
                        return this.getEncodedHex(),
                            this.hV
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return ""
                    }
            }
            ,
            KJUR.asn1.DERAbstractString = function(a) {
                KJUR.asn1.DERAbstractString.superclass.constructor.call(this);
                this.getString = function() {
                    return this.s
                }
                    ,
                    this.setString = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.s = a,
                            this.hV = stohex(this.s)
                    }
                    ,
                    this.setStringHex = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.s = null,
                            this.hV = a
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return this.hV
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.str ? this.setString(a.str) : "undefined" != typeof a.hex && this.setStringHex(a.hex))
            }
            ,
            JSX.extend(KJUR.asn1.DERAbstractString, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERAbstractTime = function() {
                KJUR.asn1.DERAbstractTime.superclass.constructor.call(this);
                this.localDateToUTC = function(a) {
                    utc = a.getTime() + 6e4 * a.getTimezoneOffset();
                    var b = new Date(utc);
                    return b
                }
                    ,
                    this.formatDate = function(a, b) {
                        var c = this.zeroPadding
                            , d = this.localDateToUTC(a)
                            , e = String(d.getFullYear());
                        "utc" == b && (e = e.substr(2, 2));
                        var f = c(String(d.getMonth() + 1), 2)
                            , g = c(String(d.getDate()), 2)
                            , h = c(String(d.getHours()), 2)
                            , i = c(String(d.getMinutes()), 2)
                            , j = c(String(d.getSeconds()), 2);
                        return e + f + g + h + i + j + "Z"
                    }
                    ,
                    this.zeroPadding = function(a, b) {
                        return a.length >= b ? a : new Array(b - a.length + 1).join("0") + a
                    }
                    ,
                    this.getString = function() {
                        return this.s
                    }
                    ,
                    this.setString = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.s = a,
                            this.hV = stohex(this.s)
                    }
                    ,
                    this.setByDateValue = function(a, b, c, d, e, f) {
                        var g = new Date(Date.UTC(a, b - 1, c, d, e, f, 0));
                        this.setByDate(g)
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return this.hV
                    }
            }
            ,
            JSX.extend(KJUR.asn1.DERAbstractTime, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERAbstractStructured = function(a) {
                KJUR.asn1.DERAbstractString.superclass.constructor.call(this);
                this.setByASN1ObjectArray = function(a) {
                    this.hTLV = null,
                        this.isModified = !0,
                        this.asn1Array = a
                }
                    ,
                    this.appendASN1Object = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.asn1Array.push(a)
                    }
                    ,
                    this.asn1Array = new Array,
                "undefined" != typeof a && "undefined" != typeof a.array && (this.asn1Array = a.array)
            }
            ,
            JSX.extend(KJUR.asn1.DERAbstractStructured, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERBoolean = function() {
                KJUR.asn1.DERBoolean.superclass.constructor.call(this),
                    this.hT = "01",
                    this.hTLV = "0101ff"
            }
            ,
            JSX.extend(KJUR.asn1.DERBoolean, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERInteger = function(a) {
                KJUR.asn1.DERInteger.superclass.constructor.call(this),
                    this.hT = "02",
                    this.setByBigInteger = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.hV = KJUR.asn1.ASN1Util.bigIntToMinTwosComplementsHex(a)
                    }
                    ,
                    this.setByInteger = function(a) {
                        var b = new BigInteger(String(a),10);
                        this.setByBigInteger(b)
                    }
                    ,
                    this.setValueHex = function(a) {
                        this.hV = a
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return this.hV
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.bigint ? this.setByBigInteger(a.bigint) : "undefined" != typeof a["int"] ? this.setByInteger(a["int"]) : "undefined" != typeof a.hex && this.setValueHex(a.hex))
            }
            ,
            JSX.extend(KJUR.asn1.DERInteger, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERBitString = function(a) {
                KJUR.asn1.DERBitString.superclass.constructor.call(this),
                    this.hT = "03",
                    this.setHexValueIncludingUnusedBits = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.hV = a
                    }
                    ,
                    this.setUnusedBitsAndHexValue = function(a, b) {
                        if (0 > a || a > 7)
                            throw "unused bits shall be from 0 to 7: u = " + a;
                        var c = "0" + a;
                        this.hTLV = null,
                            this.isModified = !0,
                            this.hV = c + b
                    }
                    ,
                    this.setByBinaryString = function(a) {
                        a = a.replace(/0+$/, "");
                        var b = 8 - a.length % 8;
                        8 == b && (b = 0);
                        for (var c = 0; b >= c; c++)
                            a += "0";
                        for (var d = "", c = 0; c < a.length - 1; c += 8) {
                            var e = a.substr(c, 8)
                                , f = parseInt(e, 2).toString(16);
                            1 == f.length && (f = "0" + f),
                                d += f
                        }
                        this.hTLV = null,
                            this.isModified = !0,
                            this.hV = "0" + b + d
                    }
                    ,
                    this.setByBooleanArray = function(a) {
                        for (var b = "", c = 0; c < a.length; c++)
                            b += 1 == a[c] ? "1" : "0";
                        this.setByBinaryString(b)
                    }
                    ,
                    this.newFalseArray = function(a) {
                        for (var b = new Array(a), c = 0; a > c; c++)
                            b[c] = !1;
                        return b
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return this.hV
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.hex ? this.setHexValueIncludingUnusedBits(a.hex) : "undefined" != typeof a.bin ? this.setByBinaryString(a.bin) : "undefined" != typeof a.array && this.setByBooleanArray(a.array))
            }
            ,
            JSX.extend(KJUR.asn1.DERBitString, KJUR.asn1.ASN1Object),
            KJUR.asn1.DEROctetString = function(a) {
                KJUR.asn1.DEROctetString.superclass.constructor.call(this, a),
                    this.hT = "04"
            }
            ,
            JSX.extend(KJUR.asn1.DEROctetString, KJUR.asn1.DERAbstractString),
            KJUR.asn1.DERNull = function() {
                KJUR.asn1.DERNull.superclass.constructor.call(this),
                    this.hT = "05",
                    this.hTLV = "0500"
            }
            ,
            JSX.extend(KJUR.asn1.DERNull, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERObjectIdentifier = function(a) {
                var b = function(a) {
                    var b = a.toString(16);
                    return 1 == b.length && (b = "0" + b),
                        b
                }
                    , c = function(a) {
                    var c = ""
                        , d = new BigInteger(a,10)
                        , e = d.toString(2)
                        , f = 7 - e.length % 7;
                    7 == f && (f = 0);
                    for (var g = "", h = 0; f > h; h++)
                        g += "0";
                    e = g + e;
                    for (var h = 0; h < e.length - 1; h += 7) {
                        var i = e.substr(h, 7);
                        h != e.length - 7 && (i = "1" + i),
                            c += b(parseInt(i, 2))
                    }
                    return c
                };
                KJUR.asn1.DERObjectIdentifier.superclass.constructor.call(this),
                    this.hT = "06",
                    this.setValueHex = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.s = null,
                            this.hV = a
                    }
                    ,
                    this.setValueOidString = function(a) {
                        if (!a.match(/^[0-9.]+$/))
                            throw "malformed oid string: " + a;
                        var d = ""
                            , e = a.split(".")
                            , f = 40 * parseInt(e[0]) + parseInt(e[1]);
                        d += b(f),
                            e.splice(0, 2);
                        for (var g = 0; g < e.length; g++)
                            d += c(e[g]);
                        this.hTLV = null,
                            this.isModified = !0,
                            this.s = null,
                            this.hV = d
                    }
                    ,
                    this.setValueName = function(a) {
                        if ("undefined" == typeof KJUR.asn1.x509.OID.name2oidList[a])
                            throw "DERObjectIdentifier oidName undefined: " + a;
                        var b = KJUR.asn1.x509.OID.name2oidList[a];
                        this.setValueOidString(b)
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return this.hV
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.oid ? this.setValueOidString(a.oid) : "undefined" != typeof a.hex ? this.setValueHex(a.hex) : "undefined" != typeof a.name && this.setValueName(a.name))
            }
            ,
            JSX.extend(KJUR.asn1.DERObjectIdentifier, KJUR.asn1.ASN1Object),
            KJUR.asn1.DERUTF8String = function(a) {
                KJUR.asn1.DERUTF8String.superclass.constructor.call(this, a),
                    this.hT = "0c"
            }
            ,
            JSX.extend(KJUR.asn1.DERUTF8String, KJUR.asn1.DERAbstractString),
            KJUR.asn1.DERNumericString = function(a) {
                KJUR.asn1.DERNumericString.superclass.constructor.call(this, a),
                    this.hT = "12"
            }
            ,
            JSX.extend(KJUR.asn1.DERNumericString, KJUR.asn1.DERAbstractString),
            KJUR.asn1.DERPrintableString = function(a) {
                KJUR.asn1.DERPrintableString.superclass.constructor.call(this, a),
                    this.hT = "13"
            }
            ,
            JSX.extend(KJUR.asn1.DERPrintableString, KJUR.asn1.DERAbstractString),
            KJUR.asn1.DERTeletexString = function(a) {
                KJUR.asn1.DERTeletexString.superclass.constructor.call(this, a),
                    this.hT = "14"
            }
            ,
            JSX.extend(KJUR.asn1.DERTeletexString, KJUR.asn1.DERAbstractString),
            KJUR.asn1.DERIA5String = function(a) {
                KJUR.asn1.DERIA5String.superclass.constructor.call(this, a),
                    this.hT = "16"
            }
            ,
            JSX.extend(KJUR.asn1.DERIA5String, KJUR.asn1.DERAbstractString),
            KJUR.asn1.DERUTCTime = function(a) {
                KJUR.asn1.DERUTCTime.superclass.constructor.call(this, a),
                    this.hT = "17",
                    this.setByDate = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.date = a,
                            this.s = this.formatDate(this.date, "utc"),
                            this.hV = stohex(this.s)
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.str ? this.setString(a.str) : "undefined" != typeof a.hex ? this.setStringHex(a.hex) : "undefined" != typeof a.date && this.setByDate(a.date))
            }
            ,
            JSX.extend(KJUR.asn1.DERUTCTime, KJUR.asn1.DERAbstractTime),
            KJUR.asn1.DERGeneralizedTime = function(a) {
                KJUR.asn1.DERGeneralizedTime.superclass.constructor.call(this, a),
                    this.hT = "18",
                    this.setByDate = function(a) {
                        this.hTLV = null,
                            this.isModified = !0,
                            this.date = a,
                            this.s = this.formatDate(this.date, "gen"),
                            this.hV = stohex(this.s)
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.str ? this.setString(a.str) : "undefined" != typeof a.hex ? this.setStringHex(a.hex) : "undefined" != typeof a.date && this.setByDate(a.date))
            }
            ,
            JSX.extend(KJUR.asn1.DERGeneralizedTime, KJUR.asn1.DERAbstractTime),
            KJUR.asn1.DERSequence = function(a) {
                KJUR.asn1.DERSequence.superclass.constructor.call(this, a),
                    this.hT = "30",
                    this.getFreshValueHex = function() {
                        for (var a = "", b = 0; b < this.asn1Array.length; b++) {
                            var c = this.asn1Array[b];
                            a += c.getEncodedHex()
                        }
                        return this.hV = a,
                            this.hV
                    }
            }
            ,
            JSX.extend(KJUR.asn1.DERSequence, KJUR.asn1.DERAbstractStructured),
            KJUR.asn1.DERSet = function(a) {
                KJUR.asn1.DERSet.superclass.constructor.call(this, a),
                    this.hT = "31",
                    this.getFreshValueHex = function() {
                        for (var a = new Array, b = 0; b < this.asn1Array.length; b++) {
                            var c = this.asn1Array[b];
                            a.push(c.getEncodedHex())
                        }
                        return a.sort(),
                            this.hV = a.join(""),
                            this.hV
                    }
            }
            ,
            JSX.extend(KJUR.asn1.DERSet, KJUR.asn1.DERAbstractStructured),
            KJUR.asn1.DERTaggedObject = function(a) {
                KJUR.asn1.DERTaggedObject.superclass.constructor.call(this),
                    this.hT = "a0",
                    this.hV = "",
                    this.isExplicit = !0,
                    this.asn1Object = null,
                    this.setASN1Object = function(a, b, c) {
                        this.hT = b,
                            this.isExplicit = a,
                            this.asn1Object = c,
                            this.isExplicit ? (this.hV = this.asn1Object.getEncodedHex(),
                                this.hTLV = null,
                                this.isModified = !0) : (this.hV = null,
                                this.hTLV = c.getEncodedHex(),
                                this.hTLV = this.hTLV.replace(/^../, b),
                                this.isModified = !1)
                    }
                    ,
                    this.getFreshValueHex = function() {
                        return this.hV
                    }
                    ,
                "undefined" != typeof a && ("undefined" != typeof a.tag && (this.hT = a.tag),
                "undefined" != typeof a.explicit && (this.isExplicit = a.explicit),
                "undefined" != typeof a.obj && (this.asn1Object = a.obj,
                    this.setASN1Object(this.isExplicit, this.hT, this.asn1Object)))
            }
            ,
            JSX.extend(KJUR.asn1.DERTaggedObject, KJUR.asn1.ASN1Object),
            function(a) {
                "use strict";
                var b, c = {};
                c.decode = function(c) {
                    var d;
                    if (b === a) {
                        var e = "0123456789ABCDEF"
                            , f = " \f\n\r	聽\u2028\u2029";
                        for (b = [],
                                 d = 0; 16 > d; ++d)
                            b[e.charAt(d)] = d;
                        for (e = e.toLowerCase(),
                                 d = 10; 16 > d; ++d)
                            b[e.charAt(d)] = d;
                        for (d = 0; d < f.length; ++d)
                            b[f.charAt(d)] = -1
                    }
                    var g = []
                        , h = 0
                        , i = 0;
                    for (d = 0; d < c.length; ++d) {
                        var j = c.charAt(d);
                        if ("=" == j)
                            break;
                        if (j = b[j],
                        -1 != j) {
                            if (j === a)
                                throw "Illegal character at offset " + d;
                            h |= j,
                                ++i >= 2 ? (g[g.length] = h,
                                    h = 0,
                                    i = 0) : h <<= 4
                        }
                    }
                    if (i)
                        throw "Hex encoding incomplete: 4 bits missing";
                    return g
                }
                    ,
                    window.Hex = c
            }(),
            function(a) {
                "use strict";
                var b, c = {};
                c.decode = function(c) {
                    var d;
                    if (b === a) {
                        var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                            , f = "= \f\n\r	聽\u2028\u2029";
                        for (b = [],
                                 d = 0; 64 > d; ++d)
                            b[e.charAt(d)] = d;
                        for (d = 0; d < f.length; ++d)
                            b[f.charAt(d)] = -1
                    }
                    var g = []
                        , h = 0
                        , i = 0;
                    for (d = 0; d < c.length; ++d) {
                        var j = c.charAt(d);
                        if ("=" == j)
                            break;
                        if (j = b[j],
                        -1 != j) {
                            if (j === a)
                                throw "Illegal character at offset " + d;
                            h |= j,
                                ++i >= 4 ? (g[g.length] = h >> 16,
                                    g[g.length] = h >> 8 & 255,
                                    g[g.length] = 255 & h,
                                    h = 0,
                                    i = 0) : h <<= 6
                        }
                    }
                    switch (i) {
                        case 1:
                            throw "Base64 encoding incomplete: at least 2 bits missing";
                        case 2:
                            g[g.length] = h >> 10;
                            break;
                        case 3:
                            g[g.length] = h >> 16,
                                g[g.length] = h >> 8 & 255
                    }
                    return g
                }
                    ,
                    c.re = /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
                    c.unarmor = function(a) {
                        var b = c.re.exec(a);
                        if (b)
                            if (b[1])
                                a = b[1];
                            else {
                                if (!b[2])
                                    throw "RegExp out of sync";
                                a = b[2]
                            }
                        return c.decode(a)
                    }
                    ,
                    window.Base64 = c
            }(),
            function(a) {
                "use strict";
                function b(a, c) {
                    a instanceof b ? (this.enc = a.enc,
                        this.pos = a.pos) : (this.enc = a,
                        this.pos = c)
                }
                function c(a, b, c, d, e) {
                    this.stream = a,
                        this.header = b,
                        this.length = c,
                        this.tag = d,
                        this.sub = e
                }
                var d = 100
                    , e = "鈥�"
                    , f = {
                    tag: function(a, b) {
                        var c = document.createElement(a);
                        return c.className = b,
                            c
                    },
                    text: function(a) {
                        return document.createTextNode(a)
                    }
                };
                b.prototype.get = function(b) {
                    if (b === a && (b = this.pos++),
                    b >= this.enc.length)
                        throw "Requesting byte offset " + b + " on a stream of length " + this.enc.length;
                    return this.enc[b]
                }
                    ,
                    b.prototype.hexDigits = "0123456789ABCDEF",
                    b.prototype.hexByte = function(a) {
                        return this.hexDigits.charAt(a >> 4 & 15) + this.hexDigits.charAt(15 & a)
                    }
                    ,
                    b.prototype.hexDump = function(a, b, c) {
                        for (var d = "", e = a; b > e; ++e)
                            if (d += this.hexByte(this.get(e)),
                            c !== !0)
                                switch (15 & e) {
                                    case 7:
                                        d += "  ";
                                        break;
                                    case 15:
                                        d += "\n";
                                        break;
                                    default:
                                        d += " "
                                }
                        return d
                    }
                    ,
                    b.prototype.parseStringISO = function(a, b) {
                        for (var c = "", d = a; b > d; ++d)
                            c += String.fromCharCode(this.get(d));
                        return c
                    }
                    ,
                    b.prototype.parseStringUTF = function(a, b) {
                        for (var c = "", d = a; b > d; ) {
                            var e = this.get(d++);
                            c += String.fromCharCode(128 > e ? e : e > 191 && 224 > e ? (31 & e) << 6 | 63 & this.get(d++) : (15 & e) << 12 | (63 & this.get(d++)) << 6 | 63 & this.get(d++))
                        }
                        return c
                    }
                    ,
                    b.prototype.parseStringBMP = function(a, b) {
                        for (var c = "", d = a; b > d; d += 2) {
                            var e = this.get(d)
                                , f = this.get(d + 1);
                            c += String.fromCharCode((e << 8) + f)
                        }
                        return c
                    }
                    ,
                    b.prototype.reTime = /^((?:1[89]|2\d)?\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/,
                    b.prototype.parseTime = function(a, b) {
                        var c = this.parseStringISO(a, b)
                            , d = this.reTime.exec(c);
                        return d ? (c = d[1] + "-" + d[2] + "-" + d[3] + " " + d[4],
                        d[5] && (c += ":" + d[5],
                        d[6] && (c += ":" + d[6],
                        d[7] && (c += "." + d[7]))),
                        d[8] && (c += " UTC",
                        "Z" != d[8] && (c += d[8],
                        d[9] && (c += ":" + d[9]))),
                            c) : "Unrecognized time: " + c
                    }
                    ,
                    b.prototype.parseInteger = function(a, b) {
                        var c = b - a;
                        if (c > 4) {
                            c <<= 3;
                            var d = this.get(a);
                            if (0 === d)
                                c -= 8;
                            else
                                for (; 128 > d; )
                                    d <<= 1,
                                        --c;
                            return "(" + c + " bit)"
                        }
                        for (var e = 0, f = a; b > f; ++f)
                            e = e << 8 | this.get(f);
                        return e
                    }
                    ,
                    b.prototype.parseBitString = function(a, b) {
                        var c = this.get(a)
                            , d = (b - a - 1 << 3) - c
                            , e = "(" + d + " bit)";
                        if (20 >= d) {
                            var f = c;
                            e += " ";
                            for (var g = b - 1; g > a; --g) {
                                for (var h = this.get(g), i = f; 8 > i; ++i)
                                    e += h >> i & 1 ? "1" : "0";
                                f = 0
                            }
                        }
                        return e
                    }
                    ,
                    b.prototype.parseOctetString = function(a, b) {
                        var c = b - a
                            , f = "(" + c + " byte) ";
                        c > d && (b = a + d);
                        for (var g = a; b > g; ++g)
                            f += this.hexByte(this.get(g));
                        return c > d && (f += e),
                            f
                    }
                    ,
                    b.prototype.parseOID = function(a, b) {
                        for (var c = "", d = 0, e = 0, f = a; b > f; ++f) {
                            var g = this.get(f);
                            if (d = d << 7 | 127 & g,
                                e += 7,
                                !(128 & g)) {
                                if ("" === c) {
                                    var h = 80 > d ? 40 > d ? 0 : 1 : 2;
                                    c = h + "." + (d - 40 * h)
                                } else
                                    c += "." + (e >= 31 ? "bigint" : d);
                                d = e = 0
                            }
                        }
                        return c
                    }
                    ,
                    c.prototype.typeName = function() {
                        if (this.tag === a)
                            return "unknown";
                        var b = this.tag >> 6
                            , c = (this.tag >> 5 & 1,
                        31 & this.tag);
                        switch (b) {
                            case 0:
                                switch (c) {
                                    case 0:
                                        return "EOC";
                                    case 1:
                                        return "BOOLEAN";
                                    case 2:
                                        return "INTEGER";
                                    case 3:
                                        return "BIT_STRING";
                                    case 4:
                                        return "OCTET_STRING";
                                    case 5:
                                        return "NULL";
                                    case 6:
                                        return "OBJECT_IDENTIFIER";
                                    case 7:
                                        return "ObjectDescriptor";
                                    case 8:
                                        return "EXTERNAL";
                                    case 9:
                                        return "REAL";
                                    case 10:
                                        return "ENUMERATED";
                                    case 11:
                                        return "EMBEDDED_PDV";
                                    case 12:
                                        return "UTF8String";
                                    case 16:
                                        return "SEQUENCE";
                                    case 17:
                                        return "SET";
                                    case 18:
                                        return "NumericString";
                                    case 19:
                                        return "PrintableString";
                                    case 20:
                                        return "TeletexString";
                                    case 21:
                                        return "VideotexString";
                                    case 22:
                                        return "IA5String";
                                    case 23:
                                        return "UTCTime";
                                    case 24:
                                        return "GeneralizedTime";
                                    case 25:
                                        return "GraphicString";
                                    case 26:
                                        return "VisibleString";
                                    case 27:
                                        return "GeneralString";
                                    case 28:
                                        return "UniversalString";
                                    case 30:
                                        return "BMPString";
                                    default:
                                        return "Universal_" + c.toString(16)
                                }
                            case 1:
                                return "Application_" + c.toString(16);
                            case 2:
                                return "[" + c + "]";
                            case 3:
                                return "Private_" + c.toString(16)
                        }
                    }
                    ,
                    c.prototype.reSeemsASCII = /^[ -~]+$/,
                    c.prototype.content = function() {
                        if (this.tag === a)
                            return null;
                        var b = this.tag >> 6
                            , c = 31 & this.tag
                            , f = this.posContent()
                            , g = Math.abs(this.length);
                        if (0 !== b) {
                            if (null !== this.sub)
                                return "(" + this.sub.length + " elem)";
                            var h = this.stream.parseStringISO(f, f + Math.min(g, d));
                            return this.reSeemsASCII.test(h) ? h.substring(0, 2 * d) + (h.length > 2 * d ? e : "") : this.stream.parseOctetString(f, f + g)
                        }
                        switch (c) {
                            case 1:
                                return 0 === this.stream.get(f) ? "false" : "true";
                            case 2:
                                return this.stream.parseInteger(f, f + g);
                            case 3:
                                return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(f, f + g);
                            case 4:
                                return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(f, f + g);
                            case 6:
                                return this.stream.parseOID(f, f + g);
                            case 16:
                            case 17:
                                return "(" + this.sub.length + " elem)";
                            case 12:
                                return this.stream.parseStringUTF(f, f + g);
                            case 18:
                            case 19:
                            case 20:
                            case 21:
                            case 22:
                            case 26:
                                return this.stream.parseStringISO(f, f + g);
                            case 30:
                                return this.stream.parseStringBMP(f, f + g);
                            case 23:
                            case 24:
                                return this.stream.parseTime(f, f + g)
                        }
                        return null
                    }
                    ,
                    c.prototype.toString = function() {
                        return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
                    }
                    ,
                    c.prototype.print = function(b) {
                        if (b === a && (b = ""),
                            document.writeln(b + this),
                        null !== this.sub) {
                            b += "  ";
                            for (var c = 0, d = this.sub.length; d > c; ++c)
                                this.sub[c].print(b)
                        }
                    }
                    ,
                    c.prototype.toPrettyString = function(b) {
                        b === a && (b = "");
                        var c = b + this.typeName() + " @" + this.stream.pos;
                        if (this.length >= 0 && (c += "+"),
                            c += this.length,
                            32 & this.tag ? c += " (constructed)" : 3 != this.tag && 4 != this.tag || null === this.sub || (c += " (encapsulates)"),
                            c += "\n",
                        null !== this.sub) {
                            b += "  ";
                            for (var d = 0, e = this.sub.length; e > d; ++d)
                                c += this.sub[d].toPrettyString(b)
                        }
                        return c
                    }
                    ,
                    c.prototype.toDOM = function() {
                        var a = f.tag("div", "node");
                        a.asn1 = this;
                        var b = f.tag("div", "head")
                            , c = this.typeName().replace(/_/g, " ");
                        b.innerHTML = c;
                        var d = this.content();
                        if (null !== d) {
                            d = String(d).replace(/</g, "&lt;");
                            var e = f.tag("span", "preview");
                            e.appendChild(f.text(d)),
                                b.appendChild(e)
                        }
                        a.appendChild(b),
                            this.node = a,
                            this.head = b;
                        var g = f.tag("div", "value");
                        if (c = "Offset: " + this.stream.pos + "<br/>",
                            c += "Length: " + this.header + "+",
                            c += this.length >= 0 ? this.length : -this.length + " (undefined)",
                            32 & this.tag ? c += "<br/>(constructed)" : 3 != this.tag && 4 != this.tag || null === this.sub || (c += "<br/>(encapsulates)"),
                        null !== d && (c += "<br/>Value:<br/><b>" + d + "</b>",
                        "object" == typeof oids && 6 == this.tag)) {
                            var h = oids[d];
                            h && (h.d && (c += "<br/>" + h.d),
                            h.c && (c += "<br/>" + h.c),
                            h.w && (c += "<br/>(warning!)"))
                        }
                        g.innerHTML = c,
                            a.appendChild(g);
                        var i = f.tag("div", "sub");
                        if (null !== this.sub)
                            for (var j = 0, k = this.sub.length; k > j; ++j)
                                i.appendChild(this.sub[j].toDOM());
                        return a.appendChild(i),
                            b.onclick = function() {
                                a.className = "node collapsed" == a.className ? "node" : "node collapsed"
                            }
                            ,
                            a
                    }
                    ,
                    c.prototype.posStart = function() {
                        return this.stream.pos
                    }
                    ,
                    c.prototype.posContent = function() {
                        return this.stream.pos + this.header
                    }
                    ,
                    c.prototype.posEnd = function() {
                        return this.stream.pos + this.header + Math.abs(this.length)
                    }
                    ,
                    c.prototype.fakeHover = function(a) {
                        this.node.className += " hover",
                        a && (this.head.className += " hover")
                    }
                    ,
                    c.prototype.fakeOut = function(a) {
                        var b = / ?hover/;
                        this.node.className = this.node.className.replace(b, ""),
                        a && (this.head.className = this.head.className.replace(b, ""))
                    }
                    ,
                    c.prototype.toHexDOM_sub = function(a, b, c, d, e) {
                        if (!(d >= e)) {
                            var g = f.tag("span", b);
                            g.appendChild(f.text(c.hexDump(d, e))),
                                a.appendChild(g)
                        }
                    }
                    ,
                    c.prototype.toHexDOM = function(b) {
                        var c = f.tag("span", "hex");
                        if (b === a && (b = c),
                            this.head.hexNode = c,
                            this.head.onmouseover = function() {
                                this.hexNode.className = "hexCurrent"
                            }
                            ,
                            this.head.onmouseout = function() {
                                this.hexNode.className = "hex"
                            }
                            ,
                            c.asn1 = this,
                            c.onmouseover = function() {
                                var a = !b.selected;
                                a && (b.selected = this.asn1,
                                    this.className = "hexCurrent"),
                                    this.asn1.fakeHover(a)
                            }
                            ,
                            c.onmouseout = function() {
                                var a = b.selected == this.asn1;
                                this.asn1.fakeOut(a),
                                a && (b.selected = null,
                                    this.className = "hex")
                            }
                            ,
                            this.toHexDOM_sub(c, "tag", this.stream, this.posStart(), this.posStart() + 1),
                            this.toHexDOM_sub(c, this.length >= 0 ? "dlen" : "ulen", this.stream, this.posStart() + 1, this.posContent()),
                        null === this.sub)
                            c.appendChild(f.text(this.stream.hexDump(this.posContent(), this.posEnd())));
                        else if (this.sub.length > 0) {
                            var d = this.sub[0]
                                , e = this.sub[this.sub.length - 1];
                            this.toHexDOM_sub(c, "intro", this.stream, this.posContent(), d.posStart());
                            for (var g = 0, h = this.sub.length; h > g; ++g)
                                c.appendChild(this.sub[g].toHexDOM(b));
                            this.toHexDOM_sub(c, "outro", this.stream, e.posEnd(), this.posEnd())
                        }
                        return c
                    }
                    ,
                    c.prototype.toHexString = function() {
                        return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
                    }
                    ,
                    c.decodeLength = function(a) {
                        var b = a.get()
                            , c = 127 & b;
                        if (c == b)
                            return c;
                        if (c > 3)
                            throw "Length over 24 bits not supported at position " + (a.pos - 1);
                        if (0 === c)
                            return -1;
                        b = 0;
                        for (var d = 0; c > d; ++d)
                            b = b << 8 | a.get();
                        return b
                    }
                    ,
                    c.hasContent = function(a, d, e) {
                        if (32 & a)
                            return !0;
                        if (3 > a || a > 4)
                            return !1;
                        var f = new b(e);
                        3 == a && f.get();
                        var g = f.get();
                        if (g >> 6 & 1)
                            return !1;
                        try {
                            var h = c.decodeLength(f);
                            return f.pos - e.pos + h == d
                        } catch (i) {
                            return !1
                        }
                    }
                    ,
                    c.decode = function(a) {
                        a instanceof b || (a = new b(a,0));
                        var d = new b(a)
                            , e = a.get()
                            , f = c.decodeLength(a)
                            , g = a.pos - d.pos
                            , h = null;
                        if (c.hasContent(e, f, a)) {
                            var i = a.pos;
                            if (3 == e && a.get(),
                                h = [],
                            f >= 0) {
                                for (var j = i + f; a.pos < j; )
                                    h[h.length] = c.decode(a);
                                if (a.pos != j)
                                    throw "Content size is not correct for container starting at offset " + i
                            } else
                                try {
                                    for (; ; ) {
                                        var k = c.decode(a);
                                        if (0 === k.tag)
                                            break;
                                        h[h.length] = k
                                    }
                                    f = i - a.pos
                                } catch (l) {
                                    throw "Exception while decoding undefined length content: " + l
                                }
                        } else
                            a.pos += f;
                        return new c(d,g,f,e,h)
                    }
                    ,
                    c.test = function() {
                        for (var a = [{
                            value: [39],
                            expected: 39
                        }, {
                            value: [129, 201],
                            expected: 201
                        }, {
                            value: [131, 254, 220, 186],
                            expected: 16702650
                        }], d = 0, e = a.length; e > d; ++d) {
                            var f = new b(a[d].value,0)
                                , g = c.decodeLength(f);
                            g != a[d].expected && document.write("In test[" + d + "] expected " + a[d].expected + " got " + g + "\n")
                        }
                    }
                    ,
                    window.ASN1 = c
            }(),
            ASN1.prototype.getHexStringValue = function() {
                var a = this.toHexString()
                    , b = 2 * this.header
                    , c = 2 * this.length;
                return a.substr(b, c)
            }
            ,
            RSAKey.prototype.parseKey = function(a) {
                try {
                    var b = 0
                        , c = 0
                        , d = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/
                        , e = d.test(a) ? Hex.decode(a) : Base64.unarmor(a)
                        , f = ASN1.decode(e);
                    if (3 === f.sub.length && (f = f.sub[2].sub[0]),
                    9 === f.sub.length) {
                        b = f.sub[1].getHexStringValue(),
                            this.n = parseBigInt(b, 16),
                            c = f.sub[2].getHexStringValue(),
                            this.e = parseInt(c, 16);
                        var g = f.sub[3].getHexStringValue();
                        this.d = parseBigInt(g, 16);
                        var h = f.sub[4].getHexStringValue();
                        this.p = parseBigInt(h, 16);
                        var i = f.sub[5].getHexStringValue();
                        this.q = parseBigInt(i, 16);
                        var j = f.sub[6].getHexStringValue();
                        this.dmp1 = parseBigInt(j, 16);
                        var k = f.sub[7].getHexStringValue();
                        this.dmq1 = parseBigInt(k, 16);
                        var l = f.sub[8].getHexStringValue();
                        this.coeff = parseBigInt(l, 16)
                    } else {
                        if (2 !== f.sub.length)
                            return !1;
                        var m = f.sub[1]
                            , n = m.sub[0];
                        b = n.sub[0].getHexStringValue(),
                            this.n = parseBigInt(b, 16),
                            c = n.sub[1].getHexStringValue(),
                            this.e = parseInt(c, 16)
                    }
                    return !0
                } catch (o) {
                    return !1
                }
            }
            ,
            RSAKey.prototype.getPrivateBaseKey = function() {
                var a = {
                    array: [new KJUR.asn1.DERInteger({
                        "int": 0
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.n
                    }), new KJUR.asn1.DERInteger({
                        "int": this.e
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.d
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.p
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.q
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.dmp1
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.dmq1
                    }), new KJUR.asn1.DERInteger({
                        bigint: this.coeff
                    })]
                }
                    , b = new KJUR.asn1.DERSequence(a);
                return b.getEncodedHex()
            }
            ,
            RSAKey.prototype.getPrivateBaseKeyB64 = function() {
                return hex2b64(this.getPrivateBaseKey())
            }
            ,
            RSAKey.prototype.getPublicBaseKey = function() {
                var a = {
                    array: [new KJUR.asn1.DERObjectIdentifier({
                        oid: "1.2.840.113549.1.1.1"
                    }), new KJUR.asn1.DERNull]
                }
                    , b = new KJUR.asn1.DERSequence(a);
                a = {
                    array: [new KJUR.asn1.DERInteger({
                        bigint: this.n
                    }), new KJUR.asn1.DERInteger({
                        "int": this.e
                    })]
                };
                var c = new KJUR.asn1.DERSequence(a);
                a = {
                    hex: "00" + c.getEncodedHex()
                };
                var d = new KJUR.asn1.DERBitString(a);
                a = {
                    array: [b, d]
                };
                var e = new KJUR.asn1.DERSequence(a);
                return e.getEncodedHex()
            }
            ,
            RSAKey.prototype.getPublicBaseKeyB64 = function() {
                return hex2b64(this.getPublicBaseKey())
            }
            ,
            RSAKey.prototype.wordwrap = function(a, b) {
                if (b = b || 64,
                    !a)
                    return a;
                var c = "(.{1," + b + "})( +|$\n?)|(.{1," + b + "})";
                return a.match(RegExp(c, "g")).join("\n")
            }
            ,
            RSAKey.prototype.getPrivateKey = function() {
                var a = "-----BEGIN RSA PRIVATE KEY-----\n";
                return a += this.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
                    a += "-----END RSA PRIVATE KEY-----"
            }
            ,
            RSAKey.prototype.getPublicKey = function() {
                var a = "-----BEGIN PUBLIC KEY-----\n";
                return a += this.wordwrap(this.getPublicBaseKeyB64()) + "\n",
                    a += "-----END PUBLIC KEY-----"
            }
            ,
            RSAKey.prototype.hasPublicKeyProperty = function(a) {
                return a = a || {},
                a.hasOwnProperty("n") && a.hasOwnProperty("e")
            }
            ,
            RSAKey.prototype.hasPrivateKeyProperty = function(a) {
                return a = a || {},
                a.hasOwnProperty("n") && a.hasOwnProperty("e") && a.hasOwnProperty("d") && a.hasOwnProperty("p") && a.hasOwnProperty("q") && a.hasOwnProperty("dmp1") && a.hasOwnProperty("dmq1") && a.hasOwnProperty("coeff")
            }
            ,
            RSAKey.prototype.parsePropertiesFrom = function(a) {
                this.n = a.n,
                    this.e = a.e,
                a.hasOwnProperty("d") && (this.d = a.d,
                    this.p = a.p,
                    this.q = a.q,
                    this.dmp1 = a.dmp1,
                    this.dmq1 = a.dmq1,
                    this.coeff = a.coeff)
            }
        ;
        var JSEncryptRSAKey = function(a) {
            RSAKey.call(this),
            a && ("string" == typeof a ? this.parseKey(a) : (this.hasPrivateKeyProperty(a) || this.hasPublicKeyProperty(a)) && this.parsePropertiesFrom(a))
        };
        JSEncryptRSAKey.prototype = new RSAKey,
            JSEncryptRSAKey.prototype.constructor = JSEncryptRSAKey;
        var JSEncrypt = function(a) {
            a = a || {},
                this.default_key_size = parseInt(a.default_key_size) || 1024,
                this.default_public_exponent = a.default_public_exponent || "010001",
                this.log = a.log || !1,
                this.key = null
        };
        JSEncrypt.prototype.setKey = function(a) {
            this.log && this.key && console.warn("A key was already set, overriding existing."),
                this.key = new JSEncryptRSAKey(a)
        }
            ,
            JSEncrypt.prototype.setPrivateKey = function(a) {
                this.setKey(a)
            }
            ,
            JSEncrypt.prototype.setPublicKey = function(a) {
                this.setKey(a)
            }
            ,
            JSEncrypt.prototype.decrypt = function(a) {
                try {
                    return this.getKey().decrypt(b64tohex(a))
                } catch (b) {
                    return !1
                }
            }
            ,
            JSEncrypt.prototype.encrypt = function(a) {
                try {
                    return hex2b64(this.getKey().encrypt(a))
                } catch (b) {
                    return !1
                }
            }
            ,
            JSEncrypt.prototype.getKey = function(a) {
                if (!this.key) {
                    if (this.key = new JSEncryptRSAKey,
                    a && "[object Function]" === {}.toString.call(a))
                        return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, a);
                    this.key.generate(this.default_key_size, this.default_public_exponent)
                }
                return this.key
            }
            ,
            JSEncrypt.prototype.getPrivateKey = function() {
                return this.getKey().getPrivateKey()
            }
            ,
            JSEncrypt.prototype.getPrivateKeyB64 = function() {
                return this.getKey().getPrivateBaseKeyB64()
            }
            ,
            JSEncrypt.prototype.getPublicKey = function() {
                return this.getKey().getPublicKey()
            }
            ,
            JSEncrypt.prototype.getPublicKeyB64 = function() {
                return this.getKey().getPublicBaseKeyB64()
            }
        ;
        exports.JSEncrypt = JSEncrypt;
    }
)(JSEncryptExports);
var JSEncrypt = JSEncryptExports.JSEncrypt;

encryptFn = function(e) {
    var o = new JSEncrypt;
    return o.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"),
        o.encrypt(e)
}
enc=function(pwd ,data){
    return encryptFn(pwd + '' + data)
}