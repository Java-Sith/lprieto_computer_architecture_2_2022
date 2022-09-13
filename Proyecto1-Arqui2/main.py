from tkinter import *
import time
from random import randint
from threading import *

root = Tk()
root.title("Threading Example!")
root.geometry("500x400")

P1 = [["B1", "I", "0x000", 0], ["B2", "I", "0x000", 0], ["B3", "I", "0x010", 0], ["B4", "I", "0x011", 0]]
P2 = [["B1", "I", "0x110", 0], ["B2", "I", "0x010", 0], ["B3", "I", "0x110", 0], ["B4", "I", "0x010", 0]]
P3 = [["B1", "I", "0x101", 0], ["B2", "I", "0x011", 0], ["B3", "I", "0x111", 0], ["B4", "I", "0x100", 0]]
P4 = [["B1", "I", "0x011", 0], ["B2", "I", "0x111", 0], ["B3", "I", "0x011", 0], ["B4", "I", "0x101", 0]]
Memoria = {"0x000": 0, "0x001": 0, "0x010": 0, "0x011": 0, "0x100": 0, "0x101": 0, "0x110": 0, "0x111": 0}

def five_seconds():
    time.sleep(5)
    my_label.config(text="5 Seconds Is Up!")

my_label = Label(root, text="I made a thread")
my_label.pack(pady=20)

my_button1 = Button(root, text="5 Seconds", command=Thread(target=five_seconds()).start())
# my_button1 = Button(root, text="5 Seconds", command=five_seconds)
my_button1.pack(pady=20)

random_label = Label(root, text="Random number")
random_label.pack(pady=20)

def rando():
    random_label.config(text=f'Random number is: {randint(1, 100)}')

my_button2 = Button(root, text="Pick Random Number", command=rando)
my_button2.pack(pady=20)

def fact(x):
    f = 1
    for i in range(x):
        f = f * (i + 1)
    return f

def bincoeff(a, b):
    comb = fact(a) / (fact(b) * fact(a - b))
    return comb

def binomial_dist(n, k, p):
    dist = bincoeff(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return dist

if __name__ == '__main__':
    mainloop()
"""     dist = binomial_dist(10, 4, 0.3)
    print(dist) """

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
