import tkinter

def buttonclick(x):#function will b called as soon as we click on app
    global v
    v=v+str(x)#converting x to string
    data.set(v)

def clear(x):
    global v
    v=""
    data.set("")

def equal(x):
    global v
    result=str(eval(v))
    #eval functions produces the arthematic results
    data.set(result)

#TODO:error is still there when user presses = first


task=tkinter.Tk()
task.title("Calculator")
task.geometry("400x400")
task.resizable(width=False,height=False)

task.columnconfigure(0,weight=1)
task.columnconfigure(1,weight=1)
task.columnconfigure(2,weight=1)
task.columnconfigure(3,weight=1)
task.columnconfigure(4,weight=1)

task.rowconfigure(0,weight=1)
task.rowconfigure(1,weight=1)
task.rowconfigure(2,weight=1)
task.rowconfigure(3,weight=1)
task.rowconfigure(4,weight=1)

v=""
data=tkinter.StringVar()
#the text variable data will b used to display and give the output on screen
screen=tkinter.Entry(task,textvariable=data,bg="powder blue",justify="right",bd=50,font=("bold",32))
screen.grid(row=0,column=0,columnspan=4,sticky="ns")

button1=tkinter.Button(task,text="1",width=15,bg="white",height=2,font=20,command=lambda:buttonclick(1))
button1.grid(row=1,column=0,sticky="ns")
#to call a fn we use command and to pass an argument we use lambda
button2=tkinter.Button(task,text="2",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick(2))
button2.grid(row=1,column=1,sticky="ns")
button3=tkinter.Button(task,text="3",width=15,bg="white",height=2,font=20,command=lambda:buttonclick(3))
button3.grid(row=1,column=2,sticky="ns")
button4=tkinter.Button(task,text="4",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick(4))
button4.grid(row=1,column=3,sticky="ns")

button5=tkinter.Button(task,text="5",width=15,bg="white",height=2,font=20,command=lambda:buttonclick(5))
button5.grid(row=2,column=0,sticky="ns")
button6=tkinter.Button(task,text="6",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick(6))
button6.grid(row=2,column=1,sticky="ns")
button7=tkinter.Button(task,text="7",width=15,bg="white",height=2,font=20,command=lambda:buttonclick(7))
button7.grid(row=2,column=2,sticky="ns")
button8=tkinter.Button(task,text="8",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick(8))
button8.grid(row=2,column=3,sticky="ns")

button9=tkinter.Button(task,text="9",width=15,bg="white",height=2,font=20,command=lambda:buttonclick(9))
button9.grid(row=3,column=0,sticky="ns")
buttonadd=tkinter.Button(task,text="+",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick("+"))
buttonadd.grid(row=3,column=1,sticky="ns")
buttonsub=tkinter.Button(task,text="-",width=15,bg="white",height=2,font=20,command=lambda:buttonclick("-"))
buttonsub.grid(row=3,column=2,sticky="ns")
buttondiv=tkinter.Button(task,text="/",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick("/"))
buttondiv.grid(row=3,column=3,sticky="ns")

buttonmul=tkinter.Button(task,text="*",width=15,bg="white",height=2,font=20,command=lambda:buttonclick("*"))
buttonmul.grid(row=4,column=0,sticky="ns")
buttondot=tkinter.Button(task,text=".",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick("."))
buttondot.grid(row=4,column=1,sticky="ns")
buttoncancel=tkinter.Button(task,text="C",width=15,bg="white",height=2,font=20,command=lambda:clear(""))
buttoncancel.grid(row=4,column=2,sticky="ns")
button0=tkinter.Button(task,text="0",width=15,bg="grey",height=2,font=20,command=lambda:buttonclick(0))
button0.grid(row=4,column=3,sticky="ns")

buttoneq=tkinter.Button(task,text="=",width=15,bg="grey",height=2,font=20,command=lambda:equal("="))
buttoneq.grid(row=5,column=0,columnspan=4,sticky="nsew")

task.mainloop()