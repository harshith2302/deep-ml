import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    probabilities=[]
    for x in features:
        linear_comb = sum(f*w for f,w in zip(x,weights))+bias
        prob=1/(1+math.exp(-linear_comb))
        probabilities.append(round(prob,4))
    mse=sum((p-l)**2 for p,l in zip(probabilities,labels))/len(labels) 
    return probabilities, round(mse,4)