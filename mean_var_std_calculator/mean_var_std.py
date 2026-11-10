import numpy as np

def calculate(lst):
    lst = np.array(lst)
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    numbers = np.array(lst, dtype=float).reshape(3, 3)
    
    calculations = {
        "mean": [
            np.mean(numbers, axis=0).tolist(),
            np.mean(numbers, axis=1).tolist(),
            float(np.mean(numbers)),
        ],
        "variance": [
            np.var(numbers, axis=0).tolist(),
            np.var(numbers, axis=1).tolist(),
            float(np.var(numbers)),
        ],
        "standard deviation": [
            np.std(numbers, axis=0).tolist(),
            np.std(numbers, axis=1).tolist(),
            float(np.std(numbers)),
        ],
        "max": [
            np.max(numbers, axis=0).tolist(),
            np.max(numbers, axis=1).tolist(),
            float(np.max(numbers)),
        ],
        "min": [
            np.min(numbers, axis=0).tolist(),
            np.min(numbers, axis=1).tolist(),
            float(np.min(numbers)),
        ],
        "sum": [
            np.sum(numbers, axis=0).tolist(),
            np.sum(numbers, axis=1).tolist(),
            float(np.sum(numbers)),
        ],
    }
    return calculations


calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])