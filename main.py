from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from typing import Any
from pydantic import BaseModel


app = FastAPI(
    title="Get Request - psami",
    description="Get Request Parameters of an api call",
    version="1.0.0",
)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/request")
async def get_request(body: BaseModel, request: Request):
    req_body = await request.json()
    headers = request.headers
    url = request.url
    query_params = request.query_params

    return {
        "body": req_body,
        "headers": headers,
        "url": url,
        "query_params": query_params._dict
    }
    
