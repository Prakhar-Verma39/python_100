with open("Input/Letters/starting_letter.txt") as f:
    message = f.read()
with open("Input/Names/invited_names.txt") as f:
    people = f.readlines()
    for person in people:
        person = person.strip('\n')
        with open(f"Output/ReadyToSend/letter_for_{person}", 'w') as file:
            file.write(message.replace("[name]", person))
