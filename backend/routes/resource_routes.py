from flask import Blueprint, jsonify, render_template, request

from backend.services.location_client import get_user_location
from backend.services.google_maps_client import search_resources
from backend.services.gemini_client import get_recommendation
from backend.services.articles_client import search_articles
from backend.utils.geo import zip_to_latlng

resources_bp = Blueprint("resources", __name__)

IDENTITY_QUERY_TERMS = {
    "lgbtq": "LGBTQ+ affirming",
    "black": "Black therapist",
    "latino": "Latino Hispanic therapist",
    "asian": "Asian American therapist",
    "indigenous": "Indigenous Native American therapist",
}

COMMUNITY_QUERY_TERMS = "free grief support group community center hospice religious"


@resources_bp.route("/resources")
def resources_page():
    return render_template("resources.html")


@resources_bp.route("/api/resources", methods=["GET"])
def get_resources():
    query = request.args.get("query", "").strip()
    zip_code = request.args.get("zip_code", "").strip()
    identity = request.args.get("identity", "").strip()
    include_community = request.args.get("include_community") == "1"

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

    if zip_code:
        latitude, longitude = zip_to_latlng(zip_code)
        if latitude is None:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": f"We couldn't find location data for ZIP {zip_code}. Try another ZIP code.",
                    }
                ),
                400,
            )
    else:
        location = get_user_location()

        if location.get("success"):
            latitude = location.get("latitude")
            longitude = location.get("longitude")

    identity_term = IDENTITY_QUERY_TERMS.get(identity)
    search_query = f"{identity_term} {query}" if identity_term else query

    resources = search_resources(
        query=search_query,
        latitude=latitude,
        longitude=longitude,
    )

    if include_community:
        community_query = (
            f"{identity_term} {COMMUNITY_QUERY_TERMS}" if identity_term else COMMUNITY_QUERY_TERMS
        )
        community_resources = search_resources(
            query=community_query,
            latitude=latitude,
            longitude=longitude,
        )
        seen = {(r.get("name"), r.get("address")) for r in resources}
        for r in community_resources:
            key = (r.get("name"), r.get("address"))
            if key not in seen:
                resources.append(r)
                seen.add(key)

    resources.sort(key=lambda r: r.get("rating") or 0, reverse=True)

    articles = search_articles(query)

    recommendation = get_recommendation(
        search_query,
        resources,
        articles,
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