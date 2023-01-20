# Trustpilot Scraper

Scrape Trustpilot utilising Smartproxy's Web Scraping API

[<img src="https://i.ibb.co/PwMvX0P/Web.png">](https://dashboard.smartproxy.com/register?utm_source=Github&utm_medium=banner&utm_campaign=Web)

## Dependencies

```http
glom
BeautifulSoup
```

## Authentication

Once you have an active Web Scraping API subscription, you can try sending a request right from the dashboard Web Scraping API > API playground method tab simply by clicking on Send Request. You will also see an example of curl request generated on the right. 

### This Pyhton code example uses Base64 encoded ```user:pass``` authentication.

## Python scripts

| Parser type | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| HTML to JSON        | [Trustpilot_parser.py](https://github.com/Smartproxy/trustpilot_python_scraper/blob/main/Trustpilot_parser.py) |``` curl https://raw.githubusercontent.com/Smartproxy/trustpilot_python_scraper/blob/main/Trustpilot_parser.py > Trustpilot_parser.py ``` |
| JSON to JSON                 | [trustpilot_json_parser_glom.py](https://github.com/Smartproxy/trustpilot_python_scraper/blob/main/trustpilot_json_parser_glom.py)   | ``` curl https://raw.githubusercontent.com/Smartproxy/trustpilot_python_scraper/blob/main/trustpilot_json_parser_glom.py > trustpilot_json_parser_glom.py ``` |
