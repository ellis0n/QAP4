# This program was written for Intro to Python - QAP 4 with Mo Baubin
# It was written by Glen May between late February and early March 2022.

# This program will allow the user to select one of four options from a menu. Each option calls on a function to run.
# These functions serve various purposes for the ONE STOP INSURANCE COMPANY.
# The user can input new policies and generate both detailed and exception reports based on those policies.

# Import universal libraries
import datetime
from datetime import date
import time
from datetime import timedelta


# Prevents empty user inputs or null strings.
def blank(x):  # Accepts any variable
    if x == "":
        return True
    else:
        return False


# Build allowable characters for user input
def allow(x):
    allow = "abcdefghijklmnopqrstuvwxyz01234567890,.- '"
    return set(x.lower()).issubset(allow)


# Allows user to quit program by entering the word 'END'
def escape(x):
    if x.upper() == "END":
        quit()


# Format dollar values for display
def cur(x):
    return "${:,.2f}".format(x)


# Function that displays a detailed report of all policies in data file
def policyReport(x):
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
    d.close()

    curDate = datetime.datetime.now()
    policyDate = curDate.strftime("%Y-%m-%d")
    while True:
        print("0        1         2         3         4         5         6         7")
        print("1234567890123456789012345678901234567890123456789012345678901234567890")
        print()
        print("ONE STOP INSURANCE COMPANY")
        print("POLICY LISTING AS OF {}".format(policyDate))
        print()
        print("POLICY   CUSTOMER             INSURANCE    EXTRA      TOTAL")
        print("NUMBER   NAME                  PREMIUM     COSTS     PREMIUM")
        print("=" * 60)

        policyCtr = 0
        premAcc = 0
        extraAcc = 0
        totAcc = 0

        while True:
            f = open("Policies.dat", "r")
            for custLine in f:
                line = custLine.split(",")

                policyNum = line[0].strip()
                policyDate = line[1].strip()
                custFName = line[2].strip()
                custLName = line[3].strip()
                numCar = int(line[9].strip())
                liabOpt = line[10].strip()
                glassOpt = line[11].strip()
                loanOpt = line[12].strip()
                monthPay = line[13].strip()
                totPrem = line[14].strip()

                # Processing

                liabCov = 0
                glassCov = 0
                loanCov = 0
                monthPayDsp = 0
                discCar = BASIC_PREM - (BASIC_PREM * ADD_DISC)
                if numCar >= 2:
                    custPrem = BASIC_PREM + (discCar * (numCar - 1))
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
                taxAmt = totPrem * TAX_RATE
                totalCost = totPrem + taxAmt
                if monthPay == "M":
                    monthPayDsp = (totalCost + PROC_FEE) / 12
                custName = custFName + " " + custLName

                policyCtr += 1
                premAcc += custPrem
                extraAcc += totExtra
                totAcc += totPrem

                custPrem = cur(custPrem)
                totExtra = cur(totExtra)
                totPrem = cur(totPrem)
                premAccDsp = cur(premAcc)
                extraAccDsp = cur(extraAcc)
                totAccDsp = cur(totAcc)

                print("{}{:^20}{:>11}{:>10}{:>12}".format(policyNum, custName, custPrem, totExtra, totPrem))
            print("=" * 60)
            print("Total Policies: {:>4}{:>16}{:>12}{:>12}".format(policyCtr, premAccDsp, extraAccDsp, totAccDsp))
            print()
            print()
            print()
            break
        break


