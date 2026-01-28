# You have a sentence and a list of banned words, for example
# ["bad", "ugly"]. Use split() to break the sentence into words.
# Replace any banned word with "***".
# Use " ".join(...) to rebuild the sentence and print it.

sentence = "You are ugly and bad!"
banned_words = ["ugly", "bad"]

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
