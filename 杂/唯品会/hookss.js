function bb(){
    Interceptor.attach(Module.findExportByName("libJniHelper.so", 'getByteHash'), {
        onEnter: function (args) {
        	//经过确认参数是string的，直接打印
            console.log('参数3', args[2].readCString());
            console.log('参数4', args[3]);
            console.log('参数5', args[4]);
        },
        onLeave: function (retval) {
            console.log('getByteHash returned:', retval.readCString());
        }
    });
}
