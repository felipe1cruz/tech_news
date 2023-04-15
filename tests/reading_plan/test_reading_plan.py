from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch, MagicMock

mock_find_news = [
           {
            "url": "url1",
            "title": "Noticia 5min",
            "writer": "Escritor 1",
            "summary": "1 - Noticia",
            "reading_time": 5,
            "timestamp": "01/02/2022",
            "category": "Noticia",
           },
           {
            "url": "url2",
            "title": "Noticia 10min",
            "writer": "Escritor 2",
            "summary": "2 - Noticia",
            "reading_time": 10,
            "timestamp": "02/02/2022",
            "category": "Noticia",
           },
           {
            "url": "url3",
            "title": "Noticia 15min",
            "writer": "Escritor 3",
            "summary": "3 - Noticia",
            "reading_time": 15,
            "timestamp": "03/02/2022",
            "category": "Noticia",
           },
    ]


def test_reading_plan_group_news():
    mock_news = MagicMock(return_value=mock_find_news)
    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch.object(
        ReadingPlanService, "_db_news_proxy", mock_news
    ):
        result = ReadingPlanService.group_news_for_available_time(10)
        assert result == {
            "readable": [
                {
                    "unfilled_time": 5,
                    "chosen_news": [("Noticia 5min", 5)],
                },
                {
                    "unfilled_time": 0,
                    "chosen_news": [("Noticia 10min", 10)],
                },
            ],
            "unreadable": [("Noticia 15min", 15)]
        }