# Function that displays an exception report for all policies on a monthly payment structure.
def monthlyReport(x):
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
    d.close()
    curDate = datetime.datetime.now()
    policyDate = curDate.strftime('%d-%b-%y')

    # Display report headings
    print("0        1         2         3         4         5         6         7")
    print("1234567890123456789012345678901234567890123456789012345678901234567890")
    print()
    print("ONE STOP INSURANCE COMPANY")
    print("MONTHLY PAYMENT LISTING AS OF {}".format(policyDate))  # dd-MON-yy
    print()
    print("POLICY   CUSTOMER            TOTAL                  TOTAL      MONTHLY")
    print("NUMBER   NAME                PREMIUM       HST      COST       PAYMENT")
    print("=" * 70)

    # Establish counters and accumulators
    policyCtr = 0
    premAcc = 0
    taxAcc = 0
    totalAcc = 0
    monthAcc = 0

    # Open user input data file and read data.
    while True:
        f = open("Policies.dat", "r")
        for custLine in f:
            line = custLine.split(",")

            policyNum = line[0].strip()
            policyDate = line[1].strip()
            custFName = line[2].strip()
            custLName = line[3].strip()
            numCar = int(line[9].strip())
            liabOpt = line[10].strip()
            glassOpt = line[11].strip()
            loanOpt = line[12].strip()
            monthPay = line[13].strip()
            totPrem = line[14].strip()

            # Process customer data file
            liabCov = 0
            glassCov = 0
            loanCov = 0
            monthPayDsp = 0
            discCar = BASIC_PREM - (BASIC_PREM * ADD_DISC)
            if numCar >= 2:
                custPrem = BASIC_PREM + (discCar * (numCar - 1))
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
            taxAmt = totPrem * TAX_RATE
            totalCost = totPrem + taxAmt
            if monthPay == "M":
                monthPayDsp = (totalCost + PROC_FEE) / 12
            custName = custFName + " " + custLName

            # Establish exception and print
            if monthPay == "M":
                # Increase counters and accumulators
                policyCtr += 1
                premAcc += totPrem
                taxAcc += taxAmt
                totalAcc += totalCost
                monthAcc += monthPayDsp

                # Format to dollar values
                totPremDsp = cur(totPrem)
                taxAmtDsp = cur(taxAmt)
                totalCostDsp = cur(totalCost)
                monthPayDsp = cur(monthPayDsp)
                premAccDsp = cur(premAcc)
                taxAccDsp = cur(taxAcc)
                totalAccDsp = cur(totalAcc)
                monthAccDsp = cur(monthAcc)

                print(
                    "{}{:^20}{:>11}{:>10}{:>12}{:>10}".format(policyNum, custName, totPremDsp, taxAmtDsp, totalCostDsp,
                                                              monthPayDsp))

        # Print remainder readout including counters and accumulators
        print("=" * 70)
        print("Total Policies: {:>4}{:>16}{:>12}{:>12}{:>10}".format(policyCtr, premAccDsp, taxAccDsp, totalAccDsp,
                                                                     monthAccDsp))
        print()
        print()
        print()
        break


