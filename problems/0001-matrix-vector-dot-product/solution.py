import torch

def matrix_dot_vector(a, b) -> torch.Tensor:
    """
    Compute the product of matrix `a` and vector `b` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of length m, or tensor(-1) if dimensions mismatch.
    """
    # Your implementation here
    if not isinstance(a,torch.Tensor):
        a=torch.tensor(a,dtype=torch.float32)
    if not isinstance(b,torch.Tensor):
        b=torch.tensor(b,dtype=torch.float32)
    if a.ndim != 2 or b.ndim != 1 or a.shape[1] != b.shape[0]:
        return torch.tensor(-1)
    
    return torch.matmul(a,b)
