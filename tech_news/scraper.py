import requests
from time import sleep
# from parsel import Selector
# from urllib.parse import urlparse
# import re


# Requisito 1
def fetch(url: str, wait: int = 3, user_agent="Fake user-agent") -> str:
    headers = {"user-agent": user_agent}
    try:
        response = requests.get(url, headers=headers, timeout=wait)
        sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        sleep(1)
        return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
