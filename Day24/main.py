# Mail Merger

PLACEHOLDER = "[name]"


with open("Input/Letters/starting_letter.txt") as letter:
    new_letter = letter.read()


with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    formatted_name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{formatted_name}.txt", 'w') as out:
        name_letter = new_letter
        name_letter = name_letter.replace(PLACEHOLDER, formatted_name)
        out.write(name_letter)
