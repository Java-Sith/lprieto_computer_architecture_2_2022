from multiprocessing import process
from tkinter import *
import time
from random import randint
from threading import *
from random import *

# root = Tk()
# root.title("Threading Example!")
# root.geometry("500x400")

P0 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
P1 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
P2 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
P3 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
Memory = {"0000": 0, "0001": 0, "0010": 0, "0011": 0, "0100": 0, "0101": 0, "0110": 0, "0111": 0}
readMiss = 0
writeMiss = 0
readHit = 0
writeHit = 0

# def five_seconds():
#     time.sleep(5)
#     my_label.config(text="5 Seconds Is Up!")

# my_label = Label(root, text="I made a thread")
# my_label.pack(pady=20)

# my_button1 = Button(root, text="5 Seconds", command=Thread(target=five_seconds()).start())
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
    return round(dist * 10)

def write_back(mem_block, data):
    if(mem_block is not None):
        for key in Memory:
            if(mem_block == key):
                Memory[key] = data
    else:
        print("This didn't work")

def state_change(current_state, action, processor, row, inMemory):
    if(current_state == "I"):
        if(action == "Read"):
            if(inMemory):
                processor[row][1] = "E"
            else:
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
            write_back(processor[row][2], processor[row][3])
        elif(action == "ReadCache"):
            processor[row][1] = "S"
            write_back(processor[row][2], processor[row][3])
    elif(current_state == "E"):
        if(action == "WriteCache"):
            processor[row][1] = "I"
        elif(action == "Write"):
            processor[row][1] = "M"
        elif(action == "ReadCache"):
            processor[row][1] = "S"

def read_memory(mem_block, processor, row):
    for key in Memory:
        if (key == mem_block):
            if(key == "0000" or key == "0100"):
                processor[0][2] = key
                processor[0][3] = Memory[key]
                return 0, True
            elif(key == "0001" or key == "0101"):
                processor[1][2] = key
                processor[1][3] = Memory[key]
                return 1, True
            elif(key == "0010" or key == "0110"):
                processor[2][2] = key
                processor[2][3] = Memory[key]
                return 2, True
            elif(key == "0011" or key == "0111"):
                processor[3][2] = key
                processor[3][3] = Memory[key]
                return 3, True
            else:
                print("Key not found!")
                break
        else:
            print("Key not compatible!")

def write_inst(mem_block, processor, data):
    global writeMiss
    global writeHit
    for i in range(4):
        if(processor[i][2] == mem_block):
            processor[i][3] = data
            writeHit += 1
            return i, False
        else:
            if(processor[i][2] == "I"):
                processor[i][3] = data
                writeMiss += 1
                return i, False
            elif(processor[i][2] == "S" or processor[i][2] == "M"):
                processor[i][3] = data
                writeMiss += 1
                return i, False
            else:
                writeMiss += 1

def read_inst(mem_block, processor):
    global readMiss
    global readHit
    for i in range(4):
        if (P0[i][2] == mem_block and P0[i][1] == "E"):
            processor[i][3] = P0[i][3]
            if(processor != P0):
                readMiss += 1
            else:
                readHit += 1
            return i, False
    for i in range(4):
        if (P1[i][2] == mem_block and P1[i][1] == "E"):
            processor[i][3] = P1[i][3]
            if(processor != P1):
                readMiss += 1
            else:
                readHit += 1
            return i, False
    for i in range(4):
        if (P2[i][2] == mem_block and P2[i][1] == "E"):
            processor[i][3] = P2[i][3]
            if(processor != P2):
                readMiss += 1
            else:
                readHit += 1
            return i, False
    for i in range(4):    
        if (P3[i][2] == mem_block and P3[i][1] == "E"):
            processor[i][3] = P3[i][3]
            row = i
            if(processor != P3):
                readMiss += 1
            else:
                readHit += 1
            return i, False
    else:
        readMiss += 1
        row, inMemory = read_memory(mem_block, processor, i)
        return row, inMemory

def generate_inst(processor):
    n = randint(1, 20)
    k = randint(1, 10)
    p = randint(0, 5) / randint(5, 10)
    dist = binomial_dist(n, k, p)
    if(processor == P0):
        if(dist == 0):
            inst = "P0" + " " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P0" + " " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "CALC"
    elif(processor == P1):
        if(dist == 0):
            inst = "P1" + " " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P1" + " " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "CALC"
    elif(processor == P2):
        if(dist == 0):
            inst = "P2" + " " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P2" + " " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "CALC"
    elif(processor == P3):
        if(dist == 0):
            inst = "P3" + " " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P3" + " " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "CALC"
    return inst

