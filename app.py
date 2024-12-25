import pandas as pd
from enum import Enum
import os
import platform

df = pd.read_csv('diamonds.csv')

class Options(Enum):

    MOST_EXPENSIVE = 1
    AVARAGE_PRICE = 2
    IDEAL = 3
    COLORS = 4
    MEDIAN_PREMIUM = 5
    AVARAGE_PER_CUT = 6
    AVARAGE_PER_COLOR = 7
    EXIT = 8

def printMenu():
    print("------------------------------")
    print("MENU")
    for option in Options:
        print(f"{option.value} - {option.name}")

def mostExpensive():
    mostExpensiveDiamond = list(df['price'])
    mostExpensiveDiamond = max(mostExpensiveDiamond)
    print(f"Most expensive diamonds is worth: {mostExpensiveDiamond}$")

def avaragePrice():
    avarage = df["price"].mean()
    print(f"The avarage price of a diamond is: {avarage:.2f}$")

def idealCount():
    count = 0
    cuts = list(df['cut'])
    for cut in cuts:
        if cut == "Ideal":
            count += 1

    print(f"Found {count} Ideals!")

def countColors():
    colors = list(df['color'].unique())
    print(f"There are {len(colors)} colors:")

    for index, color in enumerate(colors):
        print(f"{index+1}: '{color}'")

def medianPremium():
    filteredCaratForPremium = df[df['cut']=='Premium']['carat'].median()
    print(f"The Median carat for Premium cut is: {filteredCaratForPremium} carat")

def avaragePerCut():
    cuts = list(df['cut'].unique())
    for index,cut in enumerate(cuts):
        print(f"{index}: '{cut}'")
    try:
        cut_selection = input("Select a cut to find avarage carat for (by name): ").title()
        if cut_selection.isdigit() == False:
            
            if cut_selection == "":
                print("Please give me something to work with...")
            
            elif cut_selection not in cuts:
                print(f"Couldn't find a cut by the name of: {cut_selection}")
            
            else:
                avarageForCut = df[df['cut']== cut_selection]['carat'].mean()
                print(f"The avarage carat for {cut_selection} is {avarageForCut :.2f} carat")
                
        else:
            print("Select by name, not index!")
            

    except ValueError:
        print("Make sure to type in the exact same names for cuts!")
    
def avaragePerColor():
    colors = list(df['color'].unique())
    for color in (colors):
        print(f"color: '{color}'")
    try:
        color_selection = input("select a color to find avarage price for (by name): ").capitalize()

        if color_selection.isdigit() == False:

            if color_selection == "":
                    print("Please give me something to work with...")

            elif color_selection not in colors:
                    print(f"Couldn't find a color by the name of: {color_selection}")

            else:
                avarageForColor = df[df['color']== color_selection]['price'].mean()
                print(f"The avarage price for  color: '{color_selection}' is {avarageForColor :.2f}$")
            
        else:
            print("Select by name, not index!")
    
        

    except ValueError:
        print("Invalid option!")

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
   
    while True:
        try:
            printMenu()
            user_selection = input("Select an option (by index): ")
            clear_terminal()
            if user_selection.isdigit():
                user_selection = Options(int(user_selection))

                if user_selection == Options.MOST_EXPENSIVE:
                    mostExpensive()
                if user_selection == Options.AVARAGE_PRICE:
                    avaragePrice()
                if user_selection == Options.IDEAL:
                    idealCount()
                if user_selection == Options.COLORS:
                    countColors()
                if user_selection == Options.MEDIAN_PREMIUM:
                    medianPremium()
                if user_selection == Options.AVARAGE_PER_CUT:
                    avaragePerCut()
                if user_selection == Options.AVARAGE_PER_COLOR:
                    avaragePerColor()
                if user_selection == Options.AVARAGE_PER_COLOR:
                    exit()
            else:
                print("invalid option!")
        except ValueError:
            print("Out of range!")