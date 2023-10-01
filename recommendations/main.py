"""Module main."""
import asyncio
from concurrent import futures
from prisma import Prisma
import grpc
from generated_recommendations.recommendation_pb2_grpc import (
    add_RecommendationsServicer_to_server,
)
from services.recommendation import RecommendationService


async def main() -> None:
    """main db"""
    try:
        database = Prisma(auto_register=True)
        await database.connect()
        server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
        add_RecommendationsServicer_to_server(RecommendationService(), server)
        server.add_insecure_port("[::]:50051")
        await server.start()
        print("i have started")
        await server.wait_for_termination()
    except ImportError as error:
        print(f"An import error occurred {error}")
    except ConnectionError as error:
        print(f"An connection error occurred {error}")
    except grpc.RpcError as error:
        print(f"An rpc error occurred {error}")
    finally:
        await database.disconnect()
        await server.stop(None).wait()
        print("i am disconnected")


if __name__ == "__main__":
    asyncio.run(main())
