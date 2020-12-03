import pandas

# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    """
    Asks user for a word and prints out the word using
    the NATO phonetic alphabet.
    """
    # print(phonetic_dict)
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
