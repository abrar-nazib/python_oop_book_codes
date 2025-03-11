# from functools import total_ordering


# @total_ordering
# class WeridSortee:
#     def __init__(self, string, number, sort_num):
#         self.string = string
#         self.number = number
#         self.sort_num = sort_num

#     def __lt__(self, object):
#         if self.sort_num:
#             return self.number < object.number

#         return self.string < object.string

#     def __repr__(self):
#         return f"{self.string}:{self.number}"

#     def __eq__(self, object):
#         return all(
#             (
#                 self.string == object.string,
#                 self.number == object.number,
#             )
#         )


# a = WeridSortee("a", 4, True)
# b = WeridSortee("b", 3, True)
# c = WeridSortee("c", 2, True)
# d = WeridSortee("d", 1, True)
# l = [a, b, c, d]
# print(l)
# l.sort()
# print(l)  # [d:1, c:2, b:3, a:4]
# for i in l:
#     i.sort_num = False
# l.sort()
# print(l)  # [a:4, b:3, c:2, d:1]


# Usage of key

# l = ["hello", "Help", "Helo"]
# l.sort() # ['Helo', 'Help', 'hello']
# print(l)
# l.sort(key=str.lower) # ['hello', 'Helo', 'Help']
# print(l)

# Sorting based on tuple elements
from operator import itemgetter

l = [("h", 4), ("n", 6), ("o", 5), ("p", 1), ("t", 3), ("y", 2)]
print(l)
l.sort(key=itemgetter(1))
print(l)
