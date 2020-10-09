#import pickle, os, subprocess, scraper, img_scraper, file_search
from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "200"

# @app.route("/results", methods = ["POST"])
# def results():


# @app.route("/results_default", methods = ["POST"])
# def results_default():


if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8001)
