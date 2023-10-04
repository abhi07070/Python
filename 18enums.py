from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# Three different ways to achieve the same results
print(State.ACTIVE.value)
print(State['ACTIVE'].value)
print(State(1).value)

print(len(State))