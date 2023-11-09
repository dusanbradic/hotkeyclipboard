#Import tkinter library
import tkinter as tk
from tkinter import messagebox
from keyboard import add_hotkey, write, wait, unhook_all

#Create an instance of tkinter window or frame
root=tk.Tk()
root.title('hotkey clipboard')
# root.geometry("700x700")


def popup(title, message):
   messagebox.showinfo(title, message)

def get_input():
   box1_content = box1.get("1.0","end-1c")
   box2_content = box2.get("1.0","end-1c")
   box3_content = box3.get("1.0","end-1c")
   box4_content = box4.get("1.0","end-1c")
   unhook_all()
   add_hotkey('left alt + 1', lambda: write(box1_content))
   add_hotkey('left alt + 2', lambda: write(box2_content))
   add_hotkey('left alt + 3', lambda: write(box3_content))
   add_hotkey('left alt + 4', lambda: write(box4_content))
   popup("Info", "Hotkeys saved")

#Creating text box widgets
label1 = tk.Label(root, text="ALT + 1")
label1.grid(column=0, row=0)
box1=tk.Text(root, height=8, width=80)
box1.grid(column=0, row=1)

label2 = tk.Label(root, text="ALT + 2")
label2.grid(column=0, row=2)
box2=tk.Text(root, height=8, width=80)
box2.grid(column=0, row=3)

label3 = tk.Label(root, text="ALT + 3")
label3.grid(column=0, row=4)
box3=tk.Text(root, height=8, width=80)
box3.grid(column=0, row=5)

label4 = tk.Label(root, text="ALT + 4")
label4.grid(column=0, row=6)
box4=tk.Text(root, height=8, width=80)
box4.grid(column=0, row=7)

# Create a button for save
comment= tk.Button(root, height=5, width=10, text="Save", command=lambda: get_input())
comment.grid(column=0, row=8)


for child in root.winfo_children():
    child.grid_configure(padx=10, pady=1)

root.mainloop()
wait()


