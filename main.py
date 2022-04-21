from fastapi import FastAPI, Query
import json

app = FastAPI()


##opening the json file
with open('data.json','r') as f:
    file= json.load(f)


@app.get('/')
def home():
    return{"Hello":"World"}

##This will return all the information
@app.get('/getuser')
def get_data(page:int = Query(None, le=2)):
    for new in file:
        if new["page"]==page:
            return new
        else:
            return{"No Details"}


#This will return the information of only a specific user id
@app.get('/user')
def get_user(user_id:int=Query(None, le=12 , ge=7)):
    for new in file:
        for data in new['data']:
            if data["id"]==user_id:
                return data


    
    


