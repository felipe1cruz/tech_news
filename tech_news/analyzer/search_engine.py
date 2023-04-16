from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    data = []
    for new in news:
        data.append((new["title"], new["url"]))

    return data


# Requisito 8
def search_by_date(date):
    try:
        data_objeto = datetime.strptime(date, "%Y-%m-%d")
        data_formatada = datetime.strftime(data_objeto, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": data_formatada}}
    data = []
    news = search_news(query)
    for new in news:
        data.append((new["title"], new["url"]))

    return data


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = search_news(query)
    data = []
    for new in news:
        data.append((new["title"], new["url"]))

    return data
