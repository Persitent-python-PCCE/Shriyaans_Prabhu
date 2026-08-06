inv = [
("Masala Chai", "Tea", 5, 20),
("Green Tea", "Tea", 15, 30),
("Samosa", "Snack", 8, 15),
("Biscuit", "Snack", 25, 10),
]
def inventory_report(inventory, gst=0.05, **filters):
    ls=[]
    ls_stc=[]
    pcps=[]
    GST_lst=[]
    item_ls=[]
    i=0
    for pd,ctg,stc,pc in inventory:
        ls.append(ctg)
        ls_stc.append((pd,stc))
        pcps.append([pd,pc])
    ls=set(ls)
    print(f"Cagegories:{list(ls)}")
    lsnm=list(filter(lambda Q:Q[1]<10,ls_stc))
    print(f"Reorder soon (stock < 10):{lsnm}")
    GST=list(map(lambda C: (C[1]*1.05),pcps))
    print(GST)
    for pd,ctg,stc,pc in inventory:
        GST_lst.append((pd,GST[i]))
    print(f"Prices incl. GST: {GST_lst}")
    print(f"Matching filters {filters}",end=" :")
    for pd,ctg,stc,pc in inventory:
      fg1=False
      fg2=False
      if "category" in filters and ctg==filters["category"]:
        fg1=True
      if "max_price" in filters and pc<=filters["max_price"]:
        fg2=True
      if fg1 and fg2:
        item_ls.append(pd)
    print(item_ls)
inventory_report(inv, category="Tea",max_price=20)
