CURATED_RESOURCES = [
    {
        "title": "What's Your Grief",
        "summary": "A library of down-to-earth, practical articles on coping with loss, written by grief counselors -- not clinical definitions.",
        "url": "https://whatsyourgrief.com/",
        "image": "https://images.unsplash.com/photo-1701634441311-e624c7fdfedf?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "coping", "education"],
    },
    {
        "title": "Coping with Grief and Loss (HelpGuide.org)",
        "summary": "A nonprofit mental-health guide walking through healthy ways to process loss and grieve, with concrete coping strategies.",
        "url": "https://www.helpguide.org/mental-health/grief/coping-with-grief-and-loss",
        "image": "https://images.unsplash.com/photo-1521002988617-015f06b816cc?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "coping", "stress"],
    },
    {
        "title": "The Dougy Center Grief Support Resources",
        "summary": "Resources for grieving children, teens, young adults, and the parents/caregivers supporting them, from a nonprofit running peer grief support groups since 1982.",
        "url": "https://www.dougy.org/grief-support-resources",
        "image": "https://images.unsplash.com/photo-1439920120577-eb3a83c16dd7?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "children", "family"],
    },
    {
        "title": "Modern Loss",
        "summary": "Candid personal essays from people navigating loss of every kind -- for when you want to feel less alone rather than read a clinical overview.",
        "url": "https://modernloss.com/",
        "image": "https://images.unsplash.com/photo-1603136324205-01cdebce04ab?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "essays"],
    },
    {
        "title": "National Alliance for Children's Grief",
        "summary": "A national organization focused entirely on supporting grieving children and the families around them, including a directory of local support groups.",
        "url": "https://nacg.org/",
        "image": "https://images.unsplash.com/photo-1565340419825-cd1ac212cbce?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "children", "family"],
    },
    {
        "title": "Option B",
        "summary": "Resilience-focused guidance co-founded by Sheryl Sandberg after her husband's death, including real workplace bereavement-leave guidance and a large peer community.",
        "url": "https://optionb.org/",
        "image": "https://images.unsplash.com/photo-1625562105714-581fdc5c8ee5?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "coping", "family"],
    },
    {
        "title": "Grief (Psychology Today)",
        "summary": "An evidence-based overview that debunks common grief myths like the \"five stages,\" explains disenfranchised grief, and includes a therapist finder filtered for grief specialists.",
        "url": "https://www.psychologytoday.com/us/basics/grief",
        "image": "https://images.unsplash.com/photo-1519791883288-dc8bd696e667?w=320&h=220&fit=crop&auto=format",
        "tags": ["grief", "education", "anxiety", "stress"],
    },
]


FALLBACK_TITLES = {"What's Your Grief", "Coping with Grief and Loss (HelpGuide.org)"}


def search_articles(query):
    """Matches `query` against each resource's tags/title/summary. Returns
    the curated list unfiltered if the query is empty, and a couple of
    broad starting points (not []) if nothing matches -- an empty result
    for a genuine grief-adjacent search is worse than an imperfect one.
    """
    term = (query or "").strip().lower()
    if not term:
        return list(CURATED_RESOURCES)

    matches = [
        r
        for r in CURATED_RESOURCES
        if term in r["title"].lower()
        or term in r["summary"].lower()
        or any(term in tag for tag in r["tags"])
    ]

    if matches:
        return matches

    return [r for r in CURATED_RESOURCES if r["title"] in FALLBACK_TITLES]