from flask import Flask, render_template
from api.bug.routes import bug_bp

app = Flask(__name__)
app.static_folder = "public"
app.register_blueprint(bug_bp, url_prefix="/api/bug")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


app.run(port=3030, debug=True)
