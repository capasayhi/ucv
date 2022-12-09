# Problem A
""" Dos palabras son anagramas si tienen la mismas letras pero, en otro orden. Por ejemplo, «torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» tiene una r de más y una a de menos . Diseñe un programa que indique si un par de palabras suministradas como datos son anagramas. """


print("\nType 2 words to determine if they are anagrams\n")

typing_alert = "Hey! there's an error, make sure you're typing words with only letthers, and no spaces"

# This is so that the program works regardless of whether the words are in uppercase or lowercase.
word_1 = input("First word: ").lower()
if word_1.isalpha():
    word_2 = input("Second word: ").lower()
    if word_2.isalpha():

        list_1 = []
        list_2 = []

        for character in list_1:
            list_1.append(character)
        list_1.sort()h
        for character in list_2:
            list_2.append(character)
        list_2.sort()

        if list_1 == list_2:
            print("Words are anagrams")
        else:
            print("Words are not anagrams")
    else:
        print(typing_alert)
else:
    print(typing_alert)


# Alternative to problem A (efficient method, without validations)
"""
word_1 = input("First word: ")
word_2 = input("Second word: ")

 if (sorted(word_1.lower()) == sorted(word_2.lower()):
    print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")
 """

""" The sorted() function returns a sorted list of the specified iterable object. You can specify an ascending or descending order. Strings are sorted alphabetically and numbers are sorted numerically. """


# Problem B
""" A tautogram is a sentence in which each word begins with the same letter. For example "Truly tautograms triumph",  is a valid tautogram, while "Pedro suffers from programming" is not a tautogram. Design a program that outputs True if the input sentence is a tautogram and False if it is not. """


print("\nNow enter a sentence to determine if it is a Tautogram\n")
sentence = input("Sentence: ").lower()

words_in_sentence = sentence.split(" ")
comparator = sentence[0]

print(words_in_sentence)
print(comparator)


if len(words_in_sentence) > 1:
    character_validator = True
    tautogram_validator = True

    for word in words_in_sentence:
        if not word.isalpha() or word == '':
            character_validator = False
        elif word[0] != comparator:
            tautogram_validator = False
    if character_validator:
        print(f"{tautogram_validator}")
    else:
        print("Oops! Try again and verify you're typing words with only letters separated for one space")
else:
    print("Type a sentence of at least two words")
