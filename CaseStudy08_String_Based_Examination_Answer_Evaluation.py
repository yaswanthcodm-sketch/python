answer_key = ["A", "C", "B", "D", "A"]
answers = input("Enter 5 answers separated by spaces (use - for blank): ")
answers = answers.upper().split()

if len(answers) != 5:
    print("Please enter exactly 5 answers.")
else:
    correct = 0
    incorrect = 0
    unanswered = 0

    for i in range(len(answer_key)):
        if answers[i] == "-":
            unanswered += 1
        elif answers[i] == answer_key[i]:
            correct += 1
        else:
            incorrect += 1

    score = correct * 2 - incorrect * 0.5
    print("\n--- Examination Result ---")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Unanswered:", unanswered)
    print("Final score:", round(score, 2), "out of 10")
