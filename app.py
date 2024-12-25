import pandas as pd
from enum import Enum
import statistics
df = pd.read_csv('diamonds.csv')

class Options(Enum):

    MOST_EXPENSIVE = 1
    AVARAGE_PRICE = 2
    IDEAL = 3
    COLORS = 4
    MEDIAN_PREMIUM = 5
    AVARAGE_PER_CUT = 6
    AVARAGE_PER_COLOR = 7

def printMenu():
    for option in Options:
        print(f"{option.value} - {option.name}")

def mostExpensive():
    mostExpensiveDiamond = list(df['price'])
    mostExpensiveDiamond = max(mostExpensiveDiamond)
    print(f"Most expensive diamonds is worth: {mostExpensiveDiamond}$")

def avaragePrice():
    avarage = df["price"].mean()
    print(f"The avarage price of aa diamond is: {avarage:.2f}$")

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
    print(filteredCaratForPremium)

def avaragePerCut():
    cuts = list(df['cut'].unique())
    for index,cut in enumerate(cuts):
        print(f"{index}: {cut}")
    cut_selection = input("select a cut to find avarage for (by name): ")
    
    avarageForCut = df[df['cut']== cut_selection]['carat'].mean()
    print(f"The avarage carat for {cut_selection} is {avarageForCut :.2f}")
    
def avaragePerColor():
    colors = list(df['color'].unique())
    for index,color in enumerate(colors):
        print(f"{index}: {color}")
    color_selection = input("select a cut to find avarage for (by name): ")

    avarageForColor = df[df['color']== color_selection]['price'].mean()
    print(f"The avarage price for  color: '{color_selection}' is {avarageForColor :.2f}")
    

if __name__ == "__main__":

    printMenu()
    user_selection = input("Select an option (by index): ")

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

    else:
        print("invalid option!")