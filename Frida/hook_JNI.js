Java.perform(function () {
    console.log("Frida script loaded successfully!");

    try {
        // 获取 newStringUTF 函数的地址
        var newStringUTF = Module.findExportByName("libart.so", "NewStringUTF");
        if (newStringUTF) {
            console.log("Found NewStringUTF at: " + newStringUTF);

            // Hook NewStringUTF
            Interceptor.attach(newStringUTF, {
                onEnter: function (args) {
                    // args[0] 是 JNIEnv*
                    // args[1] 是 const char* (UTF-8 字符串)
                    var utf8String = args[1].readCString();
                    console.log("NewStringUTF called:");
                    console.log("  UTF-8 string: " + utf8String);
                },
                onLeave: function (retval) {
                    // retval 是 jstring
                    console.log("NewStringUTF returned: " + retval);
                }
            });
        } else {
            console.log("NewStringUTF not found in libart.so");
        }
    } catch (e) {
        console.log("Error: " + e);
    }
});