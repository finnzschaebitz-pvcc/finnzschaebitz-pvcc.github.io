# Name: Finn Zschaebitz
# Program Purpose: This program uses lists to find the personal property tax for vehicles in Charlottesville
# and produces a report which displays all data and the total tax due
#
# Personal property tax in Charlottesville
#       -- $4.20 per $100 of vehicle value (4.20% per year)
#       -- Paid every six months
# Personal Property Tax Relief (PPTR):
#       -- Eligibility: Owned or leased vehicles which are predominantly used for non-business purpose & have passenger license plates
#       -- Tax relief for qualified vehicles is 33%

import datetime

################ define tax rates ################
PPT_RATE = .042
RELIEF_RATE = .33

###################### define global variables ######################

tax_due = 0
tax_due_r = 0
total = 0


######################     define program functions     ######################

def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate the property tax for another vehicle? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False

def get_user_data():
    global vehicle_value, pptr_eligible

    vehicle_value = int(input("What is the value of your vehicle?: "))
    pptr_eligible = input("\nIs your vehicle eligible for Personal Property Tax Relief (Y or N)?: ")



def perform_calculations():
    global tax_due, vehicle_value, PPT_RATE, pptr_eligible, tax_due_r, total

    tax_due = (vehicle_value * PPT_RATE) / 2

    if pptr_eligible.upper() == "Y" or pptr_eligible == "y":
        tax_due_r = tax_due * .67
    else:
        tax_due_r = 0

    total = tax_due - tax_due_r

def display_results():
    global vehicle_value, tax_due, tax_due_r, total
    moneyf = '8,.2f'
    line = ("------------------------------------------------------------------------")
    tab = "\t"

    print (line)
    print ("***************** PERSONAL PROPERTY TAX REPORT *****************")
    print ("                   Charlottesville, Virginia")

    print ("\n\t\tRUN DATE/TIME: " + str(datetime.datetime.now()))
    print ("\n Assessed value of vehicle: " + tab + format(vehicle_value, moneyf))
    print ("\n Full annual amount owed: " + tab + format(tax_due, moneyf))
    print ("\n Relief amount: " + tab + tab + format(tax_due_r, moneyf))
    print ("----------------------------------------")
    print (" Total due: " + tab + tab + tab + format(total, moneyf))

main()
