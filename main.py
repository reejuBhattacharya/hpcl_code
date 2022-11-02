# from tkinter import *

# top = Tk()  
# #Entering the event main loop  
# top.mainloop()

import json
import tkinter as tk
from tkinter.font import BOLD

file = open("data.json");

data = json.load(file);

# print(data["670"]);

# temp = int(input("Enter the temperature of the substance: "))*2;
# density = input("Enter the density of the substance: ");

# print(data[density][temp]);

window = tk.Tk()
root = tk.Frame(window, relief= 'sunken')
root.pack(fill= "both", expand= True, padx= 10, pady=20)

result = tk.StringVar()

# fuelTypeLabel = tk.Label(root, text="Petrol", bg="red", fg="white").grid(row=0, column=2, padx=5, pady=5)
tempLabel = tk.Label(root, text="Temp: ").grid(row=1, column=0)
densLabel = tk.Label(root, text="Density: ").grid(row=2, column=0)
tempEntry = tk.Entry(root)
tempEntry.grid(row=1, column=1)
densEntry = tk.Entry(root)
densEntry.grid(row=2, column=1)
resLabel = tk.Label(root, bg="lightgreen", fg="blue", height=2, font=("Arial", 17, BOLD), textvariable=result)
resLabel.grid(row=3, column=0, columnspan = 2, sticky = tk.W+tk.E, padx=1)


def resClick():
    temp = int(tempEntry.get())
    density = densEntry.get()
    result.set(data[density][temp*2])

def shiftCell():
    if str(window.focus_get())==".!frame.!entry" :
        densEntry.focus_set()
    else :
        tempEntry.focus_set()

# buttons 
buttonFrame = tk.Frame(root)

upButton = tk.Button(buttonFrame, text="U")
downButton = tk.Button(buttonFrame, text="D")
shiftButton = tk.Button(buttonFrame, text="SHIFT", command=shiftCell)
resButton = tk.Button(buttonFrame, text="RES", command=resClick)

upButton.pack(side="left")
downButton.pack(side="left")
shiftButton.pack(side="left")
resButton.pack(side="left")

buttonFrame.grid(row=5, column=0, columnspan = 2, sticky = tk.W+tk.E)

root.mainloop()
