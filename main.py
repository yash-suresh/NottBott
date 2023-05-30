## This is the starting point for NottBot. ##

from QA import *
from nameWeatherCheck import *
from weather import *
from smallTalk import *
from datetime import datetime


def ReturnTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

isRunning = True
#The loops keeps the chatbot listening to user input until it is changed to false 




print("\nWelcome to the University of Nottingham!")
username = input("My name is NottBot, what's your name?\n")

print("Hi " + username + ", what can i help you with today?\n")


while(isRunning):
#the loop keeps running until 'bye' is input
    
    userInput = input("\n>>" + username + ": ")
    if userInput == "bye" or userInput == "quit":
        isRunning = False

    
    else:
        if(IsNameChange(userInput)):
            username = input("\n>>Nottbot: What would you like me to call you instead?\n")
            print("Hi " + username + ", what can i help you with today?\n")

            
        elif(IsWeather(userInput)):
            print("\n>>NottBot: " + ReturnWeather() + ". Local time: " + ReturnTime())


        elif(IsSmallTalk(userInput)):
            print("\n>>NottBot: "+ returnSmallTalk(userInput))
        
        else:
            answer = answerQuestion(userInput)
            print("\n>>NottBot: " + answer)
    
    
print("\n\nHope to see you on our sprawling green campus soon, " + username + " !\nTake Care..\n\n")