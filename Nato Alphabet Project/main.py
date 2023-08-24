import pandas

nato_phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dict = {item[0]: item[1] for item in
                               [row[1].values for row in nato_phonetic_alphabet_data.iterrows()]}
print(nato_phonetic_alphabet_dict)


def generate_phonetic() -> object:
    word = input("Enter a word: ").upper()
    try:
        phonetics = [nato_phonetic_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetics)


generate_phonetic()
