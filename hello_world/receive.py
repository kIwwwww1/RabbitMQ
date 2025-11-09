import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def main(ch, method, propertis, body):
    print(f'Получено сообщение {body.decode()}')

channel.basic_consume(queue='hello',
                      on_message_callback=main,
                      auto_ack=True)

print('Ожиданое сообщений')
channel.start_consuming()