import pickle, os, subprocess
from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("table-responsive.html")

@app.route("/trends")
def trends():
    return render_template("trends.html")

@app.route("/downloads")
def downloads():
    return render_template("downloads.html")

#AIzaSyA5aevdcRxbI2nBJ8UGTh_m7kESdN0AVqA


if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8001)
