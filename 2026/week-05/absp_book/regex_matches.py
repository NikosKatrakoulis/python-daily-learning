# The best and worst thing about regular expressions is that they will match
# exactly what you ask for. Here are some common points of confusion
# regarding character classes:
# • The [A-Z] or [a-z] character class matches uppercase or lowercase
# letters, respectively, but not both. You need to use [A-Za-z] to match
# both cases.
# • The [A-Za-z] character class matches only plain, unaccented letters. For
# example, the regex string r'First Name: ([A-Za-z]+)' would match “First
# Name: ” followed by a group of one or more unaccented letters. But
# singer Sinéad O’Connor’s first name would match up to the é only, and
# the group would be set to 'Sin'.
# • The \w character class matches all letters, including accented letters
# and characters from other alphabets. But it also matches numbers and
# the underscore character, so the regex string r'First Name: (\w+)' may
# match more than you intended.
# • The \w character class matches all letters, but the regex string r'Last
# Name: (\w+)' would capture Sinéad O’Connor’s last name only up until
# the apostrophe character. This means the group would capture her last
# name as 'O'.
# • Straight and smart quote characters (' " ‘ ’ “ ”) are considered com
# pletely different from each other and must be specified separately.
# Real-world data is complicated. Even if your program manages to cap
# ture Sinéad O’Connor’s name, it could fail with Jean-Paul Sartre’s name
# because of the hyphen.
