# Project 24: Mail Merge
# Guillaume CC, aka TheFirewallDragon

with open("./input/names/invitedNames.txt") as invited_names:
    names_list = (invited_names.readlines())

with open("./input/letters/startingLetter.txt") as file:
    contents = file.read()

    for name in names_list:
        name = name.strip()
        new = contents.replace("[name]", name)
        with open(f"./output_readyToSend/letter_for_{name}.txt",
                  mode="w") as final_file:
            final_file.write(new)