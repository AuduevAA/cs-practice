from statistics import mean

def winner(names, scores):
    best = max(zip(names, scores), key=lambda x: x[1])
    return best[0]

def average(scores) -> float:
    return round(mean(scores), 2)

def ranking(names, scores):
    sorted_p = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)
    return [pair[0] for pair in sorted_p]

def above_average(names, scores):
    avg = average(scores)
    return [name for name, score in zip(names, scores) if score > avg]
