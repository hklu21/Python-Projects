import tkinter
from tkinter import Tk
from tkinter import *
import random

# show result of the turn
def GameResult():
    global RChoice , HChoice , win , winLabel , human_point, computer_point, RChoice_label, HChoice_label

    #show robot choice lable
    if RChoice == 'rock':
        rockL.place(x = 210 , y = 10)
        RChoice_label = Label(main , font = 'arial' , text = "Computer chose ROCK")
        RChoice_label.place(x = 230 , y = 165)
        
    elif RChoice == 'paper':
        paperL.place(x = 210 , y = 10)
        RChoice_label = Label(main , font = 'arial' , text = "Computer chose PAPER")
        RChoice_label.place(x = 230 , y = 165)
    elif RChoice == 'scissors':
        scissorsL.place(x = 210 , y = 10)
        RChoice_label = Label(main , font = 'arial' , text = "Computer chose SCISSORS")
        RChoice_label.place(x = 215 , y = 165)

    #show human choice lable
    if HChoice == 'rock':
        rockLH.place(x = 210 , y = 225)
        HChoice_label = Label(main , font = 'arial' , text = "You chose ROCK")
        HChoice_label.place(x = 248 , y = 380)

    elif HChoice == 'paper':
        paperLH.place(x = 210 , y = 225)
        HChoice_label = Label(main , font = 'arial' , text = "You chose PAPER")
        HChoice_label.place(x = 245 , y = 380)

    elif HChoice == 'scissors':
        scissorsLH.place(x = 210 , y = 225)
        HChoice_label = Label(main , font = 'arial' , text = "You chose SCISSORS")
        HChoice_label.place(x = 234 , y = 380)

    #add labels on screen
    if win == "You":
        winLabel = Label(main , font = 'arial' , text = win + " win!")
        winLabel.pack()
        winLabel.place(x = 270 , y = 200)
    elif win == "Computer":
        winLabel = Label(main , font = 'arial' , text = win + " wins!")
        winLabel.pack()
        winLabel.place(x = 255 , y = 200)
    else:
        winLabel = Label(main , font = 'arial' , text = "It is a Tie!")
        winLabel.pack()
        winLabel.place(x = 270 , y = 200)
    winLabel['bg'] = 'white'
    winLabel['fg'] = 'red'
    HChoice_label['bg'] = '#E3E3FF'
    RChoice_label['bg'] = '#E3E3FF'


    

    #hide button
    rock.place(x = 210 , y = 600)
    paper.place(x = 210 , y = 600)
    scissors.place(x = 210 , y = 600)


    # add play again button
    playagainButton = tkinter.Button(main , text = 'Continue' , command = Continue)
    playagainButton.pack()
    playagainButton.place(x = 547 , y = 398)
    playagainButton['bg'] = '#F9F2BB'

    # add restart button
    restartButton = tkinter.Button(main , text = 'Restart' , command = Clear)
    restartButton.pack()
    restartButton.place(x = 0 , y = 398)
    restartButton['bg'] = '#F9F2BB'


#play again function
def Continue():
    global winLable, HChoice_label, RChoice_label

    #hide robot lable choice
    rockL.place(x = 210 , y = 600)
    paperL.place(x = 210 , y = 600)
    scissorsL.place(x = 210 , y = 600)

    #hide human lable choice
    rockLH.place(x = 210 , y = 560)
    paperLH.place(x = 210 , y = 600)
    scissorsLH.place(x = 210 , y = 600)

    #destroy labels
    winLabel.destroy()
    HChoice_label.destroy()
    RChoice_label.destroy()

    #show buttons
    rock.place(x = 10 , y = 100)
    paper.place(x = 210 , y = 100)
    scissors.place(x = 410 , y = 100)

#restart function
def Clear():
    global winLable, human_point, computer_point, HChoice_label, RChoice_label

    #hide robot lable choice
    rockL.place(x = 210 , y = 500)
    paperL.place(x = 210 , y = 500)
    scissorsL.place(x = 210 , y = 500)

    #hide human lable choice
    rockLH.place(x = 210 , y = 500)
    paperLH.place(x = 210 , y = 500)
    scissorsLH.place(x = 210 , y = 500)

    #destroy labels
    winLabel.destroy()
    HChoice_label.destroy()
    RChoice_label.destroy()


    #show buttons
    rock.place(x = 10 , y = 100)
    paper.place(x = 210 , y = 100)
    scissors.place(x = 410 , y = 100)

    human_point = 0
    computer_point = 0
    human_score.config(text = "Your Score : " + str(human_point))
    computer_score.config(text = "Computer Score : " + str(computer_point))

