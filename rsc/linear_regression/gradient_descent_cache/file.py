import numpy as np
from time import time
from sys import exit
from csv import DictReader

dt = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]])


def check():
    with open("cache_1.csv", "r") as file:
        fl = DictReader(file)

        data = []
        w = 0
        b = 0

        for row in fl:
           rd1 = row["data1"]
           rd2 = row["data2"]
           data_row = np.array([float(rd1), float(rd2)])  # Convert to float
           data.append(data_row)

        if np.array_equal(dt, data):
            print("data familiar, cache enabled!")

            with open("cache_2.csv", "r") as file:
                fl = DictReader(file)

                for row in fl:
                    w = float(row["w"])  # Convert to float
                    b = float(row["b"])  # Convert to float

            x_in = float(input("enter x: "))
            y_hat = f([b, w], x_in)

            print(f"y prediction: {y_hat:.2f}")
            exit(0)
        else:
            print("data change detected!")



def f(theta, x):
    return theta[0] + theta[1] * x

def cost_func(theta, x, y):
    sigma = 0

    m = len(y)

    for i in range(m):
        sigma += (f(theta, x[i]) - y[i]) ** 2

    return (1 / (2 * m)) * sigma

def gradient_descent(theta, x, y, alpha, iterations):

    m = len(y)
    for iteration in range(iterations):
        w = 0
        b = 0
        for i in range(m):
            w += (f(theta, x[i]) - y[i]) * x[i]
            b += f(theta, x[i]) - y[i]

        theta[1] = theta[1] - alpha * w / m
        theta[0] = theta[0] - alpha * b / m

        theta1_val = theta[1]
        theta0_val = theta[0]

#        print(f"{iteration}: {theta1_val:.2f} {theta0_val:.2f}")

def main():
    theta = [0, 0]

    x = dt[:, 0]
    y = dt[:, 1]
    iterations = 4000
    alpha = 0.03

    t = time()

    gradient_descent(theta, x, y, alpha, iterations)

    t = time() - t

    print(f"finished in: {t}s")

    with open("cache_1.csv", "w") as fl:
        fl.write("data1,data2\n")
        for t in dt:
            fl.write(f"{t[0]},{t[1]}\n")

    with open("cache_2.csv", "w") as fl:
        fl.write("b,w\n")
        fl.write(f"{theta[0]}, {theta[1]}\n")

    x_in = float(input("enter x: "))
    print(f"y prediction: {f(theta, x_in):.2f}")

if __name__ == "__main__":
    check()
    main()