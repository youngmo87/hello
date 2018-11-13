# int_numbers = range(-5,6)
# print(list(int_numbers))

# negatives=filter(lambda x: x<0, int_numbers)
# print(list(negatives))



# def make_double(n):
#         return n*2

# numbers = range(-1,5)
# double_numbers=map(make_double, numbers)
# print(list(double_numbers))

# triple_numbers = map(lambda x: x*3, numbers)
# print(list(triple_numbers))

# negatives=filter(lambda x: x<0, int_numbers)
# print(list(negatives))
# negatives=map(lambda x: x<0, int_numbers)
# print(list(negatives))

from functools import reduce
product = 1
lst = [1, 2, 3, 4]
for num in lst:
    product = product * num

print("product1>>", product)

product2 = reduce(lambda x, y: x * y, lst)
print("product2>>", product2)
