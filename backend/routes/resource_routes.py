from flask import Blueprint, jsonify, request

from services.location_client import get_location
from services.google_maps_client import search_resources
from services.gemini_client import get_recommendation
from services.articles_client import search_articles

resource_routes = Blueprint("resource_routes", __name__)


@resource_routes.route("/api/resources", methods=["GET"])
def get_resources():
    query = request.args.get("query", "").strip()
    zip_code = request.args.get("zip_code", "").strip()

    if not query:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Please enter a resource type.",
                }
            ),
            400,
        )

    latitude = None
    longitude = None

    if not zip_code:
        location = get_location()

        if location.get("success"):
            latitude = location.get("latitude")
            longitude = location.get("longitude")

    resources = search_resources(
        query=query,
        latitude=latitude,
        longitude=longitude,
        zip_code=zip_code or None,
    )

    articles = search_articles(query)

    recommendation = get_recommendation(
        query,
        resources,
    )

    return jsonify(
        {
            "success": True,
            "query": query,
            "resources": resources,
            "articles": articles,
            "recommendation": recommendation,
        }
    )
