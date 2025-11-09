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


# queue_declare(queue='hello', durable=True)
# Создаёт очередь с именем hello, если её ещё нет.
# durable=True делает очередь устойчивой — она сохранится после перезапуска RabbitMQ.



# exchange_declare(exchange='logs', exchange_type='direct')
# Что делает:
# Создаёт exchange (обменник) с именем logs.
# exchange_type='direct' — тип маршрутизации сообщений (direct, fanout, topic, headers).
# Зачем нужна:
# Exchange решает, куда отправлять сообщения внутри RabbitMQ.


# queue_bind(exchange='logs', queue='error_queue', routing_key='error')
# Что делает:
# Связывает очередь error_queue с exchange logs.
# routing_key='error' — фильтр, который определяет, какие сообщения попадут в очередь.
# Зачем нужна:
# Без бинда очередь не будет получать сообщения из exchange.


# basic_publish(exchange='logs', routing_key='error', body='Message')
# Что делает:
# Отправляет сообщение (body) в exchange с указанным routing_key.
# Зачем нужна:
# Это фактическая отправка сообщения, аналог producer.send(...) в других системах.


# basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
# Что делает:
# Подписывает consumer на очередь hello
# callback — функция, которая будет вызвана для обработки каждого сообщения.
# auto_ack=True — автоматически подтверждает получение сообщения после обработки.
# Зачем нужна:
# Чтобы consumer получал сообщения и обрабатывал их.


# start_consuming()
# Что делает:
# Запускает бесконечный цикл ожидания сообщений.
# Consumer "сидит" и ждёт, пока в очередь придут новые сообщения.
# Зачем нужна:
# Без этого consumer не будет получать сообщения, даже если подписан на очередь.






