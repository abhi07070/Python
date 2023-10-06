filename = '37test.txt'

try:
    with open(filename, 'r') as file:
       content = file.read()
       print(content)
except Exception as e:
    print(f"An error occurred: {e}")