from PIL import Image
import io
import time
import base64

# 滑块背景图还原 - 极验3.0
def background_reduction(
        b_puzzle_path: str = '4e7f20fb8.jpg',
        save_file: bool = False,
        save_file_path: str = ''):
    '''
    :param b_puzzle_path:  本地滑块背景图的路径 可处理3.0极验
    :param save_file:  是否保存最终修改后的图片 默认False
    :param save_file_path:  保存最终修改后的图片名称，不含后缀    默认：自动生成
    :return: base64图片
    '''
    # 打开PNG图片
    image = Image.open(b_puzzle_path)
    # 创建新的空白图片
    new_image = Image.new('RGBA', (260, 160))
    # 坐标
    k = 0
    # 定值, 在极验3.0版本中, 通过画布断点获取数据
    ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42,
          12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    # ut有多少参数, 就有多少个小碎片拼图
    for _ in range(len(ut)):
        # 通过计算得出 小碎片的起始坐标
        c = ut[_] % 26 * 12 + 1
        # 计算是否当前小碎片在第一层还是第二层, 三元表达式
        u = (lambda: 80 if 25 < ut[_] else 0)()
        # 将裁切下来小碎片的数据存储
        image2 = image.crop((c, u, c + 10, u + 80))
        # 当存储量达到26, 则重置小碎片的放置坐标, 每层只能放26小碎片
        if _ == 26:
            k = 0
        if _ > 25:
            # 第二层
            new_image.paste(image2, (k, 80))
            k += 10
        else:
            # 第一层
            new_image.paste(image2, (k, 0))
            k += 10
    if save_file:
        if save_file_path:
            new_image.save(save_file_path + '.png')
        else:
            # 保存最终图片  随机名称
            new_image.save(''.join(str(time.time()).split('.') + [".png"]))
    buffered = io.BytesIO()
    # 将数据写入buffered里
    new_image.save(buffered, format="PNG")
    return {'base64': base64.b64encode(buffered.getvalue()).decode()}
'''
:param b_puzzle_path:  本地滑块背景图的路径 可处理3.0极验
:param save_file:  是否保存最终修改后的图片 默认False
:param save_file_path:  保存最终修改后的图片名称，不含后缀    默认：自动生成文件名称
:return: base64图片
'''

print(background_reduction('4e7f20fb8.jpg', True, '2'))