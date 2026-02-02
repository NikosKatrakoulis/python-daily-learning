# Create a program that transforms English text using the following rules:
# If a word starts with a vowel, add "woo" to the end
# If a word starts with a consonant, move the first consonant group to the end and add "zip"
# Keep all punctuation in the correct place
# Restore the original capitalization of each word
# The program should read a sentence from the user and print the
# transformed result.


text = input(
    "Enter an English sentence and I will transform it into a silly suffix language.")

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
        word = word[::-1] + "woo"
    else:
        prefix_consonants = []
        while word and word[0] not in VOWELS:
            prefix_consonants.append(word[0])
            word = word[1:]
        word = word + "".join(prefix_consonants) + "zip"

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
