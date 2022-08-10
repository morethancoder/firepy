# install firebase_admin
# link our db
import json
from firebase_admin import credentials,initialize_app,db
cred = credentials.Certificate("the PATH of your pravite keys")
app = initialize_app(cred,{
   # هنا نخلي الخدمة الي نريد نستعملها من فايربيس
   'databaseURL':'the URL to your database'
})

#* write data
# we need refrence !
# ref = db.reference("/books/")
# with open("./data.json","r") as f:
#     data=json.load(f) 
# ref.set(data)
#* another way to write data
# ref.push(data)
# print("database has been updated ! ")

#* read data
# get ?
# ref=db.reference("/books/")
# print(ref.get())
# get ordered data (مرتبة حسب خاصية معينة)
# ordered_by_price=ref.order_by_child("price").get()
# print("ordered by price")
# for key,item in ordered_by_price.items():
#     print(f"{key} price {item['price']}")
# most_expensive=ref.order_by_child("price").limit_to_last(1).get()
# print("*** most expensive book ***")
# for key,item in most_expensive.items():
#     print(f"{key} with price of : {item['price']}")
# print(ref.order_by_child("price").equal_to(50).get())

#* update data
# ref=db.reference("/books/")
# books=ref.get()
# for key,value in books.items():
#     if(value["author"] == "Potato"):
#         ref.child(key).update({"price":2})

#* delete data
# ref=db.reference("/books/")
# ref.set({})
# print("database has been updated ! ")