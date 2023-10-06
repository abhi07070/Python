# if you return a netsted function from a function
# that nested function has access to a variable 
# that is defined in that function even if that 
# function is not actived anymore.

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()

print(increment()) #1
print(increment()) #2
print(increment()) #3