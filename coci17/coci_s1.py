wind_initial_obey = input()
number_of_duels = int(input())
duels = list()


for i in range(number_of_duels):
    duels.append(input().split())
    

for item in duels: 
    if item[1] == wind_initial_obey:
        currently_obeying = item[0]
    
        
print(currently_obeying)