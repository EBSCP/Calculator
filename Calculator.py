from tkinter import *

Window = Tk()
Window.geometry("400x400")
Window.title("Calculator")
Window.configure(bg="purple")
Window.resizable(FALSE,FALSE)

entry = Entry(Window,width= 20,borderwidth = 10)
entry.grid(row=0,column=0,columnspan=4)
            
def tiklanan_buton (sayi):
    entry.insert(END,sayi)
    
    
def Toplam():
    global number1
    global islem
    islem ="Toplam"
    number1 = int(entry.get())
    entry.delete(0,END)
    
def Cikarma():
    global number1
    global islem
    islem ="Cikarma"
    number1 = int(entry.get())
    entry.delete(0,END)

def Carpma():
    global number1
    global islem
    islem ="Carpma"
    number1 = int(entry.get())
    entry.delete(0,END)
    
def Bolme():
    global number1
    global islem
    islem ="Bolme"
    number1 = int(entry.get())
    entry.delete(0,END)

def  equal():
    number2= int(entry.get())
    entry.delete(0,END)
    
    if islem=="Toplam":
        entry.insert(0,number1+number2)        
    if islem=="Cikarma":
        entry.insert(0,number1-number2)
    if islem =="Bolme":
        entry.insert(0,number1/number2)
    if islem =="Carpma":
        entry.insert(0,number1*number2)
        
        
def temizleme():
    entry.delete(0,END)            


       
        
button_0= Button(Window,text="0",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(0))
button_0.grid(row=1 ,column=0,padx=4,pady=4,ipadx=26)

button_1= Button(Window,text="1",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(1))
button_1.grid(row=1 ,column=1,padx=4,pady=4,ipadx=26)


button_2= Button(Window,text="2",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(2))
button_2.grid(row=1 ,column=2,padx=4,pady=4,ipadx=26)


button_3= Button(Window,text="3",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(3))
button_3.grid(row=2 ,column=0,padx=4,pady=4,ipadx=26)


button_4= Button(Window,text="4",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(4))
button_4.grid(row=2 ,column=1,padx=4,pady=4,ipadx=26)

button_5= Button(Window,text="5",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(5))
button_5.grid(row=2,column=2,padx=4,pady=4,ipadx=26)

button_6= Button(Window,text="6",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(6))
button_6.grid(row=3,column=0,padx=4,pady=4,ipadx=26)

button_7= Button(Window,text="7",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(7))
button_7.grid(row=3,column=1,padx=4,pady=4,ipadx=26)

button_8= Button(Window,text="8",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(8))
button_8.grid(row=3 ,column=2,padx=4,pady=4,ipadx=26)

button_9= Button(Window,text="9",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: tiklanan_buton(9))
button_9.grid(row=4,column=0,padx=4,pady=4,ipadx=26)

button_toplam= Button(Window,text="+",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: Toplam())
button_toplam.grid(row=4 ,column=1,padx=4,pady=4,ipadx=26)

button_cikarma= Button(Window,text="-",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: Cikarma())
button_cikarma.grid(row=4 ,column=2,padx=4,pady=4,ipadx=26)

button_bolme= Button(Window,text="/",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: Bolme())
button_bolme.grid(row=5 ,column=0,padx=4,pady=4,ipadx=26)

button_carpma= Button(Window,text="*",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: Carpma())
button_carpma.grid(row=5 ,column=1,padx=4,pady=4,ipadx=26)

button_Temizleme= Button(Window,text="<-",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: temizleme())
button_Temizleme.grid(row=5 ,column=2,padx=4,pady=4,ipadx=26)


button_equal= Button(Window,text="=",font=" times 14",bg="orange",fg="blue",
                 activebackground="green",relief=RAISED,
                 command=lambda: equal())
button_equal.grid(row=6 ,column=1,padx=4,pady=4,ipadx=26)

Window.mainloop()
