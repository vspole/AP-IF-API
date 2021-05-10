from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models import *
from firebase import *

app = FastAPI()

db = getFirebaseDB()


@app.get("/")
async def root():
    return {"message": "Welcome to AP-IF part 2"}

@app.post("/createGroup", response_model = Group )
async def createGroup(group:Group):
    newGroup = createGroupInFirebase(group)
    return newGroup

@app.post("/addUserToGroup", response_model = User )
async def createUser(user:User):
    newUser = addUserToGroupFirebase(user)
    return newUser
