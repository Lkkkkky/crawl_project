import asyncio
import websockets
import requests
import json
async def receive_message(websocket, path):
    try:
        while True:
            send_text = input("请输入要加密的字符串: ")
            if send_text.lower() == "exit":
                await websocket.send(send_text)
                break
            await websocket.send(send_text)
            response_text = await websocket.recv()
            print("\n加密结果：", response_text)
    except websockets.exceptions.ConnectionClosed:
        print("连接已关闭。")
    except Exception as e:
        print(f"发生错误: {e}")

async def main():
    async with websockets.serve(receive_message, '127.0.0.1', 1234):
        print("WebSocket 服务器已启动，等待连接...")
        await asyncio.Future()  # 保持服务器运行

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n服务器已停止。")
# 简化调用方式
def get_h5st(data):
    params = {
        'group': 'test_web3',
        'clientId': 'jd33',
        'action': 'jd',
        'pp': data,
        'param': 22
    }
    for i in range(50):

        res=requests.get('http://127.0.0.1:5612/business/invoke',params=params)
        if('fb5df' in res.text):
            # logger.info(json.loads(res.text).get('data'))
            return json.loads(res.text).get('data')
