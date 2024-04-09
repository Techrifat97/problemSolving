wind_initial_obey = input()
number_of_duels = int(input())
duels = list()
new_obey = wind_initial_obey

for i in range(number_of_duels):
    duels.append(input().split())
count = 1
for item in duels:
    if item[1] == new_obey:
        new_obey = item[0]
        if new_obey != wind_initial_obey:
            count += 1
    
print(new_obey)
print(count)
            
