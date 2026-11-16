import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    arr=np.array(vectors,dtype=float)
    cov_matrix=np.cov(arr,rowvar=True)
    return cov_matrix.tolist()