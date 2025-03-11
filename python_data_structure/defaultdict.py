from collections import defaultdict


def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


print(letter_frequency("Hii, what's up? how do you do??"))

stock_prices = defaultdict(list)
stock_prices["II"].append("hello")
stock_prices["II"].append("Hi")
stock_prices["JJ"].append("Yoo")
print(stock_prices)

num_items = 0


def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])


d = defaultdict(tuple_counter)
d["a"][1].append("Hii")
d["b"][1].append("Hello")
print(d)
