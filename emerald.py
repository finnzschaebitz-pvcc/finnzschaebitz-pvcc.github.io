# Name: Finn Zschaebitz
# Prog Purpose: To calculate and create a web page sales report for a resort

import datetime

### define global vars ###

cust = []
r_rate = (195,250,350)
tax    = (.065,.1125)

### create output file ###
outfile = 'hotelsalesrep.html'

### def prog functions ###
def main():
    read_in_cust_file()
    open_outfile()
    create_output_file()
    
def read_in_cust_file():
    cust_data = open("emerald.csv", "r")
    cust_in = cust_data.readlines()
    cust_data.close()

    #split the data into fields
    for i in cust_in:
          cust.append(i.split(","))

    print(cust)
def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #83c5be; background-image: url(emerald.png); color: #023047;">\n')


def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]
    g_total = 0

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "7">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #83c5be;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2> <style> h2{text-align: center} </style> Emerald Beach Hotel & Resort</h2>' + endtr)
    f.write(colsp + '\n')
    f.write(colsp + '<h2>Sales Report Date/Time: ' + day_time + '</h2>' + endtr)
    f.write(tr + 'Last' + endtd + 'First' + endtd + 'Num Nights' + endtd + 'Subtotal' + endtd + 'Sales Tax' + endtd + 'Occ. Tax' + endtd + 'Total' + endtr)
    for i in range(len(cust)):
        if cust[i][2] == 'SR':
            subtotal = float(cust[i][3]) * r_rate[0]
        elif cust[i][2] == 'DR':
            subtotal = float(cust[i][3]) * r_rate[1]
        else:
            subtotal = float(cust[i][3]) * r_rate[2]
        s_tax = subtotal * tax[0]
        o_tax = subtotal * tax[1]
        total = subtotal + s_tax + o_tax
        g_total += total
        f.write(tr + cust[i][0] + endtd + cust[i][1] + endtd + cust[i][3] + endtd + str(format(subtotal, currency)) + endtd + str(format(s_tax, currency)) + endtd + str(format(o_tax, currency)) + endtd + str(format(total, currency)) + endtr)
    f.write(colsp + '<h3> <style> h3{text-align: right} </style> Grand Total: ' + str(format(g_total, currency)) + '</h3>' + endtr)
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()

##########  call on main program to execute ############
main()              

    
