# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
#new_list = ['hello','world']

def FindCharacters(listOfWords, character):
    new_list = []
    for everyWord in listOfWords:
        if everyWord.find(character) >= 0:
            new_list.append(everyWord)
    return new_list

print FindCharacters(word_list, char)