import os
from datetime import date
from statistics import mean
from math import isnan
from itertools import filterfalse


flavours={"pistacho": 0, "cookies and cream": 0, "chocolate": 0, "vanilla": 0, "strawberry": 0, "dulce de leche": 0, "chocalte chip": 0, "chocolate mint": 0, "mango": 0, "coffee": 0}
specials={"unicorny": 0, "extra chocolate": 0}
sales = {}
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
    print("\n[1]See flavours \n[2]Order now \n[3]Sales \n[4] Finish Day \n[5] Flavours Sold \n[6]Check files \n[7]Stadistics \n[q]Quit \n")
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
        if scoops < 3: 
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
    year = int(input("Set year: "))
    month = int(input("Set month: "))
    day = int(input("Set day: "))
    set_keyDate = date(year, month, day)
    return set_keyDate

def printing_flavours(flav):
    for flavs in flav:
        print(flavs.capitalize(), "sold -",flav[flavs], "Scoops")

# Add file, for having records of the sales and scoops sold
# f = open("myfile.txt", "a")

# def Upload_file(add_list, which_is):
#     os.system('clear')
#     f.write("\n")
#     f.write(which_is)
#     f.write("\n\n")
#     for flavs in add_list:
#         f.write(flavs)
#         f.write(" scoops sold: ")
#         f.write(str(add_list[flavs]))
#         f.write("\n")

#Class where it will be stored with fucntions about stadistics, such as the trend, flavors most time scooped and others.
class Mathematics: 
    def __init__(self, listes, name):
        self.listes = listes
        self.name = name
    
    def sort_list(self):
        sort_lists = []
        for flavs in self.listes:
            sort_lists.append(self.listes[flavs])
        sort_lists = sorted(sort_lists)
        key_list = list(self.listes.keys())
        val_list = list(self.listes.values())
 
        position = val_list.index(sort_lists[-1])
        
        print("The flavour with bigger selling today was", key_list[position].capitalize(), "by selling: ", sort_lists[-1], "Scoops")
        return sort_lists

    def get_media(self):
        average = (float(mean(list(self.listes.values()))))
        sum_up = sum(list(self.listes.values())) 
        return print("From ", sum_up, "scoops sold of the", self.name, ",at least", average, "of the scoops were of this same flavour"   )

    def get_less_favorite(self):
        for i in self.listes:
            if self.listes[i] == 0:
                self.listes[i] = float('NaN')
            else: 
                pass
        print(sum(map(isnan, list(self.listes.values()))), '/', len(self.listes), "flavours in", self.name, "didnt sold any scoop at all")


        clean = list(filterfalse(isnan, list(self.listes.values())))
        key_list = list(self.listes.keys())
        val_list = list(self.listes.values())
        print("The next flavours were the only ones that made sales today")
        for i in clean: 
            position = val_list.index(i)
            print("- ", key_list[position].capitalize()) 

def check_sells(list):
    x = 0
    for flavs in list:
        if list[flavs] == 0:
            x += 1 
    return x        
### MAIN PROGRAM ###

# Set up a loop where users can choose what they'd like to do.
names = []

choice = ''
display_title_bar()
while choice != 'q':    
    
    choice = get_user_choice()
    
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        show_names()
    elif choice == '2':
        make_order()
    elif choice == '3':
        print("Sales so far: ", sum(sold))
    elif choice == '4':
        sales[set_date()] = sum(sold)
        print(sales)
    elif choice == '5':
        printing_flavours(flavours)
        print("\n")
        printing_flavours(specials)
    elif choice == '6':
        pass
        # f = open("myfile.txt", "a")
        # f.write(str(set_date()))
        # Upload_file(flavours, "Classic flavours")
        # Upload_file(specials, "Special Flavours")
    elif choice == '7':
        if (check_sells(flavours) == 10) or (check_sells(specials) == 2):
            print("We havens sold any Classic flavour yet! Try again later")
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

    elif choice == 'q':
        print("\nThank you for your order. See you soon!.")
    else:
        print("\nI didn't understand that choice.\n")