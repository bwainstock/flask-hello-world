import socket
import datetime

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    time = datetime.datetime.now().isoformat()
    hostname = socket.gethostname()
    sorted_headers = sorted(request.headers)
    headers = "<br>".join(["<b>{}</b>: {}".format(x,y) for x,y in sorted_headers])
    return "<h1>{}</h1><h3>{}</h3><br>{}".format(hostname, time, headers)

if __name__ == "__main__":
    app.run(debug=True)
