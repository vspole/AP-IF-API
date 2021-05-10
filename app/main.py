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
    doc_ref = db.collection(u'groups').document(u'321')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    return {"message": "Welcome to AP-IF part 2"}

@app.post("/createGroup", response_model = Group )
async def createGroup(group:Group):
    createGroupInFirebase(group)
    return group
