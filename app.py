import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/quotes/quotesText.txt',
                   './_data/quotes/quotesDocx.docx',
                   './_data/quotes/quotesPDF.pdf',
                   './_data/quotes/quotesCSV.csv']

    quotes = [quote for quote_file in quote_files
              for quote in Ingestor.parse(quote_file)]

    images_path = "./_data/photos/"

    imgs = [images_path + image for image in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = requests.get(img_url, allow_redirects=True)
    tmp = f'./tmp/{random.randint(0, 100000000)}.png'
    open(tmp, 'wb').write(r.content)

    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
