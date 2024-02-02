from csv import DictReader
from matplotlib.pyplot import scatter, title, ylabel,xlabel,legend,show
from numpy import array
data = []

with open("data.csv", "r") as file:
    fl = DictReader(file)
    for row in fl:
        data.append([float(row['x']),float(row['y'])])

data = array(data)
x = data[:, 0]
y = data[:, 1]

def plott(x,y):
    scatter(x,y,label="X",marker=".",c="b")
    title("Exponential Growth Plot")
    ylabel("Y Outcome")
    xlabel("X Features")
    legend()
    show()

plott(x,y)
