input_data = input()
number_to_remove = int(input())
initial_list = input_data.split(" ")
new_list = []
final_list = []
for index in range(len(initial_list)):
    integer = int(initial_list[index])
    new_list.append(integer)
for _ in range(number_to_remove):
    a = min(new_list)
    new_list.remove(a)
for number in range(len(new_list)):
    symbol = str(new_list[number])
    final_list.append(symbol)
result = ", ".join(final_list)
print(result)