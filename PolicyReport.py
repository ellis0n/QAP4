# Import libraries

import datetime
from datetime import date
import time
from datetime import timedelta

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
    print("="*60)

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
            custName = custFName+" "+custLName

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
