# main.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import AsyncOpenAI
import json

from function_schemas import search_recalls_schema, get_recall_stats_schema
from tools import tool_search_recalls, tool_get_recall_stats


client = AsyncOpenAI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class AskRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask(req: AskRequest):
    user_question = req.question

    # First LLM call (decide whether to call a tool)
    response = await client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": user_question}],
        tools=[search_recalls_schema, get_recall_stats_schema]
    )

    msg = response.choices[0].message

    # If the model requested a tool
    if msg.tool_calls:

        call = msg.tool_calls[0]
        name = call.function.name
        raw_args = call.function.arguments

        # Ensure tool arguments are parsed correctly
        if isinstance(raw_args, str):
            try:
                args = json.loads(raw_args)
            except Exception:
                args = {}
        else:
            args = raw_args or {}
        
        print(call)
        result = None
        # Call the correct tool
        if name == "search_recalls":
            result = await tool_search_recalls(**args)
        elif name == "get_recall_stats":
            result = await tool_get_recall_stats()
        # else:
        #     result = {"error": "Unknown tool called"}

        # Second LLM call (final natural-language summary)
        print(result)
        final = await client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "user", "content": user_question},
                msg,
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(result)
                },
            ]
        )

        return {"answer": final.choices[0].message.content}

    # No tool: return direct answer
    return {"answer": msg.content}
