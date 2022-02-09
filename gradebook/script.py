last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#create lists
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

#add more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

#modify gradebook
gradebook[-1][-1] = 98

#change numerical grade to Pass
gradebook[2].remove(85)
gradebook[2].append("Pass")

#combine lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)