import uuid

def generate_device_id():
    # 生成随机UUID
    random_uuid = uuid.uuid4()
    # 转换为大写的字符串格式
    device_id = str(random_uuid).upper()
    return device_id

if __name__ == '__main__':
    # 生成并打印一个新的设备ID
    new_device_id = generate_device_id()
    print(f'生成的设备ID: {new_device_id}')