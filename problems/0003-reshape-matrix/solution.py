import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    arr=np.array(a)
    total_elements = arr.size
    r,c = new_shape
    if(total_elements!=r*c):
        return []

    return arr.reshape(new_shape).tolist()