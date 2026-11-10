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


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []

    arr = np.asarray(matrix)
    means = np.mean(arr, axis=0)
    means_rounded = np.round(means, 6)

    return means_rounded.tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0

    arr = np.asarray(matrix)
    col_data = arr[:, column]
    rng = np.max(col_data) - np.min(col_data)

    return float(np.round(rng, 6))