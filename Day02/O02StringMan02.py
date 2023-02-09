

# st = "hello"
# print(dir(st))

print("find".center(40, "-"))
st1 = 'hello world'
st2 = 'the quick brown fox jumps over the lazy dog'

print(f"st1 :{st1}")
print("w :", st1.find("w"))
print("l :", st1.find("l"))
print("l :", st1.find("l", st1.find("l")+1))
print("l :", st1.find("l", st1.find("l", st1.find("l")+1)+1))

print(f"st2 :{st2}")
print("fox :", st2.find("fox"))
print("the :", st2.find("the"))
print("the :", st2.find("the", st2.find("the")+1))

print("replace".center(40,"-"))
st1 = 'hello world'
st2 = 'the quick brown fox jumps over the lazy dog'

print(f"st1 :{st1}")
print(st1.replace("h", "H"))
print(st1.replace("l", "L"))
print(st1.replace("l", "L", 1))
print(st1.replace("l", "L", 2))

print(f"st2 :{st2}")
print(st2.replace("fox", "tiger"))
print(st2.replace("the", "The"))
print(st2.replace("the", "The", 1))

# maketrans, translate
print("maketrans".center(40, "-"))
st1 = 'hello world'
print(st1)
a = 'helowrd'
b = 'HELOWRD'
resTbl = st1.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("translate".center(40, "-"))
res = st1.translate(resTbl)
print(res)

print("strip".center(40, "-"))
st = "******hello******"
print(f"st :{st}")

print(st.lstrip("*"))
print(st.rstrip("*"))
print(st.strip("*"))

print("format".center(40, "-"))
st = "Hello {}, what a {} player"
print(st)
print(st.format("Messi", "class"))
print("Hello {}, what a {} player".format("Messi", "superb"))
print("Hello {}, with a rating of {} what a {} player".format("Messi", 9.75, 'class'))
print("Hello {0}, with a rating of {1} what a {2} player".format("Messi", 9.75, 'class'))
print("Hello {0}, with a rating of {1:.3f} what a {2} player".format("Messi", 9.75, 'class'))
print("Hello {0}, with a rating of {1:.3f} what a {2} player".format("Messi", 9.7534534, 'class'))

print("Hello {pname}, with a rating of {rating} what a {adj} player for club {club}".format(
pname="Messi", rating=9.7534534, adj='class', club="PSG"))

print("Hello {pname}, with a rating of {rating:.3f} what a {adj} player for club {club}".format(pname="Messi", rating=9.7534534, adj='class', club="PSG"))

