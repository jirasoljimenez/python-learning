
def student_name():
    """Prompt for and return student name"""
    return input ("Student name: ")

def is_valid_score(s):
    """Helper: validate a single score"""
    if s < 0 or s > 100:
        print("Invalid!")
        return False
    return True

def get_exam_scores(n):
    """Collect n exam scores with validation"""
    scores = []
    for i in range(n):
        scores.append(get_validated_scores(i))
    print(scores)
    return(scores)

def get_validated_scores(i):
    """Helper: retry loop for score entry"""
    s = 0
    while True:
        try:
            s = int(input(f"Exam {i+1} score: "))
            if is_valid_score(s): break
        except ValueError:
            print("Numbers please") 
    print(s)
    return(s)

def calculate_average(scores):
    """Compute mean of a scores list"""
    average = sum(scores) / len(scores)
    return average

def determine_letter_grade(average):
    """Map average to letter grade"""
    if average >= 90: grade = "A"
    elif average >= 80: grade = "B"
    elif average >= 70: grade = "C"
    elif average >= 60: grade = "D"
    else: grade = "F"
    return grade

def determine_standing(grade):
    """Map average to academic standing"""
    if grade == "A": standing = "Deans's List"
    elif grade == "B" or grade == "C": standing = "Good Standing"
    elif grade == "D": standing = "Academic Probation"
    else: standing = "Academic Warning"
    return standing

def print_divider():
    """Helper: print a decorative line"""
    print("=" * 30)

def display_report(name, scores, average, grade, standing):
    """Print the formatted grade report"""

    print_divider()
    print("STUDENT GRADE REPORT")
    print_divider()

    print(F"Student: {name}")

    #for loop to print scores
    for i in range(len(scores)):
        print(f"Exam {i}: {scores[i]}")

    print("-"*30)
    print(f"Average: {average:.02f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print_divider()

def main():
    """Orchestrate the full program"""
    print("Student Grade Tracker")
    name = student_name()
    scores = get_exam_scores(3)
    average = calculate_average(scores)
    grade = determine_letter_grade(average)
    standing = determine_standing(grade)
    display_report(name, scores, average, grade, standing)

def test_grade_tracker():
    """Run all unit tests"""
    name = student_name()
    scores = get_exam_scores(3)
    average = calculate_average(scores)
    grade = determine_letter_grade(average)
    standing = determine_standing(grade)
    print(f"{name}, {scores}, {grade}, {standing}")
    
main()
