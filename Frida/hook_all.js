Java.perform(function () {
    console.log("Frida script loaded successfully!");

    try {
        var CustomCipher = Java.use("com.example.CustomCipher");

        // 获取所有方法
        var methods = CustomCipher.class.getDeclaredMethods();
        for (var i = 0; i < methods.length; i++) {
            var method = methods[i];
            console.log("Hooking method: " + method.getName());

            // Hook 方法
            CustomCipher[method.getName()].overloads.forEach(function (overload) {
                overload.implementation = function () {
                    console.log("CustomCipher." + method.getName() + " called:");
                    for (var j = 0; j < arguments.length; j++) {
                        console.log("  arg[" + j + "]: " + arguments[j]);
                    }

                    return this[method.getName()].apply(this, arguments);
                };
            });
        }
    } catch (e) {
        console.log("Error: " + e);
    }
});