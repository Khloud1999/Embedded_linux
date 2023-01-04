import tkinter as tk
from tkinter import *
from tkinter import ttk

def fun():
	#text_1.delete("1.0", "end-1c")
	#text_2.delete("1.0", "end-1c")
	#text_3.delete("1.0", "end-1c")
	text_4.delete("1.0", "end-1c")
	price=0
	input_1=int(text_1.get("1.0", "end-1c"))
	input_2=int(text_2.get("1.0", "end-1c"))
	input_3=int(text_3.get("1.0", "end-1c"))
	price =int(input_1*10+input_2*5+input_3*7)
	text_4.insert(END,price)

	
	
	
window_1 = Tk() 
window_1.title(" 2asp shop ")
window_1.geometry('550x650')

label_1 = Label(window_1,width=500,height=500,bg="#CDCD66")
label_1.place(x = 0,y = 0)
Label_2=Label(window_1 , text = "welcom to 2asp shop" ,bg="#CDCD66", font = ('Verdana', 20)).pack(side=TOP)

label_3=Label(window_1,text="Menu:",bg="#CDCD66",font =('verdana',15)).place(x=50,y=70)

photo_1 = PhotoImage(file='large.png')
photo_1 = photo_1.subsample(2,2)
photo_2 = PhotoImage(file='small.png')
photo_2 = photo_2.subsample(5,5)
photo_3 = PhotoImage(file='medium.png')
photo_3 = photo_3.subsample(2,2)

lable_4= Label(window_1,image=photo_1)
lable_4.place(x = 50,y =110 )
label_5=Label(window_1,text="Large  10",bg="#CDCD66",font =('verdana',12)).place(x=50,y=230)
text_1 = Text(window_1, width=9, height=1)
text_1.place(x=50 , y=260)

lable_6= Label(window_1,image=photo_2)
lable_6.place(x = 210,y =310 )
label_7=Label(window_1,text=" Small  5",bg="#CDCD66",font =('verdana',12)).place(x=210,y=435)
text_2 = Text(window_1, width=9, height=1)
text_2.place(x=210 , y=465)

lable_8= Label(window_1,image=photo_3)
lable_8.place(x = 350,y =110 )
label_9=Label(window_1,text="Medium  7",bg="#CDCD66",font =('verdana',12)).place(x=350,y=230)
text_3 = Text(window_1, width=9, height=1)
text_3.place(x=350 , y=260)


b_2 = Button(window_1 , text = "price" ,width= 7, bg="#CDCD66" , fg = "black" , bd ='5', command=fun).place(x=50,y=540)
text_4 = Text(window_1, width=9, height=1)
text_4.place(x=140 , y=545)

b_3 = Button(window_1 , text = "Close" ,width= 7, bg="#CDCD66" , fg = "black" , bd ='5', command = window_1.destroy).pack(side = BOTTOM)

window_1.mainloop()