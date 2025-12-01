import os
import re
from typing import Optional

import requests
from constants import *
from dotenv import load_dotenv


def get_headers() -> dict:
    headers = {}
    load_dotenv()
    COOKIE_VAR = os.getenv("COOKIE")
    USER_AGENT = os.getenv("USER-AGENT")
    if COOKIE_VAR is not None and COOKIE_VAR != "PUT_COOKIE_HERE":
        COOKIE = re.findall("[0-9a-f]+", COOKIE_VAR)
        if len(COOKIE) != 1:
            assert "Invalid cookie."
        else:
            headers["Cookie"] = f"session={COOKIE[0]}"
    if USER_AGENT is not None and USER_AGENT != "PUT_USER_AGENT_HERE":
        headers["User-Agent"] = USER_AGENT

    return headers


def scrape_articles(day: int, headers: dict) -> list[str]:
    headers["Referer"] = ARTICLE_REFERER
    article_resp = requests.get(
        ARTICLE_ENDPOINT.replace("XX", str(day)), headers=headers
    )

    if article_resp.status_code == 404:
        assert f"Day {str(day)} article is not out yet.\nText: {article_resp.text}"

    articles = re.findall(ARTICLE_RE, article_resp.text)

    if len(articles) == 0:
        assert f"Could not scrape article. Status code: {article_resp.status_code}"

    return articles


def scrape_inputs(day: int, headers: dict, articles: Optional[list[str]]) -> list:
    headers["Referer"] = INPUT_REFERER
    input_resp = requests.get(INPUT_ENDPOINT.replace("XX", str(day)), headers=headers)

    if input_resp.status_code == 404:
        assert f"Day {str(day)} input is not out yet.\nResponse: {input_resp.text}"

    inputs = [input_resp.text.strip(), "Failed to scrape", "Failed to scrape"]

    if not articles:
        headers["Referer"] = ARTICLE_REFERER
        articles = scrape_articles(day, headers)

    for part, article in enumerate(articles, start=1):
        codeblocks = re.findall(INPUT_FROM_ARTICLE_RE, article)
        if len(codeblocks) >= 1:
            inputs[part] = codeblocks[0].strip()[11:-13].strip()

    return inputs
