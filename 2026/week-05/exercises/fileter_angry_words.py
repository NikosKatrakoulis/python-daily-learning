# You are given a sentence and a list of angry words such as
# ["angry", "furious", "mad"].
# Write a program that:
# splits the sentence into words
# replaces any angry word with "***" (case-insensitive)
# preserves punctuation marks like ! , . ?
# rebuilds and prints the cleaned sentence using " ".join(...)

sentence = "I'am angry, furious and mad with what you did to yourself."
banned_words = ["angry", "furious", "mad"]

words = sentence.split()
clean_words = []

for word in words:
    punctuation = " "

    if word[-1] in "?!,.":
        punctuation = word[-1]
        clean_word = word[:-1]
    else:
        clean_word = word

    if clean_word.lower() in banned_words:
        clean_words.append('***' + punctuation)
    else:
        clean_words.append(word)

clean_sentence = " ".join(clean_words)
print(clean_sentence)
