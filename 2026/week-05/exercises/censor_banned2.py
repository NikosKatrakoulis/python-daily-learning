# You have a sentence and a list of negative words such as
# ["hate", "stupid", "terrible"].
# Write a program that:
# splits the sentence into words
# replaces each negative word with "***" (case-insensitive)
# keeps punctuation intact
# rebuilds and prints the sentence using join().

sentence = "I hate you! You are stupid and terrible!"
banned_words = ["hate", "stupid", "terrible"]

words = sentence.split()
clean_words = []

for word in words:
    clean_word = word.strip("!.?,")
    if clean_word.lower() in banned_words:
        clean_words.append("***")
    else:
        clean_words.append(word)

clean_sentence = " ".join(clean_words)
print(clean_sentence)
