import json, time, ast, traceback, logging, requests
from pymongo import MongoClient

from typing import Optional
from fastapi import FastAPI, Request, HTTPException, Response, WebSocket, Security, Depends
from fastapi.responses import PlainTextResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import pickle
import os.path
from googleapiclient.discovery import build
from google.auth.transport.requests import Request as GRequest
from google.oauth2.credentials import Credentials
from oauth2client import client as InstalledAppFlow
import fuzzywuzzy.process as fw

from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from google.oauth2 import id_token
from google.auth.transport import requests
from jose import JWTError, jwt
