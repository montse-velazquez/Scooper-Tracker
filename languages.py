import os


flavours={"pistacho": 0, "cookies and cream": 0, "chocolate": 0, "vanilla": 0, "strawberry": 0, "dulce de leche": 0, "chocalte chip": 0, "chocolate mint": 0, "mango": 0, "coffee": 0}
specials={"unicorny": 0, "extra chocolate": 0}

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
    
    
    
def get_user_choice():
    # Let users know what they can do.
    return input("\nWhat would you like to do? \n[1]See flavours \n[2]Order now \n[q]Quit \n")
    
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
    bill = input("Would you like to get your bill? [y/n]") #Ask user if they will want to get the bill 
    if bill == 'y':
        make_bill(num_scoops)
    elif bill == 'n':
        print("Thank you for preference! ")
    else:
        print("Sorry i could get your answer")

#Creates the bill of the user and goes back to the menu
def make_bill(scoops):
    if scoops == 1:
        print("Your bill is: $5")
    else:
        print("Your bill is: $7")
        
                        
def make_order():
    print("\n\t[1] One Scoop\n \t[2] Two Scoop\n ")
    scoops = int(input("How many scoops? "))
    if scoops < 3: 
        make_flavour(scoops)
        return scoops ###
    else: 
        print("Invalid number of scoops\n")
        make_order()
         
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
    elif choice == 'q':
        print("\nThank you for your order. See you soon!.")
    else:
        print("\nI didn't understand that choice.\n")