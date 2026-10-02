import unicodedata


def sanitize_text(text):
    if not isinstance(text, str):
        raise TypeError("Please enter correct type of text")

    normalize = unicodedata.normalize("NFKC", text)

    lowered = normalize.casefold()

    cleaned = "".join(char for char in lowered if char.isalnum())

    return cleaned


def is_palindrome(text):
    cleaned = sanitize_text(text)

    if len(cleaned) <= 1:
        return True

    return cleaned == cleaned[::-1]


def format_result(text, result):
    status = "symmetric word" if result else "Not symmetric word"
    return f"Result for {text} : {result}"


def test_case():
    test_case = [
        ("hello", False),
        ("repaper", True),
        ("tenet", True),
        ("گرگ", True)
    ]

    for phrase, expected in test_case:
        actual = is_palindrome(phrase)

        assert actual == expected, f"error in {phrase}"
        print(f"Pass: '{phrase}', '{actual}'")


def main():
    test_case()
    while True:
        user_input = input(f"Enter the word that you think it's Palindrome:) : ")

        if not user_input:
            print("You must enter a word")
            return

        result = is_palindrome(user_input)
        print(format_result(user_input, result))

        answer = input("Do you want to continue? (y/n): ").lower().strip()
        if answer != 'y':
            print("\n have a good day")
            break


if __name__ == '__main__':
    main()
