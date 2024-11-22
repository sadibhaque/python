map = {'name' : 'mendax', 'age' : 25}

print(type(map))

map['gender'] = 'male'

print(map)
print(map.keys())
print(map.values())
print(map['age'])


# iterate 
for k ,v in map.items():
    print(f"{k} = {v}")