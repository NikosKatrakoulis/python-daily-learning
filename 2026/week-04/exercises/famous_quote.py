# Find a quote from a famous person you admire. Print the quote and the
# name of its author. Your output should look something like the following,
# including the quotation marks:
#  Albert Einstein once said, "A person who never made a mistake never
# tried anything new."

famous_person = 'albert einstein'
quote = f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new."'
print(quote)

quote = '%s once said "A person who never made a mistake never tried anything new"' % (
    famous_person.title())
print(quote)

quote = '{} once said "A person who never made a mistake never tried anything new"'.format(
    famous_person.title())
print(quote)
