import os
from datetime import date   
from statistics import mean
from math import isnan
from itertools import filterfalse
from Mathematics import Mathematics
flavours={"pistacho": 0, "cookies and cream": 0, "chocolate": 0, "vanilla": 0, "strawberry": 0, "dulce de leche": 0, "chocalte chip": 0, "chocolate mint": 0, "mango": 0, "coffee": 0}
specials={}
sales = {}
sold = [0] 

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***       Welcome to Scopper Tracker!      ***")
    print("\t**********************************************")
    print("\t**********************************************")
    print("\t***           Choose your flavour          ***")
    print("\t**********************************************")
    print('\n')
    
    
    
def get_user_choice():
    # Let users know what they can do.
    print("\n[1]See flavours \n[2]Update specials \n[3]Order now \n[4]Sales \n[5] Finish Day \n[6] Flavours Sold \n[7]Save to data base \n[8]Stadistics \n[0]Quit \n")
    return input("\nWhat would you like to do? ")
    
def show_names():
    # Shows the special and regular flavours
    print("\n")
    print("\tUsual flavours: ")
    for flavour in flavours:
        print("\t-", flavour.title())

    print("\n")
    print("\tHere are the specials: ")
    for special in specials:
        print("\t-", special.title())        

#Ask user for how many scoops wants and save the flavour of the user
def make_flavour(num_scoops):
    scoop_flavour = [input("Which flavour? ")]
    for flavour in scoop_flavour:
        if flavour in flavours: 
            flavours[flavour] += num_scoops
        elif flavour in specials:
            specials[flavour] += num_scoops
        else: 
            print("Invalid flavour, we dont have this flavour in store, choose another one!")
            make_flavour() 
    bill = input("Would you like to get your bill? [y]") #Ask user if they will want to get the bill 
    if bill == 'y':
        make_bill(num_scoops)
    else:
        print("Sorry i couldn't get your answer, either way...")
        make_bill(num_scoops)

#Creates the bill of the user and goes back to the menu
sold = [0]
def make_bill(scoops, bill = 0):
    if scoops == 1:
        bill += 5
        print("Your bill is: ", bill)
        sold.append(bill)
    else:
        bill += 7
        print("Your bill is: ", bill)
        sold.append(bill)
    
    
        
 #May add a try/except in case user types flavour                       
def make_order():
    print("\n\t[1] One Scoop\n \t[2] Two Scoop\n ")
    try: 
        scoops = int(input("How many scoops? "))
        if scoops < 3 and scoops != 0: 
            make_flavour(scoops)
            return scoops ###
        else: 
            print("Invalid number of scoops\n")
            make_order()
    except:
        print("You need to input a number like [1] or [2] ")
        make_order()

def set_date():
    print("Set the day that you just finish! ")
    try:
        year = int(input("Set year: "))
        month = int(input("Set month: "))
        day = int(input("Set day: "))
     
        key_date = date(year, month, day)
        return key_date

    except ValueError:
        print("Double check you are typing down on the correct order the date")
        set_date()
    except:
        print("Double check you are typing down on the correct order the date")
        set_date()
    
    

def printing_flavours(flav):
    for flavs in flav:
        print(flavs.capitalize(), "sold -",flav[flavs], "Scoops")

#Add file, for having records of the sales and scoops sold


def Upload_file(add_list, which_is):
    os.system('clear')
    f.write("\n")
    f.write(which_is)
    f.write("\n\n")
    for flavs in add_list:
        f.write(flavs)
        f.write(" scoops sold: ")
        f.write(str(add_list[flavs]))
        f.write("\n")

def check_sells(list):
    x = 0
    for flavs in list:
        if list[flavs] == 0:
            x += 1 
    return x  

def update_flavours():
    name = input("What's is the name of today's special flavour? \n").lower()
    specials[name] = 0 
    user = input("Are you adding any other flavour? [y/n]")
    if user == 'y':
        update_flavours()
    elif user =='n':
        print("This is your new list of special flavours",)
        for special in specials:
            print("-", special.title())
    else:
        print("Sorry i could undertand your answer")
### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
names = []

choice = ''
display_title_bar()
while choice != '0':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        show_names()
    elif choice == '2':
        update_flavours()
    elif choice == '3':
        show_names()
        make_order()
    elif choice == '4':
        print("Sales so far: ", sum(sold))
    elif choice == '5':
        print("The sales of: ", set_date(),"were", sales)
    elif choice == '6':
        printing_flavours(flavours)
        print("\n")
        printing_flavours(specials)
    elif choice == '7':
        f = open("scooper.txt", "a")
        f.write(str(set_date()))
        Upload_file(flavours, "Classic flavours")
        Upload_file(specials, "Special Flavours")
        f.write("It was sold: ")
        f.write(sales)
        f.write("\n")
        f.close() 
        
    elif choice == '8':
        if (check_sells(flavours) == len(flavours)) and (check_sells(specials) == len(specials)):
            print("We havens sold any flavours yet! Try again later")
        else: 
            sort_1 = Mathematics(flavours, "Classic flavours")
            sort_2 = Mathematics(specials, "Special flavours")
            sort_1.sort_list()
            sort_1.get_media()
            sort_1.get_less_favorite()
            print('\n')
            sort_2.sort_list()
            sort_2.get_media()
            sort_2.get_less_favorite()
    elif choice == '9':
        f = open("myfile.txt", "r")
        print(f.read())

    elif choice == '0':
        print("\nThank you for your order. See you soon!.")
    else:
        print("\nI didn't understand that choice.\n")