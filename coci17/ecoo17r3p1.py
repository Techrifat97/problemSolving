my_list = []
for dataset in range(10):
    new_list = []
    convert_list = []
    my_list = []
    franchise_days = ''
    franchise_days = input().split()
    
    franchise = int(franchise_days[0])
    day = int(franchise_days[1])
    
    for i in range(day):
        new_list = []
        new_list.append(input().split())
        for item in new_list:
            my_list.append(item)
   
    new_list = []
    for items in my_list:
        convert_list = []
        for item in items:
            convert_list.append(int(item))
        new_list.append(convert_list)
      
    bonus_count = 0
    for item in new_list:
        if sum(item) % 13 == 0:
           bonus_count += sum(item) // 13 
    
    for i in range (franchise):
        add = 0
        for j in range(day):
            add += new_list[j][i]
        if add % 13 == 0:
            bonus_count += add // 13 
    
    print(bonus_count)
