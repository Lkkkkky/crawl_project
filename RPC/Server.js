(function() {
  if (window.flagSkyx) return;

  try {
    var ws = new WebSocket("ws://127.0.0.1:1234");
    window.flagSkyx = true;

    ws.onmessage = function(param) {
      console.log("接受到参数: " + param.data);

      if (param.data === 'exit') {
        ws.close(); // 关闭 WebSocket
      } else {
        // 自定义代码逻辑
        ws.send(aa(param.data)); // 使用 aa 函数处理参数并发送
      }
    };
  } catch {
    console.log("连接出错");
    window.flagSkyx = false; // 连接错误时设置为 false
  }
})();


