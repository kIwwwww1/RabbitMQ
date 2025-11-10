import pika

RMQ_HOST = '0.0.0.0'
RMQ_PORT = 5672

MQ_ROUTING_KEY = 'hello'

connection_params = pika.ConnectionParameters(host=RMQ_HOST, port=RMQ_PORT)

def get_connection():
    return pika.BlockingConnection(parameters=connection_params)