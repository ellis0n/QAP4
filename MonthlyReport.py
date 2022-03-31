# Import libraries

import datetime
from datetime import date
import time
from datetime import timedelta

# Format to dollar value strings
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

        # Establish exception and print
        if monthPay == "M":
            print("{}{:^20}{:>11}{:>10}{:>12}{:>10}".format(policyNum, custName, totPremDsp, taxAmtDsp, totalCostDsp,
                                                        monthPayDsp))

   # Print remainder readout including counters and accumulators
    print("=" * 70)
    print("Total Policies: {:>4}{:>16}{:>12}{:>12}{:>10}".format(policyCtr, premAccDsp, taxAccDsp, totalAccDsp,
                                                                 monthAccDsp))
    print()
    print()
    print()
    break
