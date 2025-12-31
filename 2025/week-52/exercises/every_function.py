# Every Function: Think of things you could store in a list.
# For example, you could make a list of mountains, rivers, countries,
# cities, languages, or anything else you’d like. Write a program that
# creates a list containing these items and then uses each function
# introduced in this chapter at least once.

languages = ['python', 'java', 'c#', 'c++']
print(languages)

languages.append('javaScript')
print(languages)

languages.insert(2, 'go')
print(languages)

removed_language = languages.pop()
print(f"Unfortunatelly I don't like {removed_language}.")

number_of_languages = len(languages)
print(f"I know {number_of_languages} programming languages.")

del languages[-1]
print(languages)

languages.remove('java')
print(languages)

languages.append('java')
languages.append('go')
languages.append('c++')

print(languages)

print(sorted(languages))
print(languages)

print(sorted(languages, reverse=True))
print(languages)

languages.reverse()
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)
