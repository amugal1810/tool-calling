# tools.py
from openfda.client import (
    search_recalls_from_openfda,
    count_classification,
    count_top_firms,
    get_many_for_year_stats,
    count_recalls_by_state
)
from openfda.transforms import normalize_recall, aggregate_by_year

async def tool_search_recalls(query=None, classification=None, limit=10):
    search_parts = []
    if query:
        search_parts.append(f"product_description:{query}")
    if classification:
        search_parts.append(f'classification:"{classification}"')
    search_str = " AND ".join(search_parts) if search_parts else None
    raw = await search_recalls_from_openfda(search_str, limit=limit)
    return [normalize_recall(r) for r in raw]

async def tool_get_recall_stats():
    class_counts = await count_classification()
    firms = await count_top_firms(limit=10)
    many = await get_many_for_year_stats()
    years = aggregate_by_year(many)
    total = sum(item["count"] for item in class_counts)
    by_state = await count_recalls_by_state()
    return {
        "totalCount": total,
        "recallsByClassification": [{"classification": c["term"], "count": c["count"]} for c in class_counts],
        "topFirms": [{"firmName": f["term"], "count": f["count"]} for f in firms],
        "recallsByYear": years,
        "recallsByState": by_state,
    }
