import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    x_n = np.random.rand(data.shape[0])
    for i in range(num_steps):
        A_x_n = data.dot(x_n)
        x_n = A_x_n / np.sqrt(np.sum(A_x_n * A_x_n))

    return float(np.dot(x_n, data.dot(x_n)) / np.dot(x_n, x_n)), x_n
