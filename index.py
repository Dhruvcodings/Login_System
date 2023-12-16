from tkinter import *                                # importing full tkinter module
import tkinter.messagebox as tkmb                    # importing message box from tkinter


window = Tk()                                         # creating a seperate new blank window using tkinter
window.geometry('390x360')
window.title('RESTAURENT Log in system')              # size of window created above
window.configure(bg='brown')                          # giving background colour



title=Label(window,text='RESTAURENT \n LOG IN \n SYSTEM',borderwidth=3,width=15,height=0,font=('Algerian',20,'bold'),bg='purple',fg='gold',
         relief=SUNKEN) # creating title shown in window
title.place(x=40,y=20)  # set the title positions


#creating the username and pasasword text in window
username=Label(window,text='Username',width=8).place(x=50,y=150)
password=Label(window,text='Password',width=8).place(x=50,y=175)


# creating the white empty box for entering username and password 
txtuser=Entry(window,bg='white',font=5)
txtuser.place(x=115,y=150)
txtuser.insert(0,'DHRUV')

txtpass=Entry(window,bg='white',show='*',font=5)
txtpass.place(x=115,y=175)
txtpass.insert(0,'JSR')




global checkbuttoncount
checkbuttoncount=[1,1]


def showhidepass():
    global checkbuttoncount
    
    global txtpass

    password=txtpass.get()
    
    if len(checkbuttoncount)%2==0:
        txtpass=Entry(window,bg='white',font=5)
        txtpass.place(x=115,y=175)
        txtpass.insert(0,password)
        checkbuttoncount=checkbuttoncount+[1]
        
    else:
        txtpass=Entry(window,bg='white',show='*',font=5)
        txtpass.place(x=115,y=175)
        txtpass.insert(0,password)
        
        checkbuttoncount=checkbuttoncount+[1]
                



checkbutton=Checkbutton(window,command=showhidepass)
checkbutton.place(x=300,y=175,height=22)

def login():
    username=txtuser.get()
    password=txtpass.get()
    
    if username=='DHRUV' and password=='JSR':
        tkmb.showwarning('SUCCESSFUL Login','YOU ARE LOGGED IN')

    elif username=='dhruv':
        tkmb.showwarning('Login','Incorrect Password')
        txtpass.delete(0,END)
    elif password=='jsr':
        tkmb.showwarning('Login','Incorrect Username')   

    else:
        tkmb.showwarning('Login','Incorrect Username and Password')
        txtpass.delete(0,END)

def cancel():
    m=tkmb.askyesno('Login','Are you sure you want to cancel')
    if m:
        exit()

login_button=Button(window,text='Login',command=login,width=10).place(x=100,y=300)

cancel_button=Button(window,text='Cancel',command=cancel,width=10).place(x=200,y=300)






