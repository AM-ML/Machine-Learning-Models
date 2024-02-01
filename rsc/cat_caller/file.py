from time import sleep
from random import randint

cats = []

def initialize_cat_names():
    temps = ["Whiskers", "Cleo", "Luna", "Simba", "Misty", "Oliver", "Chloe", "Jasper", "Gizmo", "Alex"]
    
    for temp in temps:
        cats.append(temp)

initialize_cat_names()

def choose_name():
    if len(cats) == 0:
        initialize_cat_names()
    index = randint(0,len(cats)-1)
    name = cats[index]
    cats.pop(index)

    return name


def smt(x,t=0.05):
    for i in x:
        print(i, flush=True, end="")
        sleep(t/len(x))
    print()

count = int(input("enter cats: "))

for i in range(count):
    name = choose_name()
    smt(f"{i+1}: Hello, {name}!")
    sleep(0.03)

sleep(0.5)

if count >= 5:
    smt("that's alot of cats!", 0.3)
if count >= 10:
    smt(f"Do you have a spare {choose_name()} I can borrow?",0.5)
