students = {
    "Karen": [45, 67, 52, 37, None],
    "Andy": [85, None, 78, 92, None],
    "James": [68, 45, 79, 91, 48],
    "Hannah": [74, 51, None, None, 89],
    "Andrew": [88, 97, 77, 94, 94],
}

average_scores = {name: sum(score for score in scores if score is not None) /
                        len([score for score in scores if score is not None])
                  for name, scores in students.items()}

students_with_missed_work = [name for name, scores in students.items() if None in scores]

students_with_multiple_missed_works = [name for name, scores in students.items() if scores.count(None) > 1]

print("AVG grades:")
for name, average_score in average_scores.items():
    print(f"{name}: {average_score:.2f}")

print("\nStudents with only 1 missed work (alphabetical order):")
print(sorted(students_with_missed_work))

print("\nStudents with multiple missed homework (random order):")
print(students_with_multiple_missed_works)