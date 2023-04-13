import requests
from time import sleep
from parsel import Selector
from urllib.parse import urlparse
import re


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
    links = []
    selector = Selector(text=html_content)
    css_links = selector.css("a[href].cs-overlay-link")
    for link in css_links:
        links.append(link.attrib["href"])
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_page = selector.css(".next").attrib.get("href")
        if next_page:
            return next_page
        else:
            raise ValueError("Next page not found")
    except (ValueError, AssertionError):
        return None


# Requisito 4
def scrape_news(html_content):
    scrape = {}
    url = html_content.url
    path = urlparse(url).path
    category = path.split('/')[1]

    selector = Selector(text=html_content)
    scrape["url"] = selector.css("li.meta-reading-time::text").get()
    scrape["title"] = selector.css("h1.entry-title::text").get()
    scrape["timestamp"] = selector.css("li.meta-date::text").get()
    scrape["writer"] = selector.css("a.url.fn.n::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    tempo_leitura = re.search(r'\d+', reading_time)
    scrape["reading_time"] = int(tempo_leitura.group())
    summary = selector.css(".entry-content > p:nth-child(1)::text").get()
    scrape["summary"] = summary
    scrape["category"] = category

    return scrape


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
