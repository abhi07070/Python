items = [1,2,3,4]

for item in items:
    if item == 2:
        # it will skip the next iteration and go back to iterate again
        continue
    print(item) # 1 3 4

for item in items:
    if item == 2:
        # it will break the loop and stop running
        continue
    print(item) # 1 3 4