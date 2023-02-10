# Webscraper
This is a web scraping project to automate repetitive time series data collection.


## How it works

Create necessary virtual environment and download necessary packages using:

```bash
conda create --name reits-analytics python=3.11
conda activate reit-analytics
pip install -r requirements.txt
```

To run the scraper, input below into the terminal:

```bash
python -m src.scraper
```

To run dashboard, input below into the terminal:

```bash

```

## Folder Structure

```bash
.
|   .gitignore
|   README.md
|   requirements.txt
+---app
|   |   scraper.py
|   |   test.ipynb
|   |
\---data
        output.csv
```