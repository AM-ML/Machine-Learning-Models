with open("data.csv", "w") as file:
    file.write("x1,x2,x3,y\n")
    x1=1
    x2=2
    x3=3
    y =0
    for i in range(500):
        if i==0:
            x1 = 1
            x2 = 2
            x3 = 3
        else:
            x1+=9/x2
            x2+=6/x3
            x3+=4/x3

        y= (5*x1) +(6*x2)+(28*x3)
        file.write(f"{x1},{x2},{x3},{y}\n")