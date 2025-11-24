# openfda/transforms.py
def normalize_recall(raw: dict) -> dict:
    return {
        "id": raw.get("recall_number"),
        "classification": raw.get("classification"),
        "productName": raw.get("product_description"),
        "firmName": raw.get("firm_name"),
        "status": raw.get("status"),
        "recallInitiationDate": raw.get("recall_initiation_date"),
        "state": raw.get("state"),
        "reasonForRecall": raw.get("reason_for_recall"),
    }

def aggregate_by_year(recalls):
    counts = {}
    for r in recalls:
        date = r.get("recall_initiation_date")
        if not date or len(date) < 4:
            continue
        year = date[:4]
        counts[year] = counts.get(year, 0) + 1
    return [{"year": y, "count": c} for y, c in sorted(counts.items())]
