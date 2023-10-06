
# try:
    # some lines of code
# except <ERROR1>:
    # handler <ERROR1>
# except <ERROR2>:
    # handler <ERROR2>
# else:
    # no exceptions were raised, the code ran successfully
# finally:
    # do something in any case

try:
    result = 2/0
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    result = 1

print(result)