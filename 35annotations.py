"""
annotations are a way to attach metadata or additional 
information to variables, function parameters, and return values.
Annotations are primarily used for documentation purposes and
do not affect the runtime behavior of the code.

"""
def increment(n: int) -> int:
    return n + 1

count: int = 0