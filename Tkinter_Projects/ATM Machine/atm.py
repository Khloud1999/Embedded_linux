from tkinter import *
import tkinter as tk
import time
#from Pil import Imagetk, Image

current_balance = 10000

class MAINAPP(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartFram, MenuFram, WithdrawFram, DepositFram, BalanceFram):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
			
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartFram")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartFram(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#8B8B69')
        self.controller = controller
        self.controller.title('ATM')
        self.controller.state('zoomed')
		
        heading_label = tk.Label(self, text='Welcom To The ATM',font=('orbitron',45,'bold')
											,foreground='#ffffff',background='#8B8B69')
        heading_label.pack(pady=25)
		
        space_label = tk.Label(self,height=4,bg='#8B8B69')
        space_label.pack()

        password_label = tk.Label(self,text='Enter your password',
									font=('orbitron',13,'bold'),bg='#8B8B69',fg='white')
        password_label.pack(pady=10)
		
        space_label = tk.Label(self,height=2,bg='#8B8B69')
        space_label.pack()

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,textvariable=my_password,
                                           font=('orbitron',12),width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)


        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
            
            password_entry_box.bind('<FocusIn>',handle_focus_in)

        def check_password():
           if my_password.get() == '123':
               my_password.set('')
               incorrect_password_label['text']=''
               controller.show_frame('MenuFram')
           else:
               incorrect_password_label['text']='Incorrect Password'
                
        enter_button = tk.Button(self,text='Enter',command=check_password,
                                 relief='raised',borderwidth = 3,width=40,height=3,)
        enter_button.pack(pady=10)



        incorrect_password_label = tk.Label(self,text='',font=('orbitron',17),
                                             fg='white',bg='#8B8B69' ,anchor='n')
											 
        incorrect_password_label.pack(fill='both',expand=True)
        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')



        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()
        

class MenuFram(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#8B8B69')
        self.controller = controller
   
        heading_label = tk.Label(self,text='select your choice',font=('orbitron',25,'bold'),
                                 foreground='#ffffff', background='#8B8B69')
        heading_label.pack(pady=25)
        space_label = tk.Label(self,height=4,bg='#8B8B69')
        space_label.pack()

        button_frame = tk.Frame(self,bg='#8B8B69')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawFram')
            
        withdraw_button = tk.Button(button_frame,text='Withdraw', command=withdraw,
                                    relief='raised',borderwidth=3,width=50,height=5)
        withdraw_button.grid(row=0,column=1,pady=5,padx=500)

        def deposit():
            controller.show_frame('DepositFram')
            
        deposit_button = tk.Button(button_frame, text='Deposit',command=deposit,relief='raised',
                                  borderwidth=3, width=50,height=5)
								 
        deposit_button.grid(row=1,column=1,pady=5)

        def balance():
            controller.show_frame('BalanceFram')
            
        balance_button = tk.Button(button_frame, text='Balance',command=balance,
                                   relief='raised',borderwidth=3,width=50,height=5)
        balance_button.grid(row=2,column=1,pady=5)

        def exit():
            controller.show_frame('StartFram')
            
        exit_button = tk.Button(button_frame,text='Exit', command=exit,
                                relief='raised',borderwidth=3, width=50, height=5)
        exit_button.grid(row=3,column=1,pady=5)


        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

class WithdrawFram(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#8B8B69')
        self.controller = controller


        heading_label = tk.Label(self,text='Choose the amount you want to withdraw',font=('orbitron',25,'bold'),
                                 foreground='#ffffff',background='#8B8B69')
        heading_label.pack(pady=25)
        space_label = tk.Label(self,height=4,bg='#8B8B69')
        space_label.pack()

        button_frame = tk.Frame(self,bg='#8B8B69')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuFram')
            
        twenty_button = tk.Button(button_frame, text='20',command=lambda:withdraw(20),
                                  relief='raised',borderwidth=3,width=50,height=5)
        twenty_button.grid(row=0,column=0,pady=5,padx=50)

        forty_button = tk.Button(button_frame,text='40', command=lambda:withdraw(40),
                                 relief='raised',borderwidth=3,width=50,height=5)
        forty_button.grid(row=1,column=0,pady=5)

        sixty_button = tk.Button(button_frame, text='60',command=lambda:withdraw(60),
                                 relief='raised',borderwidth=3, width=50,height=5)
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button = tk.Button(button_frame,text='80',command=lambda:withdraw(80),
                                   relief='raised',borderwidth=3,width=50,height=5)
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button = tk.Button(button_frame,text='100',command=lambda:withdraw(100),
                                      relief='raised', borderwidth=3,width=50,height=5)
        one_hundred_button.grid(row=0,column=1,pady=5,padx=505)

        two_hundred_button = tk.Button(button_frame,text='200', command=lambda:withdraw(200),
                                       relief='raised',borderwidth=3,width=50,height=5)
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button = tk.Button(button_frame,text='300',command=lambda:withdraw(300),
                                         relief='raised',borderwidth=3, width=50,height=5)
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,textvariable=cash,width=59,justify='right')
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=30)

        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuFram')
            
        other_amount_entry.bind('<Return>',other_amount)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()
   

class DepositFram(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#8B8B69')
        self.controller = controller

        heading_label = tk.Label(self,text='Enter amount',font=('orbitron',25,'bold'),
                                 foreground='#ffffff',background='#8B8B69')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#8B8B69')
        space_label.pack()

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self, textvariable=cash,font=('orbitron',12), width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuFram')
            cash.set('')
            
        enter_button = tk.Button(self,text='Enter',command=deposit_cash,
                                relief='raised',borderwidth=3,width=40,height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self,bg='#8B8B69')
        two_tone_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()


class BalanceFram(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#8B8B69')
        self.controller = controller

        
        heading_label = tk.Label(self,text='Your Balance', font=('orbitron',25,'bold'),
                                 foreground='#ffffff',background='#8B8B69')
        heading_label.pack(pady=25)

        global current_balance
		
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,textvariable=controller.shared_data['Balance'],
                                 font=('orbitron',25,'bold'),fg='white',bg='#8B8B69',anchor='w')
        balance_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#8B8B69')
        space_label.pack()
		
        button_frame = tk.Frame(self,bg='#8B8B69')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuFram')
            
        menu_button = tk.Button(button_frame,command=menu,text='Menu',
                                relief='raised', borderwidth=3,width=50,height=5)
        menu_button.grid(row=0,column=1,pady=5,padx=500)

        def exit():
            controller.show_frame('StartFram')
            
        exit_button = tk.Button(button_frame,text='Exit',command=exit,
                                relief='raised',borderwidth=3,width=50,height=5)
        exit_button.grid(row=1,column=1,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()


if __name__ == "__main__":
    app = MAINAPP()
    app.mainloop()
