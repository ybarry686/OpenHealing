import requests
import xml.etree.ElementTree as ET


def search_articles(query):
    url = "https://wsearch.nlm.nih.gov/ws/query"

    params = {
        "db": "healthTopics",
        "term": query,
        "retmax": 5,
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )
        response.raise_for_status()

        root = ET.fromstring(response.text)

    except Exception as error:
        print("MedlinePlus error:", error)
        return []

    articles = []

    for document in root.findall(".//document"):
        title = ""
        summary = ""

        for content in document.findall("content"):
            if content.get("name") == "title":
                title = "".join(content.itertext()).strip()

            elif content.get("name") == "FullSummary":
                summary = "".join(content.itertext()).strip()

        articles.append(
            {
                "title": title or "MedlinePlus article",
                "summary": summary or "No summary available",
                "url": document.get("url"),
            }
        )

    return articles
