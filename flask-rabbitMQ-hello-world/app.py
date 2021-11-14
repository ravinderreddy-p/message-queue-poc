from flask import Flask, Response, request
from pykafka import KafkaClient


def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


app = Flask(__name__)


@app.route('/')
def index():
    return "Flask server is up"


@app.route('/hello-world')
def test():
    print(request.url)
    print(request.method)
    url = request.url
    return f'Flask server is Up {url}'


# Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()

    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield 'data:{0}\n\n'.format(i.value.decode())

    return Response(events(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
