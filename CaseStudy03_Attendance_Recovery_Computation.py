attended = int(input("Enter classes attended: "))
total_classes = int(input("Enter total classes held: "))
required = 75

if total_classes <= 0 or attended < 0 or attended > total_classes:
    print("Invalid attendance details.")
else:
    percentage = attended / total_classes * 100
    print("Current attendance:", round(percentage, 2), "%")

    if percentage >= required:
        print("Status: Eligible")
        print("Additional classes needed: 0")
    else:
        extra = 0
        while (attended + extra) / (total_classes + extra) * 100 < required:
            extra += 1
        print("Status: Not eligible yet")
        print("Consecutive classes to attend:", extra)
        print("Attendance after those classes:",
              round((attended + extra) / (total_classes + extra) * 100, 2), "%")
