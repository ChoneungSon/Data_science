import numpy as np
import random


def n_size_ndarray_creation(n, dtype=np.int):
    return np.array(np.arange(n**2), dtype=dtype).reshape(n, n)


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 99:
        return np.empty(shape=shape, dtype=dtype)
    elif type == 1:
        return np.ones(shape=shape, dtype=dtype)
    else:
        return np.zeros(shape=shape, dtype=dtype)


def change_shape_of_ndarray(X, n_row):
    return X.flatten() if n_row == 1 else X.reshape(n_row, -1)


def concat_ndarray(X_1, X_2, axis):
    if X_1.ndim == 1:
        X_1 = X_1.reshape(1, -1)
    if X_2.ndim == 1:
        X_2 = X_2.reshape(1, -1)
    return np.concatenate((X_1, X_2), axis=axis)


def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(dtype)
    n_row, n_column = X.shape
    if axis==99: return (X - X.mean()) / X.std()
    if axis==0:
        x_mean = np.mean(X, axis=axis).reshape(1, -1)
        x_std = np.std(X, axis=axis).reshape(1, -1)
    if axis==1:
        x_mean = np.mean(X, axis=axis).reshape(n_row, -1)
        x_std = np.std(X, axis=axis).reshape(n_row, -1)
    return (X - x_mean) / x_std


def save_ndarray(X, filename="test.npy"):
    file_test = open(filename, 'wb')
    np.save(X, file_test)


def boolean_index(X, condition):
    conditon = eval(str("X") + condition)
    return np.where(condition)


def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X-target_value))]


def get_n_largest_values(X, n):
    # index로 반환된다.
    return X[np.argsort(X)[::-1]][:n]