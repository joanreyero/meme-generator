# Quote Engine
The module consists of 7 classes:

- `QuoteMode`: The quote object, which contains the quote's body and author.
- `IngestorInterface`: The abstract class for the 4 ingesting methods:
    1. `CSVIngestor`: parses quotes from a CSV file (format: `body,author`).
    2. `PDFIngestor`: parses quotes from a PDF file (format: `body - author`).
    3. `DocxIngestor`: parses quotes from a Word file (format: `body - author`).
    4. `TextIngestor`: parses quotes from a text file (format: `body - author`).
- `Ingestor`: The class to realise the proper Ingestor given an input file, from the 4 above.

The module, given a file in any of the above formats, will parse the quotes and create a list of `QuoteMode` objects from the file.

## Usage
Import the module
```
from QuoteEngine import Ingestor
```
And parse a file, getting a list of `QuoteMode`.
```
quotes = Ingestor.parse(path_to_file)  # either .csv, .txt, .docx, .pdf
```

## Dependencies
- List
- abc
- Pandas 0.25.3
- python-docx 0.8.10
- subprocess
- pdfx