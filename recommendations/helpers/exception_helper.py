"""Module helper."""
import grpc


def catch_exception(func):
    """try catch decorator"""

    async def wrapper(self, request, context):
        try:
            return await func(self, request, context)
        except RuntimeError as error:
            await context.abort(grpc.StatusCode.INTERNAL, f"{error}")
        except grpc.RpcError as error:
            await context.abort(grpc.StatusCode.INTERNAL, f"{error}")

    return wrapper
