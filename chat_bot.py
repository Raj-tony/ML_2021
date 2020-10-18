"""
Specifations of the chat bot:
1.This bot will start with a greet and introduce itself and the asks the user name for greeting.
2.This bot will suggest a user to select a laptop model according their basic choice of preference.
3.The bot will ask the user for their choice to suggest them the appropriate model.
4.It will respond to user input appropriatly to suggest the best model.

"""

import random

def introduction():
    responses = [
        "Hello I am a technical friendly bot and will help you to select a laptop model based on your preference.",
        "Welcome!!!!, I am bot.I will help you to choose your laptop ma\odel based on your preference."
    ]
    print(random.choice(responses))


def interaction(name):
    messages = [
        "Thank you. Pleasure to meet you.",
        "Lets have nice time together."
    ]
    print(random.choice(messages))
    print("_______________________________________________________________________")


def bot_features():
    print("--->This bot will suggest a user to select a laptop model according their basic choice of preference.")
    print("--->The bot will ask the user for their choice to suggest them the appropriate model.")
    print("--->It will respond to user input appropriatly to suggest the best model.")
    print("________________________________________________________________________")


def laptop_model():
    ram = int(input("Enter your RAM requirement 4GB or 8GB : "))
    storage = int(input("Enter stroage type HDD means 1 or SSD means 2: "))
    
    if ram == 4 and storage == 1:
        print("Available laptop model with that specification is Dell Inspiron 15 3000 Series .")
        print("________________________________________________________________________")

    elif ram == 4 and storage == 2:
        print("Available laptop model with that specification is Lenovo Ideapad L340.")
        print("________________________________________________________________________")

    elif ram == 8 and storage == 1:
        print("Available laptop model with that specification is Acer nitro 5.")
        print("________________________________________________________________________")

    elif ram == 8 and storage == 2:
        print("Available laptop model with that specification is Acer Aspire 7.")
        print("________________________________________________________________________")
    else:
        print("Please enter the valid input.")
        print("________________________________________________________________________")
    


def show_menu():
    print("Please select choice from the below.")
    print("1.Know about me and my features(bot).")
    print("2.Know your laptop models available based on your prefrences.")
    print("3.End the chat if your got the model of your laptop.")
    print("________________________________________________________")
    try:
        return int(input("Enter your choice from [1-3]."))
    except:
        print("Enter choice only from 1,2,3.")
        return 0




def bot():
    introduction()
    name=input("May i know your name please : ")
    interaction(name)
    response = show_menu()
    while response != 3:
        if response == 1:
            bot_features()
        elif response == 2:           
            laptop_model()
        else:
            print("I don't understand that.Please enter a valid input from the given choice.")
        response = show_menu()
        
bot()
