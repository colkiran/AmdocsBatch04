
for i in range(1, 11):
    print(i, end= " ")
print()

# continue, break and else

for i in range(1, 30):
    # if i > 25:
    #     break               # come out of the iteration
    if i % 2 == 1:
        continue            # skip the iteration
    print(i, end=" ")
else:
    print("\nIteration completed.....")

# generating prime numbers
