goblin = ["Queens", "Manhattan",
"Brooklyn", "Bronx"]
octopus = ["Manhattan", "Brooklyn",
"Harlem"]
vulture = ["Manhattan", "Bronx",
"Harlem"]
goblin_s=set(goblin)
octopus_s=set(octopus)
vulture_s=set(vulture)
# common=goblin_s.intersection(octopus_s.intersection(vulture_s))
common=None
unique=goblin_s.union(octopus_s.union(vulture_s))
for UQ in unique:
    if UQ in goblin_s and UQ not in octopus_s and UQ not in vulture_s:
        common=UQ 
    elif UQ in octopus_s and UQ not in goblin_s and UQ not in vulture_s:
        common=UQ
    elif UQ in vulture_s and UQ not in goblin_s and UQ not in octopus_s:
        common=UQ
diff=(goblin_s.difference(octopus_s)).difference(vulture_s)
c_u=0
for i in unique:
    c_u+=1
print(f"Contested by all three:{common} Controlled by exactly one:{diff} Distinct Neighbourhoods:{c_u}")