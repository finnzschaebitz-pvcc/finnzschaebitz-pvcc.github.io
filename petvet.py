# Name: Finn Zschaebitz
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
#---------------------------------
# Canine Vaccines:
#   1. Bordatella       $30.00
#   2. DAPP             $35.00
#   3. Influenza        $48.00
#   4. Leptospirosis    $21.00
#   5. Lyme Disease     $41.00
#   6. Rabies           $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew, one chew per month)
#   Small dogs, up to 25 lbs: $9.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs: 51 to 100 lbs: $13.99

import datetime

############# define global variables #############
global PR_CHEWS_SMALL, PR_CHEWS_MED, PR_CHEWS_LARGE
# define dog prices
PR_BOARD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEPTO = 21
PR_LYME = 41
PR_RABIES = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

PR_LEUK = 35
PR_RHINO = 30
PR_CALL = 0
PR_CCHEWS = 8
#define global variables

############# define program functions #############
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            perform_dog_calculations()
            display_dog_results()
        else:
            perform_cat_calculations()
            display_cat_results()

            askAgain = input("\nWould you like to process another pet (Y/N)?: ")
            if askAgain.upper() == "N" :
                more = False
                print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet Name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)? ")
    pet_weight = int(input("Weight of your pet (in pounds): "))


def perform_dog_calculations():
    global vax_cost, chews_cost, total, PR_BORD, PR_DAPP, PR_FLU, PR_LEPTO, PR_LYME, PR_RABIES, PR_ALL, PR_CHEWS_SMALL, PR_CHEWS_MED, PR_CHEWS_LARGE, num_chews

    chews_cost = 0
# The rest of your code remains the same

    ##### vaccines

    dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Influenza \n\t6.Lyme Disease \n\t7.Rabies \n\t8.Full Vaccine Package \n\t9.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))


    if pet_vax_type == 1 :
        vax_cost = PR_BORD

    elif pet_vax_type == 2 :
        vax_cost = PR_DAPP

    elif pet_vax_type == 3 :
        vax_cost = PR_FLU

    elif pet_vax_type == 4 :
        vax_cost = PR_LEPTO

    elif pet_vax_type == 5 :
        vax_cost = PR_LYME

    elif pet_vax_type == 6 :
        vax_cost = PR_RABIES

    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU
        vax_cost = .85 * PR_ALL

    ##### heart worm chews
    if num_chews != 0:
        if pet_weight < 25:
            chews_cost = num_chews * PR_CHEWS_SMALL
        elif 26 <= pet_weight < 50:
            chews_cost = num_chews * PR_CHEWS_MED
        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    ##### find total
    total = vax_cost + chews_cost
    print("DOG CALCS")

def display_dog_results():
    moneyf = '8,.2f'
    print('------------------------------')
    print('**** PET CARE MEDS VIRGINIA *****')
    print('Your neighborhood veterinarian')
    print('------------------------------')
    print('Vaccines     $'+format(vax_cost, moneyf))
    print('Chews        $'+format(chews_cost, moneyf))
    print('Total        $'+format(total, moneyf))
    print('------------------------------')
    print(str(datetime.datetime.now()))

############# CAT functions #############

def perform_cat_calculations():
    global vax_cost, chews_cost, total, PR_LEUK, PR_RHINO, PR_CALL, PR_CCHEWS
    chews_cost = 0

    catmenu = "\n** Cat Vaccines \n\t1. Feline Leukemia \n\t2. Feline Viral Rhinotracheitis \n\t3. Rabies \n\t.4 Full \n\t.5 NONE"
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))

    if pet_vax_type == 1 :
        vax_cost = PR_LEUK

    elif pet_vax_type == 2 :
        vax_cost = PR_RHINO

    elif pet_vax_type == 3 :
        vax_cost = PR_RABIES

    else:
        PR_ALL = PR_LEUK + PR_RHINO + PR_RABIES
        vax_cost = .9 * PR_ALL

    ##### heart worm chews
    if num_chews != 0:
            chews_cost = num_chews * PR_CCHEWS
    total = vax_cost + chews_cost    
    
    print("CAT CALCS")

def display_cat_results():
    print("DISPLAY CATS")
    moneyf = '8,.2f'
    print('------------------------------')
    print('**** PET CARE MEDS VIRGINIA *****')
    print('Your neighborhood veterinarian')
    print('------------------------------')
    print('Vaccines     $'+format(vax_cost, moneyf))
    print('Chews        $'+format(chews_cost, moneyf))
    print('Total        $'+format(total, moneyf))
    print('------------------------------')
    print(str(datetime.datetime.now()))
main()
