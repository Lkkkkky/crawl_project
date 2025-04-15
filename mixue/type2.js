M = {
    un: function (L) {
        return !(!L.protocol || 0 == L.protocol.indexOf("data") || L.host.match(/(cloudauth-device|captcha-(pro-)?open).*?\.aliyuncs\.com$/));
    },
    sig: function (L) {
        for (var N = 0, g = encodeURIComponent(L),             B = 0;              B < g.length; B++) {
            N = (N << 7) - N + 398 + g.charCodeAt(B);
            N |= 0;
            // console.log(N)
        }
        return N;
    },
    uf: function (L, N) {
        return !!M.un(L) && M.F6(L, N);
    },
    F7: function (L) {
        P = {
            "mxsa.mxbc.net": "type__1286"
        }
        L = 'mxsa.mxbc.net'
        if (P[L]) {
            return P[L];
        }
        // console.log(P[L])
        for (var N = 0, g = 0; g < L.length; g++) {
            N += L[g].charCodeAt();
        }
        var B = W[N % W.length] + N % 10000;
        return P[L] = B;
    },
    F8: function (L) {
        var N = (0, H.F9)(L).host,
            N = M.F7(N);
        return (0, H.FF)(L, N);
    },
    F6: function (L, N) {
        var g = (0, H.FY)(L, !0);
        N && (g += N);
        N = M.sig(g) + "|" + (0, m.n)() + "|" + new Date().getTime() + "|1";
        g = E.FU.ua(N, !0);
        N = {};
        N[M.F7(L.host)] = g;
        L.search = (0, H.Fa)(L.search, N);
        return (0, H.FY)(L);
    }
}

function V(g, B) {
    return g.protocol + "//" + g.host + g.pathname + g.search + (B ? "" : g.hash);
}
uu = function (E, H, W) {
    if (null == E) {
        return "";
    }
    for (var P, M, K, V, L = {}, N = {}, B = "", Q = 2, R = 3, I = 2, T = [], w = 0, k = 0, v = 0; v < E.length; v += 1) {
        if (K = E.charAt(v), Object.prototype.hasOwnProperty.call(L, K) || (L[K] = R++, N[K] = !0), V = B + K, Object.prototype.hasOwnProperty.call(L, V)) {
            B = V;
        } else {
            if (Object.prototype.hasOwnProperty.call(N, B)) {
                if (B.charCodeAt(0) < 256) {
                    for (P = 0; P < I; P++) {
                        w <<= 1;
                        k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                    }
                    for (M = B.charCodeAt(0), P = 0; P < 8; P++) {
                        w = w << 1 | 1 & M;
                        k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                        M >>= 1;
                    }
                } else {
                    for (M = 1, P = 0; P < I; P++) {
                        w = w << 1 | M;
                        k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                        M = 0;
                    }
                    for (M = B.charCodeAt(0), P = 0; P < 16; P++) {
                        w = w << 1 | 1 & M;
                        k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                        M >>= 1;
                    }
                }
                0 == --Q && (Q = Math.pow(2, I), I++);
                delete N[B];
            } else {
                for (M = L[B], P = 0; P < I; P++) {
                    w = w << 1 | 1 & M;
                    k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                    M >>= 1;
                }
            }
            0 == --Q && (Q = Math.pow(2, I), I++);
            L[V] = R++;
            B = String(K);
        }
    }
    if ("" !== B) {
        if (Object.prototype.hasOwnProperty.call(N, B)) {
            if (B.charCodeAt(0) < 256) {
                for (P = 0; P < I; P++) {
                    w <<= 1;
                    k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                }
                for (M = B.charCodeAt(0), P = 0; P < 8; P++) {
                    w = w << 1 | 1 & M;
                    k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                    M >>= 1;
                }
            } else {
                for (M = 1, P = 0; P < I; P++) {
                    w = w << 1 | M;
                    k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                    M = 0;
                }
                for (M = B.charCodeAt(0), P = 0; P < 16; P++) {
                    w = w << 1 | 1 & M;
                    k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                    M >>= 1;
                }
            }
            0 == --Q && (Q = Math.pow(2, I), I++);
            delete N[B];
        } else {
            for (M = L[B], P = 0; P < I; P++) {
                w = w << 1 | 1 & M;
                k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
                M >>= 1;
            }
        }
        0 == --Q && (Q = Math.pow(2, I), I++);
    }
    for (M = 2, P = 0; P < I; P++) {
        w = w << 1 | 1 & M;
        k == H - 1 ? (k = 0, T.push(W(w)), w = 0) : k++;
        M >>= 1;
    }
    for (;;) {
        if (w <<= 1, k == H - 1) {
            T.push(W(w));
            break;
        }
        k++;
    }
    return T.join("");
}

ua = function (E, H) {
    var K = {};
    K.uGGDj = "DGi0YA7BemWnQjCl4+bR3f8SKIF9tUz/xhr2oEOgPpac=61ZqwTudLkM5vHyNXsVJ";
    var V = K;
    if (null == E) {
        return "";
    }
    var M = uu(E, 6, function (L) {
        return V.uGGDj.charAt(L);
    });
    if (H) {
        return M;
    }
    switch (M.length % 4) {
        default:
        case 0:
            return M;
        case 1:
            return M + "===";
        case 2:
            return M + "==";
        case 3:
            return M + "=";
    }
}

function K(g, B) {
    // console.log(g)
    if (0 != Object.keys(B).length) {
        var Q,
            R = "";
        for (Q in B) R += encodeURIComponent(Q) + "=" + encodeURIComponent(B[Q]) + "&";
        if (R = R.slice(0, R.length - 1), 0 == g.length) {
            g = "?" + R;
        } else {
            for (var f = g.slice(1).split("&"), u = [], I = Object.keys(B), T = 0; T < f.length; T++) {
                Q = decodeURIComponent(f[T].split("=", 1)[0]); - 1 == I.indexOf(Q) && u.push(f[T]);
            }
            g = "?" + (0 == u.length ? "" : u.join("&") + "&") + R;
        }
    }
    return g;
}

info = function (L, N) {
    /*           'https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/info?marketingId=1816854086004391938&sign=585157e19b624f0f2330884ea56f8208&s=2&stamp=1722428454218'
     */
    var g = (0, V)(L, !0);
    N && (g += N);
    N = M.sig(g) + "|" + 0 + "|" + new Date().getTime() + "|1";
    g = ua(N, !0);
    N = {};
    N[M.F7(L.host)] = g;
    // console.log(L.match(/info(\S+)/)[1])
    L = K(L.match(/info(\S+)/)[1], N);
    // console.log(L)
    return (L);
}
secretword = function (L, N) {
    /*
            'https://mxsa.mxbc.net/api/v1/h5/marketing/secretword/confirm{"marketingId":"1816854086004391938","round":"20:00","secretword":"1111","sign":"3a845253ccfce6ffa5de7ab7470429ce","s":2,"stamp":1722430651398}'
            */
    var g = L
    // console.log(g)
    N && (g += N);
    N = M.sig(g) + "|" + 0 + "|" + new Date().getTime() + "|1";
    // console.log(M.sig(g))
    g = ua(N, !0);
    N = {};
    N[M.F7(L.host)] = g;
    L = K("", N);
    // console.log(L)
    return (L);
}


// var hh=M()
// console.log(hh)
