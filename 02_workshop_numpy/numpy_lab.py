import numpy as np
import random


def n_size_ndarray_creation(n, dtype=np.int):
    return np.array(np.arange(n**2), dtype).reshape(n, n)


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 99:
        return np.array(random.sample(range(-float('inf'), float('inf')), shape[0]*shape[1]), dtype).reshape(*shape)
    else:
        return np.array([type]*(shape[0] * shape[1]), dtype).reshape(*shape)


def change_shape_of_ndarray(X, n_row):
    return X.reshape(n_row, -1)


def concat_ndarray(X_1, X_2, axis):
    return np.concatenate((X_1, X_2), axis=axis)


def normalize_ndarray(X, axis=99, dtype=np.float32):
    pass


def save_ndarray(X, filename="test.npy"):
    pass


def boolean_index(X, condition):
    pass


def find_nearest_value(X, target_value):
    pass


def get_n_largest_values(X, n):
    pass

print(n_size_ndarray_creation(9))
# print(zero_or_one_or_empty_ndarray(shape=(1,11), type=99))
print(change_shape_of_ndarray(np.array([1,2,3,4,5,6]), 2))
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(concat_ndarray(a, b, 0))