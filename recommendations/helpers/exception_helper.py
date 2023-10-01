"""Module helper."""
import grpc


def catch_exception(func):
    """try catch decorator"""

    async def wrapper(self, request, context):
        try:
            return await func(self, request, context)
        except grpc.RpcError() as error:
            await context.abort(grpc.StatusCode.FAILED_PRECONDITION, f"{error}")

    return wrapper
