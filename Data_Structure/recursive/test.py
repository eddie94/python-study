from random import randint

mid = []
final = []
PF = []

for i in range(100):
    mid.append(randint(100))
    final.append(randint(100))

for mid_score, final_score in zip(mid, final):
    if mid_score + final_score >= 110:
