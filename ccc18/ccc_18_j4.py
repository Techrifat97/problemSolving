"""American or canadian"""
word_list = list()
while True:
    word = input()
    word_size = len(word)
    vowel = 'aeiouy'
    
    if word_size > 4 and word != 'quit!':
        if word[word_size - 1] == 'r' and word [word_size - 2] and word[word_size - 3] not in vowel:
            word = word[:-2] + word[word_size - 2] + 'u' + word[word_size - 1]
            word_list.append(word)
        else:
            word_list.append(word)
            
    elif word == 'quit!':
        break
   
    elif word != 'quit!':
        word_list.append(word)
    

for item in word_list:
    print(item)