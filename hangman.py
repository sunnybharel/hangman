import random


def read_word_from_file(name_of_file):
    with open(name_of_file, 'r') as f:
        pick = random.randint(0, len(f.readlines()))
        f.seek(0)
        return f.readlines()[pick]

def input_letter():
    letter = input("Enter a letter: ")
    return letter[0] if letter.isalpha() else print("Expected non-numeric letter")

def match_letter(letter, word):
    return True if letter.lower() in word or letter.upper() in word else False

def populate_and_show(letter, word, formed_word):
    for x in range(0,len(word)-1):
        if letter ==  word[x].upper() or letter == word[x].lower():
            formed_word[x] = letter
    return formed_word

def pretty_print(what_to_print):
    for x in range(0,len(what_to_print)):
        print(what_to_print[x], end=" ")
    print ("\n")

#Common variables and initializing
formed_word = []
filename = 'words.txt'
kill_count = 20
guess_word = read_word_from_file(filename)

#Present Initial clue:
for x in range(0,len(guess_word)-1):
    print("_", end=" ")
print("\n")

#Populate empty array with underscore. This array will be used to determine player progress
for x in range(0,len(guess_word)-1):
    formed_word.append('_')

#Main loop
while kill_count > 0:

    guess_letter = input_letter()
    if match_letter(guess_letter, guess_word):
        formed_word = populate_and_show(guess_letter, guess_word, formed_word)
        pretty_print(formed_word)
    else:
        pretty_print(formed_word)
        kill_count -= 1
        print("Remaining chances: {}".format(kill_count))
        print ("Oops!")
print ("Word was: {}\nBetter luck next time".format(guess_word))


