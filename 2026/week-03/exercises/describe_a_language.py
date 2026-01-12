# Write a function called describe_language() that accepts the name of a
# language and the country where it is spoken. Give the country parameter
# a default value. The function should print a sentence describing where
# the language is spoken. Call the function for three different languages,
# including at least one that is not spoken in the default country.

def describe_language(language_name, coutry="us"):
    """Describe a language."""
    msg = f"\n{language_name.title()} language is spoken in {coutry.title()}."
    print(msg)


describe_language("english")
describe_language("spanish")
describe_language(language_name="greek", coutry="greece")
