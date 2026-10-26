subjects = ["Mathematics", "Physics", "Programming"]
first_marks = []
final_marks = []

for subject in subjects:
    mark = float(input("Enter first assessment mark for " + subject + ": "))
    first_marks.append(mark)

for subject in subjects:
    mark = float(input("Enter final assessment mark for " + subject + ": "))
    final_marks.append(mark)

all_marks = first_marks + final_marks
if any(mark < 0 or mark > 100 for mark in all_marks):
    print("Invalid marks: enter values from 0 to 100.")
else:
    print("\n--- Performance Trend ---")
    for i in range(len(subjects)):
        change = final_marks[i] - first_marks[i]
        if change > 0:
            trend = "Improved by " + str(round(change, 2))
        elif change < 0:
            trend = "Declined by " + str(round(abs(change), 2))
        else:
            trend = "No change"
        print(subjects[i] + ":", trend)

    average = sum(final_marks) / len(final_marks)
    weakest_index = final_marks.index(min(final_marks))

    if average >= 75:
        category = "Excellent"
    elif average >= 60:
        category = "Good"
    elif average >= 40:
        category = "Satisfactory"
    else:
        category = "Needs Improvement"

    print("Final average:", round(average, 2))
    print("Weakest subject:", subjects[weakest_index])
    print("Overall category:", category)
