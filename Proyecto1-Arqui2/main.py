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
Instructions = []

my_tree1 = ttk.Treeview(root)
my_tree2 = ttk.Treeview(root)
my_tree3 = ttk.Treeview(root)
my_tree4 = ttk.Treeview(root)
my_tree5 = ttk.Treeview(root)
my_tree6 = ttk.Treeview(root)
my_tree7 = ttk.Treeview(root)

my_tree1['columns'] = ("Estado", "Direccion", "Dato")
my_tree2['columns'] = ("Estado", "Direccion", "Dato")
my_tree3['columns'] = ("Estado", "Direccion", "Dato")
my_tree4['columns'] = ("Estado", "Direccion", "Dato")
my_tree5['columns'] = ("Dato")
my_tree6['columns'] = ("Instruccion")
my_tree7['columns'] = ("ReadMiss", "WriteMiss")

my_tree1.column("#0", width=100, minwidth=20)
my_tree1.column("Estado", anchor = CENTER, width=60)
my_tree1.column("Direccion", anchor = CENTER, width=100)
my_tree1.column("Dato", anchor = CENTER, width=100)

my_tree2.column("#0", width=100, minwidth=20)
my_tree2.column("Estado", anchor = CENTER, width=60)
my_tree2.column("Direccion", anchor = CENTER, width=100)
my_tree2.column("Dato", anchor = CENTER, width=100)

my_tree3.column("#0", width=100, minwidth=20)
my_tree3.column("Estado", anchor = CENTER, width=60)
my_tree3.column("Direccion", anchor = CENTER, width=100)
my_tree3.column("Dato", anchor = CENTER, width=100)

my_tree4.column("#0", width=100, minwidth=20)
my_tree4.column("Estado", anchor = CENTER, width=60)
my_tree4.column("Direccion", anchor = CENTER, width=100)
my_tree4.column("Dato", anchor = CENTER, width=100)

my_tree5.column("#0", width=100, minwidth=20)
my_tree5.column("Dato", anchor = CENTER, width=100)

my_tree6.column("#0", width=100, minwidth=20)
my_tree6.column("Instruccion", anchor = CENTER, width=300)

my_tree7.column("#0", width=20, minwidth=0)
my_tree7.column("ReadMiss", anchor = CENTER, width=100)
my_tree7.column("WriteMiss", anchor = CENTER, width=100)

my_tree1.heading("#0", text = "P0", anchor = CENTER)
my_tree1.heading("Estado", text = "Estado", anchor = CENTER)
my_tree1.heading("Direccion", text = "Direccion", anchor = CENTER)
my_tree1.heading("Dato", text = "Dato", anchor = CENTER)

my_tree2.heading("#0", text = "P1", anchor = CENTER)
my_tree2.heading("Estado", text = "Estado", anchor = CENTER)
my_tree2.heading("Direccion", text = "Direccion", anchor = CENTER)
my_tree2.heading("Dato", text = "Dato", anchor = CENTER)

my_tree3.heading("#0", text = "P2", anchor = CENTER)
my_tree3.heading("Estado", text = "Estado", anchor = CENTER)
my_tree3.heading("Direccion", text = "Direccion", anchor = CENTER)
my_tree3.heading("Dato", text = "Dato", anchor = CENTER)

my_tree4.heading("#0", text = "P3", anchor = CENTER)
my_tree4.heading("Estado", text = "Estado", anchor = CENTER)
my_tree4.heading("Direccion", text = "Direccion", anchor = CENTER)
my_tree4.heading("Dato", text = "Dato", anchor = CENTER)

my_tree5.heading("#0", text = "Memoria", anchor = CENTER)
my_tree5.heading("Dato", text = "Dato", anchor = CENTER)

my_tree6.heading("#0", text = "Procesador", anchor = CENTER)
my_tree6.heading("Instruccion", text = "Instruccion", anchor = CENTER)

my_tree7.heading("#0", text = "()", anchor = CENTER)
my_tree7.heading("ReadMiss", text = "ReadMiss", anchor = CENTER)
my_tree7.heading("WriteMiss", text = "WriteMiss", anchor = CENTER)

