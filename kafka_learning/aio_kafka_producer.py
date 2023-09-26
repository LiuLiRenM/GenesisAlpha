import asyncio
import time

from aiokafka import AIOKafkaProducer
from loguru import logger


async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers=[
            "192.168.31.19:9092",
            "192.168.31.19:9093",
            "192.168.31.19:9094",
        ]
    )
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        job_id = time.time_ns()
        message = f"[{job_id}] Super message."
        # Produce message
        await producer.send_and_wait("my_topic", str.encode(message))
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


async def bulk_production_messages():
    """
    批量生产消息

    :return:
    """
    loop = 10000
    for i in range(loop):
        logger.info(f"[{i}] Create a message.")
        await send_one()
    logger.info(f"Finished.")


if __name__ == "__main__":
    asyncio.run(bulk_production_messages())
