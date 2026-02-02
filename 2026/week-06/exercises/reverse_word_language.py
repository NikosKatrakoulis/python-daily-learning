# Write a program that translates English text into a made-up language
# using these rules: Words that start with a vowel should be reversed and
# end with "va". Words that start with a consonant or consonant cluster
# should move that cluster to the end and add "co". Preserve: punctuation
# at the beginning and end of words original capitalization (uppercase
# and title case). The program should: split the input into words, process
# each word individually rebuild and print the translated sentence.

import pyperclip

text = pyperclip.paste()

VOWELS = "aeiouy"
translated_words = []

for word in text.split():
    prefix_non_letters = []
    while word and not word[0].isalpha():
        prefix_non_letters.append(word[0])
        word = word[1:]

    if not word:
        translated_words.append("".join(prefix_non_letters))
        continue

    suffix_non_letters = []
    while word and not word[-1].isalpha():
        suffix_non_letters.append(word[-1])
        word = word[:-1]
    suffix_non_letters.reverse()

    if not word:
        translated_words.append(
            "".join(prefix_non_letters) + "".join(suffix_non_letters))
        continue

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    if word[0] in VOWELS:
        word = word[::-1] + "va"
    else:
        prefix_consonants = []
        while word and word[0] not in VOWELS:
            prefix_consonants.append(word[0])
            word = word[1:]
        word = word + "".join(prefix_consonants) + "co"

    if was_upper:
        word = word.upper()
    elif was_title:
        word = word.title()

    final_word = "".join(prefix_non_letters) + word + \
        "".join(suffix_non_letters)
    translated_words.append(final_word)

result = " ".join(translated_words)
print(result)
