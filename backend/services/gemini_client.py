import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def build_prompt(user_message, resources, articles):
    resources_text = ""

    for resource in resources:
        resources_text += (
            "Name: "
            + resource.get("name", "Unknown resource")
            + "\nAddress: "
            + resource.get("address", "No address available")
            + "\nType: "
            + resource.get("category", "Support resource")
            + "\n\n"
        )

        articles_text = ""

        for article in articles:
            articles_text += (
                "Title: "
                + article.get("title", "Unknown article")
                + "\nSummary: "
                + article.get("summary", "No summary available")
                + "\n\n"
            )

        prompt = (
            "The user is looking for support after a difficult or traumatic situation.\n\n"
            + "User message:\n"
            + user_message
            + "\n\nNearby resources:\n"
            + resources_text
            + "\nTrusted articles:\n"
            + articles_text
            + "\nGive the user a short and supportive recommendation. "
            + "Only use the resources and articles listed above. "
            + "Do not diagnose the user, provide therapy, or invent information. "
            + "If the user may be in immediate danger, tell them to contact emergency services."
        )

        return prompt


def get_recommendation(user_message, resources, articles):
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        return "Gemini recommendation is unavailable."

    prompt = build_prompt(user_message, resources, articles)

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text

        return "We could not create a recommendation right now."

    except Exception as error:
        print("Gemini error", error)
        return "We could not create a recommendation right now."
