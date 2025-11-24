# openfda/client.py
import httpx
from typing import Optional

BASE_URL = "https://api.fda.gov/drug/enforcement.json"

async def search_recalls_from_openfda(search: Optional[str], limit: int = 10, skip: int = 0):
    params = {"limit": limit, "skip": skip}
    if search:
        params["search"] = search
    async with httpx.AsyncClient() as client:
        res = await client.get(BASE_URL, params=params)
    if res.status_code != 200:
        raise Exception(f"OpenFDA error: {res.status_code}: {res.text}")
    return res.json().get("results", [])

async def count_classification():
    async with httpx.AsyncClient() as client:
        res = await client.get(BASE_URL, params={"count": "classification.exact"})
    return res.json().get("results", [])

async def count_top_firms(limit: int = 10):
    async with httpx.AsyncClient() as client:
        res = await client.get(BASE_URL, params={"count": "firm_name.exact", "limit": limit})
    return res.json().get("results", [])

async def get_many_for_year_stats(limit: int = 1000):
    async with httpx.AsyncClient() as client:
        res = await client.get(BASE_URL, params={"limit": limit})
    return res.json().get("results", [])
