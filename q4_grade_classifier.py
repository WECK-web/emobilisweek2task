# q4_grade_classifier.py

score = int(input("Enter your test score (0–100): "))

if 80 <= score <= 100:
    print("Excellent")
elif 50 <= score < 80:
    print("Good")
elif 0 <= score < 50:
    print("Needs Improvement")
else:
    print("Invalid score entered.")
# This program classifies a test score into categories: Excellent, Good, or Needs Improvement based on the score range.