my_tree1.insert(parent='', index='end', text=P0[0][0], values=(P0[0][1], P0[0][2], P0[0][3]))
my_tree1.insert(parent='', index='end', text=P0[1][0], values=(P0[1][1], P0[1][2], P0[1][3]))
my_tree1.insert(parent='', index='end', text=P0[2][0], values=(P0[2][1], P0[2][2], P0[2][3]))
my_tree1.insert(parent='', index='end', text=P0[3][0], values=(P0[3][1], P0[3][2], P0[3][3]))

my_tree2.insert(parent='', index='end', text=P1[0][0], values=(P1[0][1], P1[0][2], P1[0][3]))
my_tree2.insert(parent='', index='end', text=P1[1][0], values=(P1[1][1], P1[1][2], P1[1][3]))
my_tree2.insert(parent='', index='end', text=P1[2][0], values=(P1[2][1], P1[2][2], P1[2][3]))
my_tree2.insert(parent='', index='end', text=P1[3][0], values=(P1[3][1], P1[3][2], P1[3][3]))

my_tree3.insert(parent='', index='end', text=P2[0][0], values=(P2[0][1], P0[0][2], P0[0][3]))
my_tree3.insert(parent='', index='end', text=P2[1][0], values=(P2[1][1], P0[1][2], P0[1][3]))
my_tree3.insert(parent='', index='end', text=P2[2][0], values=(P2[2][1], P0[2][2], P0[2][3]))
my_tree3.insert(parent='', index='end', text=P2[3][0], values=(P2[3][1], P0[3][2], P0[3][3]))

my_tree4.insert(parent='', index='end', text=P3[0][0], values=(P0[0][1], P0[0][2], P0[0][3]))
my_tree4.insert(parent='', index='end', text=P3[1][0], values=(P0[1][1], P0[1][2], P0[1][3]))
my_tree4.insert(parent='', index='end', text=P3[2][0], values=(P0[2][1], P0[2][2], P0[2][3]))
my_tree4.insert(parent='', index='end', text=P3[3][0], values=(P0[3][1], P0[3][2], P0[3][3]))

my_tree5.insert(parent='', index='end', text="0000", values=Memory["0000"])
my_tree5.insert(parent='', index='end', text="0001", values=Memory["0001"])
my_tree5.insert(parent='', index='end', text="0010", values=Memory["0010"])
my_tree5.insert(parent='', index='end', text="0011", values=Memory["0011"])
my_tree5.insert(parent='', index='end', text="0100", values=Memory["0100"])
my_tree5.insert(parent='', index='end', text="0101", values=Memory["0101"])
my_tree5.insert(parent='', index='end', text="0110", values=Memory["0110"])
my_tree5.insert(parent='', index='end', text="0111", values=Memory["0111"])

my_tree6.insert(parent='', index='end', text="P0", values="None")
my_tree6.insert(parent='', index='end', text="P1", values="None")
my_tree6.insert(parent='', index='end', text="P2", values="None")
my_tree6.insert(parent='', index='end', text="P3", values="None")

my_tree1.place(x=10, y=10)
my_tree2.place(x=410, y=10)
my_tree3.place(x=10, y=310)
my_tree4.place(x=410, y=310)
my_tree5.place(x=810, y=10)
my_tree6.place(x=810, y=510)
my_tree7.place(x=810, y=260)

# my_label = Label(root, text="I made a thread")
# my_label.pack(pady=20)

# random_label = Label(root, text="Random number")
# random_label.pack(pady=20)

# def rando():
#     random_label.config(text=f'Random number is: {randint(1, 100)}')


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
            print("Debería cambiar de estado!")
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

