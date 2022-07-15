cards = input()
cards_list = cards.split()
list_team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
list_team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_terminated = False
for element in cards_list:
    if element in list_team_A:
        list_team_A.remove(element)
    elif element in list_team_B:
        list_team_B.remove(element)
    if len(list_team_A) < 7 or len(list_team_B) < 7:
        game_terminated = True
        break
print(f"Team A - {len(list_team_A)}; Team B - {len(list_team_B)}")
if game_terminated:
    print("Game was terminated")
