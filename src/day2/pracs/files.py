import csv
f=open("data.txt","r")
words=f.readlines()
print(words)
f.close()
with open("data.txt","r") as Of:
    for l in Of:
        print(l)
 
f=open("data.txt","w")
lst=["Samsung\n","Apple\n","Motorola\n","Oneplus\n"]
f.write(input("Enter you content:"))
for el in lst:
    f.write(el)
f.close()
f2=open("inof.csv","r")
reader=csv.DictReader(f2)
for row in reader:
    print(row)
f2.close()
lst = [
    ["ID", "BrandName", "Price", "Stock"],
    [1, "Samsung Galaxy S26", 95000, 2],
    [2, "Motorola Edge 50 Pro", 45000, 6],
    [3, "Apple iPhone 17", 94000, 4],
    [4, "OnePlus 13", 69999, 8],
    [5, "Google Pixel 10", 79999, 5],
    [6, "Nothing Phone 3", 49999, 10],
    [7, "Xiaomi 15", 54999, 7],
    [8, "Realme GT 8 Pro", 42999, 9],
    [9, "Vivo X300", 58999, 3],
    [10, "Oppo Find X9", 74999, 4],
    [11, "Samsung Galaxy A57", 32999, 15],
    [12, "iPhone 16e", 59999, 12],
    [13, "Motorola G96", 21999, 20],
    [14, "Redmi Note 15 Pro", 26999, 18],
    [15, "POCO F8", 34999, 11],
    [16, "iQOO Neo 11", 38999, 14],
    [17, "Asus ROG Phone 10", 89999, 5],
    [18, "Sony Xperia 1 VII", 109999, 2],
    [19, "Honor Magic 8 Pro", 65999, 6],
    [20, "Huawei P80 Pro", 72999, 3]]
# with open("inof.csv","w",newline="") as Of:
#     fieldname=["ID","BrandName","Price","Stock"]

#     write=csv.writer(Of)
#     write.writerows(lst)