def write_inst(mem_block, processor, data):
    global writeMiss
    global writeHit
    for i in range(4):
        if(processor[i][2] == mem_block):
            processor[i][3] = data
            writeHit += 1
            return i, False
    else:
        if(mem_block == "0000" or mem_block == "0100"):
            processor[0][2] = mem_block
            processor[0][3] = data
            writeMiss += 1
            return 0, False
        elif(mem_block == "0001" or mem_block == "0101"):
            processor[1][2] = mem_block
            processor[1][3] = data
            writeMiss += 1
            return 1, False
        elif(mem_block == "0010" or mem_block == "0110"):
            processor[2][2] = mem_block
            processor[2][3] = data
            writeMiss += 1
            return 2, False
        elif(mem_block == "0011" or mem_block == "0111"):
            processor[3][2] = mem_block
            processor[3][3] = data
            writeMiss += 1
            return 3, False   

def read_inst(mem_block, processor):
    global readMiss
    global readHit
    for i in range(4):
        if(processor[i][2] == mem_block and processor[i][1] != "I"):
            readHit += 1
            return i, False
    else:
        for i in range(4):
            if (P0[i][2] == mem_block and P0[i][1] == "E"):
                processor[i][3] = P0[i][3]
                processor[i][2] = P0[i][2]
                readMiss += 1
                return i, False
        for i in range(4):
            if (P1[i][2] == mem_block and P1[i][1] == "E"):
                processor[i][3] = P1[i][3]
                processor[i][2] = P1[i][2]
                readMiss += 1
                return i, False
        for i in range(4):
            if (P2[i][2] == mem_block and P2[i][1] == "E"):
                processor[i][3] = P2[i][3]
                processor[i][2] = P2[i][2]
                readMiss += 1
                return i, False
        for i in range(4):    
            if (P3[i][2] == mem_block and P3[i][1] == "E"):
                processor[i][3] = P3[i][3]
                processor[i][2] = P3[i][2]
                readMiss += 1
                return i, False
        else:
            readMiss += 1
            row, inMemory = read_memory(mem_block, processor, i)
            return row, inMemory

def generate_inst(proce, lock):
    lock.acquire()
    n = randint(0, 10)
    k = randint(0, 5)
    p = randint(1, 5) / randint(5, 10)
    dist = binomial_dist(n, k, p)
    processor = proce
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
    sleep(0.1)
    Instructions.append(inst)
    lock.release()
    return inst

def firstProcessorL1():
    lock = Lock()
    inst = generate_inst(P0, lock)
    print(inst)
    instArr = inst.split(" ")
    lock.acquire()
    if(instArr[1] == "READ"):
        row, inMemory = read_inst(instArr[2], P0)
        state_change(P0[row][1], "Read", P0, row, inMemory)
        state_change(P1[row][1], "ReadCache", P1, row, inMemory)
        state_change(P2[row][1], "ReadCache", P2, row, inMemory)
        state_change(P3[row][1], "ReadCache", P3, row, inMemory)
    elif(instArr[1] == "WRITE"):
        row, inMemory = write_inst(instArr[2], P0, instArr[3])
        print(row)
        state_change(P0[row][1], "Write", P0, row, inMemory)
        state_change(P1[row][1], "WriteCache", P1, row, inMemory)
        state_change(P2[row][1], "WriteCache", P2, row, inMemory)
        state_change(P3[row][1], "WriteCache", P3, row, inMemory)
    else:
        print("Calculating...")
    sleep(0.1)
    lock.release()
    print("Caché 1:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in P0]))
    print('\n')

def secondProcessorL1():
    lock = Lock()
    inst = generate_inst(P1, lock)
    print(inst)
    instArr = inst.split(" ")
    lock.acquire()
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
    sleep(0.1)
    lock.release()
    print("Caché 2:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
        for row in P1]))
    print('\n')

def thirdProcessorL1():
    lock = Lock()
    inst = generate_inst(P2, lock)
    print(inst)
    instArr = inst.split(" ")
    lock.acquire()
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
    sleep(0.1)
    lock.release()
    print("Caché 3:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
        for row in P2]))
    print('\n')

def fourthProcessorL1():
    lock = Lock()
    inst = generate_inst(P3, lock)
    print(inst)
    instArr = inst.split(" ")
    lock.acquire()
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
    sleep(0.1)
    lock.acquire()
    print("Caché 4:")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
        for row in P3]))
    print('\n')

