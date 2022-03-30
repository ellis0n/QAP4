while True:
    print()
    print("Hello, welcome to the ONE STOP INSURANCE COMPANY Policy Registration Software. ")
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
            import main
            break
        elif select == "2":
            print()
            print()
            try:
                import PolicyReport
            except:
                print()
                print("Data file empty. ")
                print("Please register policies before printing reports.")
            break
        elif select == "3":
            print()
            print()
            try:
                import MonthlyReport
            except:
                print()
                print("Data file empty. ")
                print("Please register policies before printing reports.")
            break
        elif select == "4":
            quit()
        else:
            print("Input not recognized.")