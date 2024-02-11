import numpy as np

def calculate(matrix):

    if matrix.shape != (3, 3):
        raise ValueError("Liste dokuz sayı içermelidir.")

    result = {
        "mean":{
            "row": np.mean(matrix,axis=1).tolist(),
            "column":np.mean(matrix,axis=0).tolist(),
            "overall": np.mean(matrix),
        },
        "varience":{
            "row":np.var(matrix,axis=1).tolist(),
            "column":np.var(matrix,axis=0).tolist(),
            "overall":np.var(matrix),
        },
        "standard_deviation": {
            "row": np.std(matrix, axis=1).tolist(),
            "column": np.std(matrix, axis=0).tolist(),
            "overall": np.std(matrix),
        },
        "max": {
            "row": np.max(matrix, axis=1).tolist(),
            "column": np.max(matrix, axis=0).tolist(),
            "overall": np.max(matrix),
        },
        "min": {
            "row": np.min(matrix, axis=1).tolist(),
            "column": np.min(matrix, axis=0).tolist(),
            "overall": np.min(matrix),
        },
        "sum": {
            "row": np.sum(matrix, axis=1).tolist(),
            "column": np.sum(matrix, axis=0).tolist(),
            "overall": np.sum(matrix),
        },
    }

    return result

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result=calculate(matrix)

print("mean:", result["mean"])
print("varience:",result["varience"])
print("standard_deviation:",result["standard_deviation"])
print("max:",result["max"])
print("min:",result["min"])
print("sum:",result["sum"])