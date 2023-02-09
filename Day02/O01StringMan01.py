
st = 'hello world'
print(f'st :{st}')
print(type(st))

print("-" * 40)
print(f"st[0] :{st[0]}")        #- strings are stored like lists
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print("-" * 40)
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

# reverse indexing
print("-" * 40)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")


# slicing
print("-" * 40)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1:-12:-2] :{st[-1:-12:-2]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# how do you find if the given string is a palindrome

print("-" * 40)

st = "abba"
print(f"String {st} is a plindrome" if (st == st[::-1]) else f"String {st} is not a palindrome")


"""
st = "dad"
rst = st[::-1]
print(f"st :{st} , rst :{rst}")
if(st == rst):
    print(f" {st} is palindrome")
else:
    print(f" {st} is not palindrome")

print("-" * 40)

st = "wow"
if st[:] == st[::-1]:
    print(f" {st} is a palidrome")
else:
    print(f"{st} is not a palidrome")

print("-" * 40)

palin = "false"
if((print :{st[::-1]})) == print (st1))}:palin = "true"

"""

# strings are immutable
# st = "hello world"
# print(f"st[0] :{st[0]}")
# st[0] = "H"
