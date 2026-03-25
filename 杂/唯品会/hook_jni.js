Java.perform(function () {
    const SO_NAME = "libJniHelper.so";
    const TARGET_OFFSET = 0x7EE10;
    let isHooked = false;

    function hookTargetFunction(base) {
        const targetAddr = base.add(TARGET_OFFSET);
        console.log(`[+] Found ${SO_NAME} at ${base}, Hooking sub_7EE10 at ${targetAddr}`);
        
        Interceptor.attach(targetAddr, {
            onEnter: function (args) {
                console.log(`\n[sub_7EE10] Called!`);
                console.log(`  - arg0 (a1): ${args[0]}`);
                console.log(`  - arg1 (a2): ${args[1]}`);
                console.log(`  - arg2 (a3): ${args[2]}`);
                console.log(`  - arg3 (a4): ${args[3]} (int: ${args[3].toInt32()})`);

                // 尝试以字符串形式读取 a3 (根据 a4 长度)
                try {
                    const len = args[3].toInt32();
                    if (len > 0 && len < 2048) {
                        const buffer = args[2].readByteArray(len);
                        console.log(`  - arg2 (a3) Data (Hex):\n${hexdump(buffer, { offset: 0, length: len, header: true, ansi: true })}`);
                        
                        try {
                            const str = args[2].readUtf8String(len);
                            console.log(`  - arg2 (a3) as UTF8: ${str}`);
                        } catch (e) {}
                    }
                } catch (e) {
                    console.log(`  - [!] Could not read arg2 as string: ${e}`);
                }
            },
            onLeave: function (retval) {
                console.log(`[sub_7EE10] Return Value: ${retval}`);
            }
        });
        isHooked = true;
    }

    // 1. 检查模块是否已经加载
    const module = Process.findModuleByName(SO_NAME);
    if (module) {
        hookTargetFunction(module.base);
    } else {
        console.log(`[-] ${SO_NAME} not found, waiting for dlopen...`);
        // 2. 如果没加载，Hook dlopen 来监听加载
        const dlopenPtr = Module.findExportByName(null, "dlopen");
        const android_dlopen_extPtr = Module.findExportByName(null, "android_dlopen_ext");

        const dlopen_callback = function (pathPtr) {
            if (pathPtr) {
                const path = pathPtr.readUtf8String();
                if (path.indexOf(SO_NAME) !== -1 && !isHooked) {
                    console.log(`[+] Detected loading: ${path}`);
                    // 延迟一点点确保加载完成
                    setTimeout(function() {
                        const m = Process.findModuleByName(SO_NAME);
                        if (m) hookTargetFunction(m.base);
                    }, 500);
                }
            }
        };

        if (dlopenPtr) {
            Interceptor.attach(dlopenPtr, {
                onEnter: function (args) { dlopen_callback(args[0]); }
            });
        }
        if (android_dlopen_extPtr) {
            Interceptor.attach(android_dlopen_extPtr, {
                onEnter: function (args) { dlopen_callback(args[0]); }
            });
        }
    }

    // 保留之前的 RegisterNatives Hook 逻辑作为备份
    function logAndHookRegisterNatives() {
        const env = Java.vm.getEnv();
        const registerNativesPtr = env.handle.readPointer().add(215 * Process.pointerSize).readPointer();
        
        Interceptor.attach(registerNativesPtr, {
            onEnter: function (args) {
                try {
                    const className = Java.vm.getEnv().getClassName(args[1]);
                    const methods = args[2];
                    const count = args[3].toInt32();
                    
                    if (className.includes("com.vip.sdk.api.i") || className.includes("JniHelper")) {
                        console.log(`\n[RegisterNatives] Called for class: ${className} (Count: ${count})`);
                        for (let i = 0; i < count; i++) {
                            const namePtr = methods.add(i * Process.pointerSize * 3).readPointer();
                            const sigPtr = methods.add(i * Process.pointerSize * 3 + Process.pointerSize).readPointer();
                            const fnPtr = methods.add(i * Process.pointerSize * 3 + Process.pointerSize * 2).readPointer();
                            
                            const name = namePtr.readUtf8String();
                            const sig = sigPtr.readUtf8String();
                            console.log(`  - Name: ${name}, Sig: ${sig}, Addr: ${fnPtr}`);

                            // 如果是 getSignHash，也可以顺便 Hook 它的 Native 实现
                            if (name === "getSignHash") {
                                Interceptor.attach(fnPtr, {
                                    onEnter: function (nativeArgs) {
                                        console.log(`\n[getSignHash] Native Called!`);
                                        const env = nativeArgs[0];
                                        const mapObj = nativeArgs[3];
                                        const strObj = nativeArgs[4];
                                        
                                        // 打印 String 参数
                                        if (strObj) {
                                            const jstr = Java.cast(strObj, Java.use("java.lang.String"));
                                            console.log(`  - String Argument: ${jstr.toString()}`);
                                        }

                                        // 打印 Map 参数
                                        if (mapObj) {
                                            const map = Java.cast(mapObj, Java.use("java.util.Map"));
                                            console.log(`  - Map Argument: ${map.toString()}`);
                                        }
                                    }
                                });
                            }
                        }
                    }
                } catch (e) {}
            }
        });
    }

    logAndHookRegisterNatives();
});
