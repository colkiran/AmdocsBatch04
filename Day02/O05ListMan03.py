
cities = ['thiruvananthapuram', 'bangalore', 'delhi', 'hyderabad', 'kolkota', 'vishakapatnam', 'pune', 'mumbai', 'coimbatore']

print(f"cities :{cities}")

print("-" * 40)
print(sorted(cities, key=len))

print("-" * 40)
months = ['dec', 'apr', 'aug', 'oct', 'jan', 'mar', 'nov', 'feb', 'may',
        'jul', 'sep', 'jun']

print(f"months :{months}")
# sort these months
from calendar import month_abbr
print(list(month_abbr))
l = []
for month in list(month_abbr):
    l.append(month.lower())
print(l)

def sort_months(mon):
    if mon in l:
        return l.index(mon)

print("-" * 40)
res = sorted(months, key=sort_months)
print(f"res :{res}")

print("reverse".center(40, "-"))
l1 = [9, 6, 10, 1, 7, 3, 8, 5, 2, 4]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                     # shallow copy - it copid the address with the data

print(f"l2 Before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("=".center(40, "-"))
l3 = [10, 20, 30, 40, 50]
print(f"l3 Before :{l3}")

l4 = l3.copy()                  #deep copy - values were copied
print(f"l4 Before :{l4}")

l4.extend([60, 70, 80])
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("=" * 40)
l5 = [11, 22, 33, 44, [1, 2, 3, 4, 5], 55]
print(f"l5 Before :{l5}")

l6 = l5.copy()                  # deep copy failed
print(f"l6 Before :{l6}")

l6[4].extend([6, 7, 9])
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("=" * 40)
l7 = [1, 2, 3, 4, [2, 4, 6, 8, 10], 5]
print(f"l7 Before :{l7}")
from copy import deepcopy

l8 = deepcopy(l7)
print(f"l8  Before :{l8}")
l8[4].extend([12, 14, 16])
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
