gifts = input()
gifts_list = gifts.split()
command_statement = input()
command_list = command_statement.split()
command = command_list[0]
while command != "No":
    if command == "OutOfStock":
        for i in range(len(gifts_list)):
            if command_list[1] == gifts_list[i]:
                gifts_list[i] = None
    elif command == "Required":
        gifts_list.pop(int(command_list[2]))
        gifts_list.insert(int(command_list[2]), command_list[1])
    elif command == "JustInCase":
        gifts_list.pop(-1)
        gifts_list.append(command_list[1])
    command_statement = input()
    command_list = command_statement.split()
    command = command_list[0]
final_list = []
for element in gifts_list:
    if element != None:
        final_list.append(element)
print(' '.join(final_list))

