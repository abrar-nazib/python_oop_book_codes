from collections import Counter


def letter_frequency(sentence):
    return Counter(sentence)


print(letter_frequency("Hii, What's up??"))

responses = ["vanilla", "chocolate", "vanilla", "caramel", "strawberry", "vanilla"]

# Returns an array of tuples
print(f"Most voted: {Counter(responses).most_common(1)}")
# Output: Most voted: [('vanilla', 3)]