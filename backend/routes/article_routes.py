from flask import Blueprint, jsonify, request

from backend.services.articles_client import search_articles

article_routes = Blueprint("article_routes", __name__)


@article_routes.route("/api/articles", methods=["GET"])
def get_articles():
    query = request.args.get("query", "").strip()

    if not query:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Please enter a search topic.",
                }
            ),
            400,
        )

    articles = search_articles(query)

    return jsonify(
        {
            "success": True,
            "query": query,
            "articles": articles,
        }
    )
