import tkinter
from tkinter import messagebox
#按键事件触发函数
var=''
operator=''
x=0
def button1_click():
    global var
    var=var+'1'
    text.set(var)

def button2_click():
    global var
    var = var + '2'
    text.set(var)

def button3_click():
    global var
    var=var+'3'
    text.set(var)

def button4_click():
    global var
    var=var+'4'
    text.set(var)

def button5_click():
    global var
    var=var+'5'
    text.set(var)

def button6_click():
    global var
    var=var+'6'
    text.set(var)

def button7_click():
    global var
    var=var+'7'
    text.set(var)

def button8_click():
    global var
    var=var+'8'
    text.set(var)

def button9_click():
    global var
    var=var+'9'
    text.set(var)

def button0_click():
    global var
    var=var+'0'
    text.set(var)


def C_button():
    global var
    global x
    global operator
    operator=""
    var=""
    x=0
    text.set(var)

def add_click():
    global x
    global var
    global operator
    x=int(var)
    operator="+"
    var=var+"+"
    text.set(var)

def minu_click():
    global x
    global var
    global operator
    x=int(var)
    operator="-"
    var=var+"-"
    text.set(var)

def mult_click():
    global x
    global var
    global operator
    x=int(var)
    operator="x"
    var=var+"x"
    text.set(var)

def divide_click():
    global x
    global var
    global operator
    x=int(var)
    operator="/"
    var=var+"/"
    text.set(var)
def back_click():
    global var
    lst=list(var)
    lst.pop()
    var = ''.join(lst)
    text.set(var)

def HEX_click():
    global var
    var=int(var)
    var=hex(var)
    text.set(var)
    var = str(var)
def OCT_click():
    global var
    var=int(var)
    var=oct(var)
    text.set(var)
    var=str(var)
def BIN_click():
    global var
    var=int(var)
    var=bin(var)
    text.set(var)
    var=str(var)
def show_result():
    global x
    global var
    global operator
    var2 = var
    #split切片分割取+号后面
    if operator=="+":
        y=int(var2.split("+")[1])
        result=x+y
        text.set(result)
        var=str(result)

    elif operator=="-":
        y=int(var2.split("-")[1])
        result=x-y
        text.set(result)
        var=str(result)

    elif operator=="x":
        y=int(var2.split("x")[1])

        result=x*y
        text.set(result)
        var=str(result)

    elif operator=="/":
        y=int(var2.split("/")[1])
        if y==0:
            messagebox.showinfo(title='提示', message="Zero can't be the denominator")
            val=""
            x=""
            text.set(val)
        else:
            result=x//y
            text.set(result)
            var=str(result)



window=tkinter.Tk()
text=tkinter.StringVar()
#布局按键
#achor控制文本（或图像）在 Label 中显示的位置	se代表东南方向
#pack 放置 fill扩充 expand 扩展
label=tkinter.Label(window, textvariable=text, font=('arial 20 bold'), bg='white', anchor='se')
label.pack(expand=True,fill='both')
frame = tkinter.Frame(window)
jz= frame
jz.pack(expand=True,fill='both')
f1= tkinter.Frame(window)
f1.pack(expand=True,fill='both')
f2= tkinter.Frame(window)
f2.pack(expand=True,fill='both')
f3= tkinter.Frame(window)
f3.pack(expand=True,fill='both')
f4= tkinter.Frame(window)
f4.pack(expand=True,fill='both')


#按键布局
#relief边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。
BIN_button= tkinter.Button(jz, text='BIN', font=('arial 16 bold'), relief='groove', border=0, command=BIN_click)
BIN_button.pack(side='left', expand=True, fill='both')
OCT_button= tkinter.Button(jz, text='OCT', font=('arial 16 bold'), relief='groove', border=0, command=OCT_click)
OCT_button.pack(side='left', expand=True, fill='both')
HEX_button= tkinter.Button(jz, text='HEX', font=('arial 16 bold'), relief='groove', border=0, command=HEX_click)
HEX_button.pack(side='left', expand=True, fill='both')
btn_back = tkinter.Button(jz, text='<<--', font=('arial 20 bold'), relief='groove', border=0, command=back_click)
btn_back.pack(side='left', expand=True, fill='both')

button7= tkinter.Button(f1, text='7', font=('arial 16 bold'), relief='groove', border=0, command=button7_click)
button7.pack(side='left', expand=True, fill='both')
button8= tkinter.Button(f1, text='8', font=('arial 16 bold'), relief='groove', border=0, command=button8_click)
button8.pack(side='left', expand=True, fill='both')
button9= tkinter.Button(f1, text='9', font=('arial 16 bold'), relief='groove', border=0, command=button9_click)
button9.pack(side='left', expand=True, fill='both')
add_button= tkinter.Button(f1, text='+', font=('arial 16 bold'), relief='groove', border=0, command=add_click)
add_button.pack(side='left', expand=True, fill='both')

button4= tkinter.Button(f2, text='4', font=('arial 16 bold'), relief='groove', border=0, command=button4_click)
button4.pack(side='left', expand=True, fill='both')
button5= tkinter.Button(f2, text='5', font=('arial 16 bold'), relief='groove', border=0, command=button5_click)
button5.pack(side='left', expand=True, fill='both')
button6= tkinter.Button(f2, text='6', font=('arial 16 bold'), relief='groove', border=0, command=button6_click)
button6.pack(side='left', expand=True, fill='both')
minu_button= tkinter.Button(f2, text='-', font=('arial 20 bold'), relief='groove', border=0, command=minu_click)
minu_button.pack(side='left', expand=True, fill='both')

button1= tkinter.Button(f3, text='1', font=('arial 16 bold'), relief='groove', border=0, command=button1_click)
button1.pack(side='left', expand=True, fill='both')
button2= tkinter.Button(f3, text='2', font=('arial 16 bold'), relief='groove', border=0, command=button2_click)
button2.pack(side='left', expand=True, fill='both')
button3= tkinter.Button(f3, text='3', font=('arial 16 bold'), relief='groove', border=0, command=button3_click)
button3.pack(side='left', expand=True, fill='both')
mul_button= tkinter.Button(f3, text='x', font=('arial 16 bold'), relief='groove', border=0, command=mult_click)
mul_button.pack(side='left', expand=True, fill='both')

zero_button= tkinter.Button(f4, text='0', font=('arial 16 bold'), relief='groove', border=0, command=button0_click)
zero_button.pack(side='left', expand=True, fill='both')
C_button= tkinter.Button(f4, text='C', font=('arial 16 bold'), relief='groove', border=0, command=C_button)
C_button.pack(side='left', expand=True, fill='both')
result_button= tkinter.Button(f4, text='=', font=('arial 16 bold'), relief='groove', border=0, command=show_result)
result_button.pack(side='left', expand=True, fill='both')
div_button= tkinter.Button(f4, text='/', font=('arial 16 bold'), relief='groove', border=0, command=divide_click)
div_button.pack(side='left', expand=True, fill='both')

window.title('计算器')
window.geometry('300x400')
window.mainloop()