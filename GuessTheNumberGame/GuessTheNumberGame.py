import random
import tkinter as tk 

window = tk.Tk()

window.geometry("600x400")
window.config(bg="pink")
window.resizable(width=False,height=False)
window.title("Number Gussesing Game")
TARGET = random.randint(0,20)
RETRIES = 0
def update_result(text):
    result.configure(text = text)
def createGussingName():
    guess_button.configure(state="normal")
    global TARGET,RETRIES
    TARGET = random.randint(0,20)
    RETRIES = 0
    update_result(text="Try to guess number between 1 to 20")
def play_game():
    #RETRIES = 0 #On the first iteraction of the loop, rETRIES has the value of 0
    global RETRIES
    choice = int(number_form.get())
    if choice != TARGET:
        RETRIES += 1
        result = "Wrong Guess!Try Again!"
        if TARGET < choice :
            hint ="Your guess is too high.The required number lies between 0 and {}".format(choice)
        else:
            hint ="Your guess is too low.The required number lies betwwen {} and 20".format(choice)
        result += "\n\nHint : \n"+hint
    else:
            result = "You guessed the correct number after {} retries".format(RETRIES)
            guess_button.configure(state="disabled")
            result +="\n"+"Click on play to start a new game "
    update_result(result)
title = tk.Label(window,text="Guessing Game",font=("Arial",24,"bold"),fg="Yellow",bg="#065569")
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),fg = "Yellow", bg="grey", justify=tk.LEFT)
# Play Button
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg = "Black", bg="#29c70a", command=createGussingName)
 
# Guess Button
guess_button = tk.Button(window,text="Guess",font=("Arial",13), state='disabled', fg="White",bg="Black", command=play_game)
exit_button = tk.Button(window,text ="Exit Game",font=("Arial",16,"bold"),fg="Black",bg="Red",command=exit)
exit_button.place(x=300,y=320)
# Entry Fields
guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
 
 
# Place the labels
 
title.place(x=170, y=50)
result.place(x=100, y=210)
 
# Place the buttons
exit_button.place(x=300,y=320)
guess_button.place(x=350, y=147) 
play_button.place(x=170, y=320)
 
# Place the entry field
number_form.place(x=180, y=150)
window.mainloop()
'''

'''