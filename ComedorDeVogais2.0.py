word_without_vowels= " "
user_word = input("Pick up a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == 'A':
        continue
    if letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        word_without_vowels = word_without_vowels + letter
print(word_without_vowels + " ")