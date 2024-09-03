from tkinter import *
parent = Tk()

p = Entry(parent).grid(rowspan=1,columnspan=8)
ACbutton = Button(parent, text='A/C')
ACbutton.grid(row=1,column=0)
PSbutton = Button(parent, text='+/-')
PSbutton.grid(row=1,column=2)
MODbutton = Button(parent, text='%')
MODbutton.grid(row=1,column=3)
DIVbutton = Button(parent, text='|')
DIVbutton.grid(row=1,column=4)
# 987X
NINEbutton = Button(parent, text='9')
NINEbutton.grid(row=2,column=0)
Ebutton = Button(parent, text='8')
Ebutton.grid(row=2,column=2)
SEVbutton = Button(parent, text='7')
SEVbutton.grid(row=2,column=3)
Xbutton = Button(parent, text='X')
Xbutton.grid(row=2,column=4)
# 654-
SIXbutton = Button(parent, text='6')
SIXbutton.grid(row=3,column=0)
FVbutton = Button(parent, text='5')
FVbutton.grid(row=3,column=2)
FORbutton = Button(parent, text='4')
FORbutton.grid(row=3,column=3)
MINbutton = Button(parent, text='-')
MINbutton.grid(row=3,column=4)
# 321+
TREbutton = Button(parent, text='3')
TREbutton.grid(row=4,column=0)
TUbutton = Button(parent, text='2')
TUbutton.grid(row=4,column=2)
ONEbutton = Button(parent, text='1')
ONEbutton.grid(row=4,column=3)
ADDbutton = Button(parent, text='+')
ADDbutton.grid(row=4,column=4)
#00.=
ZERbutton = Button(parent, text='0')
ZERbutton.grid(row=5,columnspan=2)
DOTbutton = Button(parent, text='.')
DOTbutton.grid(row=5,column=3)
EZbutton = Button(parent, text='=')
EZbutton.grid(row=5,column=4)




parent.mainloop()
