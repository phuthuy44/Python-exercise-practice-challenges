import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(bg= "LemonChiffon")

Tops = Frame(root,bg="LemonChiffon",pady = 2,width=1350,height=100,relief = RIDGE)
Tops.grid(row =0, column =0)

lblTitle = Label(Tops,font = ("arial",50,"bold"),text="Tic Tac Toe Game",bd=21,bg="Gold",fg="cornsilk",justify=CENTER)
lblTitle.grid(row = 0, column=0)

MainFrame = Frame(root,bg="Gold",border=5,padx=32,pady = 50,width=1350,height=600,relief = RIDGE)
MainFrame.grid(row =1, column =0)

LeftFrame = Frame(MainFrame,bg="Gold",width=750,height=600,pady=2,padx=10,relief= SOLID)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame,bd=10,width=600,height=600,pady=5,padx=5,bg="Dark Orange",relief=RIDGE)
RightFrame.pack(side="right")

RightFrame1 = Frame(RightFrame,bd=5,width=560,height=200,pady=10,padx=2,bg="Orange",relief=RIDGE)
RightFrame1.grid(row = 0 , column = 0)

RightFrame2 = Frame(RightFrame,width=560,height=200,pady=10,padx=2,bg="Dark Orange",relief=RIDGE)
RightFrame2.grid(row = 1 , column = 0)

PlayerX =IntVar()
Player0 =IntVar()

PlayerX.set(0)
Player0.set(0)

buttons = StringVar()
click = True
def checker(buttons):
    global click
    if buttons["text"]==" " and click == True :
        buttons["text"]="X"
        click = False
        scorekeeper()
    elif buttons["text"]==" " and click == False :
        buttons["text"]="O"
        click = True
        scorekeeper()
def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(bg="gainsboro")
    button2.configure(bg="gainsboro")
    button3.configure(bg="gainsboro")
    button4.configure(bg="gainsboro")
    button5.configure(bg="gainsboro")
    button6.configure(bg="gainsboro")
    button7.configure(bg="gainsboro")
    button8.configure(bg="gainsboro")
    button9.configure(bg="gainsboro")
def scorekeeper():
    if (button1['text']=="X" and button2['text']=="X" and button3['text']=="X"):
        button1.configure(bg="powder blue")
        button2.configure(bg="powder blue")
        button3.configure(bg="powder blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button4['text']=="X" and button5['text']=="X" and button6['text']=="X"):
        button4.configure(bg="Red")
        button5.configure(bg="Red")
        button6.configure(bg="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button7['text']=="X" and button8['text']=="X" and button9['text']=="X"):
        button7.configure(bg="Cadet blue")
        button8.configure(bg="Cadet blue")
        button9.configure(bg="Cadet Blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button3['text']=="X" and button5['text']=="X" and button7['text']=="X"):
        button3.configure(bg="Red")
        button5.configure(bg="Red")
        button7.configure(bg="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button1['text']=="X" and button5['text']=="X" and button9['text']=="X"):
        button1.configure(bg="Red")
        button5.configure(bg="Red")
        button9.configure(bg="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button1['text']=="X" and button4['text']=="X" and button7['text']=="X"):
        button1.configure(bg="Red")
        button4.configure(bg="Red")
        button7.configure(bg="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button2['text']=="X" and button5['text']=="X" and button8['text']=="X"):
        button2.configure(bg="Red")
        button5.configure(bg="Red")
        button8.configure(bg="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button3['text']=="X" and button6['text']=="X" and button9['text']=="X"):
        button3.configure(bg="Red")
        button6.configure(bg="Red")
        button9.configure(bg="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()


    if (button1['text']=="O" and button2['text']=="O" and button3['text']=="O"):
        button1.configure(bg="powder blue")
        button2.configure(bg="powder blue")
        button3.configure(bg="powder blue")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button4['text']=="O" and button5['text']=="O" and button6['text']=="O"):
        button4.configure(bg="Red")
        button5.configure(bg="Red")
        button6.configure(bg="Red")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button7['text']=="O" and button8['text']=="O" and button9['text']=="O"):
        button7.configure(bg="Cadet blue")
        button8.configure(bg="Cadet blue")
        button9.configure(bg="Cadet Blue")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button3['text']=="O" and button5['text']=="O" and button7['text']=="O"):
        button3.configure(bg="Red")
        button5.configure(bg="Red")
        button7.configure(bg="Red")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button1['text']=="O" and button5['text']=="O" and button9['text']=="O"):
        button1.configure(bg="Red")
        button5.configure(bg="Red")
        button9.configure(bg="Red")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button1['text']=="O" and button4['text']=="O" and button7['text']=="O"):
        button1.configure(bg="Red")
        button4.configure(bg="Red")
        button7.configure(bg="Red")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button2['text']=="O" and button5['text']=="O" and button8['text']=="O"):
        button2.configure(bg="Red")
        button5.configure(bg="Red")
        button8.configure(bg="Red")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
    if (button3['text']=="O" and button6['text']=="O" and button9['text']=="O"):
        button3.configure(bg="Red")
        button6.configure(bg="Red")
        button9.configure(bg="Red")
        n = float(Player0.get())
        score = (n+1)
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","You have just won the game")
        reset()
def newGame():
    a = messagebox.askyesno(title="New Game",message="Do you want to start a new game?")
    if a:
        reset()
        PlayerX.set(0)
        Player0.set(0)
lblplayerX = Label(RightFrame1, font=("arial",40,'bold'),text = "Player X:",padx=2,pady=2,bg="Orange")
lblplayerX.grid(row = 0, column =0, sticky = W)

txtplayerX = Entry(RightFrame1, font=("arial",40,'bold'),bd=2,fg="black",textvariable = PlayerX,width=14)
txtplayerX.grid(row = 0, column =1)

lblplayer0 = Label(RightFrame1, font=("arial",40,'bold'),text = "Player 0 :",padx=2,pady=2, bg="Orange")
lblplayer0.grid(row = 1, column =0, sticky = W)
txtplayer0 = Entry(RightFrame1, font=("arial",40,'bold'),bd=2,fg="black",textvariable = Player0,width=14)
txtplayer0.grid(row = 1, column =1)

btnReset = Button(RightFrame2,text ="Reset ", font=("Times 27 bold"),height = 2, width = 15, bg = "maroon",fg="Yellow",command=reset)
btnReset.grid(row =0,column = 0,padx=6,pady=11)

btnNewGame = Button(RightFrame2,text ="New Game ", font=("Times 27 bold"),height = 2, width = 15, bg = "maroon",fg="Yellow",command=newGame)
btnNewGame.grid(row =0,column = 1,padx=6,pady=10)

button1 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button1))
button1.grid(row =1,column = 0, sticky = S+N+E+W)

button2 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button2))
button2.grid(row =1,column = 1, sticky = S+N+E+W)

button3 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button3))
button3.grid(row =1,column = 2, sticky = S+N+E+W)

button4 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button4))
button4.grid(row =2,column = 0, sticky = S+N+E+W)

button5 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button5))
button5.grid(row =2,column = 1, sticky = S+N+E+W)

button6 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button6))
button6.grid(row =2,column = 2, sticky = S+N+E+W)

button7 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button7))
button7.grid(row =3,column = 0, sticky = S+N+E+W)

button8 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button8))
button8.grid(row =3,column = 1, sticky = S+N+E+W)

button9 = Button(LeftFrame,text =" ", font=("Times 26 bold"),height = 3, width = 8, bg = "gainsboro",command=lambda:checker(button9))
button9.grid(row =3,column = 2, sticky = S+N+E+W)


root.mainloop()