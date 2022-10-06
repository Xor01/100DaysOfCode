# NATO alphabet converter

import pandas

user_inp = input("Enter a word or a sentence: ").upper()

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(data)


letter_list = {row.letter: row.code for (index, row) in data.iterrows()}
NATA_alpha = [letter_list[letter] for letter in user_inp if letter in letter_list.keys()]

print(NATA_alpha)
