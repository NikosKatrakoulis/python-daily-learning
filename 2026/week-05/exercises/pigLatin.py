# Pig latin is a silly made-up language that alters English words. If a word
# begins with a vowel, the word yay is added to the end of it. If a word begins
# with a consonant or consonant cluster (like ch or gr), that consonant or con
# sonant cluster is moved to the end of the word and followed by ay.
# This program works by altering a string using the methods introduced
# in this chapter.

message = input("Enter the English message to translate into pig latin:")

VOWELS = "aeiouy"
pig_latin_words = []

for word in message.split():
    prefix_non_letters = []
    while word and not word[0].isalpha():
        prefix_non_letters.append(word[0])
        word = word[1:]

    if not word:
        pig_latin_words.append("".join(prefix_non_letters))
        continue

    suffix_non_letters = []
    while word and not word[-1].isalpha():
        suffix_non_letters.append(word[-1])
        word = word[:-1]

    suffix_non_letters.reverse()

    was_upper = word.isupper()
    was_title = word.istitle()

    prefix_consonants = []
    while word and word[0] not in VOWELS:
        prefix_consonants.append(word[0])
        word = word[1:]

    if prefix_consonants:
        word = word + "".join(prefix_consonants) + "ay"
    else:
        word = word + "yay"

    if was_upper:
        word = word.upper()
    elif was_title:
        word = word.title()

    final_word = "".join(prefix_non_letters) + word + \
        "".join(suffix_non_letters)
    pig_latin_words.append(final_word)

print(" ".join(pig_latin_words))
