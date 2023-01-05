import logging

from flask import Flask, request, render_template, send_from_directory
from loader.views import loader_blueprint
from main.views import main_blueprint

logging.basicConfig(filename='hzzchem.log', level=logging.INFO)

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(loader_blueprint)
app.register_blueprint(main_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path=path)

app.run()

