"""Martha problem """
quarters = int(input())
first_slot = int(input())
second_slot = int(input())
third_slot = int(input())
plays = 0
while quarters != 0:
    quarters -= 1
    
    if plays % 3 == 0: 
        first_slot += 1
        if first_slot % 35 == 0:
            quarters += 30
            first_slot = 0
            
    elif plays % 3 == 1:
        second_slot += 1
        
        if second_slot % 100 == 0:
            quarters += 60
            second_slot = 0
            
    elif plays % 3 == 2:
        third_slot += 1
        
        if third_slot % 10 == 0:
            quarters += 9
            third_slot = 0
    
    plays += 1
    
print('Martha plays', plays, 'times before going broke.')