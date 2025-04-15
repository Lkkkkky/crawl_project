
> 2024年1月2日

## 0.安装[betterproto](https://github.com/danielgtaylor/python-betterproto)
```shell
pip install betterproto
```
注意`betterproto`版本为`2.0.0b6`，必须为2.0以上版本
## 1.在当前目录下打开终端，输入：
```shell
protoc -I . --python_betterproto_out=. douyin.proto
```
当前目录下生成文件`douyin.py`和`__init__.py`即为成功（此程序已经生成可用）。

## Done