from multiprocessing import process
from tkinter import *
from tkinter import ttk
from time import *
from random import randint
from threading import *
from random import *

root = Tk()
root.title("MESI Cache Simulator!")
root.geometry("900x600")

P0 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
P1 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
P2 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
P3 = [["B1", "I", "0000", "0000"], ["B2", "I", "0000", "0000"], ["B3", "I", "0000", "0000"], ["B4", "I", "0000", "0000"]]
Memory = {"0000": "0000", "0001": "0000", "0010": "0000", "0011": "0000", "0100": "0000", "0101": "0000", "0110": "0000", "0111": "0000"}
readMiss = 0
writeMiss = 0
readHit = 0
writeHit = 0

# def five_seconds():
#     time.sleep(5)
#     my_label.config(text="5 Seconds Is Up!")

my_tree1 = ttk.Treeview(root)
my_tree2 = ttk.Treeview(root)
my_tree3 = ttk.Treeview(root)
my_tree4 = ttk.Treeview(root)
my_tree5 = ttk.Treeview(root)

my_tree1['columns'] = ("Bloque", "Estado", "Direccion", "Dato")
my_tree2['columns'] = ("Bloque", "Estado", "Direccion", "Dato")
my_tree3['columns'] = ("Bloque", "Estado", "Direccion", "Dato")
my_tree4['columns'] = ("Bloque", "Estado", "Direccion", "Dato")
my_tree5['columns'] = ("Direccion", "Dato")

my_tree1.column("#0", width=100, minwidth=20)
my_tree1.column("Estado", anchor = CENTER, width=100)
my_tree1.column("Direccion", anchor = W, width=100)
my_tree1.column("Dato", anchor = CENTER, width=100)

my_tree2.column("#0", width=100, minwidth=20)
my_tree2.column("Estado", anchor = CENTER, width=100)
my_tree2.column("Direccion", anchor = W, width=100)
my_tree2.column("Dato", anchor = CENTER, width=100)

my_tree3.column("#0", width=100, minwidth=20)
my_tree3.column("Estado", anchor = CENTER, width=100)
my_tree3.column("Direccion", anchor = W, width=100)
my_tree3.column("Dato", anchor = CENTER, width=100)

my_tree4.column("#0", width=100, minwidth=20)
my_tree4.column("Estado", anchor = CENTER, width=100)
my_tree4.column("Direccion", anchor = W, width=100)
my_tree4.column("Dato", anchor = CENTER, width=100)

my_tree5.column("#0", width=100, minwidth=20)
my_tree5.column("Direccion", anchor = W, width=100)
my_tree5.column("Dato", anchor = CENTER, width=100)

my_tree1.heading("#0", text = "Bloque", anchor = W)
my_tree1.heading("Estado", text = "Estado", anchor = W)
my_tree1.heading("Direccion", text = "Direccion", anchor = W)
my_tree1.heading("Dato", text = "Dato", anchor = W)

my_tree2.heading("#0", text = "Bloque", anchor = W)
my_tree2.heading("Estado", text = "Estado", anchor = W)
my_tree2.heading("Direccion", text = "Direccion", anchor = W)
my_tree2.heading("Dato", text = "Dato", anchor = W)

my_tree3.heading("#0", text = "Bloque", anchor = W)
my_tree3.heading("Estado", text = "Estado", anchor = W)
my_tree3.heading("Direccion", text = "Direccion", anchor = W)
my_tree3.heading("Dato", text = "Dato", anchor = W)

my_tree4.heading("#0", text = "Bloque", anchor = W)
my_tree4.heading("Estado", text = "Estado", anchor = W)
my_tree4.heading("Direccion", text = "Direccion", anchor = W)
my_tree4.heading("Dato", text = "Dato", anchor = W)

my_tree5.heading("#0", text = "", anchor = W)
my_tree5.heading("Direccion", text = "Direccion", anchor = W)
my_tree5.heading("Dato", text = "Dato", anchor = W)

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

