# grpc-python

A simple grpc example in Python, referring to https://github.com/grpc/grpc/tree/master/examples/python.

## 1. 安装依赖包

```shell
pip install grpcio
pip install protobuf
pip install grpcio_tools
```

## 2. 生成协议文件

```shell
python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ helloworld.proto
```

相关参数说明如下：
- I 指定 xxxx.proto 查找路径
- python_out 指定 xxxx_pb2.py 输出路径
- grpc_python_out 指定 xxxx_pb2_grpc.py 输出路径

生成文件如下：
- xxxx_pb2.py 消息序列化类
- xxxx_pb2_grpc.py 服务器和客户端 Stub，定义 RPC 服务接口。
