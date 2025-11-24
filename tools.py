# tools.py
from openfda.client import (
    search_recalls_from_openfda,
    count_classification,
    count_top_firms,
    get_many_for_year_stats,
    count_recalls_by_state
)
from openfda.transforms import normalize_recall, aggregate_by_year

async def tool_search_recalls(
    query=None,
    classification=None,
    state=None,
    firm=None,
    status=None,
    # start_date=None,
    # end_date=None,
    limit=10
):
    filters = []

    if query:
        filters.append(f"search={query}")

    if classification:
        filters.append(f"classification:\"{classification}\"")

    if state:
        filters.append(f"state:\"{state}\"")

    if firm:
        # recall field is "recalling_firm"
        filters.append(f"recalling_firm:\"{firm}\"")

    if status:
        filters.append(f"status:\"{status}\"")

    # if start_date and end_date:
    #     filters.append(f"recall_initiation_date:[{start_date} TO {end_date}]")
    # elif start_date:
    #     filters.append(f"recall_initiation_date:[{start_date} TO 99999999]")
    # elif end_date:
    #     filters.append(f"recall_initiation_date:[00000000 TO {end_date}]")

    search_expr = " AND ".join(filters) if filters else None
    raw = await search_recalls_from_openfda(search_expr, limit=limit)
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