# Function that allows the user to write and save policies for new customers.
def policyRegistration(x):
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
    d.close()

    # Gather user data
    while True:
        print("--------------------------------")
        print("|  ONE STOP INSURANCE COMPANY  |")
        print("| Policy Registration Software |")
        print("|------------------------------|")
        print("|    Type 'END' at any time    |\n|    to quit without saving.   |")
        print("================================")
        print()
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
                    liabOpt2 = "Covered"
                    break
                elif liabOpt == "N":
                    liabOpt2 = "Not Covered"
                    break
                else:
                    print("Input not recognized.")
        while True:
            glassOpt = input("Optional glass coverage [Y or N]: ").upper()
            escape(glassOpt)
            if blank(glassOpt) == False:
                if glassOpt == "Y":
                    glassOpt2 = "Covered"
                    break
                elif glassOpt == "N":
                    glassOpt2 = "Not Covered"
                    break
                else:
                    print("Input not recognized")
        while True:
            loanOpt = input("Optional loan vehicle [Y or N]: ").upper()
            escape(loanOpt)
            if blank(loanOpt) == False:
                if loanOpt == "Y":
                    loanOpt2 = "Covered"
                    break
                elif loanOpt == "N":
                    loanOpt2 = "Not Covered"
                    break
                else:
                    print("Input not recognized")
        while True:
            monthPay = input("Payment in full or monthly [F or M]: ").upper()
            escape(monthPay)
            if blank(monthPay) == False:
                if monthPay == "M":
                    break
                elif monthPay == "F":
                    break
                else:
                    print("Input not recognized.")

        # Process user data
        liabCov = 0
        glassCov = 0
        loanCov = 0
        monthPayDsp = 0
        discCar = BASIC_PREM - (BASIC_PREM * ADD_DISC)
        if numCar >= 2:
            custPrem = BASIC_PREM + (discCar * (numCar - 1))
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
        taxAmt = totPrem * TAX_RATE
        totalCost = totPrem + taxAmt
        if monthPay == "M":
            monthPayDsp = (totalCost + PROC_FEE) / 12
        policyNum = str(POLICY_NUM) + "-" + custFName[0].upper() + custLName[0].upper()

        # Date calculations
        curDate = datetime.datetime.now()
        if curDate.day > 25:  # First pay date in two months
            if 1 <= curDate.month <= 10:
                firstMonth = curDate.month + 2
                firstPay = datetime.datetime(curDate.year, firstMonth, 1)
            elif curDate.month == 11:
                firstYear = curDate.year + 1
                firstPay = datetime.datetime(firstYear, 1, 1)
            elif curDate.month == 12:
                firstYear = curDate.year + 1
                firstPay = datetime.datetime(firstYear, 2, 1)
            firstPay = firstPay.strftime("%Y-%m-%d")
            print(firstPay)
        elif curDate.day <= 25:  # First pay date in one month
            if 1 <= curDate.month <= 11:
                firstMonth = curDate.month + 1
                firstPay = datetime.datetime(curDate.year, firstMonth, 1)
            elif curDate.month == 12:
                firstYear = curDate.year + 1
                firstPay = datetime.datetime(firstYear, 1, 1)
            firstPay = firstPay.strftime("%Y-%m-%d")
            print(firstPay)
        policyDate = curDate.strftime("%Y-%m-%d")

        # Write user input to file
        p = open("Policies.dat", "a")
        p.write("{}, ".format(str(policyNum)))
        p.write("{}, ".format(str(policyDate)))
        p.write("{}, ".format(str(custFName)))
        p.write("{}, ".format(str(custLName)))
        p.write("{}, ".format(str(custAdd)))
        p.write("{}, ".format(str(custCity)))
        p.write("{}, ".format(str(custPhone)))
        p.write("{}, ".format(str(custProv)))
        p.write("{}, ".format(str(custPost)))
        p.write("{}, ".format(str(numCar)))
        p.write("{}, ".format(str(liabOpt)))
        p.write("{}, ".format(str(glassOpt)))
        p.write("{}, ".format(str(loanOpt)))
        p.write("{}, ".format(str(monthPay)))
        p.write("{}\n".format(str(round(totPrem, 2))))
        p.close()

        # Format calculations for receipt printout
        basicCovDsp = cur(BASIC_PREM)
        discCarDsp = cur(discCar)
        liabCovDsp = cur(liabCov)
        glassCovDsp = cur(glassCov)
        loanCovDsp = cur(loanCov)
        custPremDsp = cur(custPrem)
        totExtraDsp = cur(totExtra)
        totPremDsp = cur(totPrem)
        monthPayDsp = cur(monthPayDsp)
        procFeeDsp = cur(PROC_FEE)
        taxAmtDsp = cur(taxAmt)
        totalCostDsp = cur(totalCost)

        # Generate receipt
        print()
        print()
        print()
        print("0        1         2         3         4")
        print("1234567890123456789012345678901234567890")
        print()
        print("=" * 40)
        print("{:^40}".format("ONE STOP INSURANCE COMPANY"))
        print("=" * 40)
        print("{:^40}".format("Date: " + str(policyDate)))
        print("-" * 40)
        print("{:^40}".format("CUSTOMER DETAILS"))
        print("--" * 20)
        print()
        print(" {:^40}".format(custFName + " " + custLName))
        print("{:^40}".format(custPhone))
        print("{:^40}".format(custAdd))
        print("{:^40}".format(custCity + ", " + custProv))
        print("{:^40}".format(custPost))
        print()
        print("--" * 20)
        print("{:^40}".format("POLICY #{}".format(policyNum)))
        print("--" * 20)
        print()
        if numCar == 1:
            print("Auto Insured: {:>26}".format(numCar))
        else:
            print("Autos Insured: {:>25}".format(numCar))
        print("   Auto 1: {:>28})".format("(" + basicCovDsp))
        autoRange = range(1, numCar)
        for numCar in autoRange:
            if numCar <= 8:
                print("   Auto{:>2}:{:>30}".format(numCar + 1, "(" + discCarDsp + ")"))
            elif 9 <= numCar <= 98:
                print("   Auto{:>3}:{:>29}".format(numCar + 1, "(" + discCarDsp + ")"))
            elif 99 <= numCar <= 998:
                print("   Auto{:>4}:{:>29}".format(numCar + 1, "(" + discCarDsp + ")"))
            elif 999 <= numCar <= 9998:
                print("   Auto{:>5}:{:>28}".format(numCar + 1, "(" + discCarDsp + ")"))
            elif 9999 <= numCar <= 99998:
                print("   Auto{:>6}:{:>27}".format(numCar + 1, "(" + discCarDsp + ")"))
            elif 99999 <= numCar <= 999998:
                print("   Auto{:>7}:{:>26}".format(numCar + 1, "(" + discCarDsp + ")"))
            elif numCar >= 999999:
                print("   Autos registered\n   out of printable range.")
        print()
        print("Extra Liability: {:>23}".format(liabOpt2))
        print("{}{:>25})".format("($130.00/Auto)", "(" + liabCovDsp))
        print()
        print("Glass Coverage: {:>24}".format(glassOpt2))
        print("{}{:>26})".format("($86.00/Auto)", "(" + glassCovDsp))
        print()
        print("Loan Coverage: {:>25}".format(loanOpt2))
        print("{}{:>26})".format("($58.00/Auto)", "(" + loanCovDsp))
        print()
        print("--" * 20)
        print("{:^40}".format("BILLING DETAILS"))
        print("--" * 20)
        print()
        print("Premium Total: {:>25}".format(custPremDsp))
        print("Add-On Total: {:>26}".format(totExtraDsp))
        print("{:>40}".format("---------"))
        print("Subtotal: {:>30}".format(totPremDsp))
        print("Taxes: {:>33}".format(taxAmtDsp))
        print("{:>40}".format("---------"))
        print("Total Cost: {:>28}".format(totalCostDsp))
        print()
        print("--" * 20)
        print("{:^40}".format("BILLING DETAILS"))
        print("--" * 20)
        print()
        if monthPay == "F":
            print("Payment Option Selected: {:>15}".format("In Full"))
        elif monthPay == "M":
            print("Payment Option Selected: {:>15}".format("Monthly"))
            print("Processing Fee: {:>24}".format(procFeeDsp))
            print("")
            print("Monthly Payment Amount: {:>16}".format(monthPayDsp))
            print("First Payment On: {:>22}".format(firstPay))
            print()
        print("==" * 20)
        print("{:^40}".format("THANK YOU"))
        print("==" * 20)
        print()
        print()
        print()

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
        d.close()
        break


# Main menu program
while True:
    print()
    print("Welcome to the ONE STOP INSURANCE COMPANY Policy Registration Software. ")
    print()
    print("Please select from the following options: ")
    print()
    print("     1. New Policy Registration")
    print("     2. Detailed Policy Report")
    print("     3. Monthly Payment Customer Report")
    print("     4. Quit Program")
    print()
    while True:
        select = input("To select an option, enter the relevant number: ")
        if select == "1":
            print()
            print()
            policyRegistration(select)
            break
        if select == "2":
            print()
            print()
            try:
                policyReport(select)
                break
            except:
                print()
                print("Data file empty. ")
                print("Please register policies before printing reports.")
            break
        if select == "3":
            print()
            print()
            try:
                monthlyReport(select)
                break
            except:
                print()
                print("Data file empty. ")
                print("Please register policies before printing reports.")
            break
        if select == "4":
            quit()
        else:
            print("Input not recognized.")
