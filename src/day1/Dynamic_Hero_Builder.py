def create_hero(name,*powers,**stats):
    sum=0
    for k in stats:
        sum+=stats[k]
    avg=sum/len(stats)
        

    print(f"Hero:{name} Powers:{powers} Stats:{stats} Overall Rating: {avg:.1f}",end="")
    if avg>90:
        print(f" --> S-Tier *")
create_hero("Spider-Man", "wall-crawl",
"spider-sense",
strength=85, agility=95,
intelligence=92)
# dc={1:"shriyaans",2:"prakash"}
# for v in dc:
#     print(dc[v])