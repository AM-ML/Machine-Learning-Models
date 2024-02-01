import numpy as np

a = 1

data = np.array([[1, 1], [2, 2], [3, 3]])

def J():
    errors = a * data[:, 0] - data[:, 1]
    squared_errors = np.square(errors)
    total_error = np.sum(squared_errors)
    
    return total_error / (2 * len(data))


while True:
    a = float(input("enter slope:     "))
    print(f"       cost:     {J()}")
