from collections import (
    _OrderedDictItemsView,
    _OrderedDictValuesView,
    _OrderedDictKeysView,
)


class DictSorted(dict):
    ordered_keys = []

    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        """self[key] = value"""
        if (
            key not in self.ordered_keys
        ):  # Bad lookup strategy into list. Could be optimized with dicts
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def keys(self):
        return _OrderedDictKeysView(self)

    def values(self):
        return _OrderedDictValuesView(self)

    def items(self):
        return _OrderedDictItemsView(self)

    def __iter__(self):
        """for x in self"""
        return self.ordered_keys.__iter__()  # What's done here??


ds = DictSorted()
d = {}

ds["a"] = 1
ds["b"] = 2
ds.setdefault("c", 3)

d["a"] = 1
d["b"] = 2
d.setdefault("c", 3)

print(ds)
print(d)

for k, v in ds.items():
    print(f"K: {k}, V: {v}")

for k, v in d.items():
    print(f"K: {k}, V: {v}")
