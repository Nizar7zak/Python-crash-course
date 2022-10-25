numbers = [6, 3, 2, 8, 5, 8, 8]

numbers.append(13)
print(numbers)

print(numbers.index(3))

numbers.insert(2, 99)
print(numbers)

numbers.remove(99)
print(numbers)


numbers.pop()
print(numbers)

print(5 in numbers)

print(numbers.count(8))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
print(numbers2, 'numbers2')

numbers.clear()
print(numbers)
