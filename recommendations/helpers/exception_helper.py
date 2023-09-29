import grpc


async def catch_exception(func):
    try:
        func()
    except grpc.RpcError() as e:
        raise e
