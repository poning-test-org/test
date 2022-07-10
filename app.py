from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/system")
def system():
    return os.system("ls")


@app.route("/system2")
def system2():
    return os.system(request.args["command"])


@app.route("/system3")
def system3():
    return os.system(request.args["x"])
