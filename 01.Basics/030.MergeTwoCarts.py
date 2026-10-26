# Given two dictionaries of item quantities, combine them. If an item appears in both, add its quantities.
# Example: {"apple": 2, "pear": 1} and {"apple": 3, "orange": 4} → {"apple": 5, "pear": 1, "orange": 4}

dict1 = {"apple": 2, "pear": 1}
dict2 = {"apple": 3, "orange": 4}

combined_dict = {}

combined_dict.update(dict1)
for key,val in dict2.items():
    if key in combined_dict:
        combined_dict[key] += val
    else:
        combined_dict[key] = val

print(combined_dict)


