cards = input()
cards_list = cards.split()
list_team_A = []
list_team_B = []
for element in cards_list:
    element_list = element.split("-")
    for symbol in element_list:
        if symbol == "A":
            list_team_A.append(element)
        elif symbol == "B":
            list_team_B.append(element)
list_team_A = set(list_team_A)
list_team_B = set(list_team_B)
remaining_players_team_A = 11 - len(list_team_A)
remaining_players_team_B = 11 - len(list_team_B)
print(f"Team A - {remaining_players_team_A}; Team B - {remaining_players_team_B}")
if remaining_players_team_A < 7 or remaining_players_team_B < 7:
    print("Game was terminated")
    # gets 80% from Judge!
