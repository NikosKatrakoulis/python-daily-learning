# Ask the user for a sentence (example: "I love python programming").
# Use split() to get the words, convert them to lowercase, and then use
# join() to produce:
# "#i #love #python #programming"
# Print the final hashtag string.

sentence = input("Give me a sentence:")

words = sentence.lower().split()

hashtags = ['#' + word for word in words]

result = ' '.join(hashtags)
print(result)
