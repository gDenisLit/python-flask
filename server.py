from flask import Flask, jsonify, request, send_file, render_template
import os

app = Flask(__name__)
app.static_folder = "public"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/bugs", methods=["GET"])
def get_bugs():
    
    return jsonify()


app.run(port=3030, debug=True)
