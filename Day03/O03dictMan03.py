

print("items".center(40, "-"))
# items = keys + values
emp = {
    'emp1': {'name':'Mike', 'age': 28, 'dept':'MKT', 'desig': 'MKT-Exe', 'sal': 35000, 'loc': 'Delhi'},
    'emp2': {'name':'Emily', 'age': 30, 'dept':'Finance', 'desig': 'TL', 'sal': 55000, 'loc': 'Chennai'},
    'emp3': {'name':'John', 'age': 34, 'dept':'IT', 'desig': 'PM', 'sal': 95000, 'loc': 'Bangalore'}
}


print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))

emp2 =  {'name':'Emily', 'age': 30, 'dept':'Finance', 'desig': 'TL', 'sal': 55000, }
emp3 = {'name':'John', 'age': 34, 'dept':'IT', 'desig': 'PM',  'loc': 'Bangalore'}

print(f"emp2 :{emp2}")
print(f"emp3 :{emp3}")

print("-" * 40)

emp2.update(emp3)

print(f"emp2 :{emp2}")
print(f"emp3 :{emp3}")

print("clear".center(40, "-"))
emp1 = {'name':'John', 'age': 34, 'dept':'IT', 'desig': 'PM',  'loc': 'Bangalore'}
print(f"emp1 :{emp1}")

emp1.clear()

print(f"emp1 :{emp1}")

print("\n", '-'  * 40,  "\n")

print("copy".center(40, "-"))

emp1 = {'name':'John', 'age': 34, 'dept':'IT', 'desig': 'PM',  'loc': 'Bangalore'}
print(f"emp1 Before :{emp1}")

emp2 = emp1             # shallow => copying  the address of the dict with the data

print(f"emp2 Before :{emp2}")

emp2['salary'] = 45000
emp2['gender'] = 'male'
print("-" * 40)
print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")

print("\n", '-'  * 40,  "\n")

emp3 = {'name':'Emily', 'age': 30, 'dept':'Finance', 'desig': 'TL', 'loc': 'Chennai'}
print(f"emp3 Before :{emp3}")

emp4 = emp3.copy()          # deep copy -> only copies the values

print(f"emp4 Before :{emp4}")
emp4['salary'] = 45000
emp4['gender'] = 'male'

print("-" * 40)
print(f'emp4 After :{emp4}')
print(f"emp3 After :{emp3}")

print("\n", '-'  * 40,  "\n")

emp5 =  {'name':'Mike', 'age': 35, 'dept':'MKT', 'desig': {'hp':'trainee', 'ibm':'MKT-Exe', 'wipro':'BDM'}, 'loc': 'Delhi'}

print(f"emp5 Before :{emp5}")

emp6 = emp5.copy()

print(f"emp6 Before :{emp6}")

emp6['desig']['abb'] = 'AGM'
emp6['desig']['SAP'] = 'GM'

print("-"  * 40)
print(f"emp6 After :{emp6}")
print(f"emp5 After :{emp5}")

print("\n", '-'  * 40,  "\n")

emp7 =  {'name':'Mike', 'age': 35, 'dept':'MKT', 'desig': {'hp':'trainee', 'ibm':'MKT-Exe', 'wipro':'BDM'}, 'loc': 'Delhi'}

print(f"emp7 Before :{emp7}")
from copy import deepcopy

emp8 = deepcopy(emp7)

print(f"emp8 Before :{emp8}")
print("-"  * 40)

emp8['desig']['abb'] = 'AGM'
emp8['desig']['SAP'] = 'GM'
print(f"emp8 After :{emp8}")
print(f"emp7 After :{emp7}")