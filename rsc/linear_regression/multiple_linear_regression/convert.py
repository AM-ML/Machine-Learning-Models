from csv import DictReader
import numpy as np


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
    data['x1'] = np.array(data['x1'])
    data['x2'] = np.array(data['x2'])
    data['x3'] = np.array(data['x3'])
    data['y'] = np.array(data['y'])

    return data['x'], data['x1'], data['x2'], data['x3'], data['y']

def main():
    x, x1, x2, x3, y = fetch()

  

    mx3 = np.max(x3)
    mx1,mx2,my = mx3,mx3,mx3
    for i in range(len(y)):

        x[i][0] = x[i][0] / mx1
        x[i][1] = x[i][1] / mx2
        x[i][2] = x[i][2] / mx3
        y[i] = y[i] / my

    print(x[-1])
    print(y[-1])


if __name__ == "__main__":
     main()