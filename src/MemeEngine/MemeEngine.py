from PIL import Image, ImageDraw, ImageFont
from numpy.random import randint


class MemeEngine():
    """Meme engine class.
    Attributes:
      - output_dir {str}: the output directory
    """
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path: str,
                  text=None, author=None,
                  width=500) -> str:
        """Create a Postcard With a Text Greeting

        Arguments:
        img_path {str} -- the file location for the input image.
        text {str} -- the body of the quote.
        author {str} -- the author of the quote.
        width (def: 500px) {float} -- the width of the image.
        Returns:
        str -- the file path to the output image.
        """
        img = Image.open(img_path)

        # If a width is provided
        if width is not None:
            # resize maintaing the aspect ratio
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:  # if a text is provided
            if author is not None:  # if the author is provided
                text = f'{text}\n    - {author}'

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('_data/fonts/LilitaOne-Regular.ttf', 15)

            # Getting a random position for the text, making sure
            # all the text will show
            text_width, text_height = draw.textsize(text, font=font)
            width, height = img.size
            # A random number from the are where the text can go.
            x = randint(width - text_width, size=1)[0]
            y = randint(height - text_height, size=1)[0]

            # Making a black border for the text
            draw.text((x-2, y-2), text, font=font, fill='black')
            draw.text((x+2, y-2), text, font=font, fill='black')
            draw.text((x-2, y+2), text, font=font, fill='black')
            draw.text((x+2, y+2), text, font=font, fill='black')

            draw.text((x, y), text, font=font)

        # Save the image and return the output image and path
        out_path = f'{self.output_dir}/{img_path.split("/")[-1]}'
        img.save(out_path)
        return out_path
