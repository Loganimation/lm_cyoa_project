#NOTE This is my second run through of the project. I decided to delete the first run through for a multitude of reasons

## VARIABLES
danger = 0
visits = 0
keys = 0
valid_keys = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # i used ai to type all the letters for me because im not wasting my time pressing all those keys
## FUNCTIONS ##
import time
import random
def t1():
    time.sleep(.5)
def t2():
    time.sleep(1)
def t3():
    time.sleep(2)
def t4():
    time.sleep(3)
## STORY FUNCTIONS ##
def stupid_ending():
    print("Your pure and utter stupidity at a single choice option was enough to kill you")
    t3()
    print()
    print("ENDING #4:")
    t2()
    print("Apitimy of Stupidity")
    print()
def bro():
    print("...")
    t4()
    print("We need to talk")
    t3()
    print("The game hasn't even started yet")
    t2()
    print("And you thought it would be funny or something to pick a non-listed item")
    t3()
    print("People like YOU get there own ending")
    t3()
    print()
    print("YOUR SPECIAL ENDING:")
    t2()
    print("Manual breathing and blinking")
    print()

def pregnantminigame():
    global keys
    global valid_keys
    print('BEFORE YOU BEGIN THE MINIGAME PLEASE TURN ON CAPS LOCK')
    t4()
    while keys < 10:
        selected_key = random.choice(valid_keys)
        user_key = input(('PUSH'+' '+selected_key+'!     '))
        if user_key == selected_key:
            keys += 1
            t1()
    t2()
    print("After all the pain of childbirth, it finally happened...")
    t3()
    print("You gave birth")
    t2()
    if danger == 0:
        gong = random.randint(1,2)
        if gong == 1:
            print("Doctor Nathan Wingrad exclaims, 'ITS A BOY!'")
        if gong == 2:
            print("Doctor Nathan Wingrad exclaims, 'ITS A GIRL!'")
        t2()
        print("You played by the rules and was given the gift of life or something")
        t2()
        print("Have fun raising your kid or whatever")
        t3()
        print()
        print("Ending 1:")
        t2()
        print("The Intentional Way to Play the Game Ending or Something Like That")
    elif danger >= 1:
        if danger >= 10:
            print("Doctor Nathan Wingard exclaims, 'OH MY GOD ITS A DEMON!'")
            t2()
            print("What the phonk did you do for this to happen")
            t3()
            print("Then it comes back to you...")
            t4()
            print("The Caffine Calamity...")
            t4()
            print("The Hellfire Hangover...")
            t4()
            print("You had created the recipe for disaster unknowingly")
            t3()
            print("The 'baby' turns its head 180 degrees to stare into your soul")
            t3()
            print("Then the ground opens up below you to suck you in to the deepest layers of hell")
            t3()
            print("In the end fate never turns up in your favor...")
            t3()
            print()
            print("Ending 3:")
            t2()
            print("Sacrifice")
            print()
        else:
            print("Doctor Nathan Wingard exclaims, 'OH MY GOD ITS DEAD!'")
            t2()
            print("Your poor descision making led to the death of your child")
            t2()
            print("Now you have to spend the rest of your life knowing that the death of your child is on your hands")
            t3()
            print()
            print("Ending 2:")
            t2()
            print("Bad Parenting")
            print()
def BIRTH():
    print("Right as you set off to go, you feel something wet")
    t2()
    print("Your water broke")
    t2()
    print("Luckily a nearby doctor noticed, his name... DOCTOR NATHAN WINGARD")
    t3()
    print("He tells you in a calming tone, 'You are gonna have to push. And when I say push, I mean push some keycaps!")
    t4()
    pregnantminigame()

def groc():
    global danger
    global visits
    visits += 1
    if visits > 3:
        BIRTH()
    else:
        print("Grocery store isn't programmed yet, sorry :(")
        path()

