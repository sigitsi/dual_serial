import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=20, width=100)
T.pack()
T2 = tk.Text(root, height=20, width=100)
T2.pack()


import serial
import serial.tools.list_ports as port_list

ports = list(port_list.comports())
num = 0
for p in ports:
    print (p,type(p))
    p2 = str(p).split()
    if 'USB' in p2 and (num==1):
        print("found a Sensinode")
        print("on port ",p2[0])
        num = 2
        port2 = p2[0]
    if 'USB' in p2 and (num==0):
        print("found a Sensinode")
        print("on port ",p2[0])
        num = 1
        port1 = p2[0]
ser1 = serial.Serial(port=port1, baudrate=115200)
ser2 = serial.Serial(port=port2, baudrate=115200)


def checkSerial():
    T.insert(tk.END, ser1.readline())
    T.see("end")
    T2.insert(tk.END, ser2.readline())
    T2.see("end")
    root.after(100, checkSerial) 

root.after(100, checkSerial)

tk.mainloop()
