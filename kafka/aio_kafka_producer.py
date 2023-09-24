import asyncio

from aiokafka import AIOKafkaProducer


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
        # Produce message
        await producer.send_and_wait("my_topic", b"Super message")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


asyncio.run(send_one())
