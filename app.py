"""Handle the flask web app."""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import *
from MemeEngineModule import *
from PIL import Image
from datetime import datetime

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    temp_path = f"./tmp/meme_tmp{datetime.now().strftime('%H_%M_%S')}.jpg"

    url = request.form['image_url']

    img = requests.get(url, stream=True, allow_redirects=True).content
    # write the image to a temp file
    with open(temp_path, "wb") as outfile:
        outfile.write(img)

    web_meme = MemeEngine("./static")
    # create the meme
    body = request.form['body']
    author = request.form['author']
    path = web_meme.make_meme(temp_path, body, author)
    # remove the temporary file
    os.remove(temp_path)
    print("The path is: ", path)
    print("Looking at: ", os.getcwd())
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
