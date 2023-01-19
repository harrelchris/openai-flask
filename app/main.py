import os

import dotenv
from flask import Flask, render_template, request
import openai

dotenv.load_dotenv()

openai.organization = os.getenv("ORGANIZATION_ID")
openai.api_key = os.getenv("API_KEY")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    text = request.form["text"]
    response = openai.Image.create(
        prompt=text,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return render_template("submit.html", text=text, image_url=image_url)
