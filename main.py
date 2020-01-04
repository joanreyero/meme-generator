import argparse
import os
import random

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine


def main():
    """Generates a meme and returns the output path.
    If an image, text and author are provided, they are used.
    Otherwise random inputs from the system are used.
    """
    if not args.image:
        images_path = '_data/photos/'
        image = images_path + random.choice(os.listdir(images_path))

    if not args.quote:
        quotes_path = '_data/quotes/'
        quote = random.choice(
            Ingestor.parse(
                quotes_path + random.choice(
                    os.listdir(quotes_path))))

    meme_generator = MemeEngine('./static')
    return meme_generator.make_meme(image, quote.body, quote.author)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate a meme")
    parser.add_argument('--quote', '-q', type=str,
                        help="The body of the quote.")
    parser.add_argument('--author', '-a', type=str,
                        help="The author of the quote.")
    parser.add_argument('--image', '-i', type=str,
                        help="An image path")

    args = parser.parse_args()
    image = args.image
    quote = args.quote
    author = args.author
    main()
