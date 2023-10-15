import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()} #Formating into an organised dictionary using comprehension


word = input("Enter a word: ").upper()

Output_list = [phonetic_dict[letter] for letter in word]
print(Output_list)
