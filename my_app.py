import datetime
import os
import socket

from flask import Flask, request
import redis

app = Flask(__name__)
if os.environ.get('GET_HOSTS_FROM', '') == 'dns':
    redis_server = 'redis-master'
else:
    redis_server = 'localhost'
r = redis.StrictRedis(redis_server)

@app.route("/")
def index():
    time = datetime.datetime.now().isoformat()
    hostname = socket.gethostname()
    redis_age = r.client_list()[0]['age']
    redis_age = "<b>Redis Server Age</b>: {}".format(redis_age)
    sorted_headers = sorted(request.headers)
    headers = "<br>".join(["<b>{}</b>: {}".format(x,y) for x,y in sorted_headers])
    return "<h1>{}</h1><h3>{}</h3><br>{}<br>{}".format(hostname, time, redis_age, headers)

if __name__ == "__main__":
    app.run(debug=True)
