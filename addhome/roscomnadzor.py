from random import choice

words = ["apple", "banana", "self"]
word = choice(words)
search = ''
save = ''
print("_ " * len(word))

while True:
    letter = input("input your letter: ")
    if letter in word and letter not in save:
        save += letter
    # for i in word:
    #     if i in save:
    #         search += str(i) + " "
    #     else:
    #         search += "_ "
    print(save)
    print(search)