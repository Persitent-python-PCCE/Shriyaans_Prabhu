import csv
import statistics
from statistics import mean
lst=[]
revenue=[]
product_revenue=[]
Top_Product={}
total_revanue=0
with open("sales.csv","r") as Of:
    dit=csv.DictReader(Of)
    for row in dit:
        # print(row)
        lst.append(row)
    # print(lst)
for L in lst:
    revenue.append((L['category'],int(L['quantity'])*int(L['unit_price'])))
    product_revenue.append((L['product'],int(L['quantity'])*int(L['unit_price'])))
# print(revenue)
category_sum={}
for ctg,price in revenue:
    if ctg in category_sum:
        category_sum[ctg]+=price
    else:
        category_sum[ctg]=price
print(f"=== Sales Report ===")
print(f"Revanue by Category:")
for C in category_sum:
    print(f"{C} : {category_sum[C]}")
    total_revanue+=category_sum[C]

for product,price in product_revenue:
    if product  in Top_Product:
        Top_Product[product]+=price
    else:
        Top_Product[product]=price
Top_P,price=max(Top_Product.items(),key=lambda x:x[1])
# print(Top)
print(f" Top Product: {Top_P} ({price})")
print(f"Total Revanue:{total_revanue}")
print(f"Avg / Txn : {(total_revanue/len(product_revenue)):.1f}")