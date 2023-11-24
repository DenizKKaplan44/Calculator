import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Calculator")

calList=[]
allnumber=""
together=""

def button_click0():
    global allnumber
    allnumber += "0"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click1():
    global allnumber
    allnumber += "1"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click2():
    global allnumber
    allnumber+="2"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click3():
    global allnumber
    allnumber+="3"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click4():
    global allnumber
    allnumber+="4"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click5():
    global allnumber
    allnumber+="5"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click6():
    global allnumber
    allnumber+="6"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click7():
    global allnumber
    allnumber+="7"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click8():
    global allnumber
    allnumber+="8"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click9():
    global allnumber
    allnumber+="9"
    box.configure(text=calList)
    box2.configure(text=allnumber)
def button_click_Add():
    global allnumber
    calList.append(allnumber)
    calList.append("+")
    box.configure(text=calList)
    allnumber=""
def button_click_Sub():
    global allnumber
    calList.append(allnumber)
    calList.append("-")
    box.configure(text=calList)
    allnumber=""
def button_click_Div():
    global allnumber
    calList.append(allnumber)
    calList.append("/")
    box.configure(text=calList)
    allnumber=""
def button_click_Times():
    global allnumber
    calList.append(allnumber)
    calList.append("*")
    box.configure(text=calList)
    allnumber=""
def button_click_Calculte():
    global allnumber,together
    calList.append(allnumber)
    if any(calList):
       if calList[-1].isdigit():
          together = ''.join(calList)
          Calculeted=eval(together)
          box.configure(text=Calculeted)
       else:
           together = ''.join(calList[:-2])
           Calculeted=eval(together)
           box.configure(text=Calculeted)
    else:
        messagebox.showinfo("Warning", "Try click a number Please.")
    box2.configure(text=None)
    calList.clear()
    allnumber=""
    
def button_click_Clear():
    global allnumber
    box.configure(text="=", font=10, background="white")
    box2.configure(text="[...]", font=10)
    calList.clear()
    allnumber=""

    
    
  

box=tk.Label(text="=",font=10,background="white")
box.grid(column=10,row=1)
box2=tk.Label(text="[...]", font=10)
box2.grid(column=11,row=2)


buttonClear=tk.Button(root, text="C", border=10, bg="Red", command=button_click_Clear)

button0 = tk.Button(root, text="0", border=5, bg="gray", command=button_click0)
buttonadd=tk.Button(root,text="+",border=5, bg="white", command=button_click_Add)
buttonnSub=tk.Button(root,text="-",border=5, bg="white", command=button_click_Sub)

buttonDiv=tk.Button(root,text="÷",border=5, bg="white", command=button_click_Div)
buttonTimes=tk.Button(root,text="x",border=5, bg="white", command=button_click_Times)

buttonCalculate=tk.Button(root,text="=",border=5,bg="green" ,command=button_click_Calculte)

button1 = tk.Button(root, text="1", border=5, bg="gray",command=button_click1)
button2 = tk.Button(root, text="2", border=5, bg="gray",command=button_click2)
button3 = tk.Button(root, text="3", border=5, bg="gray",command=button_click3)
button4 = tk.Button(root, text="4", border=5, bg="gray",command=button_click4)
button5 = tk.Button(root, text="5", border=5, bg="gray",command=button_click5)
button6 = tk.Button(root, text="6", border=5, bg="gray",command=button_click6)
button7 = tk.Button(root, text="7", border=5, bg="gray",command=button_click7)
button8 = tk.Button(root, text="8", border=5, bg="gray",command=button_click8)
button9 = tk.Button(root, text="9", border=5, bg="gray",command=button_click9)

buttonClear.grid(column=5, row=1, ipadx=5, ipady=5)

button0.grid(column=1, row=4,ipadx=10,ipady=10)
buttonadd.grid(column=2, row=4,ipadx=10,ipady=10)
buttonnSub.grid(column=3, row=4,ipadx=10,ipady=10)
buttonDiv.grid(column=4, row=4,ipadx=10,ipady=10)
buttonTimes.grid(column=5, row=4,ipadx=10,ipady=10)

buttonCalculate.grid(column=6, row=4,ipadx=10,ipady=10)


button1.grid(column=1, row=1,ipadx=10,ipady=10)
button2.grid(column=2, row=1,ipadx=10,ipady=10)
button3.grid(column=3, row=1,ipadx=10,ipady=10)
button4.grid(column=1, row=2,ipadx=10,ipady=10)
button5.grid(column=2, row=2,ipadx=10,ipady=10)
button6.grid(column=3, row=2,ipadx=10,ipady=10)
button7.grid(column=1, row=3,ipadx=10,ipady=10)
button8.grid(column=2, row=3,ipadx=10,ipady=10)
button9.grid(column=3, row=3,ipadx=10,ipady=10)


root.mainloop()
