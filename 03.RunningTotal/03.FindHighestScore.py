# Given a dictionary of names and scores, print the name with the highest score. You may assume at least one entry and no tied scores.
# Example: {"Asha": 80, "Ravi": 92, "Mina": 85} → Ravi

stu_list = {"Asha": 80, "Ravi": 92, "Mina": 85}

highest_student = max(stu_list, key=stu_list.get) # Score-Based Sorting It looks at "Asha", but evaluates it as 80.
print(highest_student)

# print(max(stu_list)) # Alphabetical Sorting


