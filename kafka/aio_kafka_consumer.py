import asyncio

from aiokafka import AIOKafkaConsumer


async def consume():
    consumer = AIOKafkaConsumer(
        "my_topic",
        bootstrap_servers=[
            "192.168.31.19:9092",
            "192.168.31.19:9093",
            "192.168.31.19:9094",
        ],
        group_id="my-group",
    )
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print(
                "consumed: ",
                msg.topic,
                msg.partition,
                msg.offset,
                msg.key,
                msg.value,
                msg.timestamp,
            )
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
