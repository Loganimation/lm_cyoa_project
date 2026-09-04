#NOTE If you see danger += 0, it doesn't do anything other than help me visualize
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
def unleashfate():
    global danger
    t2()
    print("You were destined to reach here")
    t2()
    print("It doesnt matter what you do")
    t4()
    print("This is fate...")
    t3()
    print("The innevitable end you have no power to stop")
    t3()
    print("You will never know when it happens until it does")
    t4()
    print("Are you afraid of fate?")
    input()
    t3()
    print()
    print("Secret Ending:")
    t2()
    print("Fate")
    print()
    danger = ""
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
    if danger < 1:
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
        if danger >= 20:
            print("Doctor Nathan Wingard exclaims, 'OH MY GOD ITS A DEMON!'")
            t2()
            print("What the phonk did you do for this to happen")
            t3()
            print("Then it comes back to you...")
            t4()
            print("All the stupid actions you took...")
            t4()
            print("You had created the recipe for disaster unknowingly")
            t3()
            print("The 'baby' turns its head 180 degrees to stare into your soul")
            t3()
            print("Then the ground opens up below you to suck you in to the deepest layers of hell")
            t3()
            print("In the end FATE never turns up in your favor...")
            t3()
            print()
            print("Ending 3:")
            t2()
            print("Rituals")
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
            print("Irresponsible")
            print()
def BIRTH():
    print("Right as you set off to go, you feel something strange")
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
    if visits >= 5:
        BIRTH()
    else:
        print("You enter the grocery store")
        t2()
        print("Most people would find the grocery store boring but you are a pregnant woman so its very enticing")
        t3()
        print("As your eyes glimmer in the awe at the 25% discounts")
        t2()
        print("You accidentally bump into a random lady, causing here to drop and shatter the thing she was holding")
        t3()
        print("The lady screams at you, 'Come fight me you cow!'")
        t2()
        print("What do you do?")
        t1()
        print("1 to Fight")
        t1()
        print("2 to Flight")
        t1()
        print("3 to Apologize")
        ftype = input()
        if ftype == "1":
            danger += 2
            print("You miss your throw and she gets the perfect chance to punch back")
            t2()
            print("She slams her fist into your stomach")
            t2()
            print("The pain is unbearable")
            t2()
            print("You yell out, but the woman has already ran away")
            t2()
            print("You eventually gather up the strength to leave the grocery store")
            t2()
            path()
        if ftype == "2":
            danger += 0
            print("Before she has the chance to react")
            t2()
            print("You dart out of the grocery store and escape")
            t2()
            print("Thank god thats over!")
            t2()
            path()
        if ftype == "3":
            danger += 2
            print("You try to apologize but its as if she didnt even hear it")
            t2()
            print("She slams her fist into your stomach")
            t2()
            print("The pain is unbearable")
            t2()
            print("You yell out, but the woman has already ran away")
            t2()
            print("You eventually gather up the strength to leave the grocery store")
            t2()
            path()
def coff():
    global danger
    global visits
    visits += 1
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
            danger += 10
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
    if visits >= 5:
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
        print("9 to The Hellfire Hangover")
        t1()
        print("0 to Actually I don't want aclhohol")
        atype = input()
        if atype in ["1","2"]:
            danger += 1
            print("The deep tones and colorful notes of the alchohol soothe your nerves")
            t3()
            print("The pregnancy had been causing you so much stress but it all seems to drift away")
            t3()
            print("Every sip is a another steep towards heaven")
            t2()
            print("You exit the winery, satisified")
            t2()
            path()
        elif atype in ["3","4","5","6","7","8"]:
            danger += 2
            print("The flavor is so bitter its almost repulsive")
            t2()
            print("You almost want to spit it out by how disgusting it is")
            t3()
            print("You decide though that you would rather not waste your money")
            t3()
            print("So you breathe in slowly, then chug the rest")
            t2()
            print("You exit the winery, disgusted")
            t2()
            path()
        elif atype == "9":
            danger += 10
            print("The taste is immediate and powerful")
            t2()
            print("It tastes of pure concentrated poison, and to any normal person this would be... fatal")
            t3()
            print("Luckily you aren't normal and fate had other plans for you")
            t2()
            print("By some miracle, you leave the winery")
            t2()
            path()
        elif atype == "0":
            danger += 0
            print("You came all this way just to not buy anything")
            t2()
            print("You leave the winery, disappointed")
            t2()
            path()
        else:
            stupid_ending()

def home():
    global danger
    global visits
    visits += 1
    if visits >= 5:
        BIRTH()
    else:
        print("You go back home")
        t2()
        print("You don't really know what to do right now")
        t2()
        print("Television or a nap right now would be really good")
        t2()
        print("What would like to do?")
        t1()
        print("1 to Nap")
        t1()
        print("2 to Television")
        h1type = input()
        if h1type == "1":
            print("You take a REALLY boring nap")
            t2()
            print("I don't have any words to like describe this its just a nap")
            t2()
            path()
        elif h1type == "2":
            print("What do you want to watch?")
            t1()
            print("1 to Breaking Bad")
            t1()
            print("2 to The Secret Lives of Mormon Wives")
            h2type = input()
            if h2type == "1":
                danger += 0
                print("This might just be the best show you have ever watched in your life")
                t2()
                print("Its just so peak even the baby likes it")
                t2()
                print("You leave the house")
                t2()
                path()
            elif h2type == "2":
                danger += 1
                print("The moment you open up the show, your baby begins kicking so aggressively you have to stop watching")
                t3()
                print("Maybe watching 'The Secret Liveso of Mormon Wives' wasn't your best idea")
                t3()
                print('You leave the house')
                t2()
                path()
            else:
                stupid_ending()
        else:
            stupid_ending()

def path(): #just wanted to point out 2 and 3 are REALLY similar just by the fact they are already in the same industry
    print("Where would you like to go?")
    t1()
    print("1 to Grocery Store")     #not started
    t1()
    print("2 to Coffee Shop")   #done
    t1()
    print("3 to Winery")    #done
    t1()
    print("4 to Home")  #done
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
print("Pregnancy Adventures")
t2()
print("Created by Loganimation / Logan Myers")
print()
t2()
print("Type:")
t1()
print("1 to Start")
t1()
print("2 to Quit")
t1()
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
elif start == 'Fate':
    unleashfate()
else:
    bro()
t4()
print("FINAL DANGER SCORE:", danger)
print()
