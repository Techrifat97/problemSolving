number_of_village = int(input())
positions_village = list()

while number_of_village >= 1:
    positions_village.append(int(input()))
    number_of_village -=1

positions_village.sort()

neighborhood_size = []
for index, item  in enumerate(positions_village):
    if index == 0:
        continue
    if index == len(positions_village) - 1:
        continue
    
    neighborhood_size.append((positions_village[index] - positions_village[index - 1] ) / 2 +
                             (positions_village[index + 1] - positions_village[index] )/ 2)
    
print(min(neighborhood_size))      
    