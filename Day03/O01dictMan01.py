
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'Lionel Messi', 'Age': 30, 'goals': 350, 'club': 'PSG'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'neymar'), ('Age', 32), ('goals', 230), ('club', 'PSG')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='ronaldo', age=37, goals=380, club="Al-Nasar FC")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': "Messi", 'age': 35, 'goals': 350, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)
print(f"Name  :{player['name']}")
print(f"Goals :{player['goals']}")

#iterate
print("-" * 40)
for x in player:
    print(x + ' => ' + str(player[x]))

# modify
print("-" * 40)
player['name'] = "Lionel Messi"
player['goals'] = 365
player['country'] = "Argentina"

print(f"player :{player}")

# delete
print("-" * 40)
del player['age']
del player['club']

print(f"player :{player}")

# print("-" * 40)
# print(dir(player))

print("keys".center(40, "-"))

player = {'name': "Messi", 'age': 35, 'goals': 350, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)

k = player.keys()
print(f"k :{k}")

print("-" * 40)
for k in player.keys():
    print(k, "=>", player[k])

print("values".center(40, "-"))
player = {'name': "Messi", 'age': 35, 'goals': 350, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)
v = player.values()
print(f"v :{v}")

