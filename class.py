






array = []
# word = ['ГУБЕРНАТОР']
word = 'AZAUKA'

word_completion = '_' * len(word[0])

for index, symbols in enumerate(word):
    if symbols == 'A':
        array.append(index)
print(array)

# result = ['_________']

# result[0] = 'A'

# print(result)