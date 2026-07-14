import tkinter as tk

def test():
    print("Button Clicked!")

window = tk.Tk()
window.title("My First GUI")
window.geometry("400x300")

button = tk.Button(window,text="Click Me!", command=test)
button.pack(padx=100, pady=100)

window.mainloop()