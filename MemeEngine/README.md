# MemeEngine
The `MemeEngine` module consists of a class `MemeEngine` to generate memes given an image, a quote and an author for the quote.

## Usage

First, instantiate a `MemeGenerator` object, specifying an output directory
```
meme_generator = MemeGenerator('./static')
```
Then call the `make_meme` function with an image, a quote body and an author to make a meme:
```
meme_generator.make_meme(path_to_image, body, author)
```
The meme will be saved in the pre-defined output directory.

## Dependencies
- Pillow 7.0.0
- Numpy 1.18.0
