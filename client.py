import requests
import json

while(1):
    req = input("Enter the input: ")
    try:
        req=int(req)
    except Exception as e:
        print("Please Enter a valid Input")

    if(req==1):
        id=input("Enter student id ")
        name=input("Enter student name ")
        stream=input("Enter student Stream ")
        data={"id":id,"name":name,"stream":stream}
        response =requests.post('http://localhost:8000/create',json=data).content
        print(response)

    elif(req==2):
        response = requests.get('http://localhost:8000/read').content
        print(response)

    elif(req==3):
        id=input("Enter student id ")
        name=input("Enter student name ")
        stream=input("Enter student Stream ")
        data={"id":id,"name":name,"stream":stream}
        response =requests.put('http://localhost:8000/update',json=data).content
        print(response)

    elif(req==4):
        id=input("Enter Student id ")
        response =requests.delete('http://localhost:8000/delete/{}'.format(id)).content
        print(response)
    
    elif(req==5):
        exit
    else:
        print("Please Enter an valid Input")