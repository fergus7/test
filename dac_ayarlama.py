import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
root=tk.Tk()
root.title("DAC Ayarlama")
root.geometry("450x500")
frame=ttk.Frame(padding=20)
frame.grid(column=0,row=0)
folder_path=""


def led1_test():
    global folder_path
    command1=fr'cd {folder_path} && python hwtf.py --port COM3 --c --command output --pin 25 --value 0'
    subprocess.call(command1, shell=True)
    led2_testbox.configure(bg="white")
    command2=fr'cd {folder_path} && python hwtf.py --port COM3 --c --command output --pin 26 --value 1'
    output=subprocess.check_output(command2, shell=True)
    cikis=output.decode()
    if "A C K"in cikis :
        led1_testbox.configure(bg="green")
    else:
        led1_testbox.configure(bg="red")
        messagebox.showinfo("HATA",cikis )
        
        
def led2_test():
    global folder_path
    command1=fr'cd {folder_path} && python hwtf.py --port COM3 --c --command output --pin 26 --value 0'
    subprocess.call(command1, shell=True)
    led1_testbox.configure(bg="white")
    command2=fr'cd {folder_path} && python hwtf.py --port COM3 --c --command output --pin 25 --value 1'
    output = subprocess.check_output(command2, shell=True)
    cikis=output.decode()
    if "A C K"in cikis:
        led2_testbox.configure(bg="green")
    else:
        led2_testbox.configure(bg="red")
        messagebox.showinfo("HATA",cikis)
        
    
    

       

def dosya_sec():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Seçilen dosya yolu:", folder_path)
        path_controlbox.configure(bg="green")  
    else:
        print("Dosya seçilmedi.")
        path_controlbox.configure(bg="red") 
  


def DAC_value_func(event):
    DAC_value=dac_value.get()
    error_text.grid_remove()
    if int(DAC_value)<0 or int(DAC_value)>31:
        error_text.grid(column=0, row=6, columnspan=4)
        DAC_value=0
        
    file_path=folder_path
    command=fr'cd {file_path} && python hwtf.py --port COM3 --c --command dac --pin 4 --value {DAC_value}'
    print("file path=",file_path)
    subprocess.call(command, shell=True)
    dac_value.delete(0, tk.END)
    dac_value.insert(0,"0")

def increase_func():
    current_value=int(dac_value.get())
    dac_value.delete(0,tk.END)
    dac_value.insert(0, str(current_value+1))
    if int(dac_value.get())>31:
        dac_value.delete(0,tk.END)
        dac_value.insert(0, "31")

def decrease_func():
    current_value=int(dac_value.get())
    dac_value.delete(0,tk.END)
    dac_value.insert(0, str(current_value-1))
    if int(dac_value.get())<0:
        dac_value.delete(0,tk.END)
        dac_value.insert(0, "0")

dac_text=tk.Label(frame,text="DAC Değerini Giriniz (3-31 Aralığında)", anchor="center",font=("Arial", 13))
dac_text.grid(column=0, row=4, columnspan=4)

error_text=tk.Label(frame,text="0-31 Aralığında Değer Almalı!", anchor="center",font=("Arial", 13))


dac_value=tk.Entry(frame,borderwidth=0, width=15, font=20)
dac_value.insert(0,"0")
dac_value.grid(column=0, row=5, pady=30)
dac_value.bind("<Return>",DAC_value_func)


increase_button=tk.Button(frame, text="▲", command=increase_func)
increase_button.grid(column=1, row=5)
decrease_button=tk.Button(frame, text="▼", command=decrease_func)
decrease_button.grid(column=2, row=5)


button_text=tk.Label(frame,text="HWTF Dosyasının Bulunduğu Klasörü Seçiniz:",font=("Arial", 12))
button_text.grid(column=0,row=0,columnspan=4 ,padx=10, rowspan=2)
button = tk.Button(frame, text="Dosya Seçimi", command=dosya_sec)
button.grid(column=5,row=1, rowspan=1)


path_controltext=tk.Label(frame, text="Yol Belirlendi:", font=("Arial",10))
path_controltext.grid(row=3,column=0, columnspan=4, pady=20)
path_controlbox = tk.Label(frame, bg="red", width=1, height=0, borderwidth=1)
path_controlbox.grid(row=3, column=1, pady=20)


gpio_label=tk.Label(frame, text="GPIO PIN TEST", font=("Arial", 20))
gpio_label.grid(row=7, columnspan=7)

led1_label=tk.Label(frame, text="LED Out1:", font=("Arial",12))
led1_label.grid(row=8, column=0, columnspan=3, pady=10)
led1_testbox = tk.Label(frame, bg="white", width=1, height=0, borderwidth=1)
led1_testbox.grid(row=8, column=1, pady=10)
led1_testbutton=tk.Button(frame, text="Test", borderwidth=0.5,command=led1_test)
led1_testbutton.grid(row=8, column=2, pady=10)



led2_label=tk.Label(frame, text="LED Out2: ", font=("Arial", 12))
led2_label.grid(row=9, column=0, columnspan=3, pady=10)
led2_testbox = tk.Label(frame, bg="white", width=1, height=0, borderwidth=1)
led2_testbox.grid(row=9, column=1, pady=10)
led2_testbutton=tk.Button(frame, text="Test", borderwidth=0.5,command=led2_test)
led2_testbutton.grid(row=9, column=2, pady=10)
















root.mainloop()