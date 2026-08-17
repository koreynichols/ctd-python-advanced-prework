# Country Explorer

A command-line tool that shows countries by region using data from Countries.dev API. For each region it displays countries from that region and the capital, population and area for those countries.

## API

countries.dev - https://countries.dev/countries

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to use

Run with:
```bash
python main.py
```

It will show the list of regions and ask for you to enter one and it will return all the countries from that region
