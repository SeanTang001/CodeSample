import json, time, ast, traceback, logging, requests
from pymongo import MongoClient

from typing import Optional
from fastapi import FastAPI, Request, HTTPException, Response, WebSocket, Security, Depends
from fastapi.responses import PlainTextResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta
import pickle
import os.path
import pprint
from fastapi.middleware.cors import CORSMiddleware

# from googleapiclient.discovery import build
# from google.auth.transport.requests import Request as GRequest
# from google.oauth2.credentials import Credentials
# from oauth2client import client as InstalledAppFlow
# import fuzzywuzzy.process as fw

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from jose import JWTError, jwt

app = FastAPI()

origins = [
    "http://127.0.0.1:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = MongoClient()

@app.get("/a/{category}")
async def getInventoryByCategory(request: Request, category:str):
    data = client["inventory"][category].find({},{"_id":False})
    #pprint.pprint(list(data))
    return {"data":list(data)}

@app.get("/b/{category}/{address}")
async def getInventoryByCategoryAdress(category:str, address:str):
    data = client["inventory"][category].find({"address":address},{"_id":False})
    return {"data":list(data)}
