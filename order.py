import requests
import json

# #Signup

# userid=input("Enter student id ")
# username=input("Enter student name ")
# password=input("Enter password ")
# data={"userid":userid,"username":username,"password":password}
# response =requests.post('http://localhost:8000/user/signup',json=data).content
# print(response)

# # # Login
# userid=input("Enter student id ")
# username=input("Enter student name ")
# password=input("Enter password ")
# data={"userid":userid,"username":username,"password":password}
# response =requests.post('http://localhost:8000/user/login',json=data).content
# print(response)

# n = input("Now you will be logged out after an input")

# # Logout
# print("Calling logout route")
# response =requests.get('http://localhost:8000/user/logout').content
# print(response)


# # Menu add
itemid=input("Enter item id ")
halfprice=input("Enter Half plate Price ")
fullprice=input("Enter Full Plate Price ")
data={"menuid":itemid,"halfprice":halfprice,"fullprice":fullprice}
response =requests.post('http://localhost:8000/menu/add',json=data).content
print(response)



# # Menu Read 
# response =requests.get('http://localhost:8000/menu/read').content
# print(response.decode())


## Transaction Entry
# 
# userid = input("Enter the Userid ")
# tip = input("Enter the tip ")
# discount = input("Enter the discount ")
# split = input("Enter the split ")
# total = input("Enter the total ")
# data = {'userid':userid,'tip':tip, 'discount':discount,'split':split,'total':total}
# response =requests.post('http://localhost:8000/transaction/entry',json=data).content
# print(response.decode())


## Transaction fetch of user

# userid = input("Enter the Userid ")
# data = {'userid':userid}
# response =requests.get('http://localhost:8000/transaction/fetch',json=data).content
# print(response.decode())

## All transaction
# response =requests.get('http://localhost:8000/transaction/all').content
# print(response.decode())

