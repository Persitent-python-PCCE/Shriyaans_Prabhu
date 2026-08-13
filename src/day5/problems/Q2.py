import yaml as Y
import random
import json 
import datetime
with open("config.yml","r") as Of:
    rows=Y.safe_load(Of)
# print(rows)
order_ID=0
customer_ID=0
unit_price=0
quantity=0
total_price=0
status=0
date=datetime.date.today()
product=["Laptop","Mobile Phone","Monitor","Keyboard","Mouse","Headphones"]
pd_list=[]
# print(rows['allowed_statuses'])
N=int(input("Number of orders:"))
for i in range(1,N+1):
    order_ID=random.randint(10000+i,999999)
    customer_ID=random.randint(1000,9999)
    unit_price=random.uniform(50,150000)
    quantity=random.randint(1,5)
    total_price=unit_price*quantity
    status=random.choice(rows["allowed_statuses"])
    rand_product=random.choice(product)
    pd_list.append({
      "order_id": order_ID,
      "customer_id": customer_ID,
      "product": rand_product,
      "quantity": quantity,
      "unit_price": unit_price,
    "total_amount": total_price,
      "status": status,
      "order_date": date.isoformat()
             })
    date=date+datetime.timedelta(days=7)
# for i in pd_list:
#     print(i)
with open("orders.json","w") as Of:
    json.dump(pd_list,Of,indent=2)
Of.close()
with open("orders.json","r") as ROf:
    data=json.load(ROf)
ROf.close()
sales=[]
for i in data:
    sales.append(i["unit_price"])
Delivered=0
Cancelled=0
for i in data:
    if i["status"]=="Delivered":
        Delivered+=1
    elif i["status"]=="Cancelled":
        Cancelled+=1
print("\n"+"-"*40)
print("TechStore Order Report")
print(""+"-"*40)
print(f"Total Orders : {N}")
print(f"Total Sales : INR {sum(sales)}")
print(f"Highest Order : INR {max(sales)}")
print(f"Lowest Order : INR {min(sales)}")
print(f"Delivered Orders : {Delivered}")
print(f"Cancelled Orders : {Cancelled}")
print("Order data saved successfully.")
