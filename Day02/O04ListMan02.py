
print("count".center(40, "-"))
l1 = [1, 2, 3, 1, 3, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 1,1, 2, 3, 1, 2, 2, 2, 3, 2, 2 ,2, 2, 2, 2 ,2 , 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("1 :", l1.count(1))
print("2 :", l1.count(2))
print("3 :", l1.count(3))

# functions used to delete elements of a list
# pop, remove, clear

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(res)

res = l1.pop(1)
print(res)

res = l1.pop()
print(res)

print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 3, 1, 3, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 1,1, 2, 3, 1, 2, 2, 2, 3, 2, 2 ,2, 2, 2, 2 ,2 , 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("-" * 40)
# l1.remove(3)
# print(f"l1 :{l1}")

for i in range(l1.count(1)):
   l1.remove(1)

print(f"l1 :{l1}")

print("clear".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("index".center(40, "-"))
l1 = [1, 2, 3, 1, 3, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 1, 1, 2, 3, 1, 2, 2, 2, 3, 2, 2 ,2, 2, 2, 2 ,2 , 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3)+1))
print("3 :", l1.index(3, l1.index(3, l1.index(3)+1)+1))

"""
sort    -   sort will sort the original list
sorted  -   sorted will return a copy of the sorted list
"""

print("sort".center(40, "-"))
l1 = [9, 6, 10, 1, 7, 3, 8, 5, 2, 4]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 40)
l1 = [9, 'apple', 6, 'zebra', 10, 'blue', 1, 'yellow', 7, 'green',  3, 'violet', 8, 'pink',  5, 'red', 2, 'orange', 4, 'cat', 'dog', 194, 1234, 18765, 22, 260, 2490, 20789]

print(f"l1 :{l1}")

print("-" * 40)
res = sorted(l1, key=ascii)
print(f"res :{res}")

