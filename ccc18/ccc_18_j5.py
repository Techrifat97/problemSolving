"""Magnus"""
string_input =input()
position = 0    
count = 0

while position < len(string_input):
    if string_input[position] == 'H':
        position_H = string_input.index('H', position)
        position = position_H
        
        while position < len(string_input):
            if string_input[position] == 'O':
                position_O = string_input.index('O', position)
                position = position_O
                
                while position < len(string_input):
                    if string_input[position] == 'N':
                        position_N = string_input.index('N', position)
                        position = position_N
                        
                        while position < len(string_input):
                            if string_input[position] == 'I':
                                position_I = string_input.index('I', position)
                                position = position_I
                                count += 1
                                break
                            position += 1
                        break
                    position += 1
                break
            position += 1
        continue
    position += 1

print(count)