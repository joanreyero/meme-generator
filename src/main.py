import argparse
import os
import random

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

#print(Ingestor.parse('./data/cats.csv'))
# print(Ingestor.parse('./data/cats.docx'))
# print(Ingestor.parse('./data/cats.pdf'))
# print(Ingestor.parse('./data/cats.txt'))

#meme = MemeEngine('/Users/joanreyero/Dropbox/meme-generator')
#meme.make_meme('/Users/joanreyero/Dropbox/meme-generator/src/_data/photos/dog/xan#der_1.jpg', 'Make America Great Again', 'Trump')


def main():
    if not args.image:
        images_path = '_data/photos/dog/'
        image = images_path + random.choice(os.listdir(images_path))

    if not args.quote:
        quotes_path = '_data/quotes/'
        quote = random.choice(
            Ingestor.parse(
                quotes_path + random.choice(
                    os.listdir(quotes_path))))

    meme_generator = MemeEngine('./static')
    meme_generator.make_meme(image, quote.body, quote.author)



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
