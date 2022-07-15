integers_string = input()
number_beggars = int(input())
final_list = []
list_of_integers = integers_string.split(", ")
starting_num = 0
for number in range(number_beggars):
    money_sum = 0
    for index in range(starting_num, len(list_of_integers), number_beggars):
        integer = list_of_integers[index]
        value_integer = int(integer)
        money_sum += value_integer
    final_list.append(money_sum)
    starting_num += 1
print(final_list)





