import pika
from config import get_connection, MQ_ROUTING_KEY
from pika.adapters.blocking_connection import BlockingChannel

def produce_message(channel: BlockingChannel):
    channel.queue_declare(queue=MQ_ROUTING_KEY)
    channel.basic_publish(exchange='', routing_key=MQ_ROUTING_KEY, body='Hello World!')

def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_message(channel=channel)


if __name__ == '__main__':
    main()