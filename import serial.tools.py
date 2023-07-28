import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

def get_com_ports():
    com_ports = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        com_ports.append(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")
    return com_ports

if __name__ == "__main__":
    com_ports = get_com_ports()

    root = tk.Tk()
    root.title("COM Ports")

    # Frame to hold the Scrollbox
    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Listbox to display COM Ports
    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for port_info in com_ports:
        listbox.insert(tk.END, port_info)

    scrollbar.config(command=listbox.yview)

    root.mainloop()