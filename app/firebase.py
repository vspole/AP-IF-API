from random import randint
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models import *


cred = credentials.Certificate('FirebaseKey/ap-if-1d696-cce240a3e93f.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def getFirebaseDB():
    return db

def createGroupInFirebase(group: Group):
    isUnique = False
    uniqueGroupID = 000000
    while not isUnique:
        testGroupID = createRandomGroupID()
        isUnique = checkIfGroupUnique(testGroupID)
        if isUnique:
            uniqueGroupID = testGroupID
    data = {
        "GroupID": uniqueGroupID,
        "Longitude": group.longitude,
        "Latitude": group.latitude,
        "NumberOfUsers": group.numberOfUsers,
        "NumberDone": group.numberDone,
    }
    db.collection("groups").document(str(uniqueGroupID)).set(data)

def createRandomGroupID():
    return str(randint(100000, 999999))

def checkIfGroupUnique(testGroupID):
    doc_ref = db.collection("groups").document(str(testGroupID))
    doc = doc_ref.get()
    if doc.exists:
        return False
    else:
        return True
