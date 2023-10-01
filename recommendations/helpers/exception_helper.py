"""Module try catch helper."""
import grpc
from pydantic import ValidationError


def catch_exception(func):
    """try catch decorator"""

    async def wrapper(self, request, context):
        try:
            return await func(self, request, context)
        except RuntimeError as error:
            await context.abort(grpc.StatusCode.INTERNAL, f"{error}")
        except grpc.RpcError as error:
            await context.abort(grpc.StatusCode.INTERNAL, f"{error}")
        except ValidationError as error:
            await context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(error))

    return wrapper
