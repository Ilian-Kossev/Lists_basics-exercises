input_string = input()
number_shuffles = int(input())
initial_list = input_string.split(" ")
final_list = []
border = int(len(initial_list)/2)
for shuffles in range(number_shuffles):
    for index_1 in range(border):
        final_list.append(initial_list[index_1])
        for index_2 in range(border + index_1, border + index_1 + 1):
            final_list.append(initial_list[index_2])
    initial_list = final_list
    final_list = []

print(initial_list)



