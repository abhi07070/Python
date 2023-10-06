# a function can call itself that's what recursion is

def fac(a):
    # base case always -  when we want to leave the recursive fun..
    if a == 1 :
        return 1
    # recursive case always
    return a * fac(a-1)

res = fac(5)
print(res) 