search_recalls_schema = {
    "type": "function",
    "function": {
        "name": "search_recalls",
        "description": "Search FDA drug recalls",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "classification": {
                    "type": "string",
                    "enum": ["Class I", "Class II", "Class III"]
                },
                "limit": {"type": "number"}
            },
            "required": []
        }
    }
}

get_recall_stats_schema = {
    "type": "function",
    "function": {
        "name": "get_recall_stats",
        "description": "Get summary stats about drug recalls",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
}