def coff():
    global danger
    global visits
    visits += 1
    if visits > 3:
        if visits >= 5:
            BIRTH()
    else:
        t2()
        print("You go to the coffee shop")
        t2()
        print("You walk up to register so you can like... get coffee")
        t2()
        print("The lady at the register lasily asks what you would like to order")
        t3()
        print("What would you like to order?")
        t1()
        print("1 to DECAF")
        t1()
        print("2 to Latte")
        t1()
        print("3 to Cappuccino")
        t1()
        print("4 to Macchiato")
        t1()
        print("5 to Espresso")
        t1()
        print("6 to The Caffine Calamity")
        t1()
        print("7 to Actually I don't want coffee")
        ctype = input()
        if ctype == "1":
            danger += 0
            print("This is the worst thing you have ever drank in your whole life")
            t2()
            print("You feel ashamed that you bought something so abhorent")
            t2()
            print("You leave the coffee shop, disappointed")
            t2()
            path()
        elif ctype in ["2","3","4","5"]:
            danger += 1
            print("The warmth of the coffee soothes you")
            t2()
            print("You transcend all your worries and pain")
            t2()
            print("But as you finish your coffee all the bores of the real world circle around you once more")
            t3()
            print("You exit the coffee shop, satisified")
            t2()
            path()
        elif ctype == "6":
            danger += 5
            print("The pure amount of caffine you've consumed is nausuating, and to any normal person... fatal")
            t3()
            print("Luckily you aren't normal and fate had other plans for you")
            t2()
            print("By some miracle, you leave the coffee shop")
            t2()
            path()
        elif ctype == "7":
            danger += 0
            print("You came all this way just to not buy anything")
            t2()
            print("You leave the coffee shop, disappointed")
            t2()
            path()
        else:
            stupid_ending()

def wine():
    global danger
    global visits
    visits += 1
    if visits > 3:
        BIRTH()
    else:
        t2()
        print("You go to the winery")
        t2()
        print("You walk up to register so you can like... get alchohol")
        t2()
        print("The lady at the register lasily asks what you would like to order")
        t3()
        print("What would you like to order?")
        t1()
        print("1 to Wine")
        t1()
        print("2 to Beer")
        t1()
        print("3 to Vodka")
        t1()
        print("4 to Whiskey")
        t1()
        print("5 to Rum")
        t1()
        print("6 to Tequila")
        t1()
        print("7 to Gin")
        t1()
        print("8 to Brandy")
        t1()
        print("9 to Hellfire Hangover")
        t1()
        print("0 to Actually I don't want aclhohol")
        atype = input()
    if atype in [1,2]:
        danger += 1
        t2()
        path()
    elif atype in [3,4,5,6,7,8]:
        danger += 2
        t2()
        path()
    elif atype == 9:
        danger += 5
        t2()
        path()
    elif atype == 0:
        danger +=0
        t2()
        path()

def home():
    global danger
    global visits
    visits += 1
    if visits > 2 and random.choice([1,2]) == 1:
        BIRTH()
    else:
        print("Home isn't programmed yet, sorry :(")
        path()

def path():
    print("Where would you like to go?")
    t1()
    print("1 to Grocery Store")
    t1()
    print("2 to Coffee Shop")
    t1()
    print("3 to Winery")
    t1()
    print("4 to Home")
    move = input()
    if move == "1":
        groc()
    elif move == "2":
        coff()
    elif move == "3":
        wine()
    elif move == "4":
        home()
    else:
        stupid_ending()

## Start ##
print()
t1()
print("Pregnancy Adventures [ALPHA TESTING]")
t2()
print("Created by Loganimation / Logan Myers")
print()
t2()
print("Type:")
t1()
print("1 to Start")
t1()
print("2 to Quit")
start = (input())
if start == "1":
    t2()
    print("It's been eight months since you got pregnant...")
    t2()
    print("And the baby could pop out at any time!")
    t2()
    print("Just don't be stupid or bad things will happen")
    t2()
    path()
elif start == "2":
    print("dawg what was the point of running the script if you are just gonna quit")
    t2()
    print("You don't get to quit now it's too late")
    t2()
    print("You don't even get the dignity of an introduction")
    t2()
    path()
elif start == 'pmini': #debug
    da = input("danger amount?")
    danger = int(da)
    BIRTH()
else:
    bro()
t4()
print("FINAL DANGER SCORE:", danger)
print()