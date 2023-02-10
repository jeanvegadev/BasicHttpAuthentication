from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def login():
    try:
        encode = request.headers["Authorization"].split(" ")[1]
    except:
        encode = ""
    resp = Response("¡Hola mundo!")
    resp.headers['WWW-Authenticate'] = 'Basic'
    if encode == "amVhbjp2ZWdh":
        return resp, 200
    else:
        return resp, 401