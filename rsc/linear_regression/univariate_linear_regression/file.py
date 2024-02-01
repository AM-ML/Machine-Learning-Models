import numpy as np
from sympy import symbols, diff
from time import sleep

def smt(x):
    for i in str(x):
        print(i, flush=True, end="")
        sleep(0.03)
    print()

def f(theta, x):
    return theta[0] * x + theta[1]

def cost_func(theta, x, y):
    m = len(y)
    cost = 0

    for i in range(m):
        y_hat = f(theta, x[i])
        cost += (y_hat - y[i])**2

    return (1/(2*m)) * cost

def gradient_descent(x, y, theta, alpha, iterations):
    theta0, theta1 = symbols("theta0 theta1", real=True)
    
    theta0_val = theta[0]
    theta1_val = theta[1]
  
    m = len(y)

    for iteration in range(iterations):
        
        lrdw = diff(cost_func([theta0, theta1], x, y), theta0)
        lrdb = diff(cost_func([theta0, theta1], x, y), theta1)

        theta[0] = theta[0] - (alpha * lrdw.subs({theta0: theta0_val, theta1: theta1_val}))
        theta0_val = theta[0]
        
        theta[1] = theta[1] - (alpha * lrdb.subs({theta0: theta0_val, theta1: theta1_val}))
        theta1_val = theta[1]

        out = (f"{iteration}: {theta0_val:.2f}, {theta1_val:.2f}")
        print(out)

def main():
    data = np.array([[1, -2], [2, -4], [3, -6], [4, -8], [5, -10], [6, -12]])

    x = data[:, 0]
    y = data[:, 1]

    alpha = 0.05
    iterations = 200

    theta = np.zeros(2)

    theta[0] = 0.5  # slope not y-intercept
    theta[1] = 0    # y-intercept not slope

    gradient_descent(x, y, theta, alpha, iterations)

    print(f"slope: {theta[0]}")

    x_input = float(input("enter x: "))
    y_hat = f(theta, x_input)

    out = (f"y prediction: {y_hat:.2f}")
    smt(out)

if __name__ == "__main__":
    main()
