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

#create output file
outfile = 'tuition.html'


############ define program functions ############
def main():

    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #240046; background-image: url(wp-tuition.png); color: #ffd60a;">\n')

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


    
def create_output_file():
    global inout, credratei, credrateo, feerate, scholarshipamt, total, actrate
    moneyf = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3"    style="background-color: #47161a; font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2>PVCC</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('Your tuition and fees \n')

    if inout == 1:
        f.write(tr + 'Tuition' + endtd + str(numcredits) + endtd + format(credratei, moneyf) + endtr)
        f.write(tr + 'Institutional fee' + endtd + sp + endtd + format(feerate, moneyf) + endtr)
        f.write(tr + 'Student activity fee' + endtd + sp + endtd + format(actrate, moneyf) + endtr)
        f.write(tr + 'Scholarship amount' + endtd + sp + endtd + format(scholarshipamt, moneyf) + endtr)
        f.write(tr + 'Total' + endtd + sp + endtd + format(total, moneyf) + endtr)
        f.write(colsp + 'Date/Time: ' + day_time + endtr)
        f.write('</table><br />')
    else:
        f.write(tr + 'Tuition' + endtd + str(numcredits) + endtd + format(credratei, moneyf) + endtr)
        f.write(tr + 'Institutional fee' + endtd + sp + endtd + format(feerate, moneyf) + endtr)
        f.write(tr + 'Student activity fee' + endtd + sp + endtd + format(actrate, moneyf) + endtr)
        f.write(tr + 'Student capital fee' + endtd + sp + endtd + format(caprate, moneyf) +endtr)
        f.write(tr + 'Scholarship amount' + endtd + sp + endtd + format(scholarshipamt, moneyf) + endtr)
        f.write(tr + 'Total' + endtd + sp + endtd + format(total, moneyf) + endtr)
        f.write(colsp + 'Date/Time: ' + day_time + endtr)
        f.write('</table><br />')
        

########## call on main program to execute ##########
main()
