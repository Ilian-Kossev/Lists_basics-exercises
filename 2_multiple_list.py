factor = int(input())
count = int(input())
list_numbers = []
for number in range(1, count + 1):
    integer = factor * number
    list_numbers.append(integer)
print(list_numbers)

