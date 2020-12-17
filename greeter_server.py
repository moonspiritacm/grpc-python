import logging
import grpc

from concurrent import futures
from proto import helloworld_pb2
from proto import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("Recevice: " + request.name)
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)


def main():
    # 多线程服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册本地服务
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # 监听端口
    server.add_insecure_port('[::]:50051')
    # 启动服务
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    main()
