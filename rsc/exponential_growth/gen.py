with open("data.csv","w") as file:
    x = 0
    file.write("x,y\n")
    for i in range(200):
        y = x ** 2
        x+=1
        file.write(f"{x},{y}\n")