#robot choice
def OurturnFun():
    global RChoice , dice

    #random choice for robot
    if dice == 1:
        RChoice = "rock"
    elif dice == 2:
        RChoice = "paper"
    elif dice == 3:
        RChoice = "scissors"

    #random num in range 1 - 3
    dice = random.randint(1 , 3)

#Human choice
def YourturnFun(choice):
    global HChoice

    #call robot choice function
    OurturnFun()

    #find out what is human choice
    if choice == 'rock':
        HChoice = "rock"
    elif choice == 'paper':
        HChoice = "paper"
    elif choice == 'scissors':
        HChoice = "scissors"

    #call winner function and check who win
    Winner()

def ScoreFun():
    global human_point, computer_point, win

    #calculate score
    if win == "You" :
        human_point += 1
    elif win == "Computer":
        computer_point += 1

    #refresh score on board
    human_score.config(text = "Your Score : " + str(human_point))
    computer_score.config(text = "Computer Score : " + str(computer_point))

def Winner():
    global win , HChoice , RChoice

    #check who win
    if HChoice == 'rock' and RChoice == 'rock':
        win = "Tie"
    elif HChoice == 'paper' and RChoice == 'paper':
        win = "Tie"
    elif HChoice == 'scissors' and RChoice == 'scissors':
        win = "Tie"
    elif HChoice == 'rock' and RChoice == 'scissors':
        win = "You"
    elif HChoice == 'paper' and RChoice == 'rock':
        win = "You"
    elif HChoice == 'scissors' and RChoice == 'paper':
        win = "You"
    elif HChoice == 'rock' and RChoice == 'paper':
        win = "Computer"
    elif HChoice == 'paper' and RChoice == 'scissors':
        win = "Computer"
    elif HChoice == 'scissors' and RChoice == 'rock':
        win = "Computer"

    #call score function to refresh score
    ScoreFun()
    #call Game result
    GameResult()

#Main program
main = Tk()
main.title("rock paper scissors")
main.geometry("610x420")
main.resizable(width = False, height = False)
main['bg'] = 'grey'

#Variable
human_point = 0
computer_point = 0
HChoice = ""
RChoice = ""
win = ""
dice = random.randint(1 , 3)
winLabel = Label()
RChoice_label = Label()
HChoice_label = Label()

#Image of rock ...
rockIcon = PhotoImage(file = "./Icon/rock.png")
paperIcon = PhotoImage(file = "./Icon/paper.png")
scissorsIcon = PhotoImage(file = "./Icon/scissors.png")

#score lable
human_score = Label(main , font = 'arial' , text = "Your Score : 0")
human_score.pack()
human_score.place(x = 0 , y = 0)
human_score['bg'] = 'white'
computer_score = Label(main , font = 'arial' , text = "Computer Score : 0")
computer_score.pack()
computer_score.place(x = 490 , y = 0)
computer_score['bg'] = 'white'


#rock paper scissors Lable for robot (hided)
rockL = Label(main , image = rockIcon , width = 180 )
rockL.pack()
rockL.place(x = 210 , y = 500)
rockL['bg'] = '#E3E3FF'

paperL = Label(main , image = paperIcon , width = 180 )
paperL.pack()
paperL.place(x = 210 , y = 500)
paperL['bg'] = '#E3E3FF'

scissorsL = Label(main , image = scissorsIcon , width = 180)
scissorsL.pack()
scissorsL.place(x = 210 , y = 500)
scissorsL['bg'] = '#E3E3FF'

#rock paper scissors Lable for human
rockLH = Label(main , image = rockIcon , width = 180 )
rockLH.pack()
rockLH.place(x = 210 , y = 500)
rockLH['bg'] = '#E3E3FF'

paperLH = Label(main , image = paperIcon , width = 180 )
paperLH.pack()
paperLH.place(x = 210 , y = 500)
paperLH['bg'] = '#E3E3FF'

scissorsLH = Label(main , image = scissorsIcon , width = 180)
scissorsLH.pack()
scissorsLH.place(x = 210 , y = 500)
scissorsLH['bg'] = '#E3E3FF'

# rock paper scissors button
rock = tkinter.Button(main , image = rockIcon , width = 180 , command = lambda choice = "rock" : YourturnFun(choice))
rock.pack()
rock.place(x = 10 , y = 100)
rock['bg'] = '#FFDBDB'

paper = tkinter.Button(main , image = paperIcon , width = 180 , command = lambda choice = "paper" : YourturnFun(choice))
paper.pack()
paper.place(x = 210 , y = 100)
paper['bg'] = '#FFDBDB'

scissors = tkinter.Button(main , image = scissorsIcon , width = 180 , command = lambda choice = "scissors" : YourturnFun(choice))
scissors.pack()
scissors.place(x = 410 , y = 100)
scissors['bg'] = '#FFDBDB'

#GAME loop
main.mainloop()
