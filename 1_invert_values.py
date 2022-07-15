input_string = input()
input_list = input_string.split()
output_list = []
for digit in input_list:
    value = int(digit)
    opposite_value = - value
    output_list.append(opposite_value)

print(output_list)

