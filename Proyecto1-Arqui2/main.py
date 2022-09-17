from tkinter import *
import time
from random import randint
from threading import *

# root = Tk()
# root.title("Threading Example!")
# root.geometry("500x400")

P1 = [["B1", "I", "0x000", 0], ["B2", "I", "0x000", 0], ["B3", "I", "0x010", 0], ["B4", "I", "0x011", 0]]
P2 = [["B1", "I", "0x110", 0], ["B2", "I", "0x010", 0], ["B3", "I", "0x110", 0], ["B4", "I", "0x010", 0]]
P3 = [["B1", "I", "0x101", 0], ["B2", "I", "0x011", 0], ["B3", "I", "0x111", 0], ["B4", "I", "0x100", 0]]
P4 = [["B1", "I", "0x011", 0], ["B2", "I", "0x111", 0], ["B3", "I", "0x011", 0], ["B4", "I", "0x101", 0]]
Memory = {"0x000": 0, "0x001": 0, "0x010": 0, "0x011": 0, "0x100": 0, "0x101": 0, "0x110": 0, "0x111": 0}
Instructions = {0: "P0: READ 0100", 1: "P1: CALC", 2: "P2: WRITE 1010, 4A3B", 3: "P3: CALC"}

# def five_seconds():
#     time.sleep(5)
#     my_label.config(text="5 Seconds Is Up!")

# my_label = Label(root, text="I made a thread")
# my_label.pack(pady=20)

# my_button1 = Button(root, text="5 Seconds", command=Thread(target=five_seconds()).start())
# # my_button1 = Button(root, text="5 Seconds", command=five_seconds)
# my_button1.pack(pady=20)

# random_label = Label(root, text="Random number")
# random_label.pack(pady=20)

# def rando():
#     random_label.config(text=f'Random number is: {randint(1, 100)}')

# my_button2 = Button(root, text="Pick Random Number", command=rando)
# my_button2.pack(pady=20)

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

def state_change(current_state, action, processor, row):
    if(current_state == "I"):
        if(action == "Read"):
            processor[row][1] = "S"
        elif(action == "Write"):
            processor[row][1] = "M"
    elif(current_state == "S"):
        if(action == "WriteCache"):
            processor[row][1] = "I"
        elif(action == "Write"):
            processor[row][1] = "M"
    elif(current_state == "M"):
        if(action == "WriteCache"):
            processor[row][1] = "I"
    elif(current_state == "E"):
        if(action == "WriteCache"):
            processor[row][1] = "I"
        elif(action == "Write"):
            processor[row][1] = "M"
        elif(action == "ReadCache"):
            processor[row][1] = "S"

def read_inst(mem_block, data, processor):
    if(mem_block is not None):
        if(mem_block == "0x000" or mem_block == "0x100"):
            processor[0][1] = "M"
            processor[0][3] = data
            processor[0][2] = "0x000"
        elif(mem_block == "0x001" or mem_block == "0x101"):
            processor[1][1] = "M"
            processor[1][3] = data
            processor[1][2] = "0x001"
        elif(mem_block == "0x010" or mem_block == "0x110"):
            processor[2][1] = "M"
            processor[2][3] = data
            processor[2][2] = "0x010"
        elif(mem_block == "0x011" or mem_block == "0x111"):
            processor[3][1] = "M"
            processor[3][3] = data
            processor[3][2] = "0x011"
    else:
        print("This didn't work")

def write_back(mem_block, data, processor):
    if(mem_block is not None):
        if(mem_block == "0x000" or mem_block == "0x100"):
            processor[0][1] = "M"
            processor[0][3] = data
            processor[0][2] = "0x000"
        elif(mem_block == "0x001" or mem_block == "0x101"):
            processor[1][1] = "M"
            processor[1][3] = data
            processor[1][2] = "0x001"
        elif(mem_block == "0x010" or mem_block == "0x110"):
            processor[2][1] = "M"
            processor[2][3] = data
            processor[2][2] = "0x010"
        elif(mem_block == "0x011" or mem_block == "0x111"):
            processor[3][1] = "M"
            processor[3][3] = data
            processor[3][2] = "0x011"
    else:
        print("This didn't work")
        

if __name__ == '__main__':
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in P2]))
    write_back("0x010", Memory["0x010"], P2)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in P2]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
