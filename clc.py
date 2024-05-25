from tkinter import*
root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(0,0)
root.config(bg="#17161b")

equation=""
def show(value):
 global equation
 equation+=value
 lbl_a.config(text=equation)

def clear():
 global equation
 equation=""
 lbl_a.config(text=equation)

def calculate():
 global equation
 result=""
 if equation !="":
  try:
   result=eval(equation)
  except:
   result="error"
   equation=""
 lbl_a.config(text=result)

lbl_a=Label(root,font=("Arial 30"),height=2,width=25,text="")
lbl_a.pack()
btn1=Button(root,text="C",font=("Arial 30 bold"),height=1,width=5,bg="#3697f5",bd=1,fg="#fff",command=lambda: clear())
btn1.place(x=10,y=100)

btn2=Button(root,text="/",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("/"))
btn2.place(x=150,y=100)

btn3=Button(root,text="%",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("%"))
btn3.place(x=290,y=100)

btn4=Button(root,text="*",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("*"))
btn4.place(x=430,y=100)

btn5=Button(root,text="7",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("7"))
btn5.place(x=10,y=200)

btn6=Button(root,text="8",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("8"))
btn6.place(x=150,y=200)

btn7=Button(root,text="9",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("9"))
btn7.place(x=290,y=200)

btn8=Button(root,text="-",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("-"))
btn8.place(x=430,y=200)

btn9=Button(root,text="4",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("4"))
btn9.place(x=10,y=300)

btn10=Button(root,text="5",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("5"))
btn10.place(x=150,y=300)

btn11=Button(root,text="6",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("6"))
btn11.place(x=290,y=300)

btn12=Button(root,text="+",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("+"))
btn12.place(x=430,y=300)

btn13=Button(root,text="1",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("1"))
btn13.place(x=10,y=400)

btn14=Button(root,text="2",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("2"))
btn14.place(x=150,y=400)

btn15=Button(root,text="3",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("3"))
btn15.place(x=290,y=400)

btn16=Button(root,text="0",font=("Arial 30 bold"),height=1,width=11,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("0"))
btn16.place(x=10,y=500)

btn17=Button(root,text=".",font=("Arial 30 bold"),height=1,width=5,bg="#2a2d36",bd=1,fg="#fff",command=lambda:show("."))
btn17.place(x=290,y=500)

btn18=Button(root,text="=",font=("Arial 30 bold"),height=3,width=5,bg="#fe9037",bd=1,fg="#fff",command=lambda:calculate())
btn18.place(x=430,y=400)



root.mainloop()