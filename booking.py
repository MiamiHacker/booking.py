#!/usr/bin/env python3

'''
booking.py - coded by MiamiHacker version 0.1
'''

from ast import Continue, Global
from sqlalchemy import true
import colorama
from colorama import Fore
import os
import sys

# Booking options
accommodation = "hotel, appartment, tent"
options ="breakfast, bedsheets, both"

# Booleans
option_order_both = bool
option_order_bedsheets = bool
option_order_breakfast = bool

# pricing => don't change the 0 unless you know what you're doing ;)
price = 0
brk_opt_sum = 18
bed_opt_sum = 20
both_opt_sum = 0
hotel_price = 120
appartment_price = 100
tent_price = 40
taxRate = 7
opt_sum = 0

#Input for the accommodation
print(Fore.MAGENTA + "-############- booking.py by MiamiHacker -############-")
accommodation_order = input(Fore.RESET + "What kind of accommodation you want to book?\n" 
"This is possible to book: " + accommodation + "\n")


print("LOG: accomodation output", accommodation_order)

#Accomodations 
def my_accommodation():
    #Set price to global
    global price
    if accommodation_order == "hotel":
        price = hotel_price
    elif accommodation_order == "appartment":
        price = appartment_price
    elif accommodation_order == "tent":
        price = tent_price
    else:
        print(Fore.YELLOW + "[WRN]" + " Accommodation is NOT on the list!" + Fore.RESET)
        price = 0
        def my_error():
            while True:
                while True:
                    answer = str(input(Fore.CYAN + 'Run again? (y/n): '))
                    if answer in ('y', 'n'):
                        break
                    print("invalid input.")
                if answer == 'y':
                    os.execl(sys.executable, sys.executable, *sys.argv)
                    continue
                else:
                    print("Thanks for testing!!")
                    break
        my_error()
my_accommodation()


#How many days is the reservation
quantity = (int)(input("How many days you want to book?\n"))
quantity = quantity - 1 # 2 days is 1 night to stay
#acc_sum is total the price of the accomodation 
acc_sum = price * quantity
print("Accommodation price for", quantity, "nights is $" , acc_sum)

#Input for the options
option_order = input("What kind of options you want to book?\n" 
"This is possible to book: " + options + "\n")

#Function with the 3 input options 
'''TODO: Use also none in future updates'''
def my_options():
    if option_order == "breakfast":
        brk_opt_sum = 18
        option_price = brk_opt_sum
        global option_order_breakfast
        option_order_breakfast = True
        brk_opt_sum = option_price
    elif option_order == "bedsheets":
        option_price = 20 # price not in days 
        global option_order_bedsheets
        option_order_bedsheets = True
        global bed_opt_sum
        bed_opt_sum = option_price
    elif option_order == "both":
        option_price = 18
        global option_order_both
        option_order_both = True
        global both_opt_sum
        both_opt_sum = option_price
    else:
        print(Fore.YELLOW + "[WRN]" + " We don't have that option on the list!" + Fore.RESET)
        option_price = 0
my_options()


#Functions for my breakfast 
def my_breakfast():
    global opt_sum
    if option_order_breakfast != True and option_order_both == True:
        brk_opt_sum = 0
    elif option_order_breakfast == True:
        brk_opt_sum = 18
        print("Breakfast for", quantity, "days is $", brk_opt_sum * quantity)
        opt_sum = brk_opt_sum * quantity
    elif option_order_breakfast != True and option_order_both == True:
        brk_opt_sum = brk_opt_sum
        global both_opt_sum
        both_opt_sum = (brk_opt_sum * quantity) + bed_opt_sum
    elif option_order_breakfast != True and option_order_both != True:
        brk_opt_sum = 0
        both_opt_sum = (brk_opt_sum * quantity) + bed_opt_sum
my_breakfast()

#Function for Bedsheets
def my_bedsheets():
    global bed_opt_sum
    bed_opt_sum = 20
    if option_order_bedsheets != True:
        bed_opt_sum = 0
    elif option_order_bedsheets == True and accommodation_order != ("hotel"):
        print("@@@Bedsheets for $", bed_opt_sum)
        global opt_sum
        opt_sum = bed_opt_sum
        print("Local:", opt_sum)
    elif option_order_bedsheets == True and accommodation_order == ("hotel"):
        bed_opt_sum = 0
        print("Bedsheets are for free")
my_bedsheets()

#Function for Both (Breakfast & Bedsheets)
def my_bothOption():
    global opt_sum
    if option_order_both == True and accommodation_order != ("hotel"):
        brk_opt_sum = 18
        bed_opt_sum = 20
        opt_sum = (brk_opt_sum * quantity) + bed_opt_sum
        print(">>>Bedsheets $", bed_opt_sum)
        print("Breakfast for", quantity, "days is $", brk_opt_sum * quantity)
    elif option_order_both == True and accommodation_order == ("hotel"):
        brk_opt_sum = 18
        opt_sum = (brk_opt_sum * quantity)
        print("Breakfast for", quantity, "days is $", opt_sum)
        print("Bedsheets are for free!")
my_bothOption()

price_exVat = acc_sum + opt_sum
print("Total price ex Vat $", price_exVat)
price_inVat = price_exVat * (100 + taxRate) / 100
print(Fore.GREEN + "Total price in Vat $", price_inVat)

def my_restart():
    while True:
        while True:
            answer = str(input(Fore.CYAN + 'Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            os.execl(sys.executable, sys.executable, *sys.argv)
            continue
        else:
            print("Thanks for testing!!")
            break
my_restart()

'''BUG Testing (V is passed)
Hotel Both = V
Hotel Breakfast = V
Hotel Bedsheets = V
Appartment Both = V
Appartment Breakfast = V 
Appartment Bedsheets = V
Tent Both = V
Tent Breakfast = V
Tent Bedsheets = V
'''
