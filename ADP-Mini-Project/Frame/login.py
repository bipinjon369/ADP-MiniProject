from tkinter import *
import mysql.connector
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import messagebox,simpledialog
from Frame import common,home
class Main_window:
    def __init__(self,type):
        window = Tk()
        #centering the window to the screen

        common.center(window)
        window.title("Filo")
        window.iconbitmap(r'Frame/login_img/icon.ico')
        window.geometry("1000x600")
        window.configure(bg = "#000000")

        #function of register button
        def regrun():
            #function to store user details in database after registering
            def reg_submit():
                email = reg_emailentry.get()
                pwd = reg_passentry.get()
                if email=='' or pwd=='':                                                     #checks if email or password is empty
                    answer=showinfo(title='Error',message='Email or Password cannot be empty.',icon=WARNING)
                elif (' ' in email) or (' ' in pwd):                                         #checks for whitespaces in email and password
                    answer=showinfo(title='Error',message='Email and Password cannot contain spaces.',icon=WARNING)
                    reg_emailentry.delete(0, END)
                    reg_passentry.delete(0, END)
                elif(common.emailformat(email)==None):                                       #checks email format
                    answer=showinfo(title='Error',message='Please provide a valid a email address.',icon=WARNING)
                    reg_emailentry.delete(0, END)
                    reg_passentry.delete(0, END)
                else:
                    try:
                        mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="adp")
                        mycursor = mydb.cursor()
                        mycursor.execute("insert into user_details values('"+email+"','"+pwd+"')")
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                    except:                                                                  #exception handling email already exists in database
                        answer=showinfo(title='Error',message='Email Id already exists!',icon=WARNING)
                        reg_emailentry.delete(0, END)
                        reg_passentry.delete(0, END)
                    else:
                        answer=showinfo(title='Thank You for Registering!',message='Thank You for Registering.\nYou will now be redirected to Login.')
                        loginrun()

            regbtn.config(background='#FFFFFF',foreground='#000000',activebackground="white")
            loginbtn.config(background='#000000',foreground='#FFFFFF',activebackground="white")
            regframe=Frame(window,width=1000,height=558,bg='#000000')
            regframe.place(x=0,y=42)
            Label(regframe,text='Register',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=430,y=50)
            Label(regframe,text='Enter Email',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=140)
            Label(regframe,text='Set Password',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=270)

            reg_emailentry = Entry(regframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
            reg_emailentry.place(x=330,y=200,width=350)
            
            reg_passentry = Entry(regframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0,show="*")
            reg_passentry.place(x=330,y=330,width=350)

            #submit button for register
            reg_submit = Button(regframe,text="Submit",borderwidth = 0,highlightthickness = 0,font=("Poppins",15),command = reg_submit,background="#FFFFFF",foreground="#000000",activebackground="#FFFFFF",relief = "flat")
            reg_submit.place(x=450,y=450,width=100,height=50)

        #function of login button    
        def loginrun():
            def login_submit():
                email = log_emailentry.get()
                pwd = log_passentry.get()
                if email=='' or pwd=='':                                                            #checks if email or password is empty
                    answer=showinfo(title='Error',message='Email or Password cannot be empty.',icon=WARNING)
                elif (' ' in email) or (' ' in pwd):                                                #checks for whitespaces in email and password
                    answer=showinfo(title='Error',message='Email and Password cannot contain spaces.',icon=WARNING)
                    log_emailentry.delete(0, END)
                    log_passentry.delete(0, END)
                elif(common.emailformat(email)==None):                                              #checks email format
                    answer=showinfo(title='Error',message='Please provide a valid a email address.',icon=WARNING)
                    log_emailentry.delete(0, END)
                    log_passentry.delete(0, END)
                else:
                    mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="adp")
                    mycursor = mydb.cursor()
                    mycursor.execute("select email,pwd from user_details where email='"+email+"'")
                    result = mycursor.fetchone()
                    if result == None:
                        answer = showinfo(title='Error',message='Email address not found.',icon=WARNING)
                    elif pwd != result[1]:
                        answer = showinfo(title='Error',message='Invalid Password!.',icon=WARNING)
                    else:
                        answer=showinfo(title='Successfull',message='Login Successful.')
                        window.destroy()
                        home.Mainhome()

            loginbtn.config(background='#FFFFFF',foreground='#000000')
            regbtn.config(background='#000000',foreground='#FFFFFF')
            loginframe=Frame(window,width=1000,height=558,bg='#000000')
            loginframe.place(x=0,y=42)
            Label(loginframe,text='Login',font=("Poppins",24),background='#000000',foreground='#FFFFFF').place(x=440,y=50)
            Label(loginframe,text='Email',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=140)
            Label(loginframe,text='Password',font=("Poppins",20),background='#000000',foreground='#8AF8FF').place(x=325,y=270)

            log_emailentry = Entry(loginframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0)
            log_emailentry.place(x=330,y=200,width=350)
            
            log_passentry = Entry(loginframe,bd = 0,bg = "#FFFFFF",font=("Poppins",15),highlightthickness = 0,show="*")
            log_passentry.place(x=330,y=330,width=350)

            login_submit = Button(loginframe,text="Submit",borderwidth = 0,highlightthickness = 0,font=("Poppins",15),command = login_submit,background="#FFFFFF",foreground="#000000",activebackground="#FFFFFF",relief = "flat")
            login_submit.place(x=450,y=450,width=100,height=50)


        #two labels login and register
        regbtn=Button(window,text='Register',command=regrun,font=("Poppins",24),background='#FFFFFF',foreground='#000000',activebackground="white",bd=0,highlightthickness=0,relief='sunken')
        regbtn.place(x=0,y=0,width=500,height=42)
        loginbtn=Button(window,text='Login',command=loginrun,font=("Poppins",24),background='#000000',foreground='#FFFFFF',activebackground="white",bd=0,highlightthickness=0,relief='sunken')
        loginbtn.place(x=500,y=0,width=500,height=42)
        
        if type=='login':
            loginrun()
        else:
            regrun()

        window.resizable(False,False)
        window.mainloop()