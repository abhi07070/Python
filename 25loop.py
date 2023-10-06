# while loop
count = 0
while count < 10:
    print("The condition is True")
    count += 1

# for loop
items = [1,2,3,4]

for item in items:
    print(item)

for index, item in enumerate(items):
    print(index,item)

# range (not expected)

for item in range(15):
    print(item)