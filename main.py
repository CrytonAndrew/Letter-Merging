# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Get the letter and store as list
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    lines_list = letter.readlines()

with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()


for name in names_list:
    for line in lines_list:
        new_line = line.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt",  "a") as new_letters:
            new_letters.writelines(new_line)


