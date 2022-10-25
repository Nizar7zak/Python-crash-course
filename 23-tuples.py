from os import PRIO_USER
from tokenize import cookie_re


numbers = [1, 2, 3, 4]

print(numbers[0], 'before change')

numbers[0] = 10
print(numbers[0], 'after change')


#  what if you want to save my values without change - read only values -
#  this is called Tuple

coordinates = (1, 2, 3, 4)
print(coordinates[0])
# coordinates[0] = 12
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x)

#  can i do this in more gracefully way?
x, y, z = coordinates
print(y)
