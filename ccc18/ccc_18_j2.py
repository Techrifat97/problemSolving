"""Do The Shuffle"""

song_list = ['A','B','C','D','E']
output = ''
while True:
    button = int(input())
    action = int(input())
    
    if button == 1:
        for index in range(action):
           item = song_list.pop(0)
           song_list.append(item)
    
    elif button == 2:
        for index in range(action):
            item = song_list.pop(4)
            song_list.insert(0,item)
    elif button == 3:
        song_list[0],song_list[1] = song_list[1], song_list[0]
    elif button == 4 and action == 1:
        break
print(' '.join(song_list))