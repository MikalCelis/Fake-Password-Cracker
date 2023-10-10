import tkinter as tk

window = tk.Tk()
window.title("Pegasus")

label = tk.Label(window,text="Generate Password")
label.pack()

def passwordGenerator():
    print(f"Hello")


generateButton = tk.Button(window,text="Generate",command=passwordGenerator)
generateButton.pack()

window.mainloop()

