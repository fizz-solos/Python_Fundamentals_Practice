scores = [65, 80, 90, 45, 70, 55, 30, 88]

def average_score(scores):
    return sum(scores)/len(scores)

def highest_score(scores):
    return max(scores)

passing_scores = [item for item in scores if item >= 50]

passed_students = len(passing_scores)

average = average_score(scores)
Highest = highest_score(scores)

print(f"The Average score is {average}\nThe Highest score is {Highest}\nPassing scores are {passing_scores}\nPassing students are {passed_students}")