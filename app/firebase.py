from random import randint
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models import *
from placesSearch import *

cred = credentials.Certificate("FirebaseKey/ap-if-1d696-06be194351d3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getFirebaseDB():
    return db

#Create GroupInfo
def createGroupInFirebase(group: Group):
    uniqueGroupID = createRandomGroupID()
    data = {
        "GroupID": uniqueGroupID,
        "Longitude": group.longitude,
        "Latitude": group.latitude,
        "NumberOfUsers": 0,
        "NumberDone": 0,
    }
    db.collection("groups").document(str(uniqueGroupID)).set(data)
    group.groupID = uniqueGroupID
    group.userID = (addCreatorToUsers(group)).userID
    addRestaurantsToGroup(group,reccursiveReastaurant(group.latitude, group.longitude, group.radius, []))
    return group

def createRandomGroupID():
    isUnique = False
    while not isUnique:
        groupID = randint(100000, 999999)
        isUnique = checkIfGroupUnique(groupID)
    return groupID

def checkIfGroupUnique(testGroupID):
    doc_ref = db.collection("groups").document(str(testGroupID))
    doc = doc_ref.get()
    if doc.exists:
        return False
    else:
        return True

#Create UserInfo
def addCreatorToUsers(group:Group):
    user = User(name=group.creatorName, groupID=group.groupID)
    return(addUserToGroupFirebase(user))

def addUserToGroupFirebase(user: User):
    user.userID = createRandomUserID(user.groupID)
    data = {
        "userID": user.userID,
        "Name": user.name,
        }
    db.collection("groups").document(str(user.groupID)).collection("Users").document(str(user.userID)).set(data)
    addToNumOfUsers(user.groupID)
    return user

def addToNumOfUsers(groupID):
    doc_ref = db.collection("groups").document(str(groupID))
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        previousNumber = data["NumberOfUsers"]
        doc_ref.update({"NumberOfUsers": previousNumber + 1})

def createRandomUserID(groupID):
    isUnique = False
    while not isUnique:
        userID = randint(100, 999)
        isUnique = checkUserIdUnique(userID,groupID)
    return userID

def checkUserIdUnique(userID,groupID):
    doc_ref = db.collection("groups").document(str(groupID)).collection("Users").document(str(userID))
    doc = doc_ref.get()
    if doc.exists:
        return False
    else:
        return True

def addRestaurantsToGroup(group:Group,listOfRestaurants):
    for restaurant in listOfRestaurants:
        data = {
            "RestaurantName": restaurant.name,
            "PriceLevel": restaurant.priceLevel,
            "Rating": restaurant.rating
            }
        db.collection("groups").document(str(group.groupID)).collection("Restaurants").document(restaurant.name).set(data)

def getRestaurantListFromFB(groupID):
    restaurantList = []
    restaurants = db.collection("groups").document(str(groupID)).collection("Restaurants").stream()
    for restaurant in restaurants:
        data = restaurant.to_dict()
        restaurantList.append(Restaurant(name=data["RestaurantName"]))
    return restaurantList
