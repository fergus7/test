def adc_get():
    global folder_path # Giriş kutusundan veriyi al
    command1=fr'cd {folder_path} && python hwtf.py --port COM{com} --c --command adc --pin 3'
    output=subprocess.check_output(command1, shell=True)
    veri=output.decode()
    veri=10
    adc_cikti.config(text=veri)
    
    
    
    
adc_text=tk.Label(frame,text="VBAT_ADC degeri=",font=("Arial", 13))
adc_text.grid(column=0, row=10, columnspan=4)

adc_testbutton=tk.Button(frame, text="Test", borderwidth=0.5,command=adc_get)
adc_testbutton.grid(row=10, column=3, pady=10)


adc_cikti = tk.Label(frame)
adc_cikti.grid(row=10, column=2, pady=10)
