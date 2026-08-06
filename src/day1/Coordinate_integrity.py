ls=[("Falcon", 34.05, -118.24), ("Ghost",
99.9, 12.0), ("Condor", 40.71, -74.00)]

for codename, lat, log in ls:
    if lat < -90 or lat > 90 or log < -180 or log > 180:
        print(f"INVALID: {codename}({lat},{log})")


print("Briefing (N-->S):")
for i in ls:
    if i[1]<=90 and i[1]>=-90 and i[2]<=180 and i[2]>=-180:
        print(f"{i[0]} Lat: {i[1]}, Log:{i[2]}")


    

