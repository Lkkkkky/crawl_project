Java.perform(function () {
    console.log("Frida script loaded successfully!");

    try {
        // Hook ptrace to bypass anti-debugging
        Interceptor.attach(Module.findExportByName(null, "ptrace"), {
            onEnter: function (args) {
                console.log("ptrace called");
            },
            onLeave: function (retval) {
                retval.replace(0);
            }
        });

        // Hook Java Cipher
        var Cipher = Java.use("javax.crypto.Cipher");
        Cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function (opmode, key, params) {
            console.log("Cipher.init called:");
            console.log("  opmode: " + opmode);
            console.log("  key: " + key);
            console.log("  params: " + params);
            return this.init(opmode, key, params);
        };

        Cipher.doFinal.overload('[B').implementation = function (input) {
            console.log("Cipher.doFinal called:");
            console.log("  input: " + input);
            var result = this.doFinal(input);
            console.log("  result: " + result);
            return result;
        };

        // Hook Native AES_encrypt
        var baseAddr = Module.findBaseAddress("libcrypto.so");
        if (baseAddr) {
            var AES_encrypt = Module.findExportByName("libcrypto.so", "AES_encrypt");
            if (AES_encrypt) {
                Interceptor.attach(AES_encrypt, {
                    onEnter: function (args) {
                        console.log("AES_encrypt called:");
                        console.log("  input: " + hexdump(args[0], { length: 16 }));
                        console.log("  key: " + hexdump(args[2], { length: 32 }));
                    },
                    onLeave: function (retval) {
                        console.log("AES_encrypt result: " + hexdump(retval, { length: 16 }));
                    }
                });
            } else {
                console.log("AES_encrypt not found in libcrypto.so");
            }
        } else {
            console.log("libcrypto.so not loaded");
        }
    } catch (e) {
        console.log("Error: " + e);
    }
});


// frida -U -n  com.brightdairy.personal -l hook.js   attach 模式
// frida -U -f  com.brightdairy.personal -l hook.js   spawn 模式