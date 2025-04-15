const crypto = require("crypto");
const c = [
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "0a",
    "0b",
    "0c",
    "0d",
    "0e",
    "0f",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "1a",
    "1b",
    "1c",
    "1d",
    "1e",
    "1f",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "2a",
    "2b",
    "2c",
    "2d",
    "2e",
    "2f",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "3a",
    "3b",
    "3c",
    "3d",
    "3e",
    "3f",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "4a",
    "4b",
    "4c",
    "4d",
    "4e",
    "4f",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "5a",
    "5b",
    "5c",
    "5d",
    "5e",
    "5f",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "6a",
    "6b",
    "6c",
    "6d",
    "6e",
    "6f",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "7a",
    "7b",
    "7c",
    "7d",
    "7e",
    "7f",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "8a",
    "8b",
    "8c",
    "8d",
    "8e",
    "8f",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "9a",
    "9b",
    "9c",
    "9d",
    "9e",
    "9f",
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6",
    "a7",
    "a8",
    "a9",
    "aa",
    "ab",
    "ac",
    "ad",
    "ae",
    "af",
    "b0",
    "b1",
    "b2",
    "b3",
    "b4",
    "b5",
    "b6",
    "b7",
    "b8",
    "b9",
    "ba",
    "bb",
    "bc",
    "bd",
    "be",
    "bf",
    "c0",
    "c1",
    "c2",
    "c3",
    "c4",
    "c5",
    "c6",
    "c7",
    "c8",
    "c9",
    "ca",
    "cb",
    "cc",
    "cd",
    "ce",
    "cf",
    "d0",
    "d1",
    "d2",
    "d3",
    "d4",
    "d5",
    "d6",
    "d7",
    "d8",
    "d9",
    "da",
    "db",
    "dc",
    "dd",
    "de",
    "df",
    "e0",
    "e1",
    "e2",
    "e3",
    "e4",
    "e5",
    "e6",
    "e7",
    "e8",
    "e9",
    "ea",
    "eb",
    "ec",
    "ed",
    "ee",
    "ef",
    "f0",
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "fa",
    "fb",
    "fc",
    "fd",
    "fe",
    "ff"
];
var CryptoJS = CryptoJS || (function (Math, undefined) {
    var crypto;
    if (typeof window !== 'undefined' && window.crypto) {
        crypto = window.crypto;
    }
    if (typeof self !== 'undefined' && self.crypto) {
        crypto = self.crypto;
    }
    if (typeof globalThis !== 'undefined' && globalThis.crypto) {
        crypto = globalThis.crypto;
    }
    if (!crypto && typeof window !== 'undefined' && window.msCrypto) {
        crypto = window.msCrypto;
    }
    if (!crypto && typeof global !== 'undefined' && global.crypto) {
        crypto = global.crypto;
    }
    if (!crypto && typeof require === 'function') {
        try {
            crypto = require('crypto');
        } catch (err) {
        }
    }
    var cryptoSecureRandomInt = function () {
        if (crypto) {
            if (typeof crypto.getRandomValues === 'function') {
                try {
                    return crypto.getRandomValues(new Uint32Array(1))[0];
                } catch (err) {
                }
            }
            if (typeof crypto.randomBytes === 'function') {
                try {
                    return crypto.randomBytes(4).readInt32LE();
                } catch (err) {
                }
            }
        }
        throw new Error('Native crypto module could not be used to get secure random number.');
    };
    var create = Object.create || (function () {
        function F() {
        }

        return function (obj) {
            var subtype;
            F.prototype = obj;
            subtype = new F();
            F.prototype = null;
            return subtype;
        };
    }());
    var C = {};
    var C_lib = C.lib = {};
    var Base = C_lib.Base = (function () {
        return {
            extend: function (overrides) {
                var subtype = create(this);
                if (overrides) {
                    subtype.mixIn(overrides);
                }
                if (!subtype.hasOwnProperty('init') || this.init === subtype.init) {
                    subtype.init = function () {
                        subtype.$super.init.apply(this, arguments);
                    };
                }
                subtype.init.prototype = subtype;
                subtype.$super = this;
                return subtype;
            }, create: function () {
                var instance = this.extend();
                instance.init.apply(instance, arguments);
                return instance;
            }, init: function () {
            }, mixIn: function (properties) {
                for (var propertyName in properties) {
                    if (properties.hasOwnProperty(propertyName)) {
                        this[propertyName] = properties[propertyName];
                    }
                }
                if (properties.hasOwnProperty('toString')) {
                    this.toString = properties.toString;
                }
            }, clone: function () {
                return this.init.prototype.extend(this);
            }
        };
    }());
    var WordArray = C_lib.WordArray = Base.extend({
        init: function (words, sigBytes) {
            words = this.words = words || [];
            if (sigBytes != undefined) {
                this.sigBytes = sigBytes;
            } else {
                this.sigBytes = words.length * 4;
            }
        }, toString: function (encoder) {
            return (encoder || Hex).stringify(this);
        }, concat: function (wordArray) {
            var thisWords = this.words;
            var thatWords = wordArray.words;
            var thisSigBytes = this.sigBytes;
            var thatSigBytes = wordArray.sigBytes;
            this.clamp();
            if (thisSigBytes % 4) {
                for (var i = 0; i < thatSigBytes; i++) {
                    var thatByte = (thatWords[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
                    thisWords[(thisSigBytes + i) >>> 2] |= thatByte << (24 - ((thisSigBytes + i) % 4) * 8);
                }
            } else {
                for (var j = 0; j < thatSigBytes; j += 4) {
                    thisWords[(thisSigBytes + j) >>> 2] = thatWords[j >>> 2];
                }
            }
            this.sigBytes += thatSigBytes;
            return this;
        }, clamp: function () {
            var words = this.words;
            var sigBytes = this.sigBytes;
            words[sigBytes >>> 2] &= 0xffffffff << (32 - (sigBytes % 4) * 8);
            words.length = Math.ceil(sigBytes / 4);
        }, clone: function () {
            var clone = Base.clone.call(this);
            clone.words = this.words.slice(0);
            return clone;
        }, random: function (nBytes) {
            var words = [];
            var r = (function (m_w) {
                var m_w = m_w;
                var m_z = 0x3ade68b1;
                var mask = 0xffffffff;
                return function () {
                    m_z = (0x9069 * (m_z & 0xFFFF) + (m_z >> 0x10)) & mask;
                    m_w = (0x4650 * (m_w & 0xFFFF) + (m_w >> 0x10)) & mask;
                    var result = ((m_z << 0x10) + m_w) & mask;
                    result /= 0x100000000;
                    result += 0.5;
                    return result * (Math.random() > .5 ? 1 : -1);
                }
            });
            var RANDOM = false, _r;
            try {
                cryptoSecureRandomInt();
                RANDOM = true;
            } catch (err) {
            }
            for (var i = 0, rcache; i < nBytes; i += 4) {
                if (!RANDOM) {
                    _r = r((rcache || Math.random()) * 0x100000000);
                    rcache = _r() * 0x3ade67b7;
                    words.push((_r() * 0x100000000) | 0);
                    continue;
                }
                words.push(cryptoSecureRandomInt());
            }
            return new WordArray.init(words, nBytes);
        }
    });
    var C_enc = C.enc = {};
    var Hex = C_enc.Hex = {
        stringify: function (wordArray) {
            var words = wordArray.words;
            var sigBytes = wordArray.sigBytes;
            var hexChars = [];
            for (var i = 0; i < sigBytes; i++) {
                var bite = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
                hexChars.push((bite >>> 4).toString(16));
                hexChars.push((bite & 0x0f).toString(16));
            }
            return hexChars.join('');
        }, parse: function (hexStr) {
            var hexStrLength = hexStr.length;
            var words = [];
            for (var i = 0; i < hexStrLength; i += 2) {
                words[i >>> 3] |= parseInt(hexStr.substr(i, 2), 16) << (24 - (i % 8) * 4);
            }
            return new WordArray.init(words, hexStrLength / 2);
        }
    };
    var Latin1 = C_enc.Latin1 = {
        stringify: function (wordArray) {
            var words = wordArray.words;
            var sigBytes = wordArray.sigBytes;
            var latin1Chars = [];
            for (var i = 0; i < sigBytes; i++) {
                var bite = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
                latin1Chars.push(String.fromCharCode(bite));
            }
            return latin1Chars.join('');
        }, parse: function (latin1Str) {
            var latin1StrLength = latin1Str.length;
            var words = [];
            for (var i = 0; i < latin1StrLength; i++) {
                words[i >>> 2] |= (latin1Str.charCodeAt(i) & 0xff) << (24 - (i % 4) * 8);
            }
            return new WordArray.init(words, latin1StrLength);
        }
    };
    var Utf8 = C_enc.Utf8 = {
        stringify: function (wordArray) {
            try {
                return decodeURIComponent(escape(Latin1.stringify(wordArray)));
            } catch (e) {
                throw new Error('Malformed UTF-8 data');
            }
        }, parse: function (utf8Str) {
            return Latin1.parse(unescape(encodeURIComponent(utf8Str)));
        }
    };
    var BufferedBlockAlgorithm = C_lib.BufferedBlockAlgorithm = Base.extend({
        reset: function () {
            this._data = new WordArray.init();
            this._nDataBytes = 0;
        }, _append: function (data) {
            if (typeof data == 'string') {
                data = Utf8.parse(data);
            }
            this._data.concat(data);
            this._nDataBytes += data.sigBytes;
        }, _process: function (doFlush) {
            var processedWords;
            var data = this._data;
            var dataWords = data.words;
            var dataSigBytes = data.sigBytes;
            var blockSize = this.blockSize;
            var blockSizeBytes = blockSize * 4;
            var nBlocksReady = dataSigBytes / blockSizeBytes;
            if (doFlush) {
                nBlocksReady = Math.ceil(nBlocksReady);
            } else {
                nBlocksReady = Math.max((nBlocksReady | 0) - this._minBufferSize, 0);
            }
            var nWordsReady = nBlocksReady * blockSize;
            var nBytesReady = Math.min(nWordsReady * 4, dataSigBytes);
            if (nWordsReady) {
                for (var offset = 0; offset < nWordsReady; offset += blockSize) {
                    this._doProcessBlock(dataWords, offset);
                }
                processedWords = dataWords.splice(0, nWordsReady);
                data.sigBytes -= nBytesReady;
            }
            return new WordArray.init(processedWords, nBytesReady);
        }, clone: function () {
            var clone = Base.clone.call(this);
            clone._data = this._data.clone();
            return clone;
        }, _minBufferSize: 0
    });
    var Hasher = C_lib.Hasher = BufferedBlockAlgorithm.extend({
        cfg: Base.extend(),
        init: function (cfg) {
            this.cfg = this.cfg.extend(cfg);
            this.reset();
        }, reset: function () {
            BufferedBlockAlgorithm.reset.call(this);
            this._doReset();
        }, update: function (messageUpdate) {
            this._append(messageUpdate);
            this._process();
            return this;
        }, finalize: function (messageUpdate) {
            if (messageUpdate) {
                this._append(messageUpdate);
            }
            var hash = this._doFinalize();
            return hash;
        }, blockSize: 512 / 32,
        _createHelper: function (hasher) {
            return function (message, cfg) {
                return new hasher.init(cfg).finalize(message);
            };
        }, _createHmacHelper: function (hasher) {
            return function (message, key) {
                return new C_algo.HMAC.init(hasher, key).finalize(message);
            };
        }
    });
    var C_algo = C.algo = {};
    return C;
}(Math));

(function () {
    var C = CryptoJS;
    var C_lib = C.lib;
    var WordArray = C_lib.WordArray;
    var C_enc = C.enc;
    var Base64 = C_enc.Base64 = {
        stringify: function (wordArray) {
            var words = wordArray.words;
            var sigBytes = wordArray.sigBytes;
            var map = this._map;
            wordArray.clamp();
            var base64Chars = [];
            for (var i = 0; i < sigBytes; i += 3) {
                var byte1 = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
                var byte2 = (words[(i + 1) >>> 2] >>> (24 - ((i + 1) % 4) * 8)) & 0xff;
                var byte3 = (words[(i + 2) >>> 2] >>> (24 - ((i + 2) % 4) * 8)) & 0xff;
                var triplet = (byte1 << 16) | (byte2 << 8) | byte3;
                for (var j = 0;
                     (j < 4) && (i + j * 0.75 < sigBytes); j++) {
                    base64Chars.push(map.charAt((triplet >>> (6 * (3 - j))) & 0x3f));
                }
            }
            var paddingChar = map.charAt(64);
            if (paddingChar) {
                while (base64Chars.length % 4) {
                    base64Chars.push(paddingChar);
                }
            }
            return base64Chars.join('');
        }, parse: function (base64Str) {
            var base64StrLength = base64Str.length;
            var map = this._map;
            var reverseMap = this._reverseMap;
            if (!reverseMap) {
                reverseMap = this._reverseMap = [];
                for (var j = 0; j < map.length; j++) {
                    reverseMap[map.charCodeAt(j)] = j;
                }
            }
            var paddingChar = map.charAt(64);
            if (paddingChar) {
                var paddingIndex = base64Str.indexOf(paddingChar);
                if (paddingIndex !== -1) {
                    base64StrLength = paddingIndex;
                }
            }
            return parseLoop(base64Str, base64StrLength, reverseMap);
        }, _map: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    };

    function parseLoop(base64Str, base64StrLength, reverseMap) {
        var words = [];
        var nBytes = 0;
        for (var i = 0; i < base64StrLength; i++) {
            if (i % 4) {
                var bits1 = reverseMap[base64Str.charCodeAt(i - 1)] << ((i % 4) * 2);
                var bits2 = reverseMap[base64Str.charCodeAt(i)] >>> (6 - (i % 4) * 2);
                words[nBytes >>> 2] |= (bits1 | bits2) << (24 - (nBytes % 4) * 8);
                nBytes++;
            }
        }
        return WordArray.create(words, nBytes);
    }
}());

CryptoJS.lib.Cipher || (function (undefined) {
    var C = CryptoJS;
    var C_lib = C.lib;
    var Base = C_lib.Base;
    var WordArray = C_lib.WordArray;
    var BufferedBlockAlgorithm = C_lib.BufferedBlockAlgorithm;
    var C_enc = C.enc;
    var Utf8 = C_enc.Utf8;
    var Base64 = C_enc.Base64;
    var C_algo = C.algo;
    var EvpKDF = C_algo.EvpKDF;
    var Cipher = C_lib.Cipher = BufferedBlockAlgorithm.extend({
        cfg: Base.extend(),
        createEncryptor: function (key, cfg) {
            return this.create(this._ENC_XFORM_MODE, key, cfg);
        }, createDecryptor: function (key, cfg) {
            return this.create(this._DEC_XFORM_MODE, key, cfg);
        }, init: function (xformMode, key, cfg) {
            this.cfg = this.cfg.extend(cfg);
            this._xformMode = xformMode;
            this._key = key;
            this.reset();
        }, reset: function () {
            BufferedBlockAlgorithm.reset.call(this);
            this._doReset();
        }, process: function (dataUpdate) {
            this._append(dataUpdate);
            return this._process();
        }, finalize: function (dataUpdate) {
            if (dataUpdate) {
                this._append(dataUpdate);
            }
            var finalProcessedData = this._doFinalize();
            return finalProcessedData;
        }, keySize: 128 / 32,
        ivSize: 128 / 32,
        _ENC_XFORM_MODE: 1,
        _DEC_XFORM_MODE: 2,
        _createHelper: (function () {
            function selectCipherStrategy(key) {
                if (typeof key == 'string') {
                    return PasswordBasedCipher;
                } else {
                    return SerializableCipher;
                }
            }

            return function (cipher) {
                return {
                    encrypt: function (message, key, cfg) {
                        return selectCipherStrategy(key).encrypt(cipher, message, key, cfg);
                    }, decrypt: function (ciphertext, key, cfg) {
                        return selectCipherStrategy(key).decrypt(cipher, ciphertext, key, cfg);
                    }
                };
            };
        }())
    });
    var StreamCipher = C_lib.StreamCipher = Cipher.extend({
        _doFinalize: function () {
            var finalProcessedBlocks = this._process(!!'flush');
            return finalProcessedBlocks;
        }, blockSize: 1
    });
    var C_mode = C.mode = {};
    var BlockCipherMode = C_lib.BlockCipherMode = Base.extend({
        createEncryptor: function (cipher, iv) {
            return this.Encryptor.create(cipher, iv);
        }, createDecryptor: function (cipher, iv) {
            return this.Decryptor.create(cipher, iv);
        }, init: function (cipher, iv) {
            this._cipher = cipher;
            this._iv = iv;
        }
    });
    var CBC = C_mode.CBC = (function () {
        var CBC = BlockCipherMode.extend();
        CBC.Encryptor = CBC.extend({
            processBlock: function (words, offset) {
                var cipher = this._cipher;
                var blockSize = cipher.blockSize;
                xorBlock.call(this, words, offset, blockSize);
                cipher.encryptBlock(words, offset);
                this._prevBlock = words.slice(offset, offset + blockSize);
            }
        });
        CBC.Decryptor = CBC.extend({
            processBlock: function (words, offset) {
                var cipher = this._cipher;
                var blockSize = cipher.blockSize;
                var thisBlock = words.slice(offset, offset + blockSize);
                cipher.decryptBlock(words, offset);
                xorBlock.call(this, words, offset, blockSize);
                this._prevBlock = thisBlock;
            }
        });

        function xorBlock(words, offset, blockSize) {
            var block;
            var iv = this._iv;
            if (iv) {
                block = iv;
                this._iv = undefined;
            } else {
                block = this._prevBlock;
            }
            for (var i = 0; i < blockSize; i++) {
                words[offset + i] ^= block[i];
            }
        }

        return CBC;
    }());
    var C_pad = C.pad = {};
    var Pkcs7 = C_pad.Pkcs7 = {
        pad: function (data, blockSize) {
            var blockSizeBytes = blockSize * 4;
            var nPaddingBytes = blockSizeBytes - data.sigBytes % blockSizeBytes;
            var paddingWord = (nPaddingBytes << 24) | (nPaddingBytes << 16) | (nPaddingBytes << 8) | nPaddingBytes;
            var paddingWords = [];
            for (var i = 0; i < nPaddingBytes; i += 4) {
                paddingWords.push(paddingWord);
            }
            var padding = WordArray.create(paddingWords, nPaddingBytes);
            data.concat(padding);
        }, unpad: function (data) {
            var nPaddingBytes = data.words[(data.sigBytes - 1) >>> 2] & 0xff;
            data.sigBytes -= nPaddingBytes;
        }
    };
    var BlockCipher = C_lib.BlockCipher = Cipher.extend({
        cfg: Cipher.cfg.extend({
            mode: CBC,
            padding: Pkcs7
        }),
        reset: function () {
            var modeCreator;
            Cipher.reset.call(this);
            var cfg = this.cfg;
            var iv = cfg.iv;
            var mode = cfg.mode;
            if (this._xformMode == this._ENC_XFORM_MODE) {
                modeCreator = mode.createEncryptor;
            } else {
                modeCreator = mode.createDecryptor;
                this._minBufferSize = 1;
            }
            if (this._mode && this._mode.__creator == modeCreator) {
                this._mode.init(this, iv && iv.words);
            } else {
                this._mode = modeCreator.call(mode, this, iv && iv.words);
                this._mode.__creator = modeCreator;
            }
        }, _doProcessBlock: function (words, offset) {
            this._mode.processBlock(words, offset);
        }, _doFinalize: function () {
            var finalProcessedBlocks;
            var padding = this.cfg.padding;
            if (this._xformMode == this._ENC_XFORM_MODE) {
                padding.pad(this._data, this.blockSize);
                finalProcessedBlocks = this._process(!!'flush');
            } else {
                finalProcessedBlocks = this._process(!!'flush');
                padding.unpad(finalProcessedBlocks);
            }
            return finalProcessedBlocks;
        }, blockSize: 128 / 32
    });
    var CipherParams = C_lib.CipherParams = Base.extend({
        init: function (cipherParams) {
            this.mixIn(cipherParams);
        }, toString: function (formatter) {
            return (formatter || this.formatter).stringify(this);
        }
    });
    var C_format = C.format = {};
    var OpenSSLFormatter = C_format.OpenSSL = {
        stringify: function (cipherParams) {
            var wordArray;
            var ciphertext = cipherParams.ciphertext;
            var salt = cipherParams.salt;
            if (salt) {
                wordArray = WordArray.create([0x53616c74, 0x65645f5f]).concat(salt).concat(ciphertext);
            } else {
                wordArray = ciphertext;
            }
            return wordArray.toString(Base64);
        }, parse: function (openSSLStr) {
            var salt;
            var ciphertext = Base64.parse(openSSLStr);
            var ciphertextWords = ciphertext.words;
            if (ciphertextWords[0] == 0x53616c74 && ciphertextWords[1] == 0x65645f5f) {
                salt = WordArray.create(ciphertextWords.slice(2, 4));
                ciphertextWords.splice(0, 4);
                ciphertext.sigBytes -= 16;
            }
            return CipherParams.create({
                ciphertext: ciphertext,
                salt: salt
            });
        }
    };
    var SerializableCipher = C_lib.SerializableCipher = Base.extend({
        cfg: Base.extend({
            format: OpenSSLFormatter
        }),
        encrypt: function (cipher, message, key, cfg) {
            cfg = this.cfg.extend(cfg);
            var encryptor = cipher.createEncryptor(key, cfg);
            var ciphertext = encryptor.finalize(message);
            var cipherCfg = encryptor.cfg;
            return CipherParams.create({
                ciphertext: ciphertext,
                key: key,
                iv: cipherCfg.iv,
                algorithm: cipher,
                mode: cipherCfg.mode,
                padding: cipherCfg.padding,
                blockSize: cipher.blockSize,
                formatter: cfg.format
            });
        }, decrypt: function (cipher, ciphertext, key, cfg) {
            cfg = this.cfg.extend(cfg);
            ciphertext = this._parse(ciphertext, cfg.format);
            var plaintext = cipher.createDecryptor(key, cfg).finalize(ciphertext.ciphertext);
            return plaintext;
        }, _parse: function (ciphertext, format) {
            if (typeof ciphertext == 'string') {
                return format.parse(ciphertext, this);
            } else {
                return ciphertext;
            }
        }
    });
    var C_kdf = C.kdf = {};
    var OpenSSLKdf = C_kdf.OpenSSL = {
        execute: function (password, keySize, ivSize, salt, hasher) {
            if (!salt) {
                salt = WordArray.random(64 / 8);
            }
            if (!hasher) {
                var key = EvpKDF.create({
                    keySize: keySize + ivSize
                }).compute(password, salt);
            } else {
                var key = EvpKDF.create({
                    keySize: keySize + ivSize,
                    hasher: hasher
                }).compute(password, salt);
            }
            var iv = WordArray.create(key.words.slice(keySize), ivSize * 4);
            key.sigBytes = keySize * 4;
            return CipherParams.create({
                key: key,
                iv: iv,
                salt: salt
            });
        }
    };
    var PasswordBasedCipher = C_lib.PasswordBasedCipher = SerializableCipher.extend({
        cfg: SerializableCipher.cfg.extend({
            kdf: OpenSSLKdf
        }),
        encrypt: function (cipher, message, password, cfg) {
            cfg = this.cfg.extend(cfg);
            var derivedParams = cfg.kdf.execute(password, cipher.keySize, cipher.ivSize, cfg.salt, cfg.hasher);
            cfg.iv = derivedParams.iv;
            var ciphertext = SerializableCipher.encrypt.call(this, cipher, message, derivedParams.key, cfg);
            ciphertext.mixIn(derivedParams);
            return ciphertext;
        }, decrypt: function (cipher, ciphertext, password, cfg) {
            cfg = this.cfg.extend(cfg);
            ciphertext = this._parse(ciphertext, cfg.format);
            var derivedParams = cfg.kdf.execute(password, cipher.keySize, cipher.ivSize, ciphertext.salt, cfg.hasher);
            cfg.iv = derivedParams.iv;
            var plaintext = SerializableCipher.decrypt.call(this, cipher, ciphertext, derivedParams.key, cfg);
            return plaintext;
        }
    });
}());

CryptoJS.pad.ZeroPadding = {
    pad: function (data, blockSize) {
        var blockSizeBytes = blockSize * 4;
        data.clamp();
        data.sigBytes += blockSizeBytes - ((data.sigBytes % blockSizeBytes) || blockSizeBytes);
    }, unpad: function (data) {
        var dataWords = data.words;
        var i = data.sigBytes - 1;
        while (!((dataWords[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff)) {
            i--;
        }
        data.sigBytes = i + 1;
    }
};

(function () {
    var C = CryptoJS;
    var C_lib = C.lib;
    var BlockCipher = C_lib.BlockCipher;
    var C_algo = C.algo;
    var SBOX = [];
    var INV_SBOX = [];
    var SUB_MIX_0 = [];
    var SUB_MIX_1 = [];
    var SUB_MIX_2 = [];
    var SUB_MIX_3 = [];
    var INV_SUB_MIX_0 = [];
    var INV_SUB_MIX_1 = [];
    var INV_SUB_MIX_2 = [];
    var INV_SUB_MIX_3 = [];
    (function () {
        var d = [];
        for (var i = 0; i < 256; i++) {
            if (i < 128) {
                d[i] = i << 1;
            } else {
                d[i] = (i << 1) ^ 0x11b;
            }
        }
        var x = 0;
        var xi = 0;
        for (var i = 0; i < 256; i++) {
            var sx = xi ^ (xi << 1) ^ (xi << 2) ^ (xi << 3) ^ (xi << 4);
            sx = (sx >>> 8) ^ (sx & 0xff) ^ 0x63;
            SBOX[x] = sx;
            INV_SBOX[sx] = x;
            var x2 = d[x];
            var x4 = d[x2];
            var x8 = d[x4];
            var t = (d[sx] * 0x101) ^ (sx * 0x1010100);
            SUB_MIX_0[x] = (t << 24) | (t >>> 8);
            SUB_MIX_1[x] = (t << 16) | (t >>> 16);
            SUB_MIX_2[x] = (t << 8) | (t >>> 24);
            SUB_MIX_3[x] = t;
            var t = (x8 * 0x1010101) ^ (x4 * 0x10001) ^ (x2 * 0x101) ^ (x * 0x1010100);
            INV_SUB_MIX_0[sx] = (t << 24) | (t >>> 8);
            INV_SUB_MIX_1[sx] = (t << 16) | (t >>> 16);
            INV_SUB_MIX_2[sx] = (t << 8) | (t >>> 24);
            INV_SUB_MIX_3[sx] = t;
            if (!x) {
                x = xi = 1;
            } else {
                x = x2 ^ d[d[d[x8 ^ x2]]];
                xi ^= d[d[xi]];
            }
        }
    }());
    var RCON = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36];
    var AES = C_algo.AES = BlockCipher.extend({
        _doReset: function () {
            if (this._nRounds && this._keyPriorReset === this._key) {
                return;
            }
            var key = this._keyPriorReset = this._key;
            var keyWords = key.words;
            var keySize = key.sigBytes / 4;
            var nRounds = this._nRounds = keySize + 6;
            var ksRows = (nRounds + 1) * 4;
            var keySchedule = this._keySchedule = [];
            for (var ksRow = 0; ksRow < ksRows; ksRow++) {
                if (ksRow < keySize) {
                    keySchedule[ksRow] = keyWords[ksRow];
                } else {
                    var t = keySchedule[ksRow - 1];
                    if (!(ksRow % keySize)) {
                        t = (t << 8) | (t >>> 24);
                        t = (SBOX[t >>> 24] << 24) | (SBOX[(t >>> 16) & 0xff] << 16) | (SBOX[(t >>> 8) & 0xff] << 8) | SBOX[t & 0xff];
                        t ^= RCON[(ksRow / keySize) | 0] << 24;
                    } else if (keySize > 6 && ksRow % keySize == 4) {
                        t = (SBOX[t >>> 24] << 24) | (SBOX[(t >>> 16) & 0xff] << 16) | (SBOX[(t >>> 8) & 0xff] << 8) | SBOX[t & 0xff];
                    }
                    keySchedule[ksRow] = keySchedule[ksRow - keySize] ^ t;
                }
            }
            var invKeySchedule = this._invKeySchedule = [];
            for (var invKsRow = 0; invKsRow < ksRows; invKsRow++) {
                var ksRow = ksRows - invKsRow;
                if (invKsRow % 4) {
                    var t = keySchedule[ksRow];
                } else {
                    var t = keySchedule[ksRow - 4];
                }
                if (invKsRow < 4 || ksRow <= 4) {
                    invKeySchedule[invKsRow] = t;
                } else {
                    invKeySchedule[invKsRow] = INV_SUB_MIX_0[SBOX[t >>> 24]] ^ INV_SUB_MIX_1[SBOX[(t >>> 16) & 0xff]] ^ INV_SUB_MIX_2[SBOX[(t >>> 8) & 0xff]] ^ INV_SUB_MIX_3[SBOX[t & 0xff]];
                }
            }
        }, encryptBlock: function (M, offset) {
            this._doCryptBlock(M, offset, this._keySchedule, SUB_MIX_0, SUB_MIX_1, SUB_MIX_2, SUB_MIX_3, SBOX);
        }, decryptBlock: function (M, offset) {
            var t = M[offset + 1];
            M[offset + 1] = M[offset + 3];
            M[offset + 3] = t;
            this._doCryptBlock(M, offset, this._invKeySchedule, INV_SUB_MIX_0, INV_SUB_MIX_1, INV_SUB_MIX_2, INV_SUB_MIX_3, INV_SBOX);
            var t = M[offset + 1];
            M[offset + 1] = M[offset + 3];
            M[offset + 3] = t;
        }, _doCryptBlock: function (M, offset, keySchedule, SUB_MIX_0, SUB_MIX_1, SUB_MIX_2, SUB_MIX_3, SBOX) {
            var nRounds = this._nRounds;
            var s0 = M[offset] ^ keySchedule[0];
            var s1 = M[offset + 1] ^ keySchedule[1];
            var s2 = M[offset + 2] ^ keySchedule[2];
            var s3 = M[offset + 3] ^ keySchedule[3];
            var ksRow = 4;
            for (var round = 1; round < nRounds; round++) {
                var t0 = SUB_MIX_0[s0 >>> 24] ^ SUB_MIX_1[(s1 >>> 16) & 0xff] ^ SUB_MIX_2[(s2 >>> 8) & 0xff] ^ SUB_MIX_3[s3 & 0xff] ^ keySchedule[ksRow++];
                var t1 = SUB_MIX_0[s1 >>> 24] ^ SUB_MIX_1[(s2 >>> 16) & 0xff] ^ SUB_MIX_2[(s3 >>> 8) & 0xff] ^ SUB_MIX_3[s0 & 0xff] ^ keySchedule[ksRow++];
                var t2 = SUB_MIX_0[s2 >>> 24] ^ SUB_MIX_1[(s3 >>> 16) & 0xff] ^ SUB_MIX_2[(s0 >>> 8) & 0xff] ^ SUB_MIX_3[s1 & 0xff] ^ keySchedule[ksRow++];
                var t3 = SUB_MIX_0[s3 >>> 24] ^ SUB_MIX_1[(s0 >>> 16) & 0xff] ^ SUB_MIX_2[(s1 >>> 8) & 0xff] ^ SUB_MIX_3[s2 & 0xff] ^ keySchedule[ksRow++];
                s0 = t0;
                s1 = t1;
                s2 = t2;
                s3 = t3;
            }
            var t0 = ((SBOX[s0 >>> 24] << 24) | (SBOX[(s1 >>> 16) & 0xff] << 16) | (SBOX[(s2 >>> 8) & 0xff] << 8) | SBOX[s3 & 0xff]) ^ keySchedule[ksRow++];
            var t1 = ((SBOX[s1 >>> 24] << 24) | (SBOX[(s2 >>> 16) & 0xff] << 16) | (SBOX[(s3 >>> 8) & 0xff] << 8) | SBOX[s0 & 0xff]) ^ keySchedule[ksRow++];
            var t2 = ((SBOX[s2 >>> 24] << 24) | (SBOX[(s3 >>> 16) & 0xff] << 16) | (SBOX[(s0 >>> 8) & 0xff] << 8) | SBOX[s1 & 0xff]) ^ keySchedule[ksRow++];
            var t3 = ((SBOX[s3 >>> 24] << 24) | (SBOX[(s0 >>> 16) & 0xff] << 16) | (SBOX[(s1 >>> 8) & 0xff] << 8) | SBOX[s2 & 0xff]) ^ keySchedule[ksRow++];
            M[offset] = t0;
            M[offset + 1] = t1;
            M[offset + 2] = t2;
            M[offset + 3] = t3;
        }, keySize: 256 / 32
    });
    C.AES = BlockCipher._createHelper(AES);
}());


/*! JSEncrypt v2.3.0 | https://npmcdn.com/jsencrypt@2.3.0/LICENSE.txt */
var RSA = {};
(function (exports) {
    var window = {};
    var navigator = {};
    if (!Array.prototype.forEach) {
        Array.prototype.forEach = function (callback, thisArg) {
            var T, k;
            if (this == null) {
                throw new TypeError(' this is null or not defined');
            }
            var O = Object(this);
            var len = O.length >>> 0;
            if (typeof callback !== "function") {
                throw new TypeError(callback + ' is not a function');
            }
            if (arguments.length > 1) {
                T = thisArg;
            }
            k = 0;
            while (k < len) {
                var kValue;
                if (k in O) {
                    kValue = O[k];
                    callback.call(T, kValue, k, O);
                }
                k++;
            }
        };
    }
    ;
    // Copyright (c) 2005  Tom Wu
    // All Rights Reserved.
    // See "LICENSE" for details.

    // Basic JavaScript BN library - subset useful for RSA encryption.

    // Bits per digit
    var dbits;

    // JavaScript engine analysis
    var canary = 0xdeadbeefcafe;
    var j_lm = ((canary & 0xffffff) == 0xefcafe);

    // (public) Constructor
    function BigInteger(a, b, c) {
        if (a != null)
            if ("number" == typeof a) this.fromNumber(a, b, c);
            else if (b == null && "string" != typeof a) this.fromString(a, 256);
            else this.fromString(a, b);
    }

    // return new, unset BigInteger
    function nbi() {
        return new BigInteger(null);
    }

    // am: Compute w_j += (x*this_i), propagate carries,
    // c is initial carry, returns final carry.
    // c < 3*dvalue, x < 2*dvalue, this_i < dvalue
    // We need to select the fastest one that works in this environment.

    // am1: use a single mult and divide to get the high bits,
    // max digit bits should be 26 because
    // max internal value = 2*dvalue^2-2*dvalue (< 2^53)
    function am1(i, x, w, j, c, n) {
        while (--n >= 0) {
            var v = x * this[i++] + w[j] + c;
            c = Math.floor(v / 0x4000000);
            w[j++] = v & 0x3ffffff;
        }
        return c;
    }

    // am2 avoids a big mult-and-extract completely.
    // Max digit bits should be <= 30 because we do bitwise ops
    // on values up to 2*hdvalue^2-hdvalue-1 (< 2^31)

    function am2(i, x, w, j, c, n) {
        var xl = x & 0x7fff,
            xh = x >> 15;
        while (--n >= 0) {
            var l = this[i] & 0x7fff;
            var h = this[i++] >> 15;
            var m = xh * l + h * xl;
            l = xl * l + ((m & 0x7fff) << 15) + w[j] + (c & 0x3fffffff);
            c = (l >>> 30) + (m >>> 15) + xh * h + (c >>> 30);
            w[j++] = l & 0x3fffffff;
        }
        return c;
    }

    // Alternately, set max digit bits to 28 since some
    // browsers slow down when dealing with 32-bit numbers.

    function am3(i, x, w, j, c, n) {
        var xl = x & 0x3fff,
            xh = x >> 14;
        while (--n >= 0) {
            var l = this[i] & 0x3fff;
            var h = this[i++] >> 14;
            var m = xh * l + h * xl;
            l = xl * l + ((m & 0x3fff) << 14) + w[j] + c;
            c = (l >> 28) + (m >> 14) + xh * h;
            w[j++] = l & 0xfffffff;
        }
        return c;
    }

    if (j_lm && (navigator.appName == "Microsoft Internet Explorer")) {
        BigInteger.prototype.am = am2;
        dbits = 30;
    } else if (j_lm && (navigator.appName != "Netscape")) {
        BigInteger.prototype.am = am1;
        dbits = 26;
    } else { // Mozilla/Netscape seems to prefer am3
        BigInteger.prototype.am = am3;
        dbits = 28;
    }

    BigInteger.prototype.DB = dbits;
    BigInteger.prototype.DM = ((1 << dbits) - 1);
    BigInteger.prototype.DV = (1 << dbits);

    var BI_FP = 52;
    BigInteger.prototype.FV = Math.pow(2, BI_FP);
    BigInteger.prototype.F1 = BI_FP - dbits;
    BigInteger.prototype.F2 = 2 * dbits - BI_FP;

    // Digit conversions
    var BI_RM = "0123456789abcdefghijklmnopqrstuvwxyz";
    var BI_RC = new Array();
    var rr, vv;
    rr = "0".charCodeAt(0);
    for (vv = 0; vv <= 9; ++vv) BI_RC[rr++] = vv;
    rr = "a".charCodeAt(0);
    for (vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
    rr = "A".charCodeAt(0);
    for (vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;

    function int2char(n) {
        return BI_RM.charAt(n);
    }

    function intAt(s, i) {
        var c = BI_RC[s.charCodeAt(i)];
        return (c == null) ? -1 : c;
    }

    // (protected) copy this to r
    function bnpCopyTo(r) {
        for (var i = this.t - 1; i >= 0; --i) r[i] = this[i];
        r.t = this.t;
        r.s = this.s;
    }

    // (protected) set from integer value x, -DV <= x < DV
    function bnpFromInt(x) {
        this.t = 1;
        this.s = (x < 0) ? -1 : 0;
        if (x > 0) this[0] = x;
        else if (x < -1) this[0] = x + this.DV;
        else this.t = 0;
    }

    // return bigint initialized to value
    function nbv(i) {
        var r = nbi();
        r.fromInt(i);
        return r;
    }

    // (protected) set from string and radix
    function bnpFromString(s, b) {
        var k;
        if (b == 16) k = 4;
        else if (b == 8) k = 3;
        else if (b == 256) k = 8; // byte array
        else if (b == 2) k = 1;
        else if (b == 32) k = 5;
        else if (b == 4) k = 2;
        else {
            this.fromRadix(s, b);
            return;
        }
        this.t = 0;
        this.s = 0;
        var i = s.length,
            mi = false,
            sh = 0;
        while (--i >= 0) {
            var x = (k == 8) ? s[i] & 0xff : intAt(s, i);
            if (x < 0) {
                if (s.charAt(i) == "-") mi = true;
                continue;
            }
            mi = false;
            if (sh == 0)
                this[this.t++] = x;
            else if (sh + k > this.DB) {
                this[this.t - 1] |= (x & ((1 << (this.DB - sh)) - 1)) << sh;
                this[this.t++] = (x >> (this.DB - sh));
            } else
                this[this.t - 1] |= x << sh;
            sh += k;
            if (sh >= this.DB) sh -= this.DB;
        }
        if (k == 8 && (s[0] & 0x80) != 0) {
            this.s = -1;
            if (sh > 0) this[this.t - 1] |= ((1 << (this.DB - sh)) - 1) << sh;
        }
        this.clamp();
        if (mi) BigInteger.ZERO.subTo(this, this);
    }

    // (protected) clamp off excess high words
    function bnpClamp() {
        var c = this.s & this.DM;
        while (this.t > 0 && this[this.t - 1] == c) --this.t;
    }

    // (public) return string representation in given radix
    function bnToString(b) {
        if (this.s < 0) return "-" + this.negate().toString(b);
        var k;
        if (b == 16) k = 4;
        else if (b == 8) k = 3;
        else if (b == 2) k = 1;
        else if (b == 32) k = 5;
        else if (b == 4) k = 2;
        else return this.toRadix(b);
        var km = (1 << k) - 1,
            d, m = false,
            r = "",
            i = this.t;
        var p = this.DB - (i * this.DB) % k;
        if (i-- > 0) {
            if (p < this.DB && (d = this[i] >> p) > 0) {
                m = true;
                r = int2char(d);
            }
            while (i >= 0) {
                if (p < k) {
                    d = (this[i] & ((1 << p) - 1)) << (k - p);
                    d |= this[--i] >> (p += this.DB - k);
                } else {
                    d = (this[i] >> (p -= k)) & km;
                    if (p <= 0) {
                        p += this.DB;
                        --i;
                    }
                }
                if (d > 0) m = true;
                if (m) r += int2char(d);
            }
        }
        return m ? r : "0";
    }

    // (public) -this
    function bnNegate() {
        var r = nbi();
        BigInteger.ZERO.subTo(this, r);
        return r;
    }

    // (public) |this|
    function bnAbs() {
        return (this.s < 0) ? this.negate() : this;
    }

    // (public) return + if this > a, - if this < a, 0 if equal
    function bnCompareTo(a) {
        var r = this.s - a.s;
        if (r != 0) return r;
        var i = this.t;
        r = i - a.t;
        if (r != 0) return (this.s < 0) ? -r : r;
        while (--i >= 0)
            if ((r = this[i] - a[i]) != 0) return r;
        return 0;
    }

    // returns bit length of the integer x
    function nbits(x) {
        var r = 1,
            t;
        if ((t = x >>> 16) != 0) {
            x = t;
            r += 16;
        }
        if ((t = x >> 8) != 0) {
            x = t;
            r += 8;
        }
        if ((t = x >> 4) != 0) {
            x = t;
            r += 4;
        }
        if ((t = x >> 2) != 0) {
            x = t;
            r += 2;
        }
        if ((t = x >> 1) != 0) {
            x = t;
            r += 1;
        }
        return r;
    }

    // (public) return the number of bits in "this"
    function bnBitLength() {
        if (this.t <= 0) return 0;
        return this.DB * (this.t - 1) + nbits(this[this.t - 1] ^ (this.s & this.DM));
    }

    // (protected) r = this << n*DB
    function bnpDLShiftTo(n, r) {
        var i;
        for (i = this.t - 1; i >= 0; --i) r[i + n] = this[i];
        for (i = n - 1; i >= 0; --i) r[i] = 0;
        r.t = this.t + n;
        r.s = this.s;
    }

    // (protected) r = this >> n*DB
    function bnpDRShiftTo(n, r) {
        for (var i = n; i < this.t; ++i) r[i - n] = this[i];
        r.t = Math.max(this.t - n, 0);
        r.s = this.s;
    }

    // (protected) r = this << n
    function bnpLShiftTo(n, r) {
        var bs = n % this.DB;
        var cbs = this.DB - bs;
        var bm = (1 << cbs) - 1;
        var ds = Math.floor(n / this.DB),
            c = (this.s << bs) & this.DM,
            i;
        for (i = this.t - 1; i >= 0; --i) {
            r[i + ds + 1] = (this[i] >> cbs) | c;
            c = (this[i] & bm) << bs;
        }
        for (i = ds - 1; i >= 0; --i) r[i] = 0;
        r[ds] = c;
        r.t = this.t + ds + 1;
        r.s = this.s;
        r.clamp();
    }

    // (protected) r = this >> n
    function bnpRShiftTo(n, r) {
        r.s = this.s;
        var ds = Math.floor(n / this.DB);
        if (ds >= this.t) {
            r.t = 0;
            return;
        }
        var bs = n % this.DB;
        var cbs = this.DB - bs;
        var bm = (1 << bs) - 1;
        r[0] = this[ds] >> bs;
        for (var i = ds + 1; i < this.t; ++i) {
            r[i - ds - 1] |= (this[i] & bm) << cbs;
            r[i - ds] = this[i] >> bs;
        }
        if (bs > 0) r[this.t - ds - 1] |= (this.s & bm) << cbs;
        r.t = this.t - ds;
        r.clamp();
    }

    // (protected) r = this - a
    function bnpSubTo(a, r) {
        var i = 0,
            c = 0,
            m = Math.min(a.t, this.t);
        while (i < m) {
            c += this[i] - a[i];
            r[i++] = c & this.DM;
            c >>= this.DB;
        }
        if (a.t < this.t) {
            c -= a.s;
            while (i < this.t) {
                c += this[i];
                r[i++] = c & this.DM;
                c >>= this.DB;
            }
            c += this.s;
        } else {
            c += this.s;
            while (i < a.t) {
                c -= a[i];
                r[i++] = c & this.DM;
                c >>= this.DB;
            }
            c -= a.s;
        }
        r.s = (c < 0) ? -1 : 0;
        if (c < -1) r[i++] = this.DV + c;
        else if (c > 0) r[i++] = c;
        r.t = i;
        r.clamp();
    }

    // (protected) r = this * a, r != this,a (HAC 14.12)
    // "this" should be the larger one if appropriate.
    function bnpMultiplyTo(a, r) {
        var x = this.abs(),
            y = a.abs();
        var i = x.t;
        r.t = i + y.t;
        while (--i >= 0) r[i] = 0;
        for (i = 0; i < y.t; ++i) r[i + x.t] = x.am(0, y[i], r, i, 0, x.t);
        r.s = 0;
        r.clamp();
        if (this.s != a.s) BigInteger.ZERO.subTo(r, r);
    }

    // (protected) r = this^2, r != this (HAC 14.16)
    function bnpSquareTo(r) {
        var x = this.abs();
        var i = r.t = 2 * x.t;
        while (--i >= 0) r[i] = 0;
        for (i = 0; i < x.t - 1; ++i) {
            var c = x.am(i, x[i], r, 2 * i, 0, 1);
            if ((r[i + x.t] += x.am(i + 1, 2 * x[i], r, 2 * i + 1, c, x.t - i - 1)) >= x.DV) {
                r[i + x.t] -= x.DV;
                r[i + x.t + 1] = 1;
            }
        }
        if (r.t > 0) r[r.t - 1] += x.am(i, x[i], r, 2 * i, 0, 1);
        r.s = 0;
        r.clamp();
    }

    // (protected) divide this by m, quotient and remainder to q, r (HAC 14.20)
    // r != q, this != m.  q or r may be null.
    function bnpDivRemTo(m, q, r) {
        var pm = m.abs();
        if (pm.t <= 0) return;
        var pt = this.abs();
        if (pt.t < pm.t) {
            if (q != null) q.fromInt(0);
            if (r != null) this.copyTo(r);
            return;
        }
        if (r == null) r = nbi();
        var y = nbi(),
            ts = this.s,
            ms = m.s;
        var nsh = this.DB - nbits(pm[pm.t - 1]); // normalize modulus
        if (nsh > 0) {
            pm.lShiftTo(nsh, y);
            pt.lShiftTo(nsh, r);
        } else {
            pm.copyTo(y);
            pt.copyTo(r);
        }
        var ys = y.t;
        var y0 = y[ys - 1];
        if (y0 == 0) return;
        var yt = y0 * (1 << this.F1) + ((ys > 1) ? y[ys - 2] >> this.F2 : 0);
        var d1 = this.FV / yt,
            d2 = (1 << this.F1) / yt,
            e = 1 << this.F2;
        var i = r.t,
            j = i - ys,
            t = (q == null) ? nbi() : q;
        y.dlShiftTo(j, t);
        if (r.compareTo(t) >= 0) {
            r[r.t++] = 1;
            r.subTo(t, r);
        }
        BigInteger.ONE.dlShiftTo(ys, t);
        t.subTo(y, y); // "negative" y so we can replace sub with am later
        while (y.t < ys) y[y.t++] = 0;
        while (--j >= 0) {
            // Estimate quotient digit
            var qd = (r[--i] == y0) ? this.DM : Math.floor(r[i] * d1 + (r[i - 1] + e) * d2);
            if ((r[i] += y.am(0, qd, r, j, 0, ys)) < qd) { // Try it out
                y.dlShiftTo(j, t);
                r.subTo(t, r);
                while (r[i] < --qd) r.subTo(t, r);
            }
        }
        if (q != null) {
            r.drShiftTo(ys, q);
            if (ts != ms) BigInteger.ZERO.subTo(q, q);
        }
        r.t = ys;
        r.clamp();
        if (nsh > 0) r.rShiftTo(nsh, r); // Denormalize remainder
        if (ts < 0) BigInteger.ZERO.subTo(r, r);
    }

    // (public) this mod a
    function bnMod(a) {
        var r = nbi();
        this.abs().divRemTo(a, null, r);
        if (this.s < 0 && r.compareTo(BigInteger.ZERO) > 0) a.subTo(r, r);
        return r;
    }

    // Modular reduction using "classic" algorithm
    function Classic(m) {
        this.m = m;
    }

    function cConvert(x) {
        if (x.s < 0 || x.compareTo(this.m) >= 0) return x.mod(this.m);
        else return x;
    }

    function cRevert(x) {
        return x;
    }

    function cReduce(x) {
        x.divRemTo(this.m, null, x);
    }

    function cMulTo(x, y, r) {
        x.multiplyTo(y, r);
        this.reduce(r);
    }

    function cSqrTo(x, r) {
        x.squareTo(r);
        this.reduce(r);
    }

    Classic.prototype.convert = cConvert;
    Classic.prototype.revert = cRevert;
    Classic.prototype.reduce = cReduce;
    Classic.prototype.mulTo = cMulTo;
    Classic.prototype.sqrTo = cSqrTo;

    // (protected) return "-1/this % 2^DB"; useful for Mont. reduction
    // justification:
    //         xy == 1 (mod m)
    //         xy =  1+km
    //   xy(2-xy) = (1+km)(1-km)
    // x[y(2-xy)] = 1-k^2m^2
    // x[y(2-xy)] == 1 (mod m^2)
    // if y is 1/x mod m, then y(2-xy) is 1/x mod m^2
    // should reduce x and y(2-xy) by m^2 at each step to keep size bounded.
    // JS multiply "overflows" differently from C/C++, so care is needed here.
    function bnpInvDigit() {
        if (this.t < 1) return 0;
        var x = this[0];
        if ((x & 1) == 0) return 0;
        var y = x & 3; // y == 1/x mod 2^2
        y = (y * (2 - (x & 0xf) * y)) & 0xf; // y == 1/x mod 2^4
        y = (y * (2 - (x & 0xff) * y)) & 0xff; // y == 1/x mod 2^8
        y = (y * (2 - (((x & 0xffff) * y) & 0xffff))) & 0xffff; // y == 1/x mod 2^16
        // last step - calculate inverse mod DV directly;
        // assumes 16 < DB <= 32 and assumes ability to handle 48-bit ints
        y = (y * (2 - x * y % this.DV)) % this.DV; // y == 1/x mod 2^dbits
        // we really want the negative inverse, and -DV < y < DV
        return (y > 0) ? this.DV - y : -y;
    }

    // Montgomery reduction
    function Montgomery(m) {
        this.m = m;
        this.mp = m.invDigit();
        this.mpl = this.mp & 0x7fff;
        this.mph = this.mp >> 15;
        this.um = (1 << (m.DB - 15)) - 1;
        this.mt2 = 2 * m.t;
    }

    // xR mod m
    function montConvert(x) {
        var r = nbi();
        x.abs().dlShiftTo(this.m.t, r);
        r.divRemTo(this.m, null, r);
        if (x.s < 0 && r.compareTo(BigInteger.ZERO) > 0) this.m.subTo(r, r);
        return r;
    }

    // x/R mod m
    function montRevert(x) {
        var r = nbi();
        x.copyTo(r);
        this.reduce(r);
        return r;
    }

    // x = x/R mod m (HAC 14.32)
    function montReduce(x) {
        while (x.t <= this.mt2) // pad x so am has enough room later
            x[x.t++] = 0;
        for (var i = 0; i < this.m.t; ++i) {
            // faster way of calculating u0 = x[i]*mp mod DV
            var j = x[i] & 0x7fff;
            var u0 = (j * this.mpl + (((j * this.mph + (x[i] >> 15) * this.mpl) & this.um) << 15)) & x.DM;
            // use am to combine the multiply-shift-add into one call
            j = i + this.m.t;
            x[j] += this.m.am(0, u0, x, i, 0, this.m.t);
            // propagate carry
            while (x[j] >= x.DV) {
                x[j] -= x.DV;
                x[++j]++;
            }
        }
        x.clamp();
        x.drShiftTo(this.m.t, x);
        if (x.compareTo(this.m) >= 0) x.subTo(this.m, x);
    }

    // r = "x^2/R mod m"; x != r
    function montSqrTo(x, r) {
        x.squareTo(r);
        this.reduce(r);
    }

    // r = "xy/R mod m"; x,y != r
    function montMulTo(x, y, r) {
        x.multiplyTo(y, r);
        this.reduce(r);
    }

    Montgomery.prototype.convert = montConvert;
    Montgomery.prototype.revert = montRevert;
    Montgomery.prototype.reduce = montReduce;
    Montgomery.prototype.mulTo = montMulTo;
    Montgomery.prototype.sqrTo = montSqrTo;

    // (protected) true iff this is even
    function bnpIsEven() {
        return ((this.t > 0) ? (this[0] & 1) : this.s) == 0;
    }

    // (protected) this^e, e < 2^32, doing sqr and mul with "r" (HAC 14.79)
    function bnpExp(e, z) {
        if (e > 0xffffffff || e < 1) return BigInteger.ONE;
        var r = nbi(),
            r2 = nbi(),
            g = z.convert(this),
            i = nbits(e) - 1;
        g.copyTo(r);
        while (--i >= 0) {
            z.sqrTo(r, r2);
            if ((e & (1 << i)) > 0) z.mulTo(r2, g, r);
            else {
                var t = r;
                r = r2;
                r2 = t;
            }
        }
        return z.revert(r);
    }

    // (public) this^e % m, 0 <= e < 2^32
    function bnModPowInt(e, m) {
        var z;
        if (e < 256 || m.isEven()) z = new Classic(m);
        else z = new Montgomery(m);
        return this.exp(e, z);
    }

    // protected
    BigInteger.prototype.copyTo = bnpCopyTo;
    BigInteger.prototype.fromInt = bnpFromInt;
    BigInteger.prototype.fromString = bnpFromString;
    BigInteger.prototype.clamp = bnpClamp;
    BigInteger.prototype.dlShiftTo = bnpDLShiftTo;
    BigInteger.prototype.drShiftTo = bnpDRShiftTo;
    BigInteger.prototype.lShiftTo = bnpLShiftTo;
    BigInteger.prototype.rShiftTo = bnpRShiftTo;
    BigInteger.prototype.subTo = bnpSubTo;
    BigInteger.prototype.multiplyTo = bnpMultiplyTo;
    BigInteger.prototype.squareTo = bnpSquareTo;
    BigInteger.prototype.divRemTo = bnpDivRemTo;
    BigInteger.prototype.invDigit = bnpInvDigit;
    BigInteger.prototype.isEven = bnpIsEven;
    BigInteger.prototype.exp = bnpExp;

    // public
    BigInteger.prototype.toString = bnToString;
    BigInteger.prototype.negate = bnNegate;
    BigInteger.prototype.abs = bnAbs;
    BigInteger.prototype.compareTo = bnCompareTo;
    BigInteger.prototype.bitLength = bnBitLength;
    BigInteger.prototype.mod = bnMod;
    BigInteger.prototype.modPowInt = bnModPowInt;

    // "constants"
    BigInteger.ZERO = nbv(0);
    BigInteger.ONE = nbv(1);

    // Copyright (c) 2005-2009  Tom Wu
    // All Rights Reserved.
    // See "LICENSE" for details.

    // Extended JavaScript BN functions, required for RSA private ops.

    // Version 1.1: new BigInteger("0", 10) returns "proper" zero
    // Version 1.2: square() API, isProbablePrime fix

    // (public)
    function bnClone() {
        var r = nbi();
        this.copyTo(r);
        return r;
    }

    // (public) return value as integer
    function bnIntValue() {
        if (this.s < 0) {
            if (this.t == 1) return this[0] - this.DV;
            else if (this.t == 0) return -1;
        } else if (this.t == 1) return this[0];
        else if (this.t == 0) return 0;
        // assumes 16 < DB < 32
        return ((this[1] & ((1 << (32 - this.DB)) - 1)) << this.DB) | this[0];
    }

    // (public) return value as byte
    function bnByteValue() {
        return (this.t == 0) ? this.s : (this[0] << 24) >> 24;
    }

    // (public) return value as short (assumes DB>=16)
    function bnShortValue() {
        return (this.t == 0) ? this.s : (this[0] << 16) >> 16;
    }

    // (protected) return x s.t. r^x < DV
    function bnpChunkSize(r) {
        return Math.floor(Math.LN2 * this.DB / Math.log(r));
    }

    // (public) 0 if this == 0, 1 if this > 0
    function bnSigNum() {
        if (this.s < 0) return -1;
        else if (this.t <= 0 || (this.t == 1 && this[0] <= 0)) return 0;
        else return 1;
    }

    // (protected) convert to radix string
    function bnpToRadix(b) {
        if (b == null) b = 10;
        if (this.signum() == 0 || b < 2 || b > 36) return "0";
        var cs = this.chunkSize(b);
        var a = Math.pow(b, cs);
        var d = nbv(a),
            y = nbi(),
            z = nbi(),
            r = "";
        this.divRemTo(d, y, z);
        while (y.signum() > 0) {
            r = (a + z.intValue()).toString(b).substr(1) + r;
            y.divRemTo(d, y, z);
        }
        return z.intValue().toString(b) + r;
    }

    // (protected) convert from radix string
    function bnpFromRadix(s, b) {
        this.fromInt(0);
        if (b == null) b = 10;
        var cs = this.chunkSize(b);
        var d = Math.pow(b, cs),
            mi = false,
            j = 0,
            w = 0;
        for (var i = 0; i < s.length; ++i) {
            var x = intAt(s, i);
            if (x < 0) {
                if (s.charAt(i) == "-" && this.signum() == 0) mi = true;
                continue;
            }
            w = b * w + x;
            if (++j >= cs) {
                this.dMultiply(d);
                this.dAddOffset(w, 0);
                j = 0;
                w = 0;
            }
        }
        if (j > 0) {
            this.dMultiply(Math.pow(b, j));
            this.dAddOffset(w, 0);
        }
        if (mi) BigInteger.ZERO.subTo(this, this);
    }

    // (protected) alternate constructor
    function bnpFromNumber(a, b, c) {
        if ("number" == typeof b) {
            // new BigInteger(int,int,RNG)
            if (a < 2) this.fromInt(1);
            else {
                this.fromNumber(a, c);
                if (!this.testBit(a - 1)) // force MSB set
                    this.bitwiseTo(BigInteger.ONE.shiftLeft(a - 1), op_or, this);
                if (this.isEven()) this.dAddOffset(1, 0); // force odd
                while (!this.isProbablePrime(b)) {
                    this.dAddOffset(2, 0);
                    if (this.bitLength() > a) this.subTo(BigInteger.ONE.shiftLeft(a - 1), this);
                }
            }
        } else {
            // new BigInteger(int,RNG)
            var x = new Array(),
                t = a & 7;
            x.length = (a >> 3) + 1;
            b.nextBytes(x);
            if (t > 0) x[0] &= ((1 << t) - 1);
            else x[0] = 0;
            this.fromString(x, 256);
        }
    }

    // (public) convert to bigendian byte array
    function bnToByteArray() {
        var i = this.t,
            r = new Array();
        r[0] = this.s;
        var p = this.DB - (i * this.DB) % 8,
            d, k = 0;
        if (i-- > 0) {
            if (p < this.DB && (d = this[i] >> p) != (this.s & this.DM) >> p)
                r[k++] = d | (this.s << (this.DB - p));
            while (i >= 0) {
                if (p < 8) {
                    d = (this[i] & ((1 << p) - 1)) << (8 - p);
                    d |= this[--i] >> (p += this.DB - 8);
                } else {
                    d = (this[i] >> (p -= 8)) & 0xff;
                    if (p <= 0) {
                        p += this.DB;
                        --i;
                    }
                }
                if ((d & 0x80) != 0) d |= -256;
                if (k == 0 && (this.s & 0x80) != (d & 0x80)) ++k;
                if (k > 0 || d != this.s) r[k++] = d;
            }
        }
        return r;
    }

    function bnEquals(a) {
        return (this.compareTo(a) == 0);
    }

    function bnMin(a) {
        return (this.compareTo(a) < 0) ? this : a;
    }

    function bnMax(a) {
        return (this.compareTo(a) > 0) ? this : a;
    }

    // (protected) r = this op a (bitwise)
    function bnpBitwiseTo(a, op, r) {
        var i, f, m = Math.min(a.t, this.t);
        for (i = 0; i < m; ++i) r[i] = op(this[i], a[i]);
        if (a.t < this.t) {
            f = a.s & this.DM;
            for (i = m; i < this.t; ++i) r[i] = op(this[i], f);
            r.t = this.t;
        } else {
            f = this.s & this.DM;
            for (i = m; i < a.t; ++i) r[i] = op(f, a[i]);
            r.t = a.t;
        }
        r.s = op(this.s, a.s);
        r.clamp();
    }

    // (public) this & a
    function op_and(x, y) {
        return x & y;
    }

    function bnAnd(a) {
        var r = nbi();
        this.bitwiseTo(a, op_and, r);
        return r;
    }

    // (public) this | a
    function op_or(x, y) {
        return x | y;
    }

    function bnOr(a) {
        var r = nbi();
        this.bitwiseTo(a, op_or, r);
        return r;
    }

    // (public) this ^ a
    function op_xor(x, y) {
        return x ^ y;
    }

    function bnXor(a) {
        var r = nbi();
        this.bitwiseTo(a, op_xor, r);
        return r;
    }

    // (public) this & ~a
    function op_andnot(x, y) {
        return x & ~y;
    }

    function bnAndNot(a) {
        var r = nbi();
        this.bitwiseTo(a, op_andnot, r);
        return r;
    }

    // (public) ~this
    function bnNot() {
        var r = nbi();
        for (var i = 0; i < this.t; ++i) r[i] = this.DM & ~this[i];
        r.t = this.t;
        r.s = ~this.s;
        return r;
    }

    // (public) this << n
    function bnShiftLeft(n) {
        var r = nbi();
        if (n < 0) this.rShiftTo(-n, r);
        else this.lShiftTo(n, r);
        return r;
    }

    // (public) this >> n
    function bnShiftRight(n) {
        var r = nbi();
        if (n < 0) this.lShiftTo(-n, r);
        else this.rShiftTo(n, r);
        return r;
    }

    // return index of lowest 1-bit in x, x < 2^31
    function lbit(x) {
        if (x == 0) return -1;
        var r = 0;
        if ((x & 0xffff) == 0) {
            x >>= 16;
            r += 16;
        }
        if ((x & 0xff) == 0) {
            x >>= 8;
            r += 8;
        }
        if ((x & 0xf) == 0) {
            x >>= 4;
            r += 4;
        }
        if ((x & 3) == 0) {
            x >>= 2;
            r += 2;
        }
        if ((x & 1) == 0) ++r;
        return r;
    }

    // (public) returns index of lowest 1-bit (or -1 if none)
    function bnGetLowestSetBit() {
        for (var i = 0; i < this.t; ++i)
            if (this[i] != 0) return i * this.DB + lbit(this[i]);
        if (this.s < 0) return this.t * this.DB;
        return -1;
    }

    // return number of 1 bits in x
    function cbit(x) {
        var r = 0;
        while (x != 0) {
            x &= x - 1;
            ++r;
        }
        return r;
    }

    // (public) return number of set bits
    function bnBitCount() {
        var r = 0,
            x = this.s & this.DM;
        for (var i = 0; i < this.t; ++i) r += cbit(this[i] ^ x);
        return r;
    }

    // (public) true iff nth bit is set
    function bnTestBit(n) {
        var j = Math.floor(n / this.DB);
        if (j >= this.t) return (this.s != 0);
        return ((this[j] & (1 << (n % this.DB))) != 0);
    }

    // (protected) this op (1<<n)
    function bnpChangeBit(n, op) {
        var r = BigInteger.ONE.shiftLeft(n);
        this.bitwiseTo(r, op, r);
        return r;
    }

    // (public) this | (1<<n)
    function bnSetBit(n) {
        return this.changeBit(n, op_or);
    }

    // (public) this & ~(1<<n)
    function bnClearBit(n) {
        return this.changeBit(n, op_andnot);
    }

    // (public) this ^ (1<<n)
    function bnFlipBit(n) {
        return this.changeBit(n, op_xor);
    }

    // (protected) r = this + a
    function bnpAddTo(a, r) {
        var i = 0,
            c = 0,
            m = Math.min(a.t, this.t);
        while (i < m) {
            c += this[i] + a[i];
            r[i++] = c & this.DM;
            c >>= this.DB;
        }
        if (a.t < this.t) {
            c += a.s;
            while (i < this.t) {
                c += this[i];
                r[i++] = c & this.DM;
                c >>= this.DB;
            }
            c += this.s;
        } else {
            c += this.s;
            while (i < a.t) {
                c += a[i];
                r[i++] = c & this.DM;
                c >>= this.DB;
            }
            c += a.s;
        }
        r.s = (c < 0) ? -1 : 0;
        if (c > 0) r[i++] = c;
        else if (c < -1) r[i++] = this.DV + c;
        r.t = i;
        r.clamp();
    }

    // (public) this + a
    function bnAdd(a) {
        var r = nbi();
        this.addTo(a, r);
        return r;
    }

    // (public) this - a
    function bnSubtract(a) {
        var r = nbi();
        this.subTo(a, r);
        return r;
    }

    // (public) this * a
    function bnMultiply(a) {
        var r = nbi();
        this.multiplyTo(a, r);
        return r;
    }

    // (public) this^2
    function bnSquare() {
        var r = nbi();
        this.squareTo(r);
        return r;
    }

    // (public) this / a
    function bnDivide(a) {
        var r = nbi();
        this.divRemTo(a, r, null);
        return r;
    }

    // (public) this % a
    function bnRemainder(a) {
        var r = nbi();
        this.divRemTo(a, null, r);
        return r;
    }

    // (public) [this/a,this%a]
    function bnDivideAndRemainder(a) {
        var q = nbi(),
            r = nbi();
        this.divRemTo(a, q, r);
        return new Array(q, r);
    }

    // (protected) this *= n, this >= 0, 1 < n < DV
    function bnpDMultiply(n) {
        this[this.t] = this.am(0, n - 1, this, 0, 0, this.t);
        ++this.t;
        this.clamp();
    }

    // (protected) this += n << w words, this >= 0
    function bnpDAddOffset(n, w) {
        if (n == 0) return;
        while (this.t <= w) this[this.t++] = 0;
        this[w] += n;
        while (this[w] >= this.DV) {
            this[w] -= this.DV;
            if (++w >= this.t) this[this.t++] = 0;
            ++this[w];
        }
    }

    // A "null" reducer
    function NullExp() {
    }

    function nNop(x) {
        return x;
    }

    function nMulTo(x, y, r) {
        x.multiplyTo(y, r);
    }

    function nSqrTo(x, r) {
        x.squareTo(r);
    }

    NullExp.prototype.convert = nNop;
    NullExp.prototype.revert = nNop;
    NullExp.prototype.mulTo = nMulTo;
    NullExp.prototype.sqrTo = nSqrTo;

    // (public) this^e
    function bnPow(e) {
        return this.exp(e, new NullExp());
    }

    // (protected) r = lower n words of "this * a", a.t <= n
    // "this" should be the larger one if appropriate.
    function bnpMultiplyLowerTo(a, n, r) {
        var i = Math.min(this.t + a.t, n);
        r.s = 0; // assumes a,this >= 0
        r.t = i;
        while (i > 0) r[--i] = 0;
        var j;
        for (j = r.t - this.t; i < j; ++i) r[i + this.t] = this.am(0, a[i], r, i, 0, this.t);
        for (j = Math.min(a.t, n); i < j; ++i) this.am(0, a[i], r, i, 0, n - i);
        r.clamp();
    }

    // (protected) r = "this * a" without lower n words, n > 0
    // "this" should be the larger one if appropriate.
    function bnpMultiplyUpperTo(a, n, r) {
        --n;
        var i = r.t = this.t + a.t - n;
        r.s = 0; // assumes a,this >= 0
        while (--i >= 0) r[i] = 0;
        for (i = Math.max(n - this.t, 0); i < a.t; ++i)
            r[this.t + i - n] = this.am(n - i, a[i], r, 0, 0, this.t + i - n);
        r.clamp();
        r.drShiftTo(1, r);
    }

    // Barrett modular reduction
    function Barrett(m) {
        // setup Barrett
        this.r2 = nbi();
        this.q3 = nbi();
        BigInteger.ONE.dlShiftTo(2 * m.t, this.r2);
        this.mu = this.r2.divide(m);
        this.m = m;
    }

    function barrettConvert(x) {
        if (x.s < 0 || x.t > 2 * this.m.t) return x.mod(this.m);
        else if (x.compareTo(this.m) < 0) return x;
        else {
            var r = nbi();
            x.copyTo(r);
            this.reduce(r);
            return r;
        }
    }

    function barrettRevert(x) {
        return x;
    }

    // x = x mod m (HAC 14.42)
    function barrettReduce(x) {
        x.drShiftTo(this.m.t - 1, this.r2);
        if (x.t > this.m.t + 1) {
            x.t = this.m.t + 1;
            x.clamp();
        }
        this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3);
        this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2);
        while (x.compareTo(this.r2) < 0) x.dAddOffset(1, this.m.t + 1);
        x.subTo(this.r2, x);
        while (x.compareTo(this.m) >= 0) x.subTo(this.m, x);
    }

    // r = x^2 mod m; x != r
    function barrettSqrTo(x, r) {
        x.squareTo(r);
        this.reduce(r);
    }

    // r = x*y mod m; x,y != r
    function barrettMulTo(x, y, r) {
        x.multiplyTo(y, r);
        this.reduce(r);
    }

    Barrett.prototype.convert = barrettConvert;
    Barrett.prototype.revert = barrettRevert;
    Barrett.prototype.reduce = barrettReduce;
    Barrett.prototype.mulTo = barrettMulTo;
    Barrett.prototype.sqrTo = barrettSqrTo;

    // (public) this^e % m (HAC 14.85)
    function bnModPow(e, m) {
        var i = e.bitLength(),
            k, r = nbv(1),
            z;
        if (i <= 0) return r;
        else if (i < 18) k = 1;
        else if (i < 48) k = 3;
        else if (i < 144) k = 4;
        else if (i < 768) k = 5;
        else k = 6;
        if (i < 8)
            z = new Classic(m);
        else if (m.isEven())
            z = new Barrett(m);
        else
            z = new Montgomery(m);

        // precomputation
        var g = new Array(),
            n = 3,
            k1 = k - 1,
            km = (1 << k) - 1;
        g[1] = z.convert(this);
        if (k > 1) {
            var g2 = nbi();
            z.sqrTo(g[1], g2);
            while (n <= km) {
                g[n] = nbi();
                z.mulTo(g2, g[n - 2], g[n]);
                n += 2;
            }
        }

        var j = e.t - 1,
            w, is1 = true,
            r2 = nbi(),
            t;
        i = nbits(e[j]) - 1;
        while (j >= 0) {
            if (i >= k1) w = (e[j] >> (i - k1)) & km;
            else {
                w = (e[j] & ((1 << (i + 1)) - 1)) << (k1 - i);
                if (j > 0) w |= e[j - 1] >> (this.DB + i - k1);
            }

            n = k;
            while ((w & 1) == 0) {
                w >>= 1;
                --n;
            }
            if ((i -= n) < 0) {
                i += this.DB;
                --j;
            }
            if (is1) { // ret == 1, don't bother squaring or multiplying it
                g[w].copyTo(r);
                is1 = false;
            } else {
                while (n > 1) {
                    z.sqrTo(r, r2);
                    z.sqrTo(r2, r);
                    n -= 2;
                }
                if (n > 0) z.sqrTo(r, r2);
                else {
                    t = r;
                    r = r2;
                    r2 = t;
                }
                z.mulTo(r2, g[w], r);
            }

            while (j >= 0 && (e[j] & (1 << i)) == 0) {
                z.sqrTo(r, r2);
                t = r;
                r = r2;
                r2 = t;
                if (--i < 0) {
                    i = this.DB - 1;
                    --j;
                }
            }
        }
        return z.revert(r);
    }

    // (public) gcd(this,a) (HAC 14.54)
    function bnGCD(a) {
        var x = (this.s < 0) ? this.negate() : this.clone();
        var y = (a.s < 0) ? a.negate() : a.clone();
        if (x.compareTo(y) < 0) {
            var t = x;
            x = y;
            y = t;
        }
        var i = x.getLowestSetBit(),
            g = y.getLowestSetBit();
        if (g < 0) return x;
        if (i < g) g = i;
        if (g > 0) {
            x.rShiftTo(g, x);
            y.rShiftTo(g, y);
        }
        while (x.signum() > 0) {
            if ((i = x.getLowestSetBit()) > 0) x.rShiftTo(i, x);
            if ((i = y.getLowestSetBit()) > 0) y.rShiftTo(i, y);
            if (x.compareTo(y) >= 0) {
                x.subTo(y, x);
                x.rShiftTo(1, x);
            } else {
                y.subTo(x, y);
                y.rShiftTo(1, y);
            }
        }
        if (g > 0) y.lShiftTo(g, y);
        return y;
    }

    // (protected) this % n, n < 2^26
    function bnpModInt(n) {
        if (n <= 0) return 0;
        var d = this.DV % n,
            r = (this.s < 0) ? n - 1 : 0;
        if (this.t > 0)
            if (d == 0) r = this[0] % n;
            else
                for (var i = this.t - 1; i >= 0; --i) r = (d * r + this[i]) % n;
        return r;
    }

    // (public) 1/this % m (HAC 14.61)
    function bnModInverse(m) {
        var ac = m.isEven();
        if ((this.isEven() && ac) || m.signum() == 0) return BigInteger.ZERO;
        var u = m.clone(),
            v = this.clone();
        var a = nbv(1),
            b = nbv(0),
            c = nbv(0),
            d = nbv(1);
        while (u.signum() != 0) {
            while (u.isEven()) {
                u.rShiftTo(1, u);
                if (ac) {
                    if (!a.isEven() || !b.isEven()) {
                        a.addTo(this, a);
                        b.subTo(m, b);
                    }
                    a.rShiftTo(1, a);
                } else if (!b.isEven()) b.subTo(m, b);
                b.rShiftTo(1, b);
            }
            while (v.isEven()) {
                v.rShiftTo(1, v);
                if (ac) {
                    if (!c.isEven() || !d.isEven()) {
                        c.addTo(this, c);
                        d.subTo(m, d);
                    }
                    c.rShiftTo(1, c);
                } else if (!d.isEven()) d.subTo(m, d);
                d.rShiftTo(1, d);
            }
            if (u.compareTo(v) >= 0) {
                u.subTo(v, u);
                if (ac) a.subTo(c, a);
                b.subTo(d, b);
            } else {
                v.subTo(u, v);
                if (ac) c.subTo(a, c);
                d.subTo(b, d);
            }
        }
        if (v.compareTo(BigInteger.ONE) != 0) return BigInteger.ZERO;
        if (d.compareTo(m) >= 0) return d.subtract(m);
        if (d.signum() < 0) d.addTo(m, d);
        else return d;
        if (d.signum() < 0) return d.add(m);
        else return d;
    }

    var lowprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997];
    var lplim = (1 << 26) / lowprimes[lowprimes.length - 1];

    // (public) test primality with certainty >= 1-.5^t
    function bnIsProbablePrime(t) {
        var i, x = this.abs();
        if (x.t == 1 && x[0] <= lowprimes[lowprimes.length - 1]) {
            for (i = 0; i < lowprimes.length; ++i)
                if (x[0] == lowprimes[i]) return true;
            return false;
        }
        if (x.isEven()) return false;
        i = 1;
        while (i < lowprimes.length) {
            var m = lowprimes[i],
                j = i + 1;
            while (j < lowprimes.length && m < lplim) m *= lowprimes[j++];
            m = x.modInt(m);
            while (i < j)
                if (m % lowprimes[i++] == 0) return false;
        }
        return x.millerRabin(t);
    }

    // (protected) true if probably prime (HAC 4.24, Miller-Rabin)
    function bnpMillerRabin(t) {
        var n1 = this.subtract(BigInteger.ONE);
        var k = n1.getLowestSetBit();
        if (k <= 0) return false;
        var r = n1.shiftRight(k);
        t = (t + 1) >> 1;
        if (t > lowprimes.length) t = lowprimes.length;
        var a = nbi();
        for (var i = 0; i < t; ++i) {
            //Pick bases at random, instead of starting at 2
            a.fromInt(lowprimes[Math.floor(Math.random() * lowprimes.length)]);
            var y = a.modPow(r, this);
            if (y.compareTo(BigInteger.ONE) != 0 && y.compareTo(n1) != 0) {
                var j = 1;
                while (j++ < k && y.compareTo(n1) != 0) {
                    y = y.modPowInt(2, this);
                    if (y.compareTo(BigInteger.ONE) == 0) return false;
                }
                if (y.compareTo(n1) != 0) return false;
            }
        }
        return true;
    }

    // protected
    BigInteger.prototype.chunkSize = bnpChunkSize;
    BigInteger.prototype.toRadix = bnpToRadix;
    BigInteger.prototype.fromRadix = bnpFromRadix;
    BigInteger.prototype.fromNumber = bnpFromNumber;
    BigInteger.prototype.bitwiseTo = bnpBitwiseTo;
    BigInteger.prototype.changeBit = bnpChangeBit;
    BigInteger.prototype.addTo = bnpAddTo;
    BigInteger.prototype.dMultiply = bnpDMultiply;
    BigInteger.prototype.dAddOffset = bnpDAddOffset;
    BigInteger.prototype.multiplyLowerTo = bnpMultiplyLowerTo;
    BigInteger.prototype.multiplyUpperTo = bnpMultiplyUpperTo;
    BigInteger.prototype.modInt = bnpModInt;
    BigInteger.prototype.millerRabin = bnpMillerRabin;

    // public
    BigInteger.prototype.clone = bnClone;
    BigInteger.prototype.intValue = bnIntValue;
    BigInteger.prototype.byteValue = bnByteValue;
    BigInteger.prototype.shortValue = bnShortValue;
    BigInteger.prototype.signum = bnSigNum;
    BigInteger.prototype.toByteArray = bnToByteArray;
    BigInteger.prototype.equals = bnEquals;
    BigInteger.prototype.min = bnMin;
    BigInteger.prototype.max = bnMax;
    BigInteger.prototype.and = bnAnd;
    BigInteger.prototype.or = bnOr;
    BigInteger.prototype.xor = bnXor;
    BigInteger.prototype.andNot = bnAndNot;
    BigInteger.prototype.not = bnNot;
    BigInteger.prototype.shiftLeft = bnShiftLeft;
    BigInteger.prototype.shiftRight = bnShiftRight;
    BigInteger.prototype.getLowestSetBit = bnGetLowestSetBit;
    BigInteger.prototype.bitCount = bnBitCount;
    BigInteger.prototype.testBit = bnTestBit;
    BigInteger.prototype.setBit = bnSetBit;
    BigInteger.prototype.clearBit = bnClearBit;
    BigInteger.prototype.flipBit = bnFlipBit;
    BigInteger.prototype.add = bnAdd;
    BigInteger.prototype.subtract = bnSubtract;
    BigInteger.prototype.multiply = bnMultiply;
    BigInteger.prototype.divide = bnDivide;
    BigInteger.prototype.remainder = bnRemainder;
    BigInteger.prototype.divideAndRemainder = bnDivideAndRemainder;
    BigInteger.prototype.modPow = bnModPow;
    BigInteger.prototype.modInverse = bnModInverse;
    BigInteger.prototype.pow = bnPow;
    BigInteger.prototype.gcd = bnGCD;
    BigInteger.prototype.isProbablePrime = bnIsProbablePrime;

    // JSBN-specific extension
    BigInteger.prototype.square = bnSquare;

    // BigInteger interfaces not implemented in jsbn:

    // BigInteger(int signum, byte[] magnitude)
    // double doubleValue()
    // float floatValue()
    // int hashCode()
    // long longValue()
    // static BigInteger valueOf(long val)

    // prng4.js - uses Arcfour as a PRNG

    function Arcfour() {
        this.i = 0;
        this.j = 0;
        this.S = new Array();
    }

    // Initialize arcfour context from key, an array of ints, each from [0..255]
    function ARC4init(key) {
        var i, j, t;
        for (i = 0; i < 256; ++i)
            this.S[i] = i;
        j = 0;
        for (i = 0; i < 256; ++i) {
            j = (j + this.S[i] + key[i % key.length]) & 255;
            t = this.S[i];
            this.S[i] = this.S[j];
            this.S[j] = t;
        }
        this.i = 0;
        this.j = 0;
    }

    function ARC4next() {
        var t;
        this.i = (this.i + 1) & 255;
        this.j = (this.j + this.S[this.i]) & 255;
        t = this.S[this.i];
        this.S[this.i] = this.S[this.j];
        this.S[this.j] = t;
        return this.S[(t + this.S[this.i]) & 255];
    }

    Arcfour.prototype.init = ARC4init;
    Arcfour.prototype.next = ARC4next;

    // Plug in your RNG constructor here
    function prng_newstate() {
        return new Arcfour();
    }

    // Pool size must be a multiple of 4 and greater than 32.
    // An array of bytes the size of the pool will be passed to init()
    var rng_psize = 256;

    // Random number generator - requires a PRNG backend, e.g. prng4.js
    var rng_state;
    var rng_pool;
    var rng_pptr;

    // Initialize the pool with junk if needed.
    if (rng_pool == null) {
        rng_pool = new Array();
        rng_pptr = 0;
        var t;
        if (window.crypto && window.crypto.getRandomValues) {
            // Extract entropy (2048 bits) from RNG if available
            var z = new Uint32Array(256);
            window.crypto.getRandomValues(z);
            for (t = 0; t < z.length; ++t)
                rng_pool[rng_pptr++] = z[t] & 255;
        }

        // Use mouse events for entropy, if we do not have enough entropy by the time
        // we need it, entropy will be generated by Math.random.
        var onMouseMoveListener = function (ev) {
            this.count = this.count || 0;
            if (this.count >= 256 || rng_pptr >= rng_psize) {
                if (window.removeEventListener)
                    window.removeEventListener("mousemove", onMouseMoveListener, false);
                else if (window.detachEvent)
                    window.detachEvent("onmousemove", onMouseMoveListener);
                return;
            }
            try {
                var mouseCoordinates = ev.x + ev.y;
                rng_pool[rng_pptr++] = mouseCoordinates & 255;
                this.count += 1;
            } catch (e) {
                // Sometimes Firefox will deny permission to access event properties for some reason. Ignore.
            }
        };
        if (window.addEventListener)
            window.addEventListener("mousemove", onMouseMoveListener, false);
        else if (window.attachEvent)
            window.attachEvent("onmousemove", onMouseMoveListener);

    }

    function rng_get_byte() {
        if (rng_state == null) {
            rng_state = prng_newstate();
            // At this point, we may not have collected enough entropy.  If not, fall back to Math.random
            while (rng_pptr < rng_psize) {
                var random = Math.floor(65536 * Math.random());
                rng_pool[rng_pptr++] = random & 255;
            }
            rng_state.init(rng_pool);
            for (rng_pptr = 0; rng_pptr < rng_pool.length; ++rng_pptr)
                rng_pool[rng_pptr] = 0;
            rng_pptr = 0;
        }
        // TODO: allow reseeding after first request
        return rng_state.next();
    }

    function rng_get_bytes(ba) {
        var i;
        for (i = 0; i < ba.length; ++i) ba[i] = rng_get_byte();
    }

    function SecureRandom() {
    }

    SecureRandom.prototype.nextBytes = rng_get_bytes;

    // Depends on jsbn.js and rng.js

    // Version 1.1: support utf-8 encoding in pkcs1pad2

    // convert a (hex) string to a bignum object
    function parseBigInt(str, r) {
        return new BigInteger(str, r);
    }

    function linebrk(s, n) {
        var ret = "";
        var i = 0;
        while (i + n < s.length) {
            ret += s.substring(i, i + n) + "\n";
            i += n;
        }
        return ret + s.substring(i, s.length);
    }

    function byte2Hex(b) {
        if (b < 0x10)
            return "0" + b.toString(16);
        else
            return b.toString(16);
    }

    // PKCS#1 (type 2, random) pad input string s to n bytes, and return a bigint
    function pkcs1pad2(s, n, type) {
        if (n < s.length + 11) { // TODO: fix for utf-8
            console.error("Message too long for RSA");
            return null;
        }
        var ba = new Array();
        var i = s.length - 1;
        while (i >= 0 && n > 0) {
            var c = s.charCodeAt(i--);
            if (c < 128) { // encode using utf-8
                ba[--n] = c;
            } else if ((c > 127) && (c < 2048)) {
                ba[--n] = (c & 63) | 128;
                ba[--n] = (c >> 6) | 192;
            } else {
                ba[--n] = (c & 63) | 128;
                ba[--n] = ((c >> 6) & 63) | 128;
                ba[--n] = (c >> 12) | 224;
            }
        }
        ba[--n] = 0;
        if (type == 2) {
            var rng = new SecureRandom();
            var x = new Array();
            while (n > 2) { // random non-zero pad
                x[0] = 0;
                while (x[0] == 0) rng.nextBytes(x);
                ba[--n] = x[0];
            }
        } else if (type == 0) { // zero pad
            ba[--n] = 0;
        } else {
            while (n > 2) { // fixed non-zero pad
                ba[--n] = 255;
            }
        }
        ba[--n] = type;
        ba[--n] = 0;
        return new BigInteger(ba);
    }

    // "empty" RSA key constructor
    function RSAKey() {
        this.n = null;
        this.e = 0;
        this.d = null;
        this.p = null;
        this.q = null;
        this.dmp1 = null;
        this.dmq1 = null;
        this.coeff = null;
    }

    // Set the public key fields N and e from hex strings
    function RSASetPublic(N, E) {
        if (N != null && E != null && N.length > 0 && E.length > 0) {
            this.n = parseBigInt(N, 16);
            this.e = parseInt(E, 16);
        } else
            console.error("Invalid RSA public key");
    }

    // Perform raw public operation on "x": return x^e (mod n)
    function RSADoPublic(x) {
        return x.modPowInt(this.e, this.n);
    }

    // Return the PKCS#1 RSA encryption of "text" as an even-length hex string
    function RSAPublicEncrypt(text, padding) {
        var m = pkcs1pad2(text, (this.n.bitLength() + 7) >> 3, padding); // 2
        if (m == null) return null;
        var c = this.doPublic(m);
        if (c == null) return null;
        var h = c.toString(16);
        if ((h.length & 1) == 0) return h;
        else return "0" + h;
    }

    function RSAPrivateEncrypt(text, padding) {
        var m = pkcs1pad2(text, (this.n.bitLength() + 7) >> 3, padding); // 1
        if (m == null) return null;
        var c = this.doPrivate(m);
        if (c == null) return null;
        var h = c.toString(16);
        if ((h.length & 1) == 0) return h;
        else return "0" + h;
    }

    // Return the PKCS#1 RSA encryption of "text" as a Base64-encoded string
    //function RSAEncryptB64(text) {
    //  var h = this.encrypt(text);
    //  if(h) return hex2b64(h); else return null;
    //}

    // protected
    RSAKey.prototype.doPublic = RSADoPublic;

    // public
    RSAKey.prototype.setPublic = RSASetPublic;
    RSAKey.prototype.encrypt_public = RSAPublicEncrypt;
    RSAKey.prototype.encrypt_private = RSAPrivateEncrypt;
    //RSAKey.prototype.encrypt_b64 = RSAEncryptB64;

    // Depends on rsa.js and jsbn2.js

    // Version 1.1: support utf-8 decoding in pkcs1unpad2

    // Undo PKCS#1 (type 2, random) padding and, if valid, return the plaintext
    function pkcs1unpad2(d, n, type) {
        var b = d.toByteArray();
        var i = 0;
        if (type == 0) { // zero pad
            i = -1;
        } else { // #
            while (i < b.length && b[i] == 0) ++i;
            if (b.length - i != n - 1 || b[i] != type)
                return null;
            ++i;
            while (b[i] != 0)
                if (++i >= b.length) return null;
        }
        var ret = "";
        while (++i < b.length) {
            var c = b[i] & 255;
            if (c < 128) { // utf-8 decode
                ret += String.fromCharCode(c);
            } else if ((c > 191) && (c < 224)) {
                ret += String.fromCharCode(((c & 31) << 6) | (b[i + 1] & 63));
                ++i;
            } else {
                ret += String.fromCharCode(((c & 15) << 12) | ((b[i + 1] & 63) << 6) | (b[i + 2] & 63));
                i += 2;
            }
        }
        return ret;
    }

    // Set the private key fields N, e, and d from hex strings
    function RSASetPrivate(N, E, D) {
        if (N != null && E != null && N.length > 0 && E.length > 0) {
            this.n = parseBigInt(N, 16);
            this.e = parseInt(E, 16);
            this.d = parseBigInt(D, 16);
        } else
            console.error("Invalid RSA private key");
    }

    // Set the private key fields N, e, d and CRT params from hex strings
    function RSASetPrivateEx(N, E, D, P, Q, DP, DQ, C) {
        if (N != null && E != null && N.length > 0 && E.length > 0) {
            this.n = parseBigInt(N, 16);
            this.e = parseInt(E, 16);
            this.d = parseBigInt(D, 16);
            this.p = parseBigInt(P, 16);
            this.q = parseBigInt(Q, 16);
            this.dmp1 = parseBigInt(DP, 16);
            this.dmq1 = parseBigInt(DQ, 16);
            this.coeff = parseBigInt(C, 16);
        } else
            console.error("Invalid RSA private key");
    }

    // Generate a new random private key B bits long, using public expt E
    function RSAGenerate(B, E) {
        var rng = new SecureRandom();
        var qs = B >> 1;
        this.e = parseInt(E, 16);
        var ee = new BigInteger(E, 16);
        for (; ;) {
            for (; ;) {
                this.p = new BigInteger(B - qs, 1, rng);
                if (this.p.subtract(BigInteger.ONE).gcd(ee).compareTo(BigInteger.ONE) == 0 && this.p.isProbablePrime(10)) break;
            }
            for (; ;) {
                this.q = new BigInteger(qs, 1, rng);
                if (this.q.subtract(BigInteger.ONE).gcd(ee).compareTo(BigInteger.ONE) == 0 && this.q.isProbablePrime(10)) break;
            }
            if (this.p.compareTo(this.q) <= 0) {
                var t = this.p;
                this.p = this.q;
                this.q = t;
            }
            var p1 = this.p.subtract(BigInteger.ONE);
            var q1 = this.q.subtract(BigInteger.ONE);
            var phi = p1.multiply(q1);
            if (phi.gcd(ee).compareTo(BigInteger.ONE) == 0) {
                this.n = this.p.multiply(this.q);
                this.d = ee.modInverse(phi);
                this.dmp1 = this.d.mod(p1);
                this.dmq1 = this.d.mod(q1);
                this.coeff = this.q.modInverse(this.p);
                break;
            }
        }
    }

    // Perform raw private operation on "x": return x^d (mod n)
    function RSADoPrivate(x) {
        if (this.p == null || this.q == null)
            return x.modPow(this.d, this.n);
        // TODO: re-calculate any missing CRT params
        var xp = x.mod(this.p).modPow(this.dmp1, this.p);
        var xq = x.mod(this.q).modPow(this.dmq1, this.q);

        while (xp.compareTo(xq) < 0)
            xp = xp.add(this.p);
        return xp.subtract(xq).multiply(this.coeff).mod(this.p).multiply(this.q).add(xq);
    }

    // Return the PKCS#1 RSA decryption of "ctext".
    // "ctext" is an even-length hex string and the output is a plain string.
    function RSAPrivateDecrypt(ctext, padding) {
        var c = parseBigInt(ctext, 16);
        var m = this.doPrivate(c);
        if (m == null) return null;
        return pkcs1unpad2(m, (this.n.bitLength() + 7) >> 3, padding); // 2
    }

    function RSAPublicDecrypt(ctext, padding) {
        var c = parseBigInt(ctext, 16);
        var m = this.doPublic(c);
        if (m == null) return null;
        //var unpadded = m.toString(16).replace(/^1f+00/, "");
        //console.log(m, m.toString(16), unpadded);
        return pkcs1unpad2(m, (this.n.bitLength() + 7) >> 3, padding); // 1
    }

    // Return the PKCS#1 RSA decryption of "ctext".
    // "ctext" is a Base64-encoded string and the output is a plain string.
    //function RSAB64Decrypt(ctext) {
    //  var h = b64tohex(ctext);
    //  if(h) return this.decrypt(h); else return null;
    //}

    // protected
    RSAKey.prototype.doPrivate = RSADoPrivate;

    // public
    RSAKey.prototype.setPrivate = RSASetPrivate;
    RSAKey.prototype.setPrivateEx = RSASetPrivateEx;
    RSAKey.prototype.generate = RSAGenerate;
    RSAKey.prototype.decrypt_private = RSAPrivateDecrypt;
    RSAKey.prototype.decrypt_public = RSAPublicDecrypt;
    //RSAKey.prototype.b64_decrypt = RSAB64Decrypt;

    // Copyright (c) 2011  Kevin M Burns Jr.
    // All Rights Reserved.
    // See "LICENSE" for details.
    //
    // Extension to jsbn which adds facilities for asynchronous RSA key generation
    // Primarily created to avoid execution timeout on mobile devices
    //
    // http://www-cs-students.stanford.edu/~tjw/jsbn/
    //
    // ---

    (function () {

        // Generate a new random private key B bits long, using public expt E
        var RSAGenerateAsync = function (B, E, callback) {
            //var rng = new SeededRandom();
            var rng = new SecureRandom();
            var qs = B >> 1;
            this.e = parseInt(E, 16);
            var ee = new BigInteger(E, 16);
            var rsa = this;
            // These functions have non-descript names because they were originally for(;;) loops.
            // I don't know about cryptography to give them better names than loop1-4.
            var loop1 = function () {
                var loop4 = function () {
                    if (rsa.p.compareTo(rsa.q) <= 0) {
                        var t = rsa.p;
                        rsa.p = rsa.q;
                        rsa.q = t;
                    }
                    var p1 = rsa.p.subtract(BigInteger.ONE);
                    var q1 = rsa.q.subtract(BigInteger.ONE);
                    var phi = p1.multiply(q1);
                    if (phi.gcd(ee).compareTo(BigInteger.ONE) == 0) {
                        rsa.n = rsa.p.multiply(rsa.q);
                        rsa.d = ee.modInverse(phi);
                        rsa.dmp1 = rsa.d.mod(p1);
                        rsa.dmq1 = rsa.d.mod(q1);
                        rsa.coeff = rsa.q.modInverse(rsa.p);
                        setTimeout(function () {
                            callback()
                        }, 0); // escape
                    } else {
                        setTimeout(loop1, 0);
                    }
                };
                var loop3 = function () {
                    rsa.q = nbi();
                    rsa.q.fromNumberAsync(qs, 1, rng, function () {
                        rsa.q.subtract(BigInteger.ONE).gcda(ee, function (r) {
                            if (r.compareTo(BigInteger.ONE) == 0 && rsa.q.isProbablePrime(10)) {
                                setTimeout(loop4, 0);
                            } else {
                                setTimeout(loop3, 0);
                            }
                        });
                    });
                };
                var loop2 = function () {
                    rsa.p = nbi();
                    rsa.p.fromNumberAsync(B - qs, 1, rng, function () {
                        rsa.p.subtract(BigInteger.ONE).gcda(ee, function (r) {
                            if (r.compareTo(BigInteger.ONE) == 0 && rsa.p.isProbablePrime(10)) {
                                setTimeout(loop3, 0);
                            } else {
                                setTimeout(loop2, 0);
                            }
                        });
                    });
                };
                setTimeout(loop2, 0);
            };
            setTimeout(loop1, 0);
        };
        RSAKey.prototype.generateAsync = RSAGenerateAsync;

        // Public API method
        var bnGCDAsync = function (a, callback) {
            var x = (this.s < 0) ? this.negate() : this.clone();
            var y = (a.s < 0) ? a.negate() : a.clone();
            if (x.compareTo(y) < 0) {
                var t = x;
                x = y;
                y = t;
            }
            var i = x.getLowestSetBit(),
                g = y.getLowestSetBit();
            if (g < 0) {
                callback(x);
                return;
            }
            if (i < g) g = i;
            if (g > 0) {
                x.rShiftTo(g, x);
                y.rShiftTo(g, y);
            }
            // Workhorse of the algorithm, gets called 200 - 800 times per 512 bit keygen.
            var gcda1 = function () {
                if ((i = x.getLowestSetBit()) > 0) {
                    x.rShiftTo(i, x);
                }
                if ((i = y.getLowestSetBit()) > 0) {
                    y.rShiftTo(i, y);
                }
                if (x.compareTo(y) >= 0) {
                    x.subTo(y, x);
                    x.rShiftTo(1, x);
                } else {
                    y.subTo(x, y);
                    y.rShiftTo(1, y);
                }
                if (!(x.signum() > 0)) {
                    if (g > 0) y.lShiftTo(g, y);
                    setTimeout(function () {
                        callback(y)
                    }, 0); // escape
                } else {
                    setTimeout(gcda1, 0);
                }
            };
            setTimeout(gcda1, 10);
        };
        BigInteger.prototype.gcda = bnGCDAsync;

        // (protected) alternate constructor
        var bnpFromNumberAsync = function (a, b, c, callback) {
            if ("number" == typeof b) {
                if (a < 2) {
                    this.fromInt(1);
                } else {
                    this.fromNumber(a, c);
                    if (!this.testBit(a - 1)) {
                        this.bitwiseTo(BigInteger.ONE.shiftLeft(a - 1), op_or, this);
                    }
                    if (this.isEven()) {
                        this.dAddOffset(1, 0);
                    }
                    var bnp = this;
                    var bnpfn1 = function () {
                        bnp.dAddOffset(2, 0);
                        if (bnp.bitLength() > a) bnp.subTo(BigInteger.ONE.shiftLeft(a - 1), bnp);
                        if (bnp.isProbablePrime(b)) {
                            setTimeout(function () {
                                callback()
                            }, 0); // escape
                        } else {
                            setTimeout(bnpfn1, 0);
                        }
                    };
                    setTimeout(bnpfn1, 0);
                }
            } else {
                var x = new Array(),
                    t = a & 7;
                x.length = (a >> 3) + 1;
                b.nextBytes(x);
                if (t > 0) x[0] &= ((1 << t) - 1);
                else x[0] = 0;
                this.fromString(x, 256);
            }
        };
        BigInteger.prototype.fromNumberAsync = bnpFromNumberAsync;

    })();
    var b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var b64pad = "=";

    function hex2b64(h) {
        var i;
        var c;
        var ret = "";
        for (i = 0; i + 3 <= h.length; i += 3) {
            c = parseInt(h.substring(i, i + 3), 16);
            ret += b64map.charAt(c >> 6) + b64map.charAt(c & 63);
        }
        if (i + 1 == h.length) {
            c = parseInt(h.substring(i, i + 1), 16);
            ret += b64map.charAt(c << 2);
        } else if (i + 2 == h.length) {
            c = parseInt(h.substring(i, i + 2), 16);
            ret += b64map.charAt(c >> 2) + b64map.charAt((c & 3) << 4);
        }
        while ((ret.length & 3) > 0) ret += b64pad;
        return ret;
    }

    // convert a base64 string to hex
    function b64tohex(s) {
        var ret = ""
        var i;
        var k = 0; // b64 state, 0-3
        var slop;
        for (i = 0; i < s.length; ++i) {
            if (s.charAt(i) == b64pad) break;
            v = b64map.indexOf(s.charAt(i));
            if (v < 0) continue;
            if (k == 0) {
                ret += int2char(v >> 2);
                slop = v & 3;
                k = 1;
            } else if (k == 1) {
                ret += int2char((slop << 2) | (v >> 4));
                slop = v & 0xf;
                k = 2;
            } else if (k == 2) {
                ret += int2char(slop);
                ret += int2char(v >> 2);
                slop = v & 3;
                k = 3;
            } else {
                ret += int2char((slop << 2) | (v >> 4));
                ret += int2char(v & 0xf);
                k = 0;
            }
        }
        if (k == 1)
            ret += int2char(slop << 2);
        return ret;
    }

    // convert a base64 string to a byte/number array
    function b64toBA(s) {
        //piggyback on b64tohex for now, optimize later
        var h = b64tohex(s);
        var i;
        var a = new Array();
        for (i = 0; 2 * i < h.length; ++i) {
            a[i] = parseInt(h.substring(2 * i, 2 * i + 2), 16);
        }
        return a;
    }

    /*! asn1-1.0.2.js (c) 2013 Kenji Urushima | kjur.github.com/jsrsasign/license
     */

    var JSX = JSX || {};
    JSX.env = JSX.env || {};

    var L = JSX,
        OP = Object.prototype,
        FUNCTION_TOSTRING = '[object Function]',
        ADD = ["toString", "valueOf"];

    JSX.env.parseUA = function (agent) {

        var numberify = function (s) {
                var c = 0;
                return parseFloat(s.replace(/\./g, function () {
                    return (c++ == 1) ? '' : '.';
                }));
            },

            nav = navigator,
            o = {
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
                caja: nav && nav.cajaVersion,
                secure: false,
                os: null

            },

            ua = agent || (navigator && navigator.userAgent),
            loc = window && window.location,
            href = loc && loc.href,
            m;

        o.secure = href && (href.toLowerCase().indexOf("https") === 0);

        if (ua) {

            if ((/windows|win32/i).test(ua)) {
                o.os = 'windows';
            } else if ((/macintosh/i).test(ua)) {
                o.os = 'macintosh';
            } else if ((/rhino/i).test(ua)) {
                o.os = 'rhino';
            }
            if ((/KHTML/).test(ua)) {
                o.webkit = 1;
            }
            m = ua.match(/AppleWebKit\/([^\s]*)/);
            if (m && m[1]) {
                o.webkit = numberify(m[1]);
                if (/ Mobile\//.test(ua)) {
                    o.mobile = 'Apple'; // iPhone or iPod Touch
                    m = ua.match(/OS ([^\s]*)/);
                    if (m && m[1]) {
                        m = numberify(m[1].replace('_', '.'));
                    }
                    o.ios = m;
                    o.ipad = o.ipod = o.iphone = 0;
                    m = ua.match(/iPad|iPod|iPhone/);
                    if (m && m[0]) {
                        o[m[0].toLowerCase()] = o.ios;
                    }
                } else {
                    m = ua.match(/NokiaN[^\/]*|Android \d\.\d|webOS\/\d\.\d/);
                    if (m) {
                        o.mobile = m[0];
                    }
                    if (/webOS/.test(ua)) {
                        o.mobile = 'WebOS';
                        m = ua.match(/webOS\/([^\s]*);/);
                        if (m && m[1]) {
                            o.webos = numberify(m[1]);
                        }
                    }
                    if (/ Android/.test(ua)) {
                        o.mobile = 'Android';
                        m = ua.match(/Android ([^\s]*);/);
                        if (m && m[1]) {
                            o.android = numberify(m[1]);
                        }
                    }
                }
                m = ua.match(/Chrome\/([^\s]*)/);
                if (m && m[1]) {
                    o.chrome = numberify(m[1]); // Chrome
                } else {
                    m = ua.match(/AdobeAIR\/([^\s]*)/);
                    if (m) {
                        o.air = m[0]; // Adobe AIR 1.0 or better
                    }
                }
            }
            if (!o.webkit) {
                m = ua.match(/Opera[\s\/]([^\s]*)/);
                if (m && m[1]) {
                    o.opera = numberify(m[1]);
                    m = ua.match(/Version\/([^\s]*)/);
                    if (m && m[1]) {
                        o.opera = numberify(m[1]); // opera 10+
                    }
                    m = ua.match(/Opera Mini[^;]*/);
                    if (m) {
                        o.mobile = m[0]; // ex: Opera Mini/2.0.4509/1316
                    }
                } else { // not opera or webkit
                    m = ua.match(/MSIE\s([^;]*)/);
                    if (m && m[1]) {
                        o.ie = numberify(m[1]);
                    } else { // not opera, webkit, or ie
                        m = ua.match(/Gecko\/([^\s]*)/);
                        if (m) {
                            o.gecko = 1; // Gecko detected, look for revision
                            m = ua.match(/rv:([^\s\)]*)/);
                            if (m && m[1]) {
                                o.gecko = numberify(m[1]);
                            }
                        }
                    }
                }
            }
        }
        return o;
    };

    JSX.env.ua = JSX.env.parseUA();

    JSX.isFunction = function (o) {
        return (typeof o === 'function') || OP.toString.apply(o) === FUNCTION_TOSTRING;
    };

    JSX._IEEnumFix = (JSX.env.ua.ie) ? function (r, s) {
        var i, fname, f;
        for (i = 0; i < ADD.length; i = i + 1) {

            fname = ADD[i];
            f = s[fname];

            if (L.isFunction(f) && f != OP[fname]) {
                r[fname] = f;
            }
        }
    } : function () {
    };

    JSX.extend = function (subc, superc, overrides) {
        if (!superc || !subc) {
            throw new Error("extend failed, please check that " +
                "all dependencies are included.");
        }
        var F = function () {
            },
            i;
        F.prototype = superc.prototype;
        subc.prototype = new F();
        subc.prototype.constructor = subc;
        subc.superclass = superc.prototype;
        if (superc.prototype.constructor == OP.constructor) {
            superc.prototype.constructor = superc;
        }

        if (overrides) {
            for (i in overrides) {
                if (L.hasOwnProperty(overrides, i)) {
                    subc.prototype[i] = overrides[i];
                }
            }

            L._IEEnumFix(subc.prototype, overrides);
        }
    };

    /*
     * asn1.js - ASN.1 DER encoder classes
     *
     * Copyright (c) 2013 Kenji Urushima (kenji.urushima@gmail.com)
     *
     * This software is licensed under the terms of the MIT License.
     * http://kjur.github.com/jsrsasign/license
     *
     * The above copyright and license notice shall be
     * included in all copies or substantial portions of the Software.
     */

    /**
     * @fileOverview
     * @name asn1-1.0.js
     * @author Kenji Urushima kenji.urushima@gmail.com
     * @version 1.0.2 (2013-May-30)
     * @since 2.1
     * @license <a href="http://kjur.github.io/jsrsasign/license/">MIT License</a>
     */

    /**
     * kjur's class library name space
     * <p>
     * This name space provides following name spaces:
     * <ul>
     * <li>{@link KJUR.asn1} - ASN.1 primitive hexadecimal encoder</li>
     * <li>{@link KJUR.asn1.x509} - ASN.1 structure for X.509 certificate and CRL</li>
     * <li>{@link KJUR.crypto} - Java Cryptographic Extension(JCE) style MessageDigest/Signature
     * class and utilities</li>
     * </ul>
     * </p>
     * NOTE: Please ignore method summary and document of this namespace. This caused by a bug of jsdoc2.
     * @name KJUR
     * @namespace kjur's class library name space
     */
    if (typeof KJUR == "undefined" || !KJUR) KJUR = {};

    /**
     * kjur's ASN.1 class library name space
     * <p>
     * This is ITU-T X.690 ASN.1 DER encoder class library and
     * class structure and methods is very similar to
     * org.bouncycastle.asn1 package of
     * well known BouncyCaslte Cryptography Library.
     *
     * <h4>PROVIDING ASN.1 PRIMITIVES</h4>
     * Here are ASN.1 DER primitive classes.
     * <ul>
     * <li>{@link KJUR.asn1.DERBoolean}</li>
     * <li>{@link KJUR.asn1.DERInteger}</li>
     * <li>{@link KJUR.asn1.DERBitString}</li>
     * <li>{@link KJUR.asn1.DEROctetString}</li>
     * <li>{@link KJUR.asn1.DERNull}</li>
     * <li>{@link KJUR.asn1.DERObjectIdentifier}</li>
     * <li>{@link KJUR.asn1.DERUTF8String}</li>
     * <li>{@link KJUR.asn1.DERNumericString}</li>
     * <li>{@link KJUR.asn1.DERPrintableString}</li>
     * <li>{@link KJUR.asn1.DERTeletexString}</li>
     * <li>{@link KJUR.asn1.DERIA5String}</li>
     * <li>{@link KJUR.asn1.DERUTCTime}</li>
     * <li>{@link KJUR.asn1.DERGeneralizedTime}</li>
     * <li>{@link KJUR.asn1.DERSequence}</li>
     * <li>{@link KJUR.asn1.DERSet}</li>
     * </ul>
     *
     * <h4>OTHER ASN.1 CLASSES</h4>
     * <ul>
     * <li>{@link KJUR.asn1.ASN1Object}</li>
     * <li>{@link KJUR.asn1.DERAbstractString}</li>
     * <li>{@link KJUR.asn1.DERAbstractTime}</li>
     * <li>{@link KJUR.asn1.DERAbstractStructured}</li>
     * <li>{@link KJUR.asn1.DERTaggedObject}</li>
     * </ul>
     * </p>
     * NOTE: Please ignore method summary and document of this namespace. This caused by a bug of jsdoc2.
     * @name KJUR.asn1
     * @namespace
     */
    if (typeof KJUR.asn1 == "undefined" || !KJUR.asn1) KJUR.asn1 = {};

    /**
     * ASN1 utilities class
     * @name KJUR.asn1.ASN1Util
     * @classs ASN1 utilities class
     * @since asn1 1.0.2
     */
    KJUR.asn1.ASN1Util = new function () {
        this.integerToByteHex = function (i) {
            var h = i.toString(16);
            if ((h.length % 2) == 1) h = '0' + h;
            return h;
        };
        this.bigIntToMinTwosComplementsHex = function (bigIntegerValue) {
            var h = bigIntegerValue.toString(16);
            if (h.substr(0, 1) != '-') {
                if (h.length % 2 == 1) {
                    h = '0' + h;
                } else {
                    if (!h.match(/^[0-7]/)) {
                        h = '00' + h;
                    }
                }
            } else {
                var hPos = h.substr(1);
                var xorLen = hPos.length;
                if (xorLen % 2 == 1) {
                    xorLen += 1;
                } else {
                    if (!h.match(/^[0-7]/)) {
                        xorLen += 2;
                    }
                }
                var hMask = '';
                for (var i = 0; i < xorLen; i++) {
                    hMask += 'f';
                }
                var biMask = new BigInteger(hMask, 16);
                var biNeg = biMask.xor(bigIntegerValue).add(BigInteger.ONE);
                h = biNeg.toString(16).replace(/^-/, '');
            }
            return h;
        };
        /**
         * get PEM string from hexadecimal data and header string
         * @name getPEMStringFromHex
         * @memberOf KJUR.asn1.ASN1Util
         * @function
         * @param {String} dataHex hexadecimal string of PEM body
         * @param {String} pemHeader PEM header string (ex. 'RSA PRIVATE KEY')
         * @return {String} PEM formatted string of input data
         * @description
         * @example
         * var pem  = KJUR.asn1.ASN1Util.getPEMStringFromHex('616161', 'RSA PRIVATE KEY');
         * // value of pem will be:
         * -----BEGIN PRIVATE KEY-----
         * YWFh
         * -----END PRIVATE KEY-----
         */
        this.getPEMStringFromHex = function (dataHex, pemHeader) {
            var dataWA = CryptoJS.enc.Hex.parse(dataHex);

            var dataB64 = CryptoJS.enc.Base64.stringify(dataWA);
            var pemBody = dataB64.replace(/(.{64})/g, "$1\r\n");
            pemBody = pemBody.replace(/\r\n$/, '');
            return "-----BEGIN " + pemHeader + "-----\r\n" +
                pemBody +
                "\r\n-----END " + pemHeader + "-----\r\n";
        };
    };

    // ********************************************************************
    //  Abstract ASN.1 Classes
    // ********************************************************************

    // ********************************************************************

    /**
     * base class for ASN.1 DER encoder object
     * @name KJUR.asn1.ASN1Object
     * @class base class for ASN.1 DER encoder object
     * @property {Boolean} isModified flag whether internal data was changed
     * @property {String} hTLV hexadecimal string of ASN.1 TLV
     * @property {String} hT hexadecimal string of ASN.1 TLV tag(T)
     * @property {String} hL hexadecimal string of ASN.1 TLV length(L)
     * @property {String} hV hexadecimal string of ASN.1 TLV value(V)
     * @description
     */
    KJUR.asn1.ASN1Object = function () {
        var isModified = true;
        var hTLV = null;
        var hT = '00'
        var hL = '00';
        var hV = '';

        /**
         * get hexadecimal ASN.1 TLV length(L) bytes from TLV value(V)
         * @name getLengthHexFromValue
         * @memberOf KJUR.asn1.ASN1Object
         * @function
         * @return {String} hexadecimal string of ASN.1 TLV length(L)
         */
        this.getLengthHexFromValue = function () {
            if (typeof this.hV == "undefined" || this.hV == null) {
                throw "this.hV is null or undefined.";
            }
            if (this.hV.length % 2 == 1) {
                throw "value hex must be even length: n=" + hV.length + ",v=" + this.hV;
            }
            var n = this.hV.length / 2;
            var hN = n.toString(16);
            if (hN.length % 2 == 1) {
                hN = "0" + hN;
            }
            if (n < 128) {
                return hN;
            } else {
                var hNlen = hN.length / 2;
                if (hNlen > 15) {
                    throw "ASN.1 length too long to represent by 8x: n = " + n.toString(16);
                }
                var head = 128 + hNlen;
                return head.toString(16) + hN;
            }
        };

        /**
         * get hexadecimal string of ASN.1 TLV bytes
         * @name getEncodedHex
         * @memberOf KJUR.asn1.ASN1Object
         * @function
         * @return {String} hexadecimal string of ASN.1 TLV
         */
        this.getEncodedHex = function () {
            if (this.hTLV == null || this.isModified) {
                this.hV = this.getFreshValueHex();
                this.hL = this.getLengthHexFromValue();
                this.hTLV = this.hT + this.hL + this.hV;
                this.isModified = false;
                //console.error("first time: " + this.hTLV);
            }
            return this.hTLV;
        };

        /**
         * get hexadecimal string of ASN.1 TLV value(V) bytes
         * @name getValueHex
         * @memberOf KJUR.asn1.ASN1Object
         * @function
         * @return {String} hexadecimal string of ASN.1 TLV value(V) bytes
         */
        this.getValueHex = function () {
            this.getEncodedHex();
            return this.hV;
        }

        this.getFreshValueHex = function () {
            return '';
        };
    };

    // == BEGIN DERAbstractString ================================================
    /**
     * base class for ASN.1 DER string classes
     * @name KJUR.asn1.DERAbstractString
     * @class base class for ASN.1 DER string classes
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @property {String} s internal string of value
     * @extends KJUR.asn1.ASN1Object
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>str - specify initial ASN.1 value(V) by a string</li>
     * <li>hex - specify initial ASN.1 value(V) by a hexadecimal string</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERAbstractString = function (params) {
        KJUR.asn1.DERAbstractString.superclass.constructor.call(this);
        var s = null;
        var hV = null;

        /**
         * get string value of this string object
         * @name getString
         * @memberOf KJUR.asn1.DERAbstractString
         * @function
         * @return {String} string value of this string object
         */
        this.getString = function () {
            return this.s;
        };

        /**
         * set value by a string
         * @name setString
         * @memberOf KJUR.asn1.DERAbstractString
         * @function
         * @param {String} newS value by a string to set
         */
        this.setString = function (newS) {
            this.hTLV = null;
            this.isModified = true;
            this.s = newS;
            this.hV = stohex(this.s);
        };

        /**
         * set value by a hexadecimal string
         * @name setStringHex
         * @memberOf KJUR.asn1.DERAbstractString
         * @function
         * @param {String} newHexString value by a hexadecimal string to set
         */
        this.setStringHex = function (newHexString) {
            this.hTLV = null;
            this.isModified = true;
            this.s = null;
            this.hV = newHexString;
        };

        this.getFreshValueHex = function () {
            return this.hV;
        };

        if (typeof params != "undefined") {
            if (typeof params['str'] != "undefined") {
                this.setString(params['str']);
            } else if (typeof params['hex'] != "undefined") {
                this.setStringHex(params['hex']);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERAbstractString, KJUR.asn1.ASN1Object);
    // == END   DERAbstractString ================================================

    // == BEGIN DERAbstractTime ==================================================
    /**
     * base class for ASN.1 DER Generalized/UTCTime class
     * @name KJUR.asn1.DERAbstractTime
     * @class base class for ASN.1 DER Generalized/UTCTime class
     * @param {Array} params associative array of parameters (ex. {'str': '130430235959Z'})
     * @extends KJUR.asn1.ASN1Object
     * @description
     * @see KJUR.asn1.ASN1Object - superclass
     */
    KJUR.asn1.DERAbstractTime = function (params) {
        KJUR.asn1.DERAbstractTime.superclass.constructor.call(this);
        var s = null;
        var date = null;

        // --- PRIVATE METHODS --------------------
        this.localDateToUTC = function (d) {
            utc = d.getTime() + (d.getTimezoneOffset() * 60000);
            var utcDate = new Date(utc);
            return utcDate;
        };

        this.formatDate = function (dateObject, type) {
            var pad = this.zeroPadding;
            var d = this.localDateToUTC(dateObject);
            var year = String(d.getFullYear());
            if (type == 'utc') year = year.substr(2, 2);
            var month = pad(String(d.getMonth() + 1), 2);
            var day = pad(String(d.getDate()), 2);
            var hour = pad(String(d.getHours()), 2);
            var min = pad(String(d.getMinutes()), 2);
            var sec = pad(String(d.getSeconds()), 2);
            return year + month + day + hour + min + sec + 'Z';
        };

        this.zeroPadding = function (s, len) {
            if (s.length >= len) return s;
            return new Array(len - s.length + 1).join('0') + s;
        };

        // --- PUBLIC METHODS --------------------
        /**
         * get string value of this string object
         * @name getString
         * @memberOf KJUR.asn1.DERAbstractTime
         * @function
         * @return {String} string value of this time object
         */
        this.getString = function () {
            return this.s;
        };

        /**
         * set value by a string
         * @name setString
         * @memberOf KJUR.asn1.DERAbstractTime
         * @function
         * @param {String} newS value by a string to set such like "130430235959Z"
         */
        this.setString = function (newS) {
            this.hTLV = null;
            this.isModified = true;
            this.s = newS;
            this.hV = stohex(this.s);
        };

        /**
         * set value by a Date object
         * @name setByDateValue
         * @memberOf KJUR.asn1.DERAbstractTime
         * @function
         * @param {Integer} year year of date (ex. 2013)
         * @param {Integer} month month of date between 1 and 12 (ex. 12)
         * @param {Integer} day day of month
         * @param {Integer} hour hours of date
         * @param {Integer} min minutes of date
         * @param {Integer} sec seconds of date
         */
        this.setByDateValue = function (year, month, day, hour, min, sec) {
            var dateObject = new Date(Date.UTC(year, month - 1, day, hour, min, sec, 0));
            this.setByDate(dateObject);
        };

        this.getFreshValueHex = function () {
            return this.hV;
        };
    };
    JSX.extend(KJUR.asn1.DERAbstractTime, KJUR.asn1.ASN1Object);
    // == END   DERAbstractTime ==================================================

    // == BEGIN DERAbstractStructured ============================================
    /**
     * base class for ASN.1 DER structured class
     * @name KJUR.asn1.DERAbstractStructured
     * @class base class for ASN.1 DER structured class
     * @property {Array} asn1Array internal array of ASN1Object
     * @extends KJUR.asn1.ASN1Object
     * @description
     * @see KJUR.asn1.ASN1Object - superclass
     */
    KJUR.asn1.DERAbstractStructured = function (params) {
        KJUR.asn1.DERAbstractString.superclass.constructor.call(this);
        var asn1Array = null;

        /**
         * set value by array of ASN1Object
         * @name setByASN1ObjectArray
         * @memberOf KJUR.asn1.DERAbstractStructured
         * @function
         * @param {array} asn1ObjectArray array of ASN1Object to set
         */
        this.setByASN1ObjectArray = function (asn1ObjectArray) {
            this.hTLV = null;
            this.isModified = true;
            this.asn1Array = asn1ObjectArray;
        };

        /**
         * append an ASN1Object to internal array
         * @name appendASN1Object
         * @memberOf KJUR.asn1.DERAbstractStructured
         * @function
         * @param {ASN1Object} asn1Object to add
         */
        this.appendASN1Object = function (asn1Object) {
            this.hTLV = null;
            this.isModified = true;
            this.asn1Array.push(asn1Object);
        };

        this.asn1Array = new Array();
        if (typeof params != "undefined") {
            if (typeof params['array'] != "undefined") {
                this.asn1Array = params['array'];
            }
        }
    };
    JSX.extend(KJUR.asn1.DERAbstractStructured, KJUR.asn1.ASN1Object);


    // ********************************************************************
    //  ASN.1 Object Classes
    // ********************************************************************

    // ********************************************************************
    /**
     * class for ASN.1 DER Boolean
     * @name KJUR.asn1.DERBoolean
     * @class class for ASN.1 DER Boolean
     * @extends KJUR.asn1.ASN1Object
     * @description
     * @see KJUR.asn1.ASN1Object - superclass
     */
    KJUR.asn1.DERBoolean = function () {
        KJUR.asn1.DERBoolean.superclass.constructor.call(this);
        this.hT = "01";
        this.hTLV = "0101ff";
    };
    JSX.extend(KJUR.asn1.DERBoolean, KJUR.asn1.ASN1Object);

    // ********************************************************************
    /**
     * class for ASN.1 DER Integer
     * @name KJUR.asn1.DERInteger
     * @class class for ASN.1 DER Integer
     * @extends KJUR.asn1.ASN1Object
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>int - specify initial ASN.1 value(V) by integer value</li>
     * <li>bigint - specify initial ASN.1 value(V) by BigInteger object</li>
     * <li>hex - specify initial ASN.1 value(V) by a hexadecimal string</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERInteger = function (params) {
        KJUR.asn1.DERInteger.superclass.constructor.call(this);
        this.hT = "02";

        /**
         * set value by Tom Wu's BigInteger object
         * @name setByBigInteger
         * @memberOf KJUR.asn1.DERInteger
         * @function
         * @param {BigInteger} bigIntegerValue to set
         */
        this.setByBigInteger = function (bigIntegerValue) {
            this.hTLV = null;
            this.isModified = true;
            this.hV = KJUR.asn1.ASN1Util.bigIntToMinTwosComplementsHex(bigIntegerValue);
        };

        /**
         * set value by integer value
         * @name setByInteger
         * @memberOf KJUR.asn1.DERInteger
         * @function
         * @param {Integer} integer value to set
         */
        this.setByInteger = function (intValue) {
            var bi = new BigInteger(String(intValue), 10);
            this.setByBigInteger(bi);
        };

        /**
         * set value by integer value
         * @name setValueHex
         * @memberOf KJUR.asn1.DERInteger
         * @function
         * @param {String} hexadecimal string of integer value
         * @description
         * <br/>
         * NOTE: Value shall be represented by minimum octet length of
         * two's complement representation.
         */
        this.setValueHex = function (newHexString) {
            this.hV = newHexString;
        };

        this.getFreshValueHex = function () {
            return this.hV;
        };

        if (typeof params != "undefined") {
            if (typeof params['bigint'] != "undefined") {
                this.setByBigInteger(params['bigint']);
            } else if (typeof params['int'] != "undefined") {
                this.setByInteger(params['int']);
            } else if (typeof params['hex'] != "undefined") {
                this.setValueHex(params['hex']);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERInteger, KJUR.asn1.ASN1Object);

    // ********************************************************************
    /**
     * class for ASN.1 DER encoded BitString primitive
     * @name KJUR.asn1.DERBitString
     * @class class for ASN.1 DER encoded BitString primitive
     * @extends KJUR.asn1.ASN1Object
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>bin - specify binary string (ex. '10111')</li>
     * <li>array - specify array of boolean (ex. [true,false,true,true])</li>
     * <li>hex - specify hexadecimal string of ASN.1 value(V) including unused bits</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERBitString = function (params) {
        KJUR.asn1.DERBitString.superclass.constructor.call(this);
        this.hT = "03";

        /**
         * set ASN.1 value(V) by a hexadecimal string including unused bits
         * @name setHexValueIncludingUnusedBits
         * @memberOf KJUR.asn1.DERBitString
         * @function
         * @param {String} newHexStringIncludingUnusedBits
         */
        this.setHexValueIncludingUnusedBits = function (newHexStringIncludingUnusedBits) {
            this.hTLV = null;
            this.isModified = true;
            this.hV = newHexStringIncludingUnusedBits;
        };

        /**
         * set ASN.1 value(V) by unused bit and hexadecimal string of value
         * @name setUnusedBitsAndHexValue
         * @memberOf KJUR.asn1.DERBitString
         * @function
         * @param {Integer} unusedBits
         * @param {String} hValue
         */
        this.setUnusedBitsAndHexValue = function (unusedBits, hValue) {
            if (unusedBits < 0 || 7 < unusedBits) {
                throw "unused bits shall be from 0 to 7: u = " + unusedBits;
            }
            var hUnusedBits = "0" + unusedBits;
            this.hTLV = null;
            this.isModified = true;
            this.hV = hUnusedBits + hValue;
        };

        /**
         * set ASN.1 DER BitString by binary string
         * @name setByBinaryString
         * @memberOf KJUR.asn1.DERBitString
         * @function
         * @param {String} binaryString binary value string (i.e. '10111')
         * @description
         * Its unused bits will be calculated automatically by length of
         * 'binaryValue'. <br/>
         * NOTE: Trailing zeros '0' will be ignored.
         */
        this.setByBinaryString = function (binaryString) {
            binaryString = binaryString.replace(/0+$/, '');
            var unusedBits = 8 - binaryString.length % 8;
            if (unusedBits == 8) unusedBits = 0;
            for (var i = 0; i <= unusedBits; i++) {
                binaryString += '0';
            }
            var h = '';
            for (var i = 0; i < binaryString.length - 1; i += 8) {
                var b = binaryString.substr(i, 8);
                var x = parseInt(b, 2).toString(16);
                if (x.length == 1) x = '0' + x;
                h += x;
            }
            this.hTLV = null;
            this.isModified = true;
            this.hV = '0' + unusedBits + h;
        };

        /**
         * set ASN.1 TLV value(V) by an array of boolean
         * @name setByBooleanArray
         * @memberOf KJUR.asn1.DERBitString
         * @function
         * @param {array} booleanArray array of boolean (ex. [true, false, true])
         * @description
         * NOTE: Trailing falses will be ignored.
         */
        this.setByBooleanArray = function (booleanArray) {
            var s = '';
            for (var i = 0; i < booleanArray.length; i++) {
                if (booleanArray[i] == true) {
                    s += '1';
                } else {
                    s += '0';
                }
            }
            this.setByBinaryString(s);
        };

        /**
         * generate an array of false with specified length
         * @name newFalseArray
         * @memberOf KJUR.asn1.DERBitString
         * @function
         * @param {Integer} nLength length of array to generate
         * @return {array} array of boolean faluse
         * @description
         * This static method may be useful to initialize boolean array.
         */
        this.newFalseArray = function (nLength) {
            var a = new Array(nLength);
            for (var i = 0; i < nLength; i++) {
                a[i] = false;
            }
            return a;
        };

        this.getFreshValueHex = function () {
            return this.hV;
        };

        if (typeof params != "undefined") {
            if (typeof params['hex'] != "undefined") {
                this.setHexValueIncludingUnusedBits(params['hex']);
            } else if (typeof params['bin'] != "undefined") {
                this.setByBinaryString(params['bin']);
            } else if (typeof params['array'] != "undefined") {
                this.setByBooleanArray(params['array']);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERBitString, KJUR.asn1.ASN1Object);

    // ********************************************************************
    /**
     * class for ASN.1 DER OctetString
     * @name KJUR.asn1.DEROctetString
     * @class class for ASN.1 DER OctetString
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @extends KJUR.asn1.DERAbstractString
     * @description
     * @see KJUR.asn1.DERAbstractString - superclass
     */
    KJUR.asn1.DEROctetString = function (params) {
        KJUR.asn1.DEROctetString.superclass.constructor.call(this, params);
        this.hT = "04";
    };
    JSX.extend(KJUR.asn1.DEROctetString, KJUR.asn1.DERAbstractString);

    // ********************************************************************
    /**
     * class for ASN.1 DER Null
     * @name KJUR.asn1.DERNull
     * @class class for ASN.1 DER Null
     * @extends KJUR.asn1.ASN1Object
     * @description
     * @see KJUR.asn1.ASN1Object - superclass
     */
    KJUR.asn1.DERNull = function () {
        KJUR.asn1.DERNull.superclass.constructor.call(this);
        this.hT = "05";
        this.hTLV = "0500";
    };
    JSX.extend(KJUR.asn1.DERNull, KJUR.asn1.ASN1Object);

    // ********************************************************************
    /**
     * class for ASN.1 DER ObjectIdentifier
     * @name KJUR.asn1.DERObjectIdentifier
     * @class class for ASN.1 DER ObjectIdentifier
     * @param {Array} params associative array of parameters (ex. {'oid': '2.5.4.5'})
     * @extends KJUR.asn1.ASN1Object
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>oid - specify initial ASN.1 value(V) by a oid string (ex. 2.5.4.13)</li>
     * <li>hex - specify initial ASN.1 value(V) by a hexadecimal string</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERObjectIdentifier = function (params) {
        var itox = function (i) {
            var h = i.toString(16);
            if (h.length == 1) h = '0' + h;
            return h;
        };
        var roidtox = function (roid) {
            var h = '';
            var bi = new BigInteger(roid, 10);
            var b = bi.toString(2);
            var padLen = 7 - b.length % 7;
            if (padLen == 7) padLen = 0;
            var bPad = '';
            for (var i = 0; i < padLen; i++) bPad += '0';
            b = bPad + b;
            for (var i = 0; i < b.length - 1; i += 7) {
                var b8 = b.substr(i, 7);
                if (i != b.length - 7) b8 = '1' + b8;
                h += itox(parseInt(b8, 2));
            }
            return h;
        }

        KJUR.asn1.DERObjectIdentifier.superclass.constructor.call(this);
        this.hT = "06";

        /**
         * set value by a hexadecimal string
         * @name setValueHex
         * @memberOf KJUR.asn1.DERObjectIdentifier
         * @function
         * @param {String} newHexString hexadecimal value of OID bytes
         */
        this.setValueHex = function (newHexString) {
            this.hTLV = null;
            this.isModified = true;
            this.s = null;
            this.hV = newHexString;
        };

        /**
         * set value by a OID string
         * @name setValueOidString
         * @memberOf KJUR.asn1.DERObjectIdentifier
         * @function
         * @param {String} oidString OID string (ex. 2.5.4.13)
         */
        this.setValueOidString = function (oidString) {
            if (!oidString.match(/^[0-9.]+$/)) {
                throw "malformed oid string: " + oidString;
            }
            var h = '';
            var a = oidString.split('.');
            var i0 = parseInt(a[0]) * 40 + parseInt(a[1]);
            h += itox(i0);
            a.splice(0, 2);
            for (var i = 0; i < a.length; i++) {
                h += roidtox(a[i]);
            }
            this.hTLV = null;
            this.isModified = true;
            this.s = null;
            this.hV = h;
        };

        /**
         * set value by a OID name
         * @name setValueName
         * @memberOf KJUR.asn1.DERObjectIdentifier
         * @function
         * @param {String} oidName OID name (ex. 'serverAuth')
         * @since 1.0.1
         * @description
         * OID name shall be defined in 'KJUR.asn1.x509.OID.name2oidList'.
         * Otherwise raise error.
         */
        this.setValueName = function (oidName) {
            if (typeof KJUR.asn1.x509.OID.name2oidList[oidName] != "undefined") {
                var oid = KJUR.asn1.x509.OID.name2oidList[oidName];
                this.setValueOidString(oid);
            } else {
                throw "DERObjectIdentifier oidName undefined: " + oidName;
            }
        };

        this.getFreshValueHex = function () {
            return this.hV;
        };

        if (typeof params != "undefined") {
            if (typeof params['oid'] != "undefined") {
                this.setValueOidString(params['oid']);
            } else if (typeof params['hex'] != "undefined") {
                this.setValueHex(params['hex']);
            } else if (typeof params['name'] != "undefined") {
                this.setValueName(params['name']);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERObjectIdentifier, KJUR.asn1.ASN1Object);

    // ********************************************************************
    /**
     * class for ASN.1 DER UTF8String
     * @name KJUR.asn1.DERUTF8String
     * @class class for ASN.1 DER UTF8String
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @extends KJUR.asn1.DERAbstractString
     * @description
     * @see KJUR.asn1.DERAbstractString - superclass
     */
    KJUR.asn1.DERUTF8String = function (params) {
        KJUR.asn1.DERUTF8String.superclass.constructor.call(this, params);
        this.hT = "0c";
    };
    JSX.extend(KJUR.asn1.DERUTF8String, KJUR.asn1.DERAbstractString);

    // ********************************************************************
    /**
     * class for ASN.1 DER NumericString
     * @name KJUR.asn1.DERNumericString
     * @class class for ASN.1 DER NumericString
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @extends KJUR.asn1.DERAbstractString
     * @description
     * @see KJUR.asn1.DERAbstractString - superclass
     */
    KJUR.asn1.DERNumericString = function (params) {
        KJUR.asn1.DERNumericString.superclass.constructor.call(this, params);
        this.hT = "12";
    };
    JSX.extend(KJUR.asn1.DERNumericString, KJUR.asn1.DERAbstractString);

    // ********************************************************************
    /**
     * class for ASN.1 DER PrintableString
     * @name KJUR.asn1.DERPrintableString
     * @class class for ASN.1 DER PrintableString
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @extends KJUR.asn1.DERAbstractString
     * @description
     * @see KJUR.asn1.DERAbstractString - superclass
     */
    KJUR.asn1.DERPrintableString = function (params) {
        KJUR.asn1.DERPrintableString.superclass.constructor.call(this, params);
        this.hT = "13";
    };
    JSX.extend(KJUR.asn1.DERPrintableString, KJUR.asn1.DERAbstractString);

    // ********************************************************************
    /**
     * class for ASN.1 DER TeletexString
     * @name KJUR.asn1.DERTeletexString
     * @class class for ASN.1 DER TeletexString
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @extends KJUR.asn1.DERAbstractString
     * @description
     * @see KJUR.asn1.DERAbstractString - superclass
     */
    KJUR.asn1.DERTeletexString = function (params) {
        KJUR.asn1.DERTeletexString.superclass.constructor.call(this, params);
        this.hT = "14";
    };
    JSX.extend(KJUR.asn1.DERTeletexString, KJUR.asn1.DERAbstractString);

    // ********************************************************************
    /**
     * class for ASN.1 DER IA5String
     * @name KJUR.asn1.DERIA5String
     * @class class for ASN.1 DER IA5String
     * @param {Array} params associative array of parameters (ex. {'str': 'aaa'})
     * @extends KJUR.asn1.DERAbstractString
     * @description
     * @see KJUR.asn1.DERAbstractString - superclass
     */
    KJUR.asn1.DERIA5String = function (params) {
        KJUR.asn1.DERIA5String.superclass.constructor.call(this, params);
        this.hT = "16";
    };
    JSX.extend(KJUR.asn1.DERIA5String, KJUR.asn1.DERAbstractString);

    // ********************************************************************
    /**
     * class for ASN.1 DER UTCTime
     * @name KJUR.asn1.DERUTCTime
     * @class class for ASN.1 DER UTCTime
     * @param {Array} params associative array of parameters (ex. {'str': '130430235959Z'})
     * @extends KJUR.asn1.DERAbstractTime
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>str - specify initial ASN.1 value(V) by a string (ex.'130430235959Z')</li>
     * <li>hex - specify initial ASN.1 value(V) by a hexadecimal string</li>
     * <li>date - specify Date object.</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     * <h4>EXAMPLES</h4>
     * @example
     * var d1 = new KJUR.asn1.DERUTCTime();
     * d1.setString('130430125959Z');
     *
     * var d2 = new KJUR.asn1.DERUTCTime({'str': '130430125959Z'});
     *
     * var d3 = new KJUR.asn1.DERUTCTime({'date': new Date(Date.UTC(2015, 0, 31, 0, 0, 0, 0))});
     */
    KJUR.asn1.DERUTCTime = function (params) {
        KJUR.asn1.DERUTCTime.superclass.constructor.call(this, params);
        this.hT = "17";

        /**
         * set value by a Date object
         * @name setByDate
         * @memberOf KJUR.asn1.DERUTCTime
         * @function
         * @param {Date} dateObject Date object to set ASN.1 value(V)
         */
        this.setByDate = function (dateObject) {
            this.hTLV = null;
            this.isModified = true;
            this.date = dateObject;
            this.s = this.formatDate(this.date, 'utc');
            this.hV = stohex(this.s);
        };

        if (typeof params != "undefined") {
            if (typeof params['str'] != "undefined") {
                this.setString(params['str']);
            } else if (typeof params['hex'] != "undefined") {
                this.setStringHex(params['hex']);
            } else if (typeof params['date'] != "undefined") {
                this.setByDate(params['date']);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERUTCTime, KJUR.asn1.DERAbstractTime);

    // ********************************************************************
    /**
     * class for ASN.1 DER GeneralizedTime
     * @name KJUR.asn1.DERGeneralizedTime
     * @class class for ASN.1 DER GeneralizedTime
     * @param {Array} params associative array of parameters (ex. {'str': '20130430235959Z'})
     * @extends KJUR.asn1.DERAbstractTime
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>str - specify initial ASN.1 value(V) by a string (ex.'20130430235959Z')</li>
     * <li>hex - specify initial ASN.1 value(V) by a hexadecimal string</li>
     * <li>date - specify Date object.</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERGeneralizedTime = function (params) {
        KJUR.asn1.DERGeneralizedTime.superclass.constructor.call(this, params);
        this.hT = "18";

        /**
         * set value by a Date object
         * @name setByDate
         * @memberOf KJUR.asn1.DERGeneralizedTime
         * @function
         * @param {Date} dateObject Date object to set ASN.1 value(V)
         * @example
         * When you specify UTC time, use 'Date.UTC' method like this:<br/>
         * var o = new DERUTCTime();
         * var date = new Date(Date.UTC(2015, 0, 31, 23, 59, 59, 0)); #2015JAN31 23:59:59
         * o.setByDate(date);
         */
        this.setByDate = function (dateObject) {
            this.hTLV = null;
            this.isModified = true;
            this.date = dateObject;
            this.s = this.formatDate(this.date, 'gen');
            this.hV = stohex(this.s);
        };

        if (typeof params != "undefined") {
            if (typeof params['str'] != "undefined") {
                this.setString(params['str']);
            } else if (typeof params['hex'] != "undefined") {
                this.setStringHex(params['hex']);
            } else if (typeof params['date'] != "undefined") {
                this.setByDate(params['date']);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERGeneralizedTime, KJUR.asn1.DERAbstractTime);

    // ********************************************************************
    /**
     * class for ASN.1 DER Sequence
     * @name KJUR.asn1.DERSequence
     * @class class for ASN.1 DER Sequence
     * @extends KJUR.asn1.DERAbstractStructured
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>array - specify array of ASN1Object to set elements of content</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERSequence = function (params) {
        KJUR.asn1.DERSequence.superclass.constructor.call(this, params);
        this.hT = "30";
        this.getFreshValueHex = function () {
            var h = '';
            for (var i = 0; i < this.asn1Array.length; i++) {
                var asn1Obj = this.asn1Array[i];
                h += asn1Obj.getEncodedHex();
            }
            this.hV = h;
            return this.hV;
        };
    };
    JSX.extend(KJUR.asn1.DERSequence, KJUR.asn1.DERAbstractStructured);

    // ********************************************************************
    /**
     * class for ASN.1 DER Set
     * @name KJUR.asn1.DERSet
     * @class class for ASN.1 DER Set
     * @extends KJUR.asn1.DERAbstractStructured
     * @description
     * <br/>
     * As for argument 'params' for constructor, you can specify one of
     * following properties:
     * <ul>
     * <li>array - specify array of ASN1Object to set elements of content</li>
     * </ul>
     * NOTE: 'params' can be omitted.
     */
    KJUR.asn1.DERSet = function (params) {
        KJUR.asn1.DERSet.superclass.constructor.call(this, params);
        this.hT = "31";
        this.getFreshValueHex = function () {
            var a = new Array();
            for (var i = 0; i < this.asn1Array.length; i++) {
                var asn1Obj = this.asn1Array[i];
                a.push(asn1Obj.getEncodedHex());
            }
            a.sort();
            this.hV = a.join('');
            return this.hV;
        };
    };
    JSX.extend(KJUR.asn1.DERSet, KJUR.asn1.DERAbstractStructured);

    // ********************************************************************
    /**
     * class for ASN.1 DER TaggedObject
     * @name KJUR.asn1.DERTaggedObject
     * @class class for ASN.1 DER TaggedObject
     * @extends KJUR.asn1.ASN1Object
     * @description
     * <br/>
     * Parameter 'tagNoNex' is ASN.1 tag(T) value for this object.
     * For example, if you find '[1]' tag in a ASN.1 dump,
     * 'tagNoHex' will be 'a1'.
     * <br/>
     * As for optional argument 'params' for constructor, you can specify *ANY* of
     * following properties:
     * <ul>
     * <li>explicit - specify true if this is explicit tag otherwise false
     *     (default is 'true').</li>
     * <li>tag - specify tag (default is 'a0' which means [0])</li>
     * <li>obj - specify ASN1Object which is tagged</li>
     * </ul>
     * @example
     * d1 = new KJUR.asn1.DERUTF8String({'str':'a'});
     * d2 = new KJUR.asn1.DERTaggedObject({'obj': d1});
     * hex = d2.getEncodedHex();
     */
    KJUR.asn1.DERTaggedObject = function (params) {
        KJUR.asn1.DERTaggedObject.superclass.constructor.call(this);
        this.hT = "a0";
        this.hV = '';
        this.isExplicit = true;
        this.asn1Object = null;

        /**
         * set value by an ASN1Object
         * @name setString
         * @memberOf KJUR.asn1.DERTaggedObject
         * @function
         * @param {Boolean} isExplicitFlag flag for explicit/implicit tag
         * @param {Integer} tagNoHex hexadecimal string of ASN.1 tag
         * @param {ASN1Object} asn1Object ASN.1 to encapsulate
         */
        this.setASN1Object = function (isExplicitFlag, tagNoHex, asn1Object) {
            this.hT = tagNoHex;
            this.isExplicit = isExplicitFlag;
            this.asn1Object = asn1Object;
            if (this.isExplicit) {
                this.hV = this.asn1Object.getEncodedHex();
                this.hTLV = null;
                this.isModified = true;
            } else {
                this.hV = null;
                this.hTLV = asn1Object.getEncodedHex();
                this.hTLV = this.hTLV.replace(/^../, tagNoHex);
                this.isModified = false;
            }
        };

        this.getFreshValueHex = function () {
            return this.hV;
        };

        if (typeof params != "undefined") {
            if (typeof params['tag'] != "undefined") {
                this.hT = params['tag'];
            }
            if (typeof params['explicit'] != "undefined") {
                this.isExplicit = params['explicit'];
            }
            if (typeof params['obj'] != "undefined") {
                this.asn1Object = params['obj'];
                this.setASN1Object(this.isExplicit, this.hT, this.asn1Object);
            }
        }
    };
    JSX.extend(KJUR.asn1.DERTaggedObject, KJUR.asn1.ASN1Object);
    // Hex JavaScript decoder
    // Copyright (c) 2008-2013 Lapo Luchini <lapo@lapo.it>

    // Permission to use, copy, modify, and/or distribute this software for any
    // purpose with or without fee is hereby granted, provided that the above
    // copyright notice and this permission notice appear in all copies.
    //
    // THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    // WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    // MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    // ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    // WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    // ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    // OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

    /*jshint browser: true, strict: true, immed: true, latedef: true, undef: true, regexdash: false */
    (function (undefined) {
        "use strict";

        var Hex = {},
            decoder;

        Hex.decode = function (a) {
            var i;
            if (decoder === undefined) {
                var hex = "0123456789ABCDEF",
                    ignore = " \f\n\r\t\u00A0\u2028\u2029";
                decoder = [];
                for (i = 0; i < 16; ++i)
                    decoder[hex.charAt(i)] = i;
                hex = hex.toLowerCase();
                for (i = 10; i < 16; ++i)
                    decoder[hex.charAt(i)] = i;
                for (i = 0; i < ignore.length; ++i)
                    decoder[ignore.charAt(i)] = -1;
            }
            var out = [],
                bits = 0,
                char_count = 0;
            for (i = 0; i < a.length; ++i) {
                var c = a.charAt(i);
                if (c == '=')
                    break;
                c = decoder[c];
                if (c == -1)
                    continue;
                if (c === undefined)
                    throw 'Illegal character at offset ' + i;
                bits |= c;
                if (++char_count >= 2) {
                    out[out.length] = bits;
                    bits = 0;
                    char_count = 0;
                } else {
                    bits <<= 4;
                }
            }
            if (char_count)
                throw "Hex encoding incomplete: 4 bits missing";
            return out;
        };

        // export globals
        window.Hex = Hex;
    })();
    // Base64 JavaScript decoder
    // Copyright (c) 2008-2013 Lapo Luchini <lapo@lapo.it>

    // Permission to use, copy, modify, and/or distribute this software for any
    // purpose with or without fee is hereby granted, provided that the above
    // copyright notice and this permission notice appear in all copies.
    //
    // THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    // WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    // MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    // ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    // WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    // ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    // OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

    /*jshint browser: true, strict: true, immed: true, latedef: true, undef: true, regexdash: false */
    (function (undefined) {
        "use strict";

        var Base64 = {},
            decoder;

        Base64.decode = function (a) {
            var i;
            if (decoder === undefined) {
                var b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
                    ignore = "= \f\n\r\t\u00A0\u2028\u2029";
                decoder = [];
                for (i = 0; i < 64; ++i)
                    decoder[b64.charAt(i)] = i;
                for (i = 0; i < ignore.length; ++i)
                    decoder[ignore.charAt(i)] = -1;
            }
            var out = [];
            var bits = 0,
                char_count = 0;
            for (i = 0; i < a.length; ++i) {
                var c = a.charAt(i);
                if (c == '=')
                    break;
                c = decoder[c];
                if (c == -1)
                    continue;
                if (c === undefined)
                    throw 'Illegal character at offset ' + i;
                bits |= c;
                if (++char_count >= 4) {
                    out[out.length] = (bits >> 16);
                    out[out.length] = (bits >> 8) & 0xFF;
                    out[out.length] = bits & 0xFF;
                    bits = 0;
                    char_count = 0;
                } else {
                    bits <<= 6;
                }
            }
            switch (char_count) {
                case 1:
                    throw "Base64 encoding incomplete: at least 2 bits missing";
                case 2:
                    out[out.length] = (bits >> 10);
                    break;
                case 3:
                    out[out.length] = (bits >> 16);
                    out[out.length] = (bits >> 8) & 0xFF;
                    break;
            }
            return out;
        };

        Base64.re = /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/;
        Base64.unarmor = function (a) {
            var m = Base64.re.exec(a);
            if (m) {
                if (m[1])
                    a = m[1];
                else if (m[2])
                    a = m[2];
                else
                    throw "RegExp out of sync";
            }
            return Base64.decode(a);
        };

        // export globals
        window.Base64 = Base64;
    })();
    // ASN.1 JavaScript decoder
    // Copyright (c) 2008-2013 Lapo Luchini <lapo@lapo.it>

    // Permission to use, copy, modify, and/or distribute this software for any
    // purpose with or without fee is hereby granted, provided that the above
    // copyright notice and this permission notice appear in all copies.
    //
    // THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    // WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    // MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    // ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    // WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    // ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    // OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

    /*jshint browser: true, strict: true, immed: true, latedef: true, undef: true, regexdash: false */
    /*global oids */
    (function (undefined) {
        "use strict";

        var hardLimit = 100,
            ellipsis = "\u2026",
            DOM = {
                tag: function (tagName, className) {
                    var t = document.createElement(tagName);
                    t.className = className;
                    return t;
                },
                text: function (str) {
                    return document.createTextNode(str);
                }
            };

        function Stream(enc, pos) {
            if (enc instanceof Stream) {
                this.enc = enc.enc;
                this.pos = enc.pos;
            } else {
                this.enc = enc;
                this.pos = pos;
            }
        }

        Stream.prototype.get = function (pos) {
            if (pos === undefined)
                pos = this.pos++;
            if (pos >= this.enc.length)
                throw 'Requesting byte offset ' + pos + ' on a stream of length ' + this.enc.length;
            return this.enc[pos];
        };
        Stream.prototype.hexDigits = "0123456789ABCDEF";
        Stream.prototype.hexByte = function (b) {
            return this.hexDigits.charAt((b >> 4) & 0xF) + this.hexDigits.charAt(b & 0xF);
        };
        Stream.prototype.hexDump = function (start, end, raw) {
            var s = "";
            for (var i = start; i < end; ++i) {
                s += this.hexByte(this.get(i));
                if (raw !== true)
                    switch (i & 0xF) {
                        case 0x7:
                            s += "  ";
                            break;
                        case 0xF:
                            s += "\n";
                            break;
                        default:
                            s += " ";
                    }
            }
            return s;
        };
        Stream.prototype.parseStringISO = function (start, end) {
            var s = "";
            for (var i = start; i < end; ++i)
                s += String.fromCharCode(this.get(i));
            return s;
        };
        Stream.prototype.parseStringUTF = function (start, end) {
            var s = "";
            for (var i = start; i < end;) {
                var c = this.get(i++);
                if (c < 128)
                    s += String.fromCharCode(c);
                else if ((c > 191) && (c < 224))
                    s += String.fromCharCode(((c & 0x1F) << 6) | (this.get(i++) & 0x3F));
                else
                    s += String.fromCharCode(((c & 0x0F) << 12) | ((this.get(i++) & 0x3F) << 6) | (this.get(i++) & 0x3F));
            }
            return s;
        };
        Stream.prototype.parseStringBMP = function (start, end) {
            var str = ""
            for (var i = start; i < end; i += 2) {
                var high_byte = this.get(i);
                var low_byte = this.get(i + 1);
                str += String.fromCharCode((high_byte << 8) + low_byte);
            }

            return str;
        };
        Stream.prototype.reTime = /^((?:1[89]|2\d)?\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/;
        Stream.prototype.parseTime = function (start, end) {
            var s = this.parseStringISO(start, end),
                m = this.reTime.exec(s);
            if (!m)
                return "Unrecognized time: " + s;
            s = m[1] + "-" + m[2] + "-" + m[3] + " " + m[4];
            if (m[5]) {
                s += ":" + m[5];
                if (m[6]) {
                    s += ":" + m[6];
                    if (m[7])
                        s += "." + m[7];
                }
            }
            if (m[8]) {
                s += " UTC";
                if (m[8] != 'Z') {
                    s += m[8];
                    if (m[9])
                        s += ":" + m[9];
                }
            }
            return s;
        };
        Stream.prototype.parseInteger = function (start, end) {
            //TODO support negative numbers
            var len = end - start;
            if (len > 4) {
                len <<= 3;
                var s = this.get(start);
                if (s === 0)
                    len -= 8;
                else
                    while (s < 128) {
                        s <<= 1;
                        --len;
                    }
                return "(" + len + " bit)";
            }
            var n = 0;
            for (var i = start; i < end; ++i)
                n = (n << 8) | this.get(i);
            return n;
        };
        Stream.prototype.parseBitString = function (start, end) {
            var unusedBit = this.get(start),
                lenBit = ((end - start - 1) << 3) - unusedBit,
                s = "(" + lenBit + " bit)";
            if (lenBit <= 20) {
                var skip = unusedBit;
                s += " ";
                for (var i = end - 1; i > start; --i) {
                    var b = this.get(i);
                    for (var j = skip; j < 8; ++j)
                        s += (b >> j) & 1 ? "1" : "0";
                    skip = 0;
                }
            }
            return s;
        };
        Stream.prototype.parseOctetString = function (start, end) {
            var len = end - start,
                s = "(" + len + " byte) ";
            if (len > hardLimit)
                end = start + hardLimit;
            for (var i = start; i < end; ++i)
                s += this.hexByte(this.get(i)); //TODO: also try Latin1?
            if (len > hardLimit)
                s += ellipsis;
            return s;
        };
        Stream.prototype.parseOID = function (start, end) {
            var s = '',
                n = 0,
                bits = 0;
            for (var i = start; i < end; ++i) {
                var v = this.get(i);
                n = (n << 7) | (v & 0x7F);
                bits += 7;
                if (!(v & 0x80)) { // finished
                    if (s === '') {
                        var m = n < 80 ? n < 40 ? 0 : 1 : 2;
                        s = m + "." + (n - m * 40);
                    } else
                        s += "." + ((bits >= 31) ? "bigint" : n);
                    n = bits = 0;
                }
            }
            return s;
        };

        function ASN1(stream, header, length, tag, sub) {
            this.stream = stream;
            this.header = header;
            this.length = length;
            this.tag = tag;
            this.sub = sub;
        }

        ASN1.prototype.typeName = function () {
            if (this.tag === undefined)
                return "unknown";
            var tagClass = this.tag >> 6,
                tagConstructed = (this.tag >> 5) & 1,
                tagNumber = this.tag & 0x1F;
            switch (tagClass) {
                case 0: // universal
                    switch (tagNumber) {
                        case 0x00:
                            return "EOC";
                        case 0x01:
                            return "BOOLEAN";
                        case 0x02:
                            return "INTEGER";
                        case 0x03:
                            return "BIT_STRING";
                        case 0x04:
                            return "OCTET_STRING";
                        case 0x05:
                            return "NULL";
                        case 0x06:
                            return "OBJECT_IDENTIFIER";
                        case 0x07:
                            return "ObjectDescriptor";
                        case 0x08:
                            return "EXTERNAL";
                        case 0x09:
                            return "REAL";
                        case 0x0A:
                            return "ENUMERATED";
                        case 0x0B:
                            return "EMBEDDED_PDV";
                        case 0x0C:
                            return "UTF8String";
                        case 0x10:
                            return "SEQUENCE";
                        case 0x11:
                            return "SET";
                        case 0x12:
                            return "NumericString";
                        case 0x13:
                            return "PrintableString"; // ASCII subset
                        case 0x14:
                            return "TeletexString"; // aka T61String
                        case 0x15:
                            return "VideotexString";
                        case 0x16:
                            return "IA5String"; // ASCII
                        case 0x17:
                            return "UTCTime";
                        case 0x18:
                            return "GeneralizedTime";
                        case 0x19:
                            return "GraphicString";
                        case 0x1A:
                            return "VisibleString"; // ASCII subset
                        case 0x1B:
                            return "GeneralString";
                        case 0x1C:
                            return "UniversalString";
                        case 0x1E:
                            return "BMPString";
                        default:
                            return "Universal_" + tagNumber.toString(16);
                    }
                case 1:
                    return "Application_" + tagNumber.toString(16);
                case 2:
                    return "[" + tagNumber + "]"; // Context
                case 3:
                    return "Private_" + tagNumber.toString(16);
            }
        };
        ASN1.prototype.reSeemsASCII = /^[ -~]+$/;
        ASN1.prototype.content = function () {
            if (this.tag === undefined)
                return null;
            var tagClass = this.tag >> 6,
                tagNumber = this.tag & 0x1F,
                content = this.posContent(),
                len = Math.abs(this.length);
            if (tagClass !== 0) { // universal
                if (this.sub !== null)
                    return "(" + this.sub.length + " elem)";
                //TODO: TRY TO PARSE ASCII STRING
                var s = this.stream.parseStringISO(content, content + Math.min(len, hardLimit));
                if (this.reSeemsASCII.test(s))
                    return s.substring(0, 2 * hardLimit) + ((s.length > 2 * hardLimit) ? ellipsis : "");
                else
                    return this.stream.parseOctetString(content, content + len);
            }
            switch (tagNumber) {
                case 0x01: // BOOLEAN
                    return (this.stream.get(content) === 0) ? "false" : "true";
                case 0x02: // INTEGER
                    return this.stream.parseInteger(content, content + len);
                case 0x03: // BIT_STRING
                    return this.sub ? "(" + this.sub.length + " elem)" :
                        this.stream.parseBitString(content, content + len);
                case 0x04: // OCTET_STRING
                    return this.sub ? "(" + this.sub.length + " elem)" :
                        this.stream.parseOctetString(content, content + len);
                //case 0x05: // NULL
                case 0x06: // OBJECT_IDENTIFIER
                    return this.stream.parseOID(content, content + len);
                //case 0x07: // ObjectDescriptor
                //case 0x08: // EXTERNAL
                //case 0x09: // REAL
                //case 0x0A: // ENUMERATED
                //case 0x0B: // EMBEDDED_PDV
                case 0x10: // SEQUENCE
                case 0x11: // SET
                    return "(" + this.sub.length + " elem)";
                case 0x0C: // UTF8String
                    return this.stream.parseStringUTF(content, content + len);
                case 0x12: // NumericString
                case 0x13: // PrintableString
                case 0x14: // TeletexString
                case 0x15: // VideotexString
                case 0x16: // IA5String
                //case 0x19: // GraphicString
                case 0x1A: // VisibleString
                    //case 0x1B: // GeneralString
                    //case 0x1C: // UniversalString
                    return this.stream.parseStringISO(content, content + len);
                case 0x1E: // BMPString
                    return this.stream.parseStringBMP(content, content + len);
                case 0x17: // UTCTime
                case 0x18: // GeneralizedTime
                    return this.stream.parseTime(content, content + len);
            }
            return null;
        };
        ASN1.prototype.toString = function () {
            return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + ((this.sub === null) ? 'null' : this.sub.length) + "]";
        };
        ASN1.prototype.print = function (indent) {
            if (indent === undefined) indent = '';
            document.writeln(indent + this);
            if (this.sub !== null) {
                indent += '  ';
                for (var i = 0, max = this.sub.length; i < max; ++i)
                    this.sub[i].print(indent);
            }
        };
        ASN1.prototype.toPrettyString = function (indent) {
            if (indent === undefined) indent = '';
            var s = indent + this.typeName() + " @" + this.stream.pos;
            if (this.length >= 0)
                s += "+";
            s += this.length;
            if (this.tag & 0x20)
                s += " (constructed)";
            else if (((this.tag == 0x03) || (this.tag == 0x04)) && (this.sub !== null))
                s += " (encapsulates)";
            s += "\n";
            if (this.sub !== null) {
                indent += '  ';
                for (var i = 0, max = this.sub.length; i < max; ++i)
                    s += this.sub[i].toPrettyString(indent);
            }
            return s;
        };
        ASN1.prototype.toDOM = function () {
            var node = DOM.tag("div", "node");
            node.asn1 = this;
            var head = DOM.tag("div", "head");
            var s = this.typeName().replace(/_/g, " ");
            head.innerHTML = s;
            var content = this.content();
            if (content !== null) {
                content = String(content).replace(/</g, "&lt;");
                var preview = DOM.tag("span", "preview");
                preview.appendChild(DOM.text(content));
                head.appendChild(preview);
            }
            node.appendChild(head);
            this.node = node;
            this.head = head;
            var value = DOM.tag("div", "value");
            s = "Offset: " + this.stream.pos + "<br/>";
            s += "Length: " + this.header + "+";
            if (this.length >= 0)
                s += this.length;
            else
                s += (-this.length) + " (undefined)";
            if (this.tag & 0x20)
                s += "<br/>(constructed)";
            else if (((this.tag == 0x03) || (this.tag == 0x04)) && (this.sub !== null))
                s += "<br/>(encapsulates)";
            //TODO if (this.tag == 0x03) s += "Unused bits: "
            if (content !== null) {
                s += "<br/>Value:<br/><b>" + content + "</b>";
                if ((typeof oids === 'object') && (this.tag == 0x06)) {
                    var oid = oids[content];
                    if (oid) {
                        if (oid.d) s += "<br/>" + oid.d;
                        if (oid.c) s += "<br/>" + oid.c;
                        if (oid.w) s += "<br/>(warning!)";
                    }
                }
            }
            value.innerHTML = s;
            node.appendChild(value);
            var sub = DOM.tag("div", "sub");
            if (this.sub !== null) {
                for (var i = 0, max = this.sub.length; i < max; ++i)
                    sub.appendChild(this.sub[i].toDOM());
            }
            node.appendChild(sub);
            head.onclick = function () {
                node.className = (node.className == "node collapsed") ? "node" : "node collapsed";
            };
            return node;
        };
        ASN1.prototype.posStart = function () {
            return this.stream.pos;
        };
        ASN1.prototype.posContent = function () {
            return this.stream.pos + this.header;
        };
        ASN1.prototype.posEnd = function () {
            return this.stream.pos + this.header + Math.abs(this.length);
        };
        ASN1.prototype.fakeHover = function (current) {
            this.node.className += " hover";
            if (current)
                this.head.className += " hover";
        };
        ASN1.prototype.fakeOut = function (current) {
            var re = / ?hover/;
            this.node.className = this.node.className.replace(re, "");
            if (current)
                this.head.className = this.head.className.replace(re, "");
        };
        ASN1.prototype.toHexDOM_sub = function (node, className, stream, start, end) {
            if (start >= end)
                return;
            var sub = DOM.tag("span", className);
            sub.appendChild(DOM.text(
                stream.hexDump(start, end)));
            node.appendChild(sub);
        };
        ASN1.prototype.toHexDOM = function (root) {
            var node = DOM.tag("span", "hex");
            if (root === undefined) root = node;
            this.head.hexNode = node;
            this.head.onmouseover = function () {
                this.hexNode.className = "hexCurrent";
            };
            this.head.onmouseout = function () {
                this.hexNode.className = "hex";
            };
            node.asn1 = this;
            node.onmouseover = function () {
                var current = !root.selected;
                if (current) {
                    root.selected = this.asn1;
                    this.className = "hexCurrent";
                }
                this.asn1.fakeHover(current);
            };
            node.onmouseout = function () {
                var current = (root.selected == this.asn1);
                this.asn1.fakeOut(current);
                if (current) {
                    root.selected = null;
                    this.className = "hex";
                }
            };
            this.toHexDOM_sub(node, "tag", this.stream, this.posStart(), this.posStart() + 1);
            this.toHexDOM_sub(node, (this.length >= 0) ? "dlen" : "ulen", this.stream, this.posStart() + 1, this.posContent());
            if (this.sub === null)
                node.appendChild(DOM.text(
                    this.stream.hexDump(this.posContent(), this.posEnd())));
            else if (this.sub.length > 0) {
                var first = this.sub[0];
                var last = this.sub[this.sub.length - 1];
                this.toHexDOM_sub(node, "intro", this.stream, this.posContent(), first.posStart());
                for (var i = 0, max = this.sub.length; i < max; ++i)
                    node.appendChild(this.sub[i].toHexDOM(root));
                this.toHexDOM_sub(node, "outro", this.stream, last.posEnd(), this.posEnd());
            }
            return node;
        };
        ASN1.prototype.toHexString = function (root) {
            return this.stream.hexDump(this.posStart(), this.posEnd(), true);
        };
        ASN1.decodeLength = function (stream) {
            var buf = stream.get(),
                len = buf & 0x7F;
            if (len == buf)
                return len;
            if (len > 3)
                throw "Length over 24 bits not supported at position " + (stream.pos - 1);
            if (len === 0)
                return -1; // undefined
            buf = 0;
            for (var i = 0; i < len; ++i)
                buf = (buf << 8) | stream.get();
            return buf;
        };
        ASN1.hasContent = function (tag, len, stream) {
            if (tag & 0x20) // constructed
                return true;
            if ((tag < 0x03) || (tag > 0x04))
                return false;
            var p = new Stream(stream);
            if (tag == 0x03) p.get(); // BitString unused bits, must be in [0, 7]
            var subTag = p.get();
            if ((subTag >> 6) & 0x01) // not (universal or context)
                return false;
            try {
                var subLength = ASN1.decodeLength(p);
                return ((p.pos - stream.pos) + subLength == len);
            } catch (exception) {
                return false;
            }
        };
        ASN1.decode = function (stream) {
            if (!(stream instanceof Stream))
                stream = new Stream(stream, 0);
            var streamStart = new Stream(stream),
                tag = stream.get(),
                len = ASN1.decodeLength(stream),
                header = stream.pos - streamStart.pos,
                sub = null;
            if (ASN1.hasContent(tag, len, stream)) {
                // it has content, so we decode it
                var start = stream.pos;
                if (tag == 0x03) stream.get(); // skip BitString unused bits, must be in [0, 7]
                sub = [];
                if (len >= 0) {
                    // definite length
                    var end = start + len;
                    while (stream.pos < end)
                        sub[sub.length] = ASN1.decode(stream);
                    if (stream.pos != end)
                        throw "Content size is not correct for container starting at offset " + start;
                } else {
                    // undefined length
                    try {
                        for (; ;) {
                            var s = ASN1.decode(stream);
                            if (s.tag === 0)
                                break;
                            sub[sub.length] = s;
                        }
                        len = start - stream.pos;
                    } catch (e) {
                        throw "Exception while decoding undefined length content: " + e;
                    }
                }
            } else
                stream.pos += len; // skip content
            return new ASN1(streamStart, header, len, tag, sub);
        };
        ASN1.test = function () {
            var test = [{
                value: [0x27],
                expected: 0x27
            }, {
                value: [0x81, 0xC9],
                expected: 0xC9
            }, {
                value: [0x83, 0xFE, 0xDC, 0xBA],
                expected: 0xFEDCBA
            }];
            for (var i = 0, max = test.length; i < max; ++i) {
                var pos = 0,
                    stream = new Stream(test[i].value, 0),
                    res = ASN1.decodeLength(stream);
                if (res != test[i].expected)
                    document.write("In test[" + i + "] expected " + test[i].expected + " got " + res + "\n");
            }
        };

        // export globals
        window.ASN1 = ASN1;
    })();
    /**
     * Retrieve the hexadecimal value (as a string) of the current ASN.1 element
     * @returns {string}
     * @public
     */
    window.ASN1.prototype.getHexStringValue = function () {
        var hexString = this.toHexString();
        var offset = this.header * 2;
        var length = this.length * 2;
        return hexString.substr(offset, length);
    };

    /**
     * Method to parse a pem encoded string containing both a public or private key.
     * The method will translate the pem encoded string in a der encoded string and
     * will parse private key and public key parameters. This method accepts public key
     * in the rsaencryption pkcs #1 format (oid: 1.2.840.113549.1.1.1).
     *
     * @todo Check how many rsa formats use the same format of pkcs #1.
     *
     * The format is defined as:
     * PublicKeyInfo ::= SEQUENCE {
     *   algorithm       AlgorithmIdentifier,
     *   PublicKey       BIT STRING
     * }
     * Where AlgorithmIdentifier is:
     * AlgorithmIdentifier ::= SEQUENCE {
     *   algorithm       OBJECT IDENTIFIER,     the OID of the enc algorithm
     *   parameters      ANY DEFINED BY algorithm OPTIONAL (NULL for PKCS #1)
     * }
     * and PublicKey is a SEQUENCE encapsulated in a BIT STRING
     * RSAPublicKey ::= SEQUENCE {
     *   modulus           INTEGER,  -- n
     *   publicExponent    INTEGER   -- e
     * }
     * it's possible to examine the structure of the keys obtained from openssl using
     * an asn.1 dumper as the one used here to parse the components: http://lapo.it/asn1js/
     * @argument {string} pem the pem encoded string, can include the BEGIN/END header/footer
     * @private
     */
    RSAKey.prototype.parseKey = function (pem) {
        try {
            var modulus = 0;
            var public_exponent = 0;
            var reHex = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/;
            var der = reHex.test(pem) ? Hex.decode(pem) : window.Base64.unarmor(pem);
            var asn1 = window.ASN1.decode(der);

            //Fixes a bug with OpenSSL 1.0+ private keys
            if (asn1.sub.length === 3) {
                asn1 = asn1.sub[2].sub[0];
            }
            if (asn1.sub.length === 9) {
                // Parse the private key.
                modulus = asn1.sub[1].getHexStringValue(); //bigint
                this.n = parseBigInt(modulus, 16);

                public_exponent = asn1.sub[2].getHexStringValue(); //int
                this.e = parseInt(public_exponent, 16);

                var private_exponent = asn1.sub[3].getHexStringValue(); //bigint
                this.d = parseBigInt(private_exponent, 16);

                var prime1 = asn1.sub[4].getHexStringValue(); //bigint
                this.p = parseBigInt(prime1, 16);

                var prime2 = asn1.sub[5].getHexStringValue(); //bigint
                this.q = parseBigInt(prime2, 16);

                var exponent1 = asn1.sub[6].getHexStringValue(); //bigint
                this.dmp1 = parseBigInt(exponent1, 16);

                var exponent2 = asn1.sub[7].getHexStringValue(); //bigint
                this.dmq1 = parseBigInt(exponent2, 16);

                var coefficient = asn1.sub[8].getHexStringValue(); //bigint
                this.coeff = parseBigInt(coefficient, 16);

            } else if (asn1.sub.length === 2) {
                // Parse the public key.
                var bit_string = asn1.sub[1];
                var sequence = bit_string.sub[0];

                modulus = sequence.sub[0].getHexStringValue();
                this.n = parseBigInt(modulus, 16);
                public_exponent = sequence.sub[1].getHexStringValue();
                this.e = parseInt(public_exponent, 16);
            } else {
                return false;
            }
            return true;
        } catch (ex) {
            return false;
        }
    };

    /**
     * Translate rsa parameters in a hex encoded string representing the rsa key.
     *
     * The translation follow the ASN.1 notation :
     * RSAPrivateKey ::= SEQUENCE {
     *   version           Version,
     *   modulus           INTEGER,  -- n
     *   publicExponent    INTEGER,  -- e
     *   privateExponent   INTEGER,  -- d
     *   prime1            INTEGER,  -- p
     *   prime2            INTEGER,  -- q
     *   exponent1         INTEGER,  -- d mod (p1)
     *   exponent2         INTEGER,  -- d mod (q-1)
     *   coefficient       INTEGER,  -- (inverse of q) mod p
     * }
     * @returns {string}  DER Encoded String representing the rsa private key
     * @private
     */
    RSAKey.prototype.getPrivateBaseKey = function () {
        var options = {
            'array': [
                new KJUR.asn1.DERInteger({
                    'int': 0
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.n
                }),
                new KJUR.asn1.DERInteger({
                    'int': this.e
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.d
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.p
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.q
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.dmp1
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.dmq1
                }),
                new KJUR.asn1.DERInteger({
                    'bigint': this.coeff
                })
            ]
        };
        var seq = new KJUR.asn1.DERSequence(options);
        return seq.getEncodedHex();
    };

    /**
     * base64 (pem) encoded version of the DER encoded representation
     * @returns {string} pem encoded representation without header and footer
     * @public
     */
    RSAKey.prototype.getPrivateBaseKeyB64 = function () {
        return hex2b64(this.getPrivateBaseKey());
    };

    /**
     * Translate rsa parameters in a hex encoded string representing the rsa public key.
     * The representation follow the ASN.1 notation :
     * PublicKeyInfo ::= SEQUENCE {
     *   algorithm       AlgorithmIdentifier,
     *   PublicKey       BIT STRING
     * }
     * Where AlgorithmIdentifier is:
     * AlgorithmIdentifier ::= SEQUENCE {
     *   algorithm       OBJECT IDENTIFIER,     the OID of the enc algorithm
     *   parameters      ANY DEFINED BY algorithm OPTIONAL (NULL for PKCS #1)
     * }
     * and PublicKey is a SEQUENCE encapsulated in a BIT STRING
     * RSAPublicKey ::= SEQUENCE {
     *   modulus           INTEGER,  -- n
     *   publicExponent    INTEGER   -- e
     * }
     * @returns {string} DER Encoded String representing the rsa public key
     * @private
     */
    RSAKey.prototype.getPublicBaseKey = function () {
        var options = {
            'array': [
                new KJUR.asn1.DERObjectIdentifier({
                    'oid': '1.2.840.113549.1.1.1'
                }), //RSA Encryption pkcs #1 oid
                new KJUR.asn1.DERNull()
            ]
        };
        var first_sequence = new KJUR.asn1.DERSequence(options);

        options = {
            'array': [
                new KJUR.asn1.DERInteger({
                    'bigint': this.n
                }),
                new KJUR.asn1.DERInteger({
                    'int': this.e
                })
            ]
        };
        var second_sequence = new KJUR.asn1.DERSequence(options);

        options = {
            'hex': '00' + second_sequence.getEncodedHex()
        };
        var bit_string = new KJUR.asn1.DERBitString(options);

        options = {
            'array': [
                first_sequence,
                bit_string
            ]
        };
        var seq = new KJUR.asn1.DERSequence(options);
        return seq.getEncodedHex();
    };

    /**
     * base64 (pem) encoded version of the DER encoded representation
     * @returns {string} pem encoded representation without header and footer
     * @public
     */
    RSAKey.prototype.getPublicBaseKeyB64 = function () {
        return hex2b64(this.getPublicBaseKey());
    };

    /**
     * wrap the string in block of width chars. The default value for rsa keys is 64
     * characters.
     * @param {string} str the pem encoded string without header and footer
     * @param {Number} [width=64] - the length the string has to be wrapped at
     * @returns {string}
     * @private
     */
    RSAKey.prototype.wordwrap = function (str, width) {
        width = width || 64;
        if (!str) {
            return str;
        }
        var regex = '(.{1,' + width + '})( +|$\n?)|(.{1,' + width + '})';
        return str.match(RegExp(regex, 'g')).join('\n');
    };

    /**
     * Retrieve the pem encoded private key
     * @returns {string} the pem encoded private key with header/footer
     * @public
     */
    RSAKey.prototype.getPrivateKey = function () {
        var key = "-----BEGIN RSA PRIVATE KEY-----\n";
        key += this.wordwrap(this.getPrivateBaseKeyB64()) + "\n";
        key += "-----END RSA PRIVATE KEY-----";
        return key;
    };

    /**
     * Retrieve the pem encoded public key
     * @returns {string} the pem encoded public key with header/footer
     * @public
     */
    RSAKey.prototype.getPublicKey = function () {
        var key = "-----BEGIN PUBLIC KEY-----\n";
        key += this.wordwrap(this.getPublicBaseKeyB64()) + "\n";
        key += "-----END PUBLIC KEY-----";
        return key;
    };

    /**
     * Check if the object contains the necessary parameters to populate the rsa modulus
     * and public exponent parameters.
     * @param {Object} [obj={}] - An object that may contain the two public key
     * parameters
     * @returns {boolean} true if the object contains both the modulus and the public exponent
     * properties (n and e)
     * @todo check for types of n and e. N should be a parseable bigInt object, E should
     * be a parseable integer number
     * @private
     */
    RSAKey.prototype.hasPublicKeyProperty = function (obj) {
        obj = obj || {};
        return (
            obj.hasOwnProperty('n') &&
            obj.hasOwnProperty('e')
        );
    };

    /**
     * Check if the object contains ALL the parameters of an RSA key.
     * @param {Object} [obj={}] - An object that may contain nine rsa key
     * parameters
     * @returns {boolean} true if the object contains all the parameters needed
     * @todo check for types of the parameters all the parameters but the public exponent
     * should be parseable bigint objects, the public exponent should be a parseable integer number
     * @private
     */
    RSAKey.prototype.hasPrivateKeyProperty = function (obj) {
        obj = obj || {};
        return (
            obj.hasOwnProperty('n') &&
            obj.hasOwnProperty('e') &&
            obj.hasOwnProperty('d') &&
            obj.hasOwnProperty('p') &&
            obj.hasOwnProperty('q') &&
            obj.hasOwnProperty('dmp1') &&
            obj.hasOwnProperty('dmq1') &&
            obj.hasOwnProperty('coeff')
        );
    };

    /**
     * Parse the properties of obj in the current rsa object. Obj should AT LEAST
     * include the modulus and public exponent (n, e) parameters.
     * @param {Object} obj - the object containing rsa parameters
     * @private
     */
    RSAKey.prototype.parsePropertiesFrom = function (obj) {
        this.n = obj.n;
        this.e = obj.e;
        if (obj.hasOwnProperty('d')) {
            this.d = obj.d;
            this.p = obj.p;
            this.q = obj.q;
            this.dmp1 = obj.dmp1;
            this.dmq1 = obj.dmq1;
            this.coeff = obj.coeff;
        }
    };

    /**
     * Create a new JSEncryptRSAKey that extends Tom Wu's RSA key object.
     * This object is just a decorator for parsing the key parameter
     * @param {string|Object} key - The key in string format, or an object containing
     * the parameters needed to build a RSAKey object.
     * @constructor
     */
    var JSEncryptRSAKey = function (key) {
        // Call the super constructor.
        RSAKey.call(this);
        // If a key key was provided.
        if (key) {
            // If this is a string...
            if (typeof key === 'string') {
                this.parseKey(key);
            } else if (
                this.hasPrivateKeyProperty(key) ||
                this.hasPublicKeyProperty(key)
            ) {
                // Set the values for the key.
                this.parsePropertiesFrom(key);
            }
        }
    };

    // Derive from RSAKey.
    JSEncryptRSAKey.prototype = new RSAKey();

    // Reset the contructor.
    JSEncryptRSAKey.prototype.constructor = JSEncryptRSAKey;


    /**
     *
     * @param {Object} [options = {}] - An object to customize JSEncrypt behaviour
     * possible parameters are:
     * - default_key_size        {number}  default: 1024 the key size in bit
     * - default_public_exponent {string}  default: '010001' the hexadecimal representation of the public exponent
     * - log                     {boolean} default: false whether log warn/error or not
     * @constructor
     */
    var JSEncrypt = function (options) {
        options = options || {};
        this.default_key_size = parseInt(options.default_key_size) || 1024;
        this.default_public_exponent = options.default_public_exponent || '010001'; //65537 default openssl public exponent for rsa key type
        this.log = options.log || false;
        // The private and public key.
        this.key = null;
    };

    /**
     * Method to set the rsa key parameter (one method is enough to set both the public
     * and the private key, since the private key contains the public key paramenters)
     * Log a warning if logs are enabled
     * @param {Object|string} key the pem encoded string or an object (with or without header/footer)
     * @public
     */
    JSEncrypt.prototype.setKey = function (key) {
        if (this.log && this.key) {
            console.warn('A key was already set, overriding existing.');
        }
        this.key = new JSEncryptRSAKey(key);
    };

    /**
     * Proxy method for setKey, for api compatibility
     * @see setKey
     * @public
     */
    JSEncrypt.prototype.setPrivateKey = function (privkey) {
        // Create the key.
        this.setKey(privkey);
    };

    /**
     * Proxy method for setKey, for api compatibility
     * @see setKey
     * @public
     */
    JSEncrypt.prototype.setPublicKey = function (pubkey) {
        // Sets the public key.
        this.setKey(pubkey);
    };

    /**
     * Proxy method for RSAKey object's decrypt, decrypt the string using the private
     * components of the rsa key object. Note that if the object was not set will be created
     * on the fly (by the getKey method) using the parameters passed in the JSEncrypt constructor
     * @param {string} string base64 encoded crypted string to decrypt
     * @return {string} the decrypted string
     * @public
     */
    JSEncrypt.prototype.private_decrypt = function (string) {
        // Return the decrypted string.
        try {
            return this.getKey().decrypt_private(b64tohex(string));
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.prototype.public_decrypt = function (string) {
        // Return the decrypted string.
        try {
            return this.getKey().decrypt_public(b64tohex(string));
        } catch (ex) {
            return false;
        }
    };

    /**
     * Proxy method for RSAKey object's encrypt, encrypt the string using the public
     * components of the rsa key object. Note that if the object was not set will be created
     * on the fly (by the getKey method) using the parameters passed in the JSEncrypt constructor
     * @param {string} string the string to encrypt
     * @return {string} the encrypted string encoded in base64
     * @public
     */
    JSEncrypt.prototype.public_encrypt = function (string) {
        // Return the encrypted string.
        try {
            return hex2b64(this.getKey().encrypt_public(string));
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.prototype.private_encrypt = function (str) {
        // Return the encrypted string.
        try {
            return hex2b64(this.getKey().encrypt_private(str));
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.prototype.setPublic = RSASetPublic;

    /**
     * Getter for the current JSEncryptRSAKey object. If it doesn't exists a new object
     * will be created and returned
     * @param {callback} [cb] the callback to be called if we want the key to be generated
     * in an async fashion
     * @returns {JSEncryptRSAKey} the JSEncryptRSAKey object
     * @public
     */
    JSEncrypt.prototype.getKey = function (cb) {
        // Only create new if it does not exist.
        if (!this.key) {
            // Get a new private key.
            this.key = new JSEncryptRSAKey();
            if (cb && {}.toString.call(cb) === '[object Function]') {
                this.key.generateAsync(this.default_key_size, this.default_public_exponent, cb);
                return;
            }
            // Generate the key.
            this.key.generate(this.default_key_size, this.default_public_exponent);
        }
        return this.key;
    };

    /**
     * Returns the pem encoded representation of the private key
     * If the key doesn't exists a new key will be created
     * @returns {string} pem encoded representation of the private key WITH header and footer
     * @public
     */
    JSEncrypt.prototype.getPrivateKey = function () {
        // Return the private representation of this key.
        return this.getKey().getPrivateKey();
    };

    /**
     * Returns the pem encoded representation of the private key
     * If the key doesn't exists a new key will be created
     * @returns {string} pem encoded representation of the private key WITHOUT header and footer
     * @public
     */
    JSEncrypt.prototype.getPrivateKeyB64 = function () {
        // Return the private representation of this key.
        return this.getKey().getPrivateBaseKeyB64();
    };


    /**
     * Returns the pem encoded representation of the public key
     * If the key doesn't exists a new key will be created
     * @returns {string} pem encoded representation of the public key WITH header and footer
     * @public
     */
    JSEncrypt.prototype.getPublicKey = function () {
        // Return the private representation of this key.
        return this.getKey().getPublicKey();
    };

    /**
     * Returns the pem encoded representation of the public key
     * If the key doesn't exists a new key will be created
     * @returns {string} pem encoded representation of the public key WITHOUT header and footer
     * @public
     */
    JSEncrypt.prototype.getPublicKeyB64 = function () {
        // Return the private representation of this key.
        return this.getKey().getPublicBaseKeyB64();
    };

    JSEncrypt.prototype.setPrivate = RSASetPrivate;
    JSEncrypt.prototype.setPrivateEx = RSASetPrivateEx;

    JSEncrypt.prototype.public_encryptLong = function (string, padding, output) {
        var k = this.getKey();
        var maxLength = (((k.n.bitLength() + 7) >> 3) - 11);
        try {
            var lt = "";
            var ct = "";
            if (string.length > maxLength) {
                lt = string.match(eval("/.{1," + maxLength + "}/g"));
                lt.forEach(function (entry) {
                    var t1 = k.encrypt_public(entry, padding);
                    ct += t1;
                });
                return output ? hex2b64(ct) : ct;
            }
            var t = k.encrypt_public(string, padding);
            var y = output ? hex2b64(t) : t;
            return y;
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.prototype.private_decryptLong = function (string, padding, output) {
        var k = this.getKey();
        var maxLength = (((k.n.bitLength() + 7) >> 3) - 11);
        var MAX_DECRYPT_BLOCK = parseInt((k.n.bitLength() + 1) / 4);
        try {
            var ct = "";
            string = output ? b64tohex(string) : string;
            if (string.length > maxLength) {
                var lt = string.match(eval("/.{1," + MAX_DECRYPT_BLOCK + "}/g"));
                lt.forEach(function (entry) {
                    var t1 = k.decrypt_private(entry, padding);
                    ct += t1;
                });
                return ct;
            }
            var y = k.decrypt_private(string, padding);
            return y;
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.prototype.private_encryptLong = function (string, padding, output) {
        var k = this.getKey();
        var maxLength = (((k.n.bitLength() + 7) >> 3) - 11);
        try {
            var lt = "";
            var ct = "";
            if (string.length > maxLength) {
                lt = string.match(eval("/.{1," + maxLength + "}/g"));
                lt.forEach(function (entry) {
                    var t1 = k.encrypt_private(entry, padding);
                    ct += t1;
                });
                return output ? hex2b64(ct) : ct;
            }
            var t = k.encrypt_private(string, padding);
            var y = output ? hex2b64(t) : t;
            return y;
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.prototype.public_decryptLong = function (string, padding, output) {
        var k = this.getKey();
        var maxLength = (((k.n.bitLength() + 7) >> 3) - 11);
        var MAX_DECRYPT_BLOCK = parseInt((k.n.bitLength() + 1) / 4);
        try {
            var ct = "";
            string = output ? b64tohex(string) : string;
            if (string.length > maxLength) {
                var lt = string.match(eval("/.{1," + MAX_DECRYPT_BLOCK + "}/g"));
                lt.forEach(function (entry) {
                    var t1 = k.decrypt_public(entry, padding);
                    ct += t1;
                });
                return ct;
            }
            var y = k.decrypt_public(string, padding);
            return y;
        } catch (ex) {
            return false;
        }
    };

    JSEncrypt.version = '2.3.0';
    exports.JSEncrypt = JSEncrypt;
})(RSA);

function RSA_Public_Encrypt(plain_text) {
    var public_modulus = "a70717e5ceaeb6bb2a15a7d4f047c8639e9af487f9a16bf2f1504e17f3693e534e4f79695f383c740b0e58ab0ecb03511d9cc065686205008ba386c47e663c111aa209c6e9e7dec4355c121911c1804b06557b3679956f2bb687c03aa52f0399d4e1a9c656549414d27fc45dfcf0eb3eb601d45448a1bacd96a2157ba51f7ce9";
    var public_exponent = "10001";
    var Crypt = new RSA.JSEncrypt();
    Crypt.setPublic(public_modulus, public_exponent);
    Crypt.setPublicKey({"n": Crypt.n, "e": Crypt.e});
    var enc_str = Crypt.public_encryptLong(plain_text, 2, true);
    return enc_str;
}

function AES_Encrypt(word, k, i) {
    var key = CryptoJS.enc.Utf8.parse(k);
    var iv = CryptoJS.enc.Utf8.parse(i);

    var srcs = CryptoJS.enc.Utf8.parse(word);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return encrypted.toString();
}

function AES_Decrypt(word, k, i) {
    var key = CryptoJS.enc.Utf8.parse(k);
    var iv = CryptoJS.enc.Utf8.parse(i);

    var srcs = word;
    var decrypt = CryptoJS.AES.decrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return decrypt.toString(CryptoJS.enc.Utf8);
}

function o() {
    var r, i = new Uint8Array(16);

    return crypto.getRandomValues(i)
}

// function trans(s) {
//     var li = []
//     var ss = JSON.parse(JSON.stringify(s))['sectionList']
//     ss.forEach((item, index) => {
//         li.push({
//             laborId: item.laborId,
//             id: item.id
//         })
//     })
//     return li
// }

function h(e, t, n) {
    e = e || {};
    var r = e.random || (e.rng || o)();
    if (r[6] = 15 & r[6] | 64,
        r[8] = 63 & r[8] | 128,
        t) {
        n = n || 0;
        for (var i = 0; i < 16; ++i)
            t[n + i] = r[i];
        return t
    }
    return f(r)
}

function s(e) {
    const a = /^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i
    return "string" === typeof e && a.test(e)
}

function f(e) {
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 0
        ,
        n = (c[e[t + 0]] + c[e[t + 1]] + c[e[t + 2]] + c[e[t + 3]] + "-" + c[e[t + 4]] + c[e[t + 5]] + "-" + c[e[t + 6]] + c[e[t + 7]] + "-" + c[e[t + 8]] + c[e[t + 9]] + "-" + c[e[t + 10]] + c[e[t + 11]] + c[e[t + 12]] + c[e[t + 13]] + c[e[t + 14]] + c[e[t + 15]]).toLowerCase();
    if (!s(n))
        throw TypeError("Stringified UUID is invalid");
    return n
}

//生成iv和key
function keyAndIv() {
    for (var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 16, e = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", r = "", n = 0; n < t; n++)
        r += e.charAt(cc(0, e.length - 1));
    return r
}

function cc(e, t) {
    return e >= t ? e : (e >>= 0) + Math.round(Math.random() * ((t || 9) - e))
}

function gen() {
    var e = Date.now()
    var t = h(undefined, undefined, undefined).replace(/-/gm, "")
    data = {
        token: "",
        timestamp: e,
        uuidHashCode: t
    }
    const b = "".concat(e, "@").concat(t)
    return b
}

function gen2(token) {
    var e = Date.now()
    var t = h(undefined, undefined, undefined).replace(/-/gm, "")
    data = {
        token: token,
        timestamp: e,
        uuidHashCode: t
    }
    const b = "".concat(e, "@").concat(t)
    return {time: e, b: b, uuid: t}

}

function getuuid() {
    return h(undefined, undefined, undefined).replace(/-/gm, "")
}

function reAll(phone, word) {
    var d = "username=" + phone + "&password=" + word
    var kk = keyAndIv()
    var ii = keyAndIv()
    var encData = AES_Encrypt(d, kk, ii)
    var key = RSA_Public_Encrypt(kk)
    const bf = {
        encryptData: encodeURIComponent(encData),
        key: encodeURIComponent(key),
        iv: encodeURIComponent(ii)
    }
    console.log(bf)
    return jsonToUrlParam(bf)

}

function getListAll(token) {
    var gg = gen2(token)
    var d = token
    var kk = keyAndIv()
    var ii = keyAndIv()
    var encData = AES_Encrypt(gg.b, kk, ii)
    var key = RSA_Public_Encrypt(kk)
    return {
        token: d,
        timestamp: gg.time,
        uuidHashCode: gg.uuid,
        encryptData: encData,
        key: key,
        rk: kk,
        iv: ii
    }

}

function jsonToUrlParam(json) {
    return Object.keys(json).map(key => key + '=' + json[key]).join('&');
}

// var data=reAll("13787058992@bj4923", "aaaa5599")
// fetch('https://gldzb-gateway.gldzb.com/gldzb-manage-api/api/web/loginByAuth', {
//     method: 'POST',
//     headers: {
//         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309091b) XWEB/8555',
//         'timestamp': Date.now(),
//         'timestamp2': Date.now(),
//         'Content-Type': 'application/x-www-form-urlencoded',
//         'Iv':keyAndIv(),
//         'Key':keyAndIv(),
//         'uuidhashcode':h(undefined, undefined, undefined).replace(/-/gm, "")
//     },
//     body:jsonToUrlParam(data)
// })
//     .then(response => response.text())
//     .then(data => console.log(data))
//     .catch(error => console.error(error));
// console.log(jsonToUrlParam(data))

// console.log(AES_Decrypt("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","cCkLdm2c7U7WzZSf","SHiRPRNYdIUzvQDZ"))