"""Decrypt message"""
word = input()
word_size = len(word)
vowel = 'aeiou'
new_word = ''
index_value = 0

while word_size >= 1:
    if word[index_value] not in vowel:
        new_word += word[index_value]
        word_size -=1
        index_value += 1
    
    elif word[index_value] in vowel:
        if word[index_value + 1] == 'p' and word[index_value + 2] == word[index_value]:
            new_word += word[index_value + 2]
            word_size -= 3
            index_value += 3

print(new_word)