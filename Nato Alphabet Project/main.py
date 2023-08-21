import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

#TODO 1. Create a dictionary in this format:
nato_phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dict = {item[0]: item[1] for item in [row[1].values for row in nato_phonetic_alphabet_data.iterrows()]}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetics = [nato_phonetic_alphabet_dict[letter] for letter in word]
print(phonetics)
