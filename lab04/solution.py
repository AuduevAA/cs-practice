from statistics import mean

def winner(names, scores):
    best = max(zip(names, scores), key=lambda x: x[1])
    return best[0]

def average(scores) -> float:
    return round(mean(scores), 2)