def Controlador():
    print("Se inicia el proceso: ")
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
    i = 0
    sleep(2)
    try:
        t1 = Thread(target=firstProcessorL1, args=[])
        t1.start()
        t2 = Thread(target=secondProcessorL1, args=[])
        t2.start()
        t3 = Thread(target=thirdProcessorL1, args=[])
        t3.start()
        t4 = Thread(target=fourthProcessorL1, args=[])
        t4.start()
        # t1.join()
        # t2.join()
        # t3.join()
        # t4.join()
        sleep(10)
        print("Se finaliza el proceso: ")
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
        print(Instructions)
        print("Read Miss: ", readMiss)
        print("Write Miss: ", writeMiss)

        my_tree1.item("I001", text=P0[0][0], values=(P0[0][1], P0[0][2], P0[0][3]))
        my_tree1.item("I002", text=P0[1][0], values=(P0[1][1], P0[1][2], P0[1][3]))
        my_tree1.item("I003", text=P0[2][0], values=(P0[2][1], P0[2][2], P0[2][3]))
        my_tree1.item("I004", text=P0[3][0], values=(P0[3][1], P0[3][2], P0[3][3]))

        my_tree2.item("I001", text=P1[0][0], values=(P1[0][1], P1[0][2], P1[0][3]))
        my_tree2.item("I002", text=P1[1][0], values=(P1[1][1], P1[1][2], P1[1][3]))
        my_tree2.item("I003", text=P1[2][0], values=(P1[2][1], P1[2][2], P1[2][3]))
        my_tree2.item("I004", text=P1[3][0], values=(P1[3][1], P1[3][2], P1[3][3]))

        my_tree3.item("I001", text=P2[0][0], values=(P2[0][1], P2[0][2], P2[0][3]))
        my_tree3.item("I002", text=P2[1][0], values=(P2[1][1], P2[1][2], P2[1][3]))
        my_tree3.item("I003", text=P2[2][0], values=(P2[2][1], P2[2][2], P2[2][3]))
        my_tree3.item("I004", text=P2[3][0], values=(P2[3][1], P2[3][2], P2[3][3]))

        my_tree4.item("I001", text=P3[0][0], values=(P3[0][1], P3[0][2], P3[0][3]))
        my_tree4.item("I002", text=P3[1][0], values=(P3[1][1], P3[1][2], P3[1][3]))
        my_tree4.item("I003", text=P3[2][0], values=(P3[2][1], P3[2][2], P3[2][3]))
        my_tree4.item("I004", text=P3[3][0], values=(P3[3][1], P3[3][2], P3[3][3]))

        my_tree5.item("I001", text="0000", values=Memory["0000"])
        my_tree5.item("I002", text="0001", values=Memory["0001"])
        my_tree5.item("I003", text="0010", values=Memory["0010"])
        my_tree5.item("I004", text="0011", values=Memory["0011"])
        my_tree5.item("I005", text="0100", values=Memory["0100"])
        my_tree5.item("I006", text="0101", values=Memory["0101"])
        my_tree5.item("I007", text="0110", values=Memory["0110"])
        my_tree5.item("I008", text="0111", values=Memory["0111"])

        my_tree6.item("I001", text="P0", values=Instructions[i])
        my_tree6.item("I002", text="P1", values=Instructions[i + 1])
        my_tree6.item("I003", text="P2", values=Instructions[i + 2])
        my_tree6.item("I004", text="P3", values=Instructions[i + 3])

        i += 4

        my_tree7.insert(parent='', index='end', text="", values=(readMiss, writeMiss))

        root.update()
    except:
        print("Error fatal en los threads!")

def cicloControlador():
    ciclos = 10
    while(ciclos > 0):
        Controlador()
        ciclos -= 1

my_button1 = Button(root, text="Paso a paso", command=Controlador)
my_button1.place(x=450, y=240)

my_button2 = Button(root, text="Ejecutar", command=cicloControlador)
my_button2.place(x=450, y=270)

if __name__ == '__main__':
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
