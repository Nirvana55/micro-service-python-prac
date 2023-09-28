import asyncio
from prisma import Prisma
import grpc
from concurrent import futures
from generated.recommendation_pb2_grpc import add_RecommendationsServicer_to_server
from services.recommendation import RecommendationService


async def main() -> None:
    try:
        db = Prisma(auto_register=True)
        await db.connect()
        server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
        add_RecommendationsServicer_to_server(RecommendationService(), server)
        server.add_insecure_port("[::]:50051")
        await server.start()
        print("i have started")
        await server.wait_for_termination()
    except Exception as e:
        print(f"An error occurred {e}")
    finally:
        await db.disconnect()
        await server.stop()
        print("i am disconnected")


if __name__ == "__main__":
    asyncio.run(main())
