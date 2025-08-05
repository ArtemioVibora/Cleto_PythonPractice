import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x180")


label = tk.Label(root)

def on_click():
    label.config(text="you clicked me!")

exitbutton = tk.Button(root)

root.mainloop();
