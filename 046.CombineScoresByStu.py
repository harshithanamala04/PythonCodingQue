# Given two dictionaries of student scores, combine them into one. If a student appears in both, add their scores.
# Example: {"Asha": 80, "Ravi": 70} and {"Ravi": 5, "Mina": 90} → {"Asha": 80, "Ravi": 75, "Mina": 90}

sheet1 = {"Asha": 80, "Ravi": 70} 
sheet2 = {"Ravi": 5, "Mina": 90}

combined_sheet = {}

combined_sheet.update(sheet1)

for key,val in sheet2.items():
    if key in combined_sheet:
        combined_sheet[key] += val
    else:
        combined_sheet[key] = val
print(combined_sheet)


# O(n + m) time and space, where n and m are the sizes of the two dictionaries