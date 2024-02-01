from sys import argv

with open("data.csv", "w") as file:
    file.write("x1,x2,x3,y\n")
    x1=1
    x2=2
    x3=3
    y =0
    for i in range(int(argv[1])):
        if i==0:
            x1 = 1
            x2 = 2
            x3 = 3
        else:
            x1+=0.01*x1
            x2+=(0.02*x2)-0.01*x1
            x3+=(0.03*x3)-0.02*x2

        y= (1*x1) +(2*x2)+(3*x3)
        if abs(y) >= 60:
            break
        file.write(f"{x1},{x2},{x3},{y}\n")
