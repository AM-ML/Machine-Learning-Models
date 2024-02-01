import numpy as np
from csv import DictReader
from time import time

def f(w, b, x):
    return np.dot(w, x) + b

def cost_func(w, b, x, y):
    m = len(y)
    predictions = np.dot(x, w) + b
    cost = np.sum((predictions - y) ** 2)
    return (1 / (2 * m)) * cost

def fetch():
    data = {'x1': [], 'x2': [], 'x3': [], 'x': [], 'y': []}

    with open("data.csv", "r") as file:
        fl = DictReader(file)

        for row in fl:
            data['x1'].append(np.float64(row["x1"]))
            data['x2'].append(np.float64(row["x2"]))
            data['x3'].append(np.float64(row["x3"]))
            data['x'].append([np.float64(row["x1"]), np.float64(row["x2"]), np.float64(row["x3"])])
            data['y'].append(np.float64(row["y"]))

    data['x'] = np.array(data['x'], dtype=np.float64)
    data['y'] = np.array(data['y'], dtype=np.float64)

    return data['x'], data['y']

def normalize_data(x, y):
    mx = np.max(np.concatenate((x, y.reshape(-1, 1)), axis=1))
    x /= mx
    y /= mx
    return x, y

def compute_gradient(w, b, x, y, iters, alpha):
    m = len(y)
    n = len(w)

    for iteration in range(iters):
        predictions = np.dot(x, w) + b
        errors = predictions - y

        for j in range(n):
            w_val = np.sum(errors * x[:, j]) / m
            w[j] -= alpha * w_val

        b_val = np.sum(errors) / m
        b -= alpha * b_val

        print(f"{iteration}: {w[0]:.2f} {w[1]:.2f} {w[2]:.2f} {b}")

def main():
    x, y = fetch()

    # x, y = normalize_data(x, y)

    # print(x[0], y[0])

    # print(x[-1], y[-1])

    w, b = np.zeros(3, dtype=np.float64), 0.0

    iters = 400
    alpha = 0.003

    t = time()

    compute_gradient(w, b, x, y, iters, alpha)

    t = time() - t
    t *= 1000

    print(f"finished in: {t:.0f}ms")
    print(f"{w[0]:.2f} {w[1]:.2f} {w[2]:.2f} {b:.2f}")

    x_str = input("enter x: ")
    x_in = np.array([np.float64(num) for num in x_str.split(',')])

    y_hat = f(w, b, x_in)

    print(f"y prediction: {y_hat:.2f}")

    print(x[0], y[0])

if __name__ == "__main__":
    main()
