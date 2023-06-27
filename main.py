from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

logger = logging.getLogger("uvicorn.access")
logger.setLevel(logging.INFO)


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

    response =  {
        "body": req_body,
        "headers": headers,
        "url": url,
        "query_params": query_params._dict
    }

    logger.info(response)
    print(response)
    return response
    
