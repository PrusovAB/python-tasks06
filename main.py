from functools import reduce


def multiply(x):
    return (x*x)


def add(x):
    return (x+x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num


product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
