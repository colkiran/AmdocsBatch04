"""
tuples are immutable lists
tuples are enclosed in ()
"""

t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(10, 51, 10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = {1: 'a', 2: 'b', 3: 'c'},
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
t6 = 10, 15, 20, 25, 30
print(f"t6 :{t6}")
print(type(t6))

# print("-" * 40)
# tuples are immutable

# t1 = (1, 2, 3, 4, 5)
# print(f"t1 :{t1}")
# print(f"t1[0] :{t1[0]}")
# t1[0] = 100

print("-" * 40)
# print(dir(t1))
t1 = (1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2)

# count
print("1 :", t1.count(1))
print("2 :", t1.count(2))
print("3 :", t1.count(3))

print("-" * 40)
# index
print("3 :", t1.index(3))
print("3 :", t1.index(3, t1.index(3)+1))
print("3 :", t1.index(3, t1.index(3, t1.index(3)+1)+1))

