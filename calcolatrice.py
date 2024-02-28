import tkinter as tk

class Calcolatrice():
    cor1 = "#3b3b3b" 
    cor2 = "#feffff" 
    cor3 = "#38576b" 
    cor4 = "#ECEFF1" 
    cor5 = '#FFAB40' 
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calcolatrice")
        self.root.geometry("330x475")
        self.root.resizable(False, False)
        self.root.configure(bg="#3d3d3d")
        
        #creo due frames
        self.frame1 = tk.Frame(self.root, bg=self.cor1, height=60)
        self.frame1.grid(row=0, column=0, rowspan=2, sticky="nsew")
        
        #creo entry
        self.entry = tk.Entry(self.frame1, font=("Ivy 50 bold"), bg=self.cor1, fg="#fafcff", bd=0)
        self.entry.grid(row=0, column=0, rowspan=2, columnspan=4, sticky="nsew", padx=5, pady=5)
          
        self.frame2 = tk.Frame(self.root, bg="#3d3d3d", width=330, height=475)
        self.frame2.grid(row=2, column=0, rowspan=2, columnspan=4, pady=5, padx=5, sticky="nsew")
        
        #creo i pulsanti come iphone
        self.btn1 = tk.Button(self.frame2, text="CANC", font=("Ivy 28 bold"), 
                              bg=self.cor3, fg=self.cor2, bd=1, relief="raised", 
                              width=7, height=1, overrelief="ridge", command=lambda: self.entry.delete(0, "end"))
        self.btn1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.btn3 = tk.Button(self.frame2, text="%", font=("Ivy 28 bold"), 
                              bg=self.cor3, fg=self.cor2, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "%"))
        self.btn3.grid(row=0, column=2, sticky="nsew")
        self.btn4 = tk.Button(self.frame2, text="/", font=("Ivy 28 bold"), 
                              bg=self.cor5, fg=self.cor2, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "/"))
        self.btn4.grid(row=0, column=3, sticky="nsew")
        
        self.btn5 = tk.Button(self.frame2, text="7", font=("Ivy 28 bold"), 
                              bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "7"))
        self.btn5.grid(row=1, column=0, sticky="nsew")
        self.btn6 = tk.Button(self.frame2, text="8", font=("Ivy 28 bold"), 
                              bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "8"))
        self.btn6.grid(row=1, column=1, sticky="nsew")
        self.btn7 = tk.Button(self.frame2, text="9", font=("Ivy 28 bold"), 
                              bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "9"))
        self.btn7.grid(row=1, column=2, sticky="nsew")
        self.btn8 = tk.Button(self.frame2, text="*", font=("Ivy 28 bold"), 
                              bg=self.cor5, fg=self.cor2, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "*"))
        self.btn8.grid(row=1, column=3, sticky="nsew")
        
        self.btn9 = tk.Button(self.frame2, text="4", font=("Ivy 28 bold"), 
                              bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                              width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "4"))
        self.btn9.grid(row=2, column=0, sticky="nsew")
        self.btn10 = tk.Button(self.frame2, text="5", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "5"))
        self.btn10.grid(row=2, column=1, sticky="nsew")
        self.btn11 = tk.Button(self.frame2, text="6", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "6"))
        self.btn11.grid(row=2, column=2, sticky="nsew")
        self.btn12 = tk.Button(self.frame2, text="-", font=("Ivy 28 bold"), 
                               bg=self.cor5, fg=self.cor2, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "-"))
        self.btn12.grid(row=2, column=3, sticky="nsew")
        
        self.btn13 = tk.Button(self.frame2, text="1", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "1"))
        self.btn13.grid(row=3, column=0, sticky="nsew")
        self.btn14 = tk.Button(self.frame2, text="2", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "2"))
        self.btn14.grid(row=3, column=1, sticky="nsew")
        self.btn15 = tk.Button(self.frame2, text="3", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "3"))
        self.btn15.grid(row=3, column=2, sticky="nsew")
        self.btn16 = tk.Button(self.frame2, text="+", font=("Ivy 28 bold"), 
                               bg=self.cor5, fg=self.cor2, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "+"))
        self.btn16.grid(row=3, column=3, sticky="nsew")
        
        self.btn17 = tk.Button(self.frame2, text="0", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=7, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "0"))
        self.btn17.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.btn18 = tk.Button(self.frame2, text=",", font=("Ivy 28 bold"), 
                               bg=self.cor4, fg=self.cor1, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=lambda: self.entry.insert("end", "."))
        self.btn18.grid(row=4, column=2, sticky="nsew")
        self.btn19 = tk.Button(self.frame2, text="=", font=("Ivy 28 bold"), 
                               bg=self.cor5, fg=self.cor2, bd=1, relief="raised", 
                               width=3, height=1, overrelief="ridge", command=self.calcola)
        self.btn19.grid(row=4, column=3, sticky="nsew")
        
    def calcola(self):
        try:
            risultato = eval(self.entry.get())
            self.entry.delete(0, "end")
            self.entry.insert(0, str(risultato))
        except:
            self.entry.delete(0, "end")
            self.entry.insert(0, "Errore")
    
    #mainloop
    def mainloop(self):
        self.root.mainloop()
            
if __name__ == "__main__":
    app = Calcolatrice()
    app.mainloop()