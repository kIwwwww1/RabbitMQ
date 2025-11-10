import time
import pika
from config import get_connection, MQ_ROUTING_KEY
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

def process_new_message(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
    # Аннотацию делаем что бы IDE показывал методы объектов
    print(f'[ ] Обрабатываем сообщение {body.decode()}')
    start = time.time()
    time.sleep(2)
    end = time.time() - start
    print(f'[*] Обработали сообщение {body.decode()} за {end:.3}')
    ch.basic_ack(delivery_tag=method.delivery_tag) 
    # ch.basic_ack(delivery_tag=method.delivery_tag) 
    # Подтверждает отправку
    
    # Гарантирует отправку если не произошло никакой ошибки при работе.
    # а если произойдет ошибка то сообщение не потеряется и при перезапуске или вкл программы
    # сообщение отправится

def consume_messages(channel: BlockingChannel):
    channel.basic_consume(queue=MQ_ROUTING_KEY, 
            on_message_callback=process_new_message, 
            # auto_ack=True
            # если возникнет ошибка при отправке то сообщение потеряется
            )
    channel.start_consuming()

def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_messages(channel=channel)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Buy!')