def get_longest_words(text: str):
    words = text.split()
    if not words:
        return [], 0
    max_len = max(map(len, words))
    longest = [w for w in words if len(w) == max_len]
    return longest, max_len


words, length = get_longest_words(input("Your sentence: "))

print("Longest word(s):")
for w in words:
    print(f"{w} ({length} letters)")
