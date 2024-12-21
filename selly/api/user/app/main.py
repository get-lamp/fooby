from fastapi import FastAPI
from app import globals
app = FastAPI()

globals.init(app)


from app import views