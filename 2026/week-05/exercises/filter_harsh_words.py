# You have a sentence and a list of harsh words such as
# ["awful", "horrible", "disgusting"].
# Write a program that:
# splits the sentence into words
# replaces each harsh word with "***" (case-insensitive)
# keeps punctuation intact
# rebuilds and prints the sentence using join()

sentence = "You are awful, horrible and disgusting Pablo!"
banned_words = ["awful", "horrible", "disgusting"]

words = sentence.split()
clean_words = []

for word in words:
    punctuation = " "

    if word[-1] in "!?,.":
        punctuation = word[-1]
        clean_word = word[:-1]
    else:
        clean_word = word

    if clean_word.lower() in banned_words:
        clean_words.append("***" + punctuation)
    else:
        clean_words.append(word)


clean_sentence = " ".join(clean_words)
print(clean_sentence)
