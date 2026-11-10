import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    arr = np.asarray(values)
    reshaped = arr.reshape(-1, width)

    return reshaped.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix)
    result = arr[np.ix_(rows, columns)]

    return result.tolist()