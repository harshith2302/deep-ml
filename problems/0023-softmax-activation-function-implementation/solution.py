import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score = max(scores)
    exp_scores = [math.exp(score-max_score) for score in scores]
    sum_exp = sum(exp_scores)
    return [round(val/sum_exp,4) for val in exp_scores]