def generate_inst(processor, lock):
    lock.acquire()
    n = randint(1, 20)
    k = randint(1, 10)
    p = randint(0, 5) / randint(5, 10)
    dist = binomial_dist(n, k, p)
    if(processor == P0):
        if(dist == 0):
            inst = "P0 " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P0 " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "P0 " + "CALC"
    elif(processor == P1):
        if(dist == 0):
            inst = "P1 " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P1 " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "P1 " + "CALC"
    elif(processor == P2):
        if(dist == 0):
            inst = "P2 " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P2 " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "P2 "+ "CALC"
    elif(processor == P3):
        if(dist == 0):
            inst = "P3 " + "READ" + " " + format(randint(0, 7), "04b")
        elif(dist == 1):
            inst = "P3 " + "WRITE" + " " + format(randint(0, 7), "04b") + " " + format(randint(0, 65535), "04X")
        else:
            inst = "P3 " + "CALC"
    print(inst)
    lock.release()
    return inst

def firstProcessorL1():
    lock = Lock()
    inst = generate_inst(P0, lock)
    instArr = inst.split(" ")
    if(instArr[1] == "READ"):
        row, inMemory = read_inst(instArr[2], P0)
        state_change(P0[row][1], "Read", P0, row, inMemory)
        state_change(P1[row][1], "ReadCache", P1, row, inMemory)
        state_change(P2[row][1], "ReadCache", P2, row, inMemory)
        state_change(P3[row][1], "ReadCache", P3, row, inMemory)
    elif(instArr[1] == "WRITE"):
        row, inMemory = write_inst(instArr[2], P0, instArr[3])
        state_change(P0[row][1], "Write", P0, row, inMemory)
        state_change(P1[row][1], "WriteCache", P1, row, inMemory)
        state_change(P2[row][1], "WriteCache", P2, row, inMemory)
        state_change(P3[row][1], "WriteCache", P3, row, inMemory)
    else:
        print("Calculating...")
        sleep(1)
    print("Caché 1:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P0]))
    print('\n')

def secondProcessorL1():
    lock = Lock()
    inst = generate_inst(P1, lock)
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
        sleep(1)
    print("Caché 2:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
        for row in P1]))
    print('\n')

def thirdProcessorL1():
    lock = Lock()
    inst = generate_inst(P2, lock)
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
        sleep(1)
    print("Caché 3:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
        for row in P2]))
    print('\n')

def fourthProcessorL1():
    lock = Lock()
    inst = generate_inst(P3, lock)
    instArr = inst.split(" ")
    if(instArr[1] == "READ"):
        row, inMemory = read_inst(instArr[2], P3)
        state_change(P0[row][1], "ReadCache", P0, row, inMemory)
        state_change(P1[row][1], "ReadCache", P1, row, inMemory)
        state_change(P2[row][1], "ReadCache", P2, row, inMemory)
        state_change(P3[row][1], "Read", P3, row, inMemory)
    elif(instArr[1] == "WRITE"):
        row, inMemory = write_inst(instArr[2], P3, instArr[3])
        state_change(P0[row][1], "WriteCache", P0, row, inMemory)
        state_change(P1[row][1], "WriteCache", P1, row, inMemory)
        state_change(P2[row][1], "WriteCache", P2, row, inMemory)
        state_change(P3[row][1], "Write", P3, row, inMemory)
    else:
        print("Calculating...")
        sleep(1)
    print("Caché 4:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
        for row in P3]))
    print('\n')

def Controlador():
    print("Se inicia el proceso con: ")
    sleep(2)
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
    print("Memoria:")
    print(Memory)
    print('\n')
    try:
        t1 = Thread(target=firstProcessorL1, args=[])
        t1.start()
        t2 = Thread(target=secondProcessorL1, args=[])
        t2.start()
        t3 = Thread(target=thirdProcessorL1, args=[])
        t3.start()
        t4 = Thread(target=fourthProcessorL1, args=[])
        t4.start()
        sleep(10)
        print("Se finaliza el proceso con: ")
        sleep(1)
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
        print("Memoria:")
        print(Memory)
        print('\n')
    except:
        print("Error fatal en los threads!")

if __name__ == '__main__':
    # print("Caché 1:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P0]))
    # print('\n')
    # print("Caché 2:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P1]))
    # print('\n')
    # print("Caché 3:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P2]))
    # print('\n')
    # print("Caché 4:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P3]))
    # print('\n')
    # firstProcessorL1()
    # print('\n')
    # print("Caché 1:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P0]))
    # print('\n')
    # print("Caché 2:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P1]))
    # print('\n')
    # print("Caché 3:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P2]))
    # print('\n')
    # print("Caché 4:")
    # print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    #   for row in P3]))
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
