search_recalls_schema = {
    "type": "function",
    "function": {
        "name": "search_recalls",
        "description": (
            "Search FDA drug recalls using flexible filters. "
            "Use this tool when the user asks for recalls matching "
            "a specific drug, ingredient, company, state, date, or status. "
            "Any combination of filters may be provided."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search keyword across product_description, reason_for_recall"
                },
                "classification": {
                    "type": "string",
                    "enum": ["Class I", "Class II", "Class III"],
                    "description": "Optional recall class filter"
                },
                "state": {
                    "type": "string",
                    "description": "Filter by U.S. state code (e.g., CA, TX, NY)"
                },
                "firm": {
                    "type": "string",
                    "description": "Filter by the recalling firm (matches recall 'recalling_firm')"
                },
                "status": {
                    "type": "string",
                    "description": "Recall status (e.g., 'Ongoing', 'Completed', 'Terminated')"
                },
                # "start_date": {
                #     "type": "string",
                #     "description": "Start date for recall initiation (YYYYMMDD)"
                # },
                # "end_date": {
                #     "type": "string",
                #     "description": "End date for recall initiation (YYYYMMDD)"
                # },
                "limit": {
                    "type": "number",
                    "description": "Maximum number of results to return (default 10, max 50)"
                }
            },
            "required": []
        }
    }
}


get_recall_stats_schema = {
    "type": "function",
    "function": {
        "name": "get_recall_stats",
        "description": (
            "Return aggregated statistics about FDA drug recalls. "
            "Includes: total recall count, recalls by classification "
            "(Class I, Class II, Class III), top recalling firms "
            "(using 'recalling_firm'), recalls by U.S. state, recalls "
            "grouped by year, and optionally the most common recall "
            "reasons or top products. Use this tool whenever a user asks "
            "for summary data, rankings, trends, firm comparisons, "
            "state-level recall counts, or historical patterns."
        ),
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
}

