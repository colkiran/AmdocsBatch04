
print("get".center(40, "-"))

player = {'name': "Messi", 'age': 35, 'goals': 350, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)
print(f"Name    :{player.get('name', 'Invalid Key, Please enter a valid one')}")
print(f"country :{player.get('country', 'Invalid Key, Please enter a valid one')}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd']
print(f"cities :{cities}")

print("-" * 40)
res = dict.fromkeys(cities)
print(f"res: {res}")

res = dict.fromkeys(cities, 24)
print(f"res :{res}")

print("setdefault".center(40, "-"))

player = {'name': "Messi", 'age': 35, 'goals': 350, 'club': 'PSG'}
print(f"player :{player}")

print("-" * 40)
player.setdefault('name', 'Lionel Messi')
player.setdefault('club', 'FCB')
player.setdefault('country', 'Argentina')

print(f"player :{player}")

# pop, popitem
print("pop".center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'country': 'Argentina'}
print(f"player :{player}")

print("-" * 40)
res = player.pop('age')
print(res)

res = player.pop('club')
print(res)

# res = player.pop()
# print(res)

print(f"player :{player}")

print('popitem'.center(40, "-"))
player = {'name': 'Messi', 'age': 35, 'goals': 350, 'club': 'PSG', 'country': 'Argentina'}
print(f"player :{player}")

print("-" * 40)

res = player.popitem()
print(res)

res = player.popitem()
print(res)

print(f"player :{player}")
