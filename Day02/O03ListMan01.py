
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.5, 9.0, 10+0j, 11-0j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(10, 101, 10))
print(f"l3 :{l3}")
print(type(l3))

# lists are not stored in contigious memory
print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.5, 9.0, 10+0j, 11-0j, True, False]
print(f"l2 :{l2}")
print(id(l2[0]))
print(id(l2[1]))
print(id(l2[2]))
print(id(l2[3]))

print("-" * 40)
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1[4] = 4.5
print(f"l1 :{l1}")

# print("-" * 40)
# print(dir(l1))

# funtions that can be used to add values into a list
# append, extend, insert

print("append".center(40, '-'))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13, 14])
print(f"l1 :{l1}")
print(f"l1[8] :{l1[8]}")
print(f"l1[8][2:5] :{l1[8][2:5]}")

print("extend".center(40, "-"))
l2 = [11, 22, 33, 44, 55]
print(f"l2 :{l2}")

l2.extend([66, 77, 88])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = [1, 2, 3, 4, 5]
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")
