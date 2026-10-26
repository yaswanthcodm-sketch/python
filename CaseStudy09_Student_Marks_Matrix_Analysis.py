students = ["Asha", "Ravi", "Kiran"]
subjects = ["Mathematics", "Physics", "Programming"]
marks = [
    [85, 78, 92],
    [67, 74, 70],
    [45, 52, 48]
]

print("--- Student Averages ---")
student_averages = []
for i in range(len(students)):
    average = sum(marks[i]) / len(marks[i])
    student_averages.append(average)
    print(students[i] + ":", round(average, 2))

top_index = student_averages.index(max(student_averages))
print("Highest average:", students[top_index],
      "with", round(student_averages[top_index], 2))

print("\n--- Subject Averages ---")
for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total += marks[i][j]
    average = total / len(students)
    print(subjects[j] + ":", round(average, 2))
    if average < 50:
        print("  Attention: average is below 50.")
