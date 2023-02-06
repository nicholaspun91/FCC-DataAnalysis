import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    array = np.array([list[0:3], list[3:6], list[6:9]])

    calculations = {
    'mean' : [[np.mean(array[:, 0]), np.mean(array[:, 1]), np.mean(array[:, 2])], [np.mean(array[0]), np.mean(array[1]), np.mean(array[2])], np.mean(array)],
    'variance' : [[np.var(array[:, 0]), np.var(array[:, 1]), np.var(array[:, 2])], [np.var(array[0]), np.var(array[1]), np.var(array[2])], np.var(array)],
    'standard deviation' : [[np.std(array[:, 0]), np.std(array[:, 1]), np.std(array[:, 2])], [np.std(array[0]), np.std(array[1]), np.std(array[2])], np.std(array)],
    'max' : [[np.max(array[:, 0]), np.max(array[:, 1]), np.max(array[:, 2])], [np.max(array[0]), np.max(array[1]), np.max(array[2])], np.max(array)],
    'min' : [[np.min(array[:, 0]), np.min(array[:, 1]), np.min(array[:, 2])], [np.min(array[0]), np.min(array[1]), np.min(array[2])], np.min(array)],
    'sum' : [[np.sum(array[:, 0]), np.sum(array[:, 1]), np.sum(array[:, 2])], [np.sum(array[0]), np.sum(array[1]), np.sum(array[2])], np.sum(array)]
    }
    return calculations