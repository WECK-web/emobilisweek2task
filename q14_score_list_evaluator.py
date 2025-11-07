# q14_score_list_evaluator.py

scores = [65, 88, 42, 90, 73, 55]
above_70 = 0
below_or_equal_70 = 0

for score in scores:
    if score > 70:
        above_70 += 1
    else:
        below_or_equal_70 += 1

print(f"Scores above 70: {above_70}")
print(f"Scores 70 or below: {below_or_equal_70}")
# This program evaluates a list of scores, counting how many are above 70 and how many are 70 or below, then displays the counts.