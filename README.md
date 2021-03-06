# Meme Generator

The main module for the application. Contains the scripts to run the application from the command line and as web-app.

## Usage
### Command-line interface
Run

```
python3 main.py
```
- Arguments
    - Image path (`str`)(optional): the path to the image we want to use
    - Quote (`str`)(optional): the body of the quote
    - Author (`str`)(optional): the author of the quote

If no arguments provided, a random image, text and author from the package files will be used.

The output file is stored in `static`.

### Web interface
To start the server run
```
python3 app.py
```
To generate a random meme click on the random generator. Otherwise, you can generate your own. To generate your own, provide an image, a quote and an author.

## Dependencies
- certifi==2019.11.28
- chardet==3.0.4
- Click==7.0
- Flask==1.1.1
- idna==2.8
- itsdangerous==1.1.0
- Jinja2==2.10.3
- lxml==4.4.2
- MarkupSafe==1.1.1
- numpy==1.18.0
- pandas==0.25.3
- Pillow==7.0.0
- python-dateutil==2.8.1
- python-docx==0.8.10
- pytz==2019.3
- requests==2.22.0
- six==1.13.0
- urllib3==1.25.7
- Werkzeug==0.16.0