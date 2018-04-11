from tkinter import * 
import time
import random

root=Tk()
root.geometry("1300x750+0+0")
root.title("Rest man sys")

text_input = StringVar()
operator=""




Tops = Frame(root, width=1600,height=50, bg = "powder blue" ,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800,height=700 ,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300,height=700, bg = "powder blue" ,relief=SUNKEN)
f2.pack(side=RIGHT)

###################time ############################
localtime = time.asctime(time.localtime(time.time()))

############# Info ##############################
lblInfo = Label(Tops, font=('arial',50,'bold'),text="Restaurant Management System",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',10,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


########### Calculator ##########################
def btnClick(num):
    global operator
    operator=operator+str(num)
    text_input.set(operator)

def btnClear():
    global operator
    operator =""
    text_input.set("")

def equal():
    global operator
    sumup = str(eval(operator))
    operator =sumup
    text_input.set(sumup)

def getRef():
    x=random.randint(12000,13000)
    rand_ref = str(x)
    rand.set(rand_ref)


    cof=float(fries.get())
    com=float(maggie.get())
    coc=float(coffee.get())
    coM=float(meal.get())

    

    sub_total = cof * 50 + coM * 250 + coc * 30 + com * 35
    service_charge = float(sub_total * 5 / 100)
    gst=float(sub_total * 9/100)

    total_cost = int(sub_total + service_charge + gst)
    total_cost = "Rs.", str('%.2f' % total_cost)

    subtotal.set(str(sub_total))
    service.set(str(service_charge))
    GST.set(str(gst))
    total.set(total_cost)

def qExit():
    root.destroy()

def reset():
    rand.set("")
    fries.set("")
    maggie.set("")
    coffee.set("")
    meal.set("")
    subtotal.set("")
    service.set("")
    total.set("")
    GST.set("")

    
txtDisplay = Entry(f2, font=('arial',20,'bold'), textvariable=text_input,bd=30, insertwidth=4, justify='right',bg = "powder blue")
txtDisplay.grid(columnspan=5)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="1",bg="powder blue",command = lambda:btnClick(1)).grid(row=1,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="2",bg="powder blue",command = lambda:btnClick(2)).grid(row=1,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="3",bg="powder blue",command = lambda:btnClick(3)).grid(row=1,column=2)
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="4",bg="powder blue",command = lambda:btnClick(4)).grid(row=2,column=0)


btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="5",bg="powder blue",command = lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="6",bg="powder blue",command = lambda:btnClick(6)).grid(row=2,column=2)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="7",bg="powder blue",command = lambda:btnClick(7)).grid(row=3,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="8",bg="powder blue",command = lambda:btnClick(8)).grid(row=3,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="9",bg="powder blue",command = lambda:btnClick(9)).grid(row=3,column=2)
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="0",bg="powder blue",command = lambda:btnClick(0)).grid(row=4,column=0)


Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="+",bg="powder blue",command = lambda:btnClick("+")).grid(row=1,column=3)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="-",bg="powder blue",command = lambda:btnClick("-")).grid(row=2,column=3)
multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="*",bg="powder blue",command = lambda:btnClick("*")).grid(row=3,column=3)
division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="/",bg="powder blue",command = lambda:btnClick("/")).grid(row=4,column=3)

Equal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="=",bg="powder blue",command = lambda:equal()).grid(row=4,column=1)
Clear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
             text="C",bg="powder blue",command = lambda:btnClear()).grid(row=4,column=2)



###########################################################
rand = StringVar()
fries= StringVar()
maggie=StringVar()
coffee=StringVar()
meal=StringVar()

lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16, anchor='w').grid(row=0,column=0)
txtRef= Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4, justify="right").grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text="Large Fries",bd=16, anchor='w').grid(row=1,column=0)
lblFries = Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=10,insertwidth=4, justify="right").grid(row=1,column=1)


lblMeal = Label(f1,font=('arial',16,'bold'),text="Large Meal",bd=16, anchor='w').grid(row=2,column=0)
txtMeal= Entry(f1,font=('arial',16,'bold'),textvariable=meal,bd=10,insertwidth=4, justify="right").grid(row=2,column=1)

lblMaggie = Label(f1,font=('arial',16,'bold'),text="Maggie",bd=16, anchor='w').grid(row=3,column=0)
txtMaggie= Entry(f1,font=('arial',16,'bold'),textvariable=maggie,bd=10,insertwidth=4,justify="right").grid(row=3,column=1)

lblCoffee = Label(f1,font=('arial',16,'bold'),text="Coffee",bd=16, anchor='w').grid(row=4,column=0)
txtCoffee= Entry(f1,font=('arial',16,'bold'),textvariable=coffee,bd=10,insertwidth=4, justify="right").grid(row=4,column=1)


##########################################################
subtotal = StringVar()
service= StringVar()
total=StringVar()
GST=StringVar()


lblReference = Label(f1,font=('arial',16,'bold'),text="Sub-Total",bd=16, anchor='w').grid(row=0,column=2)
txtRef= Entry(f1,font=('arial',16,'bold'),textvariable=subtotal,bd=10,insertwidth=4, justify="right").grid(row=0,column=3)

lblFries = Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16, anchor='w').grid(row=1,column=2)
lblFries = Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=10,insertwidth=4, justify="right").grid(row=1,column=3)


lblMeal = Label(f1,font=('arial',16,'bold'),text="GST",bd=16, anchor='w').grid(row=2,column=2)
txtMeal= Entry(f1,font=('arial',16,'bold'),textvariable=GST,bd=10,insertwidth=4, justify="right").grid(row=2,column=3)

lblMaggie = Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16, anchor='w').grid(row=3,column=2)
txtMaggie= Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=10,insertwidth=4,justify="right").grid(row=3,column=3)


#############################################################
Reset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=10,
             text="Reset",bg="powder blue",command = lambda:reset()).grid(row=6,column=1)

Total=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=10,
             text="Total",bg="powder blue",command = lambda:getRef()).grid(row=6,column=2)

Exit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=10,
             text="Exit",bg="powder blue",command = lambda:qExit()).grid(row=6,column=3)
root.mainloop()

