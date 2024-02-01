import numpy as np
from csv import DictReader
from time import time
import matplotlib.pyplot as plt
from subprocess import call

print("library loaded!")

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
            data['x1'].append(float(row["x1"]))
            data['x2'].append(float(row["x2"]))
            data['x3'].append(float(row["x3"]))
            data['x'].append([float(row["x1"]), float(row["x2"]), float(row["x3"])])
            data['y'].append(float(row["y"]))

    data['x'] = np.array(data['x'])
    data['y'] = np.array(data['y'])

    return data['x'], data['x1'], data['x2'], data['x3'], data['y']

def compute_gradient(w, b, x, y, max_iters, initial_alpha=0.01, epsilon=1e-9):
    m = len(y)
    n = len(w)
    alpha = initial_alpha

    prev_cost = float('inf')

    for iteration in range(max_iters):
        predictions = np.dot(x, w) + b
        errors = predictions - y

        for j in range(n):
            w_val = np.sum(errors * x[:, j]) / m
            w[j] -= alpha * w_val

        b_val = np.sum(errors) / m
        b -= alpha * b_val

        cost = cost_func(w, b, x, y)

        if iteration % 100 == 0:
            print(f"Iteration {iteration}: Cost {cost:.6f}")

        if abs(prev_cost - cost) < epsilon:
            print(f"Converged at iteration {iteration}")
            break

        if cost > prev_cost:
            # If cost increases, reduce learning rate
            alpha *= 0.5
            print(f"Reducing learning rate to {alpha}")

        prev_cost = cost

    return w, b

def plott(x1,x2,x3,y):
    plt.scatter(x1,y,label="x1",marker=".",c="r")
    plt.scatter(x2,y,label="x2",marker=".",c="g")
    plt.scatter(x3,y,label="x3",marker=".",c="b")
    plt.title("Testing Plot of X and Y")
    plt.ylabel("Outcome Y")
    plt.xlabel("X Features")
    plt.legend()
    plt.show()


def main():
    x, x1, x2, x3, y = fetch()


    w, b = np.array([0.01,0.01,0.01]), 0

    iters = 2004
    alpha = 0.005

    t = time()

    w, b = compute_gradient(w, b, x, y, max_iters=10000)

    t = time() - t
    t*=1000

    call("cls",shell=True)

    print(f"finished in: {t:.0f}ms")

    print(f"{w[0]:.2f} {w[1]:.2f} {w[2]:.2f} {b:.2f}")
    try:
     while True:
        x_str = input("enter x: ")
        x_in = np.array([float(num) for num in x_str.split(',')])
    
        y_hat = f(w, b, x_in)

        print(f"y prediction: {y_hat:.2f}")
    except KeyboardInterrupt:

        plott(x1,x2,x3,y)

if __name__ == "__main__":
    main()

