# map(), reduce() & filter()

# map()
# nums = [1,2,3]
# res = map(lambda a : a * 2 ,nums)
# print(list(res))

# filter()
# def isEven(n):
#     return n % 2 == 0
# res = filter(isEven,nums)
# print(list(res))

# reduce() is used to calculate a value of sequence like a list

from functools import reduce
expenses = [
    ('Dinner',80),
    ('Car repair',120)
]

sum = reduce(lambda a, b : a[1] + b[1],expenses)

# for expense in expenses:
#     sum += expense[1]

print(sum)