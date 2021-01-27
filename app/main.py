#!/usr/bin/env python3
import sys
import ast
import base64

import uvicorn
from fastapi import FastAPI
from fastapi import Form

import grpc
from r2r import categorizer_pb2
from r2r import categorizer_pb2_grpc

from google.protobuf.json_format import MessageToJson

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/categorize")
async def categorize(offers: str = Form(...)):
    dec_offers = base64.b64decode(offers)
    channel = grpc.insecure_channel('categorizer:50051')
    stub = categorizer_pb2_grpc.CategorizerStub(channel)
    response = stub.Categorize(categorizer_pb2.CategorizationRequest(offers=dec_offers))

    return ast.literal_eval(MessageToJson(response))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5555)