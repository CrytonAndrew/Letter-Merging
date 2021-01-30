
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    lines_list = letter.readlines()

with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()


for name in names_list:
    for line in lines_list:
        new_line = line.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt",  "a") as new_letters:
            new_letters.writelines(new_line)
