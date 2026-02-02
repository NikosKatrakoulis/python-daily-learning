# Write a program that converts English text into “pirate talk” using these rules:
# Words starting with a vowel get "arr" added to the end
# Words starting with consonants move the consonant cluster to the end and add "yo"
# Non-letter characters before or after words must remain unchanged
# Preserve uppercase and title-case words
# The program should process the input word by word and print the final pirate-style sentence.

text = input(
    "Enter an English sentence and I will tranlate it into a pirate talk way.")

VOWELS = "aeiouy"
translated_words = []

for word in text.split():
    # Prefix punctuation
    prefix_non_letters = []
    while word and not word[0].isalpha():
        prefix_non_letters.append(word[0])
        word = word[1:]

    if not word:
        translated_words.append("".join(prefix_non_letters))
        continue

    # Suffix punctuation
    suffix_non_letters = []
    while word and not word[-1].isalpha():
        suffix_non_letters.append(word[-1])
        word = word[:-1]
    suffix_non_letters.reverse()

    if not word:
        translated_words.append(
            "".join(prefix_non_letters) + "".join(suffix_non_letters))
        continue

    # Capitalization
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    # Rules
    if word[0] in VOWELS:
        word = word[::-1] + "arr"
    else:
        prefix_consonants = []
        while word and word[0] not in VOWELS:
            prefix_consonants.append(word[0])
            word = word[1:]
        word = word + "".join(prefix_consonants) + "yo"

    # Restore capitalization
    if was_upper:
        word = word.upper()
    elif was_title:
        word = word.title()

    final_word = "".join(prefix_non_letters) + word + \
        "".join(suffix_non_letters)
    translated_words.append(final_word)

result = " ".join(translated_words)
print(result)
