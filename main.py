import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()} #Formating into an organised dictionary using comprehension

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        Output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(Output_list)

generate_phonetic()
