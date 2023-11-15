# Name: Finn Zschaebitz
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates

RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 #1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0


############ define program functions ############
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE, enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global credratei, credrateo, feerate, caprate, total, actrate

    credratei = numcredits * RATE_TUITION_IN
    credrateo = numcredits * RATE_TUITION_OUT
    feerate = numcredits * RATE_INSTITUTION_FEE
    actrate = numcredits * RATE_ACTIVITY_FEE
    caprate = numcredits * RATE_CAPITAL_FEE

    if inout == 1:
        total = credratei + feerate + actrate - scholarshipamt
    else:
        total = credrateo + feerate + actrate + caprate - scholarshipamt


    
def display_results():
    global inout, credratei, credrateo, feerate, scholarshipamt, total, actrate
    print("DISPLAY TUITION")
    moneyf = '8,.2f'

    if inout == 1:
        print('--------------------------------')
        print('       **** PVCC *****')
        print('     Your tuition and fees')
        print('--------------------------------')
        print('Tuition                $' + format(credratei, moneyf))
        print('Institutional fee    + $' + format(feerate, moneyf))
        print('Student activity fee + $' + format(actrate, moneyf))
        print('Scholarship amount   - $' + format(scholarshipamt, moneyf))
        print('--------------------------------')
        print('Total                  $' + format(total, moneyf))
        print('--------------------------------')
        print(str(datetime.datetime.now()))
    else:
        print('--------------------------------')
        print('**** PVCC *****')
        print('Your tuition and fees')
        print('--------------------------------')
        print('Tuition                $' + format(credrateo, moneyf))
        print('Institutional fee    + $' + format(feerate, moneyf))
        print('Student activity fee + $' + format(actrate, moneyf))
        print('Student capital fee  + $' + format(caprate, moneyf))
        print('Scholarship amount   - $' + format(scholarshipamt, moneyf))
        print('--------------------------------')
        print('Total                  $' + format(total, moneyf))
        print('--------------------------------')
        print(str(datetime.datetime.now()))
########## call on main program to execute ##########
main()
