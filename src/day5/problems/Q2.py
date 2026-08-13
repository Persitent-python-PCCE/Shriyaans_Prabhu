import yaml as Y
import random
import json 
with open("config.yml","r") as Of:
    rows=Y.safe_load(Of)
print(rows)
order_ID=0
customer_ID=0
unit_price=0
quantity=0
total_price=0
product=["Laptop","Mobile Phone","Monitor","Keyboard","Mouse","Headphones"]
pd_list=[]
# print(rows['allowed_statuses'])
N=int(input("Number of orders:"))
for i in range(1,N+1):
    order_ID=random.randint(10000+i,999999)
    
    pd_list.append({
      "order_id": 10001,
      "customer_id": 4821,
      "product": "Laptop",
      "quantity": 2,
      "unit_price": 62500.50,
    "total_amount": 125001.00,
      "status": "Delivered",
      "order_date": "2026-03-18"
             })
