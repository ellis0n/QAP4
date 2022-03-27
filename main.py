# Import libraries
import datetime
import time

#REMOVE UNNEEDED FALSE CHECKS

# Prevents empty user inputs or null strings.
def blank(x):  # Accepts any variable
    if x == "":
        return True
    else:
        return False


def allow(x):
    allow = "abcdefghijklmnopqrstuvwxyz01234567890,.- '"
    return set(x.lower()).issubset(allow)


def escape(x):
    if x.upper() == "END":
        quit()


def cur(x):
    return "${:,.2f}".format(x)



# Open default file, read values
d = open("OSICDef.dat", "r")
POLICY_NUM = int(d.readline())
BASIC_PREM = float(d.readline())
ADD_DISC = float(d.readline())
LIAB_COV = float(d.readline())
GLASS_COV = float(d.readline())
LOAN_COV = float(d.readline())
TAX_RATE = float(d.readline())
PROC_FEE = float(d.readline())

# User data inputs
while True:
    print("Customer data entry")
    print("Type 'END' at any time to quit without saving.")
    print("===================")
    while True:
        custFName = input("First Name: ")
        escape(custFName)
        if blank(custFName) == False:
            if allow(custFName) == False:
                print("Input not recognized.")
            else:
                break
    while True:
        custLName = input("Last Name: ")
        escape(custLName)
        if blank(custLName) == False:
            if allow(custLName) == False:
                print("Input not recognized.")
            else:
                break
    while True:
        custAdd = input("Address: ")
        escape(custAdd)
        if blank(custAdd) == False:
            if allow(custAdd) == False:
                print("Input not recognized.")
            else:
                break
    while True:
        custCity = input("City: ")
        escape(custCity)
        if blank(custCity) == False:
            if allow(custCity) == False:
                print("Input not recognized.")
            else:
                break
    while True:
        custProv = input("Provincial alpha code [XX]: ").upper()
        escape(custProv)
        if blank(custProv) == False:
            if len(custProv) != 2:
                print("Input not recognized")
            elif custProv.isalpha() == False:
                print("Input not recognized.")
            else:
                break
    while True:
        custPost = input("Postal code [A0A0A0]: ")
        escape(custPost)
        if blank(custPost) == False:
            if custPost.isalnum() == False:
                print("Input not recognized")
            elif len(custPost) != 6:
                print("Input not recognized")
            else:
                break
    while True:
        custPhone = input("Phone number [10 digits]: ")
        escape(custPhone)
        if blank(custPhone) == False:
            if custPhone.isnumeric() == False:
                print("Input not recognized.")
            elif len(custPhone) != 10:
                print("Input not recognized.")
            else:
                break
    while True:
        numCar = input("Number of cars being insured: ")
        escape(numCar)
        if blank(numCar) == False:
            try:
                numCar = int(numCar)
                if numCar <= 0:
                    print("One or more cars required to continue.")
                else:
                    break
            except:
                print("Input not recognized.")
    while True:
        liabOpt = input("Extra liability up to $1,000,000 [Y or N]: ").upper()
        escape(liabOpt)
        if blank(liabOpt) == False:
            if liabOpt == "Y":
                break
            elif liabOpt == "N":
                break
            else:
                print("Input not recognized.")
    while True:
        glassOpt = input("Optional glass coverage [Y or N]: ").upper()
        escape(glassOpt)
        if blank(glassOpt) == False:
            if glassOpt == "Y":
                break
            elif glassOpt == "N":
                break
            else:
                print("Input not recognized")
    while True:
        loanOpt = input("Optional loan vehicle [Y or N]: ").upper()
        escape(loanOpt)
        if blank(loanOpt) == False:
            if loanOpt == "Y":
                break
            elif loanOpt == "N":
                break
            else:
                print("Input not recognized")
    while True:
        paySched = input("Payment in full or monthly [F or M]: ").upper()
        escape(paySched)
        if blank(paySched) == False:
            if paySched == "M":
                monthCheck = True
                break
            elif paySched == "F":
                monthCheck = False
                break
            else:
                print("Input not recognized.")

    # Processing
    liabCov = 0
    glassCov = 0
    loanCov = 0
    monthPay = 0
    discCar = BASIC_PREM - (BASIC_PREM * ADD_DISC)
    if numCar >= 2:
        custPrem = BASIC_PREM + (discCar * (numCar-1))
    else:
        custPrem = BASIC_PREM
    if liabOpt == "Y":
        liabCov = 130 * numCar
    if glassOpt == "Y":
        glassCov = 86 * numCar
    if loanOpt == "Y":
        loanCov = 58 * numCar
    totExtra = loanCov + glassCov + liabCov
    totPrem = custPrem + totExtra
    totalCost = totPrem + (totPrem * TAX_RATE)
    if monthCheck == True:
        monthPay = (totalCost + PROC_FEE) / 12

    # Write file
    save = input("Type 'END' to quit without saving, or any other key continue.").upper()
    escape(save)
    p = open("Policies.dat", "a")
    p.write("{}, ".format(str(POLICY_NUM)))
    p.write("{}, ".format(str(custFName)))
    p.write("{}, ".format(str(custLName)))
    p.write("{}, ".format(str(custAdd)))
    p.write("{}, ".format(str(custCity)))
    p.write("{}, ".format(str(custPhone)))
    p.write("{}, ".format(str(custProv)))
    p.write("{}, ".format(str(custPost)))
    p.write("{}, ".format(str(custPhone)))
    p.write("{}, ".format(str(numCar)))
    p.write("{}, ".format(str(liabOpt)))
    p.write("{}, ".format(str(glassOpt)))
    p.write("{}, ".format(str(loanOpt)))
    p.write("{}, ".format(str(paySched)))
    p.write("{}\n ".format(str(round(totPrem, 2))))
    print("Processing...")
    time.sleep(1)
    print("Saving...")
    time.sleep(1)
    print()
    print("Policy processed and saved.")

    #Format
    liabCov = cur(liabCov)
    glassCov = cur(glassCov)
    loanCov = cur(loanCov)
    custPrem = cur(custPrem)
    totExtra = cur(totExtra)
    totPrem = cur(totPrem)
    monthPay = cur(monthPay)
    procFee = cur(PROC_FEE)

    print("Generating reciept...")
    time.sleep(1)
    print()
    print()

    # Generate receipt
    print("         1         2         3         4")
    print("1234567890123456789012345678901234567890")
    print("{^40}".format("ONE STOP INSURANCE COMPANY"))
    print("Date: {}            HST#: 222-32-809-322".format("dd-MON-yy")) #FIX THIS
    print("="*40)
    print("Customer Details: ")
    print()
    print("{}{}".format(custFName, custLName))
    print("{}".format(custPhone))
    print("{}".format(custAdd))
    print("{}{}".format(custCity, custProv))
    print("{}".format(custPost))
    print()
    print("Policy Details: ")

    # Open default file, write values
    POLICY_NUM += 1  # Increase policy number
    d = open("OSICDef.dat", "w")
    d.write("{}\n".format(str(POLICY_NUM)))
    d.write("{}\n".format(str(BASIC_PREM)))
    d.write("{}\n".format(str(ADD_DISC)))
    d.write("{}\n".format(str(LIAB_COV)))
    d.write("{}\n".format(str(GLASS_COV)))
    d.write("{}\n".format(str(LOAN_COV)))
    d.write("{}\n".format(str(TAX_RATE)))
    d.write("{}\n".format(str(PROC_FEE)))
