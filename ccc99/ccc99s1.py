"Variable assignment"
total_card = 52
card_list = []
HIGH_CARDS = ['ace', 'king', 'queen', 'jack']
player_a_points = 0
player_b_points = 0

"Function  creation for removing code duplication"
def which_player(index):
    if index % 2 == 0:
        return 'A'
    else:
        return 'B'
    
def turn_ace(index,player):
    global player_b_points, player_a_points
    if (index + 4 ) <= 51:
        count = 1
        validation = 0
        
        while count != 5:
            if card_list[index + count] in HIGH_CARDS:
                validation += 1
            count += 1
        
        if validation == 0:
            print(f"Player {player} scores 4 point(s).")
            if player == 'A':
                player_a_points += 4
            elif player == 'B':
                player_b_points += 4
        
def turn_king(index,player):
    global player_b_points, player_a_points
    if (index + 3 ) <= 51:
        count = 1
        validation = 0
        
        while count != 4:
            if card_list[index + count] in HIGH_CARDS:
                validation += 1
            count += 1
        
        if validation == 0:
            print(f"Player {player} scores 3 point(s).")
            if player == 'A':
                player_a_points += 3
            elif player == 'B':
                player_b_points += 3

def turn_queen(index,player):
    global player_b_points, player_a_points
    if (index + 2 ) <= 51:
        count = 1
        validation = 0
        
        while count != 3:
            if card_list[index + count] in HIGH_CARDS:
                validation += 1
            count += 1
        
        if validation == 0:
            print(f"Player {player} scores 2 point(s).")
            if player == 'A':
                player_a_points += 2
            elif player == 'B':
                player_b_points += 2    

def turn_jack(index,player):
    global player_b_points, player_a_points
    if (index + 1 ) <= 51:
        count = 1
        validation = 0
        
        while count != 2:
            if card_list[index + count] in HIGH_CARDS:
                validation += 1
            count += 1
        
        if validation == 0:
            print(f"Player {player} scores 1 point(s).")
            if player == 'A':
                player_a_points += 1
            elif player == 'B':
                player_b_points += 1

while total_card >= 1:
    card_list.append(input())
    total_card -= 1
    
for index, item in enumerate(card_list):
    if item == 'ace':
        player = which_player(index) 
        turn_ace(index,player)       
    elif item == 'king':
        player = which_player(index) 
        turn_king(index,player)
    elif item == 'queen':
        player = which_player(index) 
        turn_queen(index,player)
    elif item == 'jack':
        player = which_player(index) 
        turn_jack(index,player)

print(f"Player A: {player_a_points} point(s).")
print(f"Player B: {player_b_points} point(s).")