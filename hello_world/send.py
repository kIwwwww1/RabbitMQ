import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print('Сообщение "Hello World" отправлено')
channel.close()

# Direct Exchange — направляет сообщения в очереди, где ключ маршрутизации (routing key) точно соответствует ключу, 
# с которым очередь связана, что позволяет доставлять сообщения одной или нескольким очередям с конкретным именем.

# Fanout Exchange — «широковещательно отправляет» каждое полученное сообщение во все очереди, 
# связанные с конкретным fanout exchange, игнорируя ключ маршрутизации.

# Topic Exchange — направляет сообщения в зависимости от шаблона ключа маршрутизации, 
# что позволяет использовать подстановочные знаки;

# Headers Exchange — использует заголовки сообщений вместо ключей маршрутизации.
