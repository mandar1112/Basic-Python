scores = [10, 20, 30, 40, 50, 31, 70, 80, 90, 100]
min_score = min(scores)
print("Minimum score:", min_score)

"""
lowest = scores[0]
for score in scores:
    if lowest > score:
        lowest = score
print(f"Lowest Score: {lowest}")
"""

max_score = max(scores)
print("Maximum score:", max_score)
"""
# Alternative way to find the highest score without using max()
highest = scores[0]

for score in scores:
    if highest < score:
        highest = score
print(f"Highest Score: {highest}")
"""

"""
lowest = highest = scores[0]
for score in scores:
    if lowest > score:
        lowest = score
    if highest < score:
        highest = score

print(f"Lowest Score: {lowest}")
print(f"Highest Score: {highest}")
"""


total_score = sum(scores)
print("Total score:", total_score)



