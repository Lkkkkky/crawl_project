// --- Native 层检测辅助与绕过 ---
function bypassNativeDetection() {
    console.log("Applying Native Detection Bypasses...");

    // 1. Hook strstr - 很多检测通过搜索 maps 里的 "frida" 字符串进行
    const strstrPtr = Module.findExportByName(null, 'strstr');
    if (strstrPtr) {
        Interceptor.attach(strstrPtr, {
            onEnter: function (args) {
                this.haystack = args[0].readUtf8String();
                this.needle = args[1].readUtf8String();
            },
            onLeave: function (retval) {
                if (this.haystack && this.needle) {
                    if (this.needle.indexOf("frida") !== -1 || this.needle.indexOf("gum-js-loop") !== -1) {
                        // console.log("Bypassing strstr check for: " + this.needle);
                        retval.replace(ptr(0)); // 返回 NULL，表示没找到
                    }
                }
            }
        });
    }

    // 2. 监控 .so 加载，定位具体崩溃点
    const openPtr = Module.findExportByName(null, 'open');
    if (openPtr) {
        Interceptor.attach(openPtr, {
            onEnter: function (args) {
                this.path = args[0].readUtf8String();
            },
            onLeave: function (retval) {
                if (this.path && this.path.indexOf(".so") !== -1) {
                    if (this.path.indexOf("libsec-aio") !== -1 || this.path.indexOf("libsmsdk") !== -1) {
                        console.log("[!] Loading Security Library: " + this.path);
                    }
                }
            }
        });
    }
}

Java.perform(function () {
    bypassNativeDetection();

    var targetClass = "com.vip.sdk.api.i";
    console.log("Searching for " + targetClass + "...");

    // 遍历 ClassLoader 以解决 ClassNotFoundException
    Java.enumerateClassLoaders({
        onMatch: function (loader) {
            try {
                if (loader.findClass(targetClass)) {
                    console.log("Successfully found class in loader: " + loader);
                    Java.classFactory.loader = loader;
                }
            } catch (e) {}
        },
        onComplete: function () {
            try {
                var JniHelper = Java.use("com.vip.sdk.base.jni.JniHelper");
                JniHelper["getSignHash"].implementation = function (context, map, str) {
                    // console.log(JSON.stringify(map));
                    var TreeMap = Java.use("java.util.TreeMap");
                    var obj = Java.cast(map, TreeMap);
                    console.log(`JniHelper.getSignHash is called: context=${context}, map=${obj}, str=${str}`);
                    let result = this["getSignHash"](context, map, str);
                    console.log(`JniHelper.getSignHash result=${result}`);
                    return result;
                };
                console.log("Hooking successfully applied!");
            } catch (e) {
                console.log("Hooking failed: " + e.message);
            }
        }
    });
});
