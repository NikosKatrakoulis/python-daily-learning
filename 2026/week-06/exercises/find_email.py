# Prompt:
# You have a text (string) and you want to identify all the e-mails it contains.
# Requirements:
# Write a regex that finds e-mails of the form username@domain.tld.
# Assume that:
# username: letters/numbers/dot/underscore
# domain: letters/numbers/hyphen
# tld: 2 to 4 letters
# You should return a list with all matches.
# Test data (indicative):
# "Send to nikos.pap_12@example.com or to test@my-site.gr. Not to a@b.c."

import re

EMAIL_RE = re.compile(
    r"""
    (?P<email>
        [a-zA-Z0-9._]+
        @
        [a-zA-Z0-9-]+
        \.
        [a-zA-Z]{2,4}
        )""",
    re.VERBOSE
)


def extract_emails(text: str) -> list[str]:
    """Return all email-like strings found in text."""
    return [m.group("email") for m in EMAIL_RE.finditer(text)]


def main() -> None:
    sample = "Send to nikos.pap_12@example.com or to test@my-site.gr. Not to a@b.c."
    print(extract_emails(sample))


if __name__ == "__main__":
    main()
