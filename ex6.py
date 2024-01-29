#Create a tuple of student names and their corresponding scores. Write a function to find
#the student with the highest score.


def find_highest_scorer(students):
    if not students:
        print("No students in the tuple.")
        return None

    highest_scorer = max(students, key=lambda x: x[1])
    return highest_scorer

student_scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

highest_scorer = find_highest_scorer(student_scores)

if highest_scorer:
    print({highest_scorer[0]},{highest_scorer[1]})


