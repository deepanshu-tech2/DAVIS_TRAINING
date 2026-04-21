q = {"2+2": "4"}
score = 0

for ques, ans in q.items():
    if input(ques + ": ") == ans:
        score += 1

print(score)