def firstProcessorL1():
    inst = generate_inst(P0)
    instArr = inst.split(" ")
    if(instArr[1] == "READ"):
        row, inMemory = read_inst(instArr[2], P0)
        state_change(P0[row][1], "Read", P0, row, inMemory)
        state_change(P1[row][1], "ReadCache", P1, row, inMemory)
        state_change(P2[row][1], "ReadCache", P2, row, inMemory)
        state_change(P3[row][1], "ReadCache", P3, row, inMemory)
    elif(instArr[1] == "WRITE"):
        row = write_inst(instArr[2], P0, instArr[3])
        state_change(P0[row][1], "Write", P0, row, inMemory)
        state_change(P1[row][1], "WriteCache", P1, row, inMemory)
        state_change(P2[row][1], "WriteCache", P2, row, inMemory)
        state_change(P3[row][1], "WriteCache", P3, row, inMemory)
    else:
        print("Calculating...")

def secondProcessorL1():
    inst = generate_inst(P1)
    instArr = inst.split(" ")
    if(instArr[1] == "READ"):
        row, inMemory = read_inst(instArr[2], P1)
        state_change(P0[row][1], "ReadCache", P0, row, inMemory)
        state_change(P1[row][1], "Read", P1, row, inMemory)
        state_change(P2[row][1], "ReadCache", P2, row, inMemory)
        state_change(P3[row][1], "ReadCache", P3, row, inMemory)
    elif(instArr[1] == "WRITE"):
        row, inMemory = write_inst(instArr[2], P1, instArr[3])
        state_change(P0[row][1], "WriteCache", P0, row, inMemory)
        state_change(P1[row][1], "Write", P1, row, inMemory)
        state_change(P2[row][1], "WriteCache", P2, row, inMemory)
        state_change(P3[row][1], "WriteCache", P3, row, inMemory)
    else:
        print("Calculating...")

def thirdProcessorL1():
    inst = generate_inst(P2)
    instArr = inst.split(" ")
    if(instArr[1] == "READ"):
        row, inMemory = read_inst(instArr[2], P2)
        state_change(P0[row][1], "ReadCache", P0, row, inMemory)
        state_change(P1[row][1], "ReadCache", P1, row, inMemory)
        state_change(P2[row][1], "Read", P2, row, inMemory)
        state_change(P3[row][1], "ReadCache", P3, row, inMemory)
    elif(instArr[1] == "WRITE"):
        row, inMemory = write_inst(instArr[2], P2, instArr[3])
        state_change(P0[row][1], "WriteCache", P0, row, inMemory)
        state_change(P1[row][1], "WriteCache", P1, row, inMemory)
        state_change(P2[row][1], "Write", P2, row, inMemory)
        state_change(P3[row][1], "WriteCache", P3, row, inMemory)
    else:
        print("Calculating...")

def fourthProcessorL1():
    inst = generate_inst(P3)
    instArr = inst.split(" ")
    if(instArr[1] == "READ"):
        row = read_inst(instArr[2], P3)
        state_change(P0[row][1], "ReadCache", P0, row)
        state_change(P1[row][1], "ReadCache", P1, row)
        state_change(P2[row][1], "ReadCache", P2, row)
        state_change(P3[row][1], "Read", P3, row)
    elif(instArr[1] == "WRITE"):
        row = write_inst(instArr[2], P3, instArr[3])
        state_change(P0[row][1], "WriteCache", P0, row)
        state_change(P1[row][1], "WriteCache", P1, row)
        state_change(P2[row][1], "WriteCache", P2, row)
        state_change(P3[row][1], "Write", P3, row)
    else:
        print("Calculating...")

if __name__ == '__main__':
    print("Caché 1:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P0]))
    print('\n')
    print("Caché 2:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P1]))
    print('\n')
    print("Caché 3:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P2]))
    print('\n')
    print("Caché 4:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P3]))
    print('\n')
    firstProcessorL1()
    print('\n')
    print("Caché 1:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P0]))
    print('\n')
    print("Caché 2:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P1]))
    print('\n')
    print("Caché 3:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P2]))
    print('\n')
    print("Caché 4:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
