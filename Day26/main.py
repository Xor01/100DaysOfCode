# NATO alphabet converter

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(data)

letter_list = {row.letter: row.code for (index, row) in data.iterrows()}


def generate():
    user_inp = input("Enter a word or a sentence: ").upper()

    try:
        nato_alpha = [letter_list[letter] for letter in user_inp ]
    except KeyError:
        print("Only English letters are allowed")
        generate()
    else:
        print(nato_alpha)


generate()
