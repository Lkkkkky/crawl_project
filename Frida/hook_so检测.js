function hook_dlopen() {
    Interceptor.attach(Module.findExportByName(null, "android_dlopen_ext"),
        {
            onEnter: function (args) {
                this.fileName = args[0].readCString()
                console.log(`dlopen onEnter: ${this.fileName}`)
            }, onLeave: function(retval){
                console.log(`dlopen onLeave fileName: ${this.fileName}`)
                if(this.fileName != null && this.fileName.indexOf("libmsaoaidsec.so") >= 0){
                    let JNI_OnLoad = Module.getExportByName(this.fileName, 'JNI_OnLoad')
                    console.log(`dlopen onLeave JNI_OnLoad: ${JNI_OnLoad}`)
                }
            }
        }
    );
}

setImmediate(hook_dlopen)