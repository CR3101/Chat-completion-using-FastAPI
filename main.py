from fastapi import FastAPI
from typing import Optional,List
import os
#import httpx
from datetime import datetime
from database import SessionLocal
from database import q_and_a
from dotenv import load_dotenv
import requests

load_dotenv()  # take environment variables from .env.
app=FastAPI()
open_api_key=os.environ.get("OPEN_API_KEY")
print(open_api_key)

#to interact with openapi

def get_openapi_response(question:str,max_tokens:int=100)->str:
    headers={"Authorization":f"Bearer {open_api_key}"}
    response=requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json={"model":"gpt-3.5-turbo","messages":[{"role":"system","content":"You are a helpful assistant."},
                                                      {"role":"user","content":question}],"max_tokens":int(max_tokens)}
        )
        # async with httpx.AsyncClient() as client:
    #     response=await client.post(
    #         "https://api.openai.com/v1/chat/completions",
    #         headers=headers,
    #         json={"model":"gpt-3.5-turbo","messages":[{"role":"system","content":"You are a helpful assistant."},
    #                                                   {"role":"user","content":question}]}
    #     )
    # return response.json()["choices"][0]["message"]["content"]
    return response.json()

db=SessionLocal()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def ask_question(question:str):
    start_time=datetime.utcnow()
    # answer=await get_openapi_response(question)
    answer=get_openapi_response(question)
    end_time=datetime.utcnow()
    response_time=(end_time-start_time).total_seconds()
    # qa_record=q_and_a(question=question,answer=answer,response_time=response_time)
    # db.add(qa_record)
    # db.commit()
    # db.refresh(qa_record)
    return{"question":question,"answer":answer,"response time":response_time}

@app.get("/history")
def get_history():
    # history=db.query(q_and_a).all()
    # return history
    pass


    
