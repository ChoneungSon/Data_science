import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    data = pd.read_csv('./'+filename)
    df = pd.DataFrame(data, dtype=dtype, columns=['source', 'target', 'rating'])
    df.set_index('source')




def get_frequent_matrix(filename, dtype=np.float32):
    pass
