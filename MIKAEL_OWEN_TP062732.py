# MIKAEL OWEN KARTIKA
# TP062732

import datetime


def date():
    t = datetime.datetime.now()
    t = t.strftime(" on %A, %d %B %Y at %X")
    return (t)

def dateRange(userData,lineNumber):
    # format: d/m/y h:m:s

    sdate = input("start date: ")
    edate = input("end date: ")
    sdate = datetime.datetime.strptime(sdate, "%d/%m/%Y %H:%M:%S")
    edate = datetime.datetime.strptime(edate, "%d/%m/%Y %H:%M:%S")
    for rec in open("report.txt").readlines():
        t = datetime.datetime.strptime(rec.split("|")[2], " on %A, %d %B %Y at %X")
        if (sdate <= t <= edate) and (rec.split("|")[0] == userData[1]):
            print(rec)

    customer_menu(userData,lineNumber)

def main():
    print("==========Welcome to BlueBank!==========")
    IDchecker = []
    for rec in open("data.txt").readlines():
        IDchecker.append(rec.split(":")[1])
    accNumber = id_input(IDchecker)
    lineNumber = IDchecker.index(accNumber)
    userData = [rec.split(':') for rec in open("data.txt").readlines()][lineNumber]
    pass_input(userData)
    account_type(userData, lineNumber)


def id_input(IDchecker):
    user_ID = input("Enter your ID: ")
    while True:
        if user_ID not in IDchecker:
            print("\nThe ID you entered is wrong\n")
            user_ID = input("Enter your ID: ")
        else:
            break
    return user_ID


def dest_input(dest_IDChecker):
    user_ID = input("Enter the account number you would like to transfer ")
    while True:
        if user_ID not in dest_IDChecker:
            print("\nThe ID you entered is wrong\n")
            user_ID = input("Enter the account number you would like to transfer ")
        else:
            break
    return user_ID


def pass_input(userData):
    read_pass = input("Enter your password: ")
    check_password = userData[2]
    while True:
        if read_pass != check_password:
            print("\nThe password you entered is wrong \n")
            read_pass = input("Enter your password: ")
        else:
            break


def account_type(userData, lineNumber):
    check_type = userData[0]
    if check_type == "S":
        super_menu(userData, lineNumber)
    elif check_type == "A":
        admin_menu(userData, lineNumber)
    elif check_type == "CC" or check_type == "CS":
        customer_menu(userData, lineNumber)


def super_menu(userData, lineNumber):
    print("\n====================Welcome to Super User Menu====================")
    print("\n 1. Create an admin account\n 2. Change password \n 3. Log Out \n")
    super_resp = input(" Enter your option 1/2/3 : ")
    while True:
        if super_resp != "1" and super_resp != "2" and super_resp != "3":
            print("\n The response you entered is invalid ... \n")
            super_resp = input(" Enter your option 1/2/3 : ")
        elif super_resp == "1":
            userData_create("ADMIN", "A", super_menu, userData, lineNumber)
        elif super_resp == "2":
            change_password(userData, lineNumber)
        elif super_resp == "3":
            print("\n       You have logged \n     out of your userData.\n   Thanks for using BlueBank!")
            main()


def admin_menu(userData, lineNumber):
    print("\n====================Welcome to Admin Staff Menu====================")
    print("\n 1. Create a new customer account\n 2. Edit customer details ")
    print(" 3. See customer's statement of account report\n 4. Change password\n 5. Log Out\n")
    admin_response = input(" Select an activity 1/2/3/4/5 : ")
    while True:
        if admin_response != "1" and admin_response != "2" and admin_response != "3" and admin_response != "4" and admin_response != "5":
            print("\n The response you entered is invalid  \n")
            admin_response = input(" Select an activity 1/2/3/4/5 : ")
        elif admin_response == "1":
            userData_create("CUSTOMER", customer_type(), admin_menu, userData, lineNumber)
        elif admin_response == "2":
            customer_edit(userData, lineNumber)
        elif admin_response == "3":
            customer_statement()
        elif admin_response == "4":
            change_password(userData, lineNumber)
        elif admin_response == "5":
            print("\n       You have logged \n     out of your userData.\n   Thanks for using MyBank!")
            main()


def customer_menu(userData, lineNumber):
    myid = userData[1]
    print("====================Welcome to Customer Menu====================")
    print("\n 1. Deposit \n 2. Withdrawal\n 3. Transfer\n "
          "4. Check Balance\n 5. View Account Report\n 6. Change Password\n 7. Log Out")
    cust_response = input(" Enter your option 1/2/3/4/5/6/7:")
    while True:
        if cust_response == "1":
            customer_deposit(userData, lineNumber)
        elif cust_response == "2":
            customer_withdraw(userData, lineNumber)
        elif cust_response == "3":
            customer_transfer(userData, lineNumber)
        elif cust_response == "4":
            user_balance(userData, lineNumber)
        elif cust_response == "5":
            customer_statement(userData,lineNumber)
        elif cust_response == "6":
            change_password(userData, lineNumber)
        elif cust_response == "7":
            main()
        else:
            print("\n The response you entered is invalid ... \n")
            customer_menu(userData,lineNumber)


def input_check(input_item, index_num):
    check_input = [rec.split(':')[index_num] for rec in open("data.txt").readlines()]
    if index_num == 3:
        input_type = "name"
    elif index_num == 4:
        input_type = "phone number"
    elif index_num == 5:
        input_type = "email address"
    while True:
        if input_item in check_input:
            print("\n This " + input_type + " has been inputted ... \n")
            input_item = input(" Enter Account owner's " + input_type + ": ")
        else:
            break


def create_id(name, number, email, acc_type, rec, menu, userData, lineNumber):
    existing_id = [rec.split(':')[1] for rec in open("data.txt").readlines()]
    new_pass = str(int(existing_id[-1][-4:]) + 1)
    if acc_type == "CS":
        new_id = "SAVINGS" + new_pass
        registerdata = acc_type + ":" + new_id + ":" + new_pass + ":" + name + ":" + number + ":" + email + ":" + "100" + "\n"
    elif acc_type == "CC":
        new_id = "CURRENT" + new_pass
        registerdata = acc_type + ":" + new_id + ":" + new_pass + ":" + name + ":" + number + ":" + email + ":" + "500" + "\n"
    else:
        new_id = "ADMIN" + new_pass
        registerdata = acc_type + ":" + new_id + ":" + new_pass + ":" + name + ":" + number + ":" + email + "\n"
    with open("data.txt", "a") as data:
            data.write(registerdata)
    print("\n Account has been created\n\n ID = " + new_id + "\n Password = " + new_pass)
    print(" Name : " + name + "\n Phone Number : " + number + "\n Email Address : " + email)
    menu(userData, lineNumber)


def userData_create(x, acc_type, menu, userData, lineNumber):
    print("\n  CREATE A NEW " + x + " ACCOUNT")
    print("=" * 20)
    name = input(" Enter Account owner's name: ")
    input_check(name, 3)
    number = input("\n Enter Account owner's phone number: ")
    input_check(number, 4)
    email = input("\n Enter Account owner's email address: ")
    input_check(email, 5)
    create_id(name, number, email, acc_type, x, menu, userData, lineNumber)
    main()


def customer_type():
    print("\n Which customer account are you planning to create?")
    cust_type = input(" Savings account (CS) or Current account(CC): ")
    while True:
        if cust_type != "CS" and cust_type != "CC":
            print("\n The response you entered is invalid ... \n")
            cust_type = input(" Savings account (CS) or Current account(CC): ")
        elif cust_type == "CS":
            acc_type = "CS"
            break
        elif cust_type == "CC":
            acc_type = "CC"
            break
    return acc_type


def customer_details(userData):
    customer_id, name, number, email = userData[1], userData[3], userData[4], userData[5]
    print(
        "\n 1. ID :" + customer_id + "\n 2. Name : " + name + "\n 3. Phone Number : " + number + "\n 4. Email Address : " + email)


def customer_edit(userData, admin_line):
    id = input("\n Enter the account number you wish to modify ")
    id_check = [x.split(':')[1] for x in open("data.txt").readlines()]
    lineNumber = id_check.index(id)
    customer_userData = [x.split(':') for x in open("data.txt").readlines()][lineNumber]
    while True:
        if id not in id_check:
            print("\n The account number you entered is invalid \n")
            id = input("\n Enter the account number you wish to modify ")
        else:
            break
    customer_details(customer_userData)
    change_info = input("\n Select an information you would like to change (3/4): ")
    while True:
        if change_info != "3" and change_info != "4":
            print("\n The response you entered is invalid ... \n")
            change_info = input("\n Select an information you want to change (3/4): ")
        elif change_info == "3":
            new_number = input(" Enter customer's new phone number: ")
            while True:
                if new_number == customer_userData[4]:
                    print("\n The new number cannot be the same to the old one \n")
                    new_number = input(" Enter customer's new phone number: ")
                else:
                    with open("data.txt", "r") as data:
                        data_content = data.readlines()
                        data_content[lineNumber] = customer_userData[0] + ":" + customer_userData[1] + ":" + \
                                                   customer_userData[2] + ":" + customer_userData[
                                                       3] + ":" + new_number + ":" + customer_userData[5] + ":" + \
                                                   customer_userData[6] + "\n"
                    with open("data.txt", "w") as data:
                        data.writelines(data_content)
                    print("\n Current phone number: " + new_number + "\n")
                    admin_menu(userData, admin_line)
        elif change_info == "4":
            new_email = input(" Enter customer's new email address: ")
            while True:
                if new_email == customer_userData[5]:
                    print("\n The new email cannot be the same to the old one \n")
                    new_email = input(" Enter customer's new email address: ")
                else:
                    with open("data.txt", "r") as data:
                        data_content = data.readlines()
                        data_content[lineNumber] = customer_userData[0] + ":" + customer_userData[1] + ":" + \
                                                   customer_userData[2] + ":" + customer_userData[3] + ":" + \
                                                   customer_userData[4] + ":" + new_email + ":" + customer_userData[
                                                       6] + "\n"
                    with open("data.txt", "w") as data:
                        data.writelines(data_content)
                    print("\n Current email address: " + new_email + "\n")
                    admin_menu(userData, admin_line)


def change_password(userData, lineNumber):
    read_pass = input(" Enter your current password: ")
    check_pass = userData[2]
    while True:
        if read_pass != check_pass:
            print("\n The password you entered is invalid ... \n")
            read_pass = input(" Enter your current password: ")
        else:
            break
    new_pass = input(" Enter a new password: ")
    while True:
        if new_pass == check_pass:
            print("\n Your new password should not be the same as your old password \n")
            new_pass = input(" Enter a new password: ")
        else:
            break
    with open("data.txt", "r") as data:
        data_content = data.readlines()
        data_content[lineNumber] = userData[0] + ":" + userData[1] + ":" + new_pass + ":" + userData[3] + ":" + \
                                   userData[4] + ":" + userData[5] + ":" + userData[6]
    with open("data.txt", "w") as data:
        data.writelines(data_content)
    print("\n Your password has been changed\n\n      Please login using\n      your new password")
    main()


def user_balance(userData, lineNumber):
    balance = userData[6]
    resp = input("\nType 1 to check user balance\n     2 to back\n")
    while True:
        if resp == "1":
            print("Your current balance is :" + balance)
            break
        elif resp == "2":
            customer_menu(userData, lineNumber)
        else:
            print("The option you entered is invalidd")



def customer_statement(userData,lineNumber):
    for rec in open("report.txt").readlines():
        if (rec.split("|")[0] == userData[1]):
            print(rec)
    dateRange(userData, lineNumber)


def customer_withdraw(userData, lineNumber):
    balance = int(userData[6])
    acc_type = userData[0]
    withdraw_amt = int(input(" How much money you would like to withdraw "))

    while True:
        if balance <= withdraw_amt:
            print("\n Your balance is not enough to withdraw  \n")
            withdraw_amt = int(input(" How much money you would like to withdraw "))
        elif acc_type == "CS" and balance - withdraw_amt <= 100 :
            print("\n Your balance is not enough to withdraw  \n")
            withdraw_amt = int(input(" How much money you would like to withdraw "))
            break
        elif acc_type == "CC" and balance - withdraw_amt <= 500 :
            print("\n Your balance is not enough to withdraw  \n")
            withdraw_amt = int(input(" How much money you would like to withdraw "))
            break
        else:
            new_balance = balance - withdraw_amt
        with open("data.txt", "r") as data:
            data_content = data.readlines()
            data_content[lineNumber] = userData[0] + ":" + userData[1] + ":" + userData[2] + ":" + userData[3] + ":" + \
                                       userData[4] + ":" + userData[5] + ":" + str(new_balance) + "\n"
        with open("data.txt", "w") as data:
            data.writelines(data_content)
        print("\n You have successfully withdraw your balance!")

        f = open("report.txt", "a")
        f.write(userData[1] + "|Withdrawal RM" + str(withdraw_amt) + "|" + date() + "|The current balance is now " + str(new_balance) + "\n")
        f.close()

        customer_menu(userData, lineNumber)


def customer_deposit(userData, lineNumber):
    balance = int(userData[6])
    deposit_amt = int(input(" How much money you would like to deposit "))
    new_balance = 0
    while True:
        new_balance = balance + deposit_amt
        with open("data.txt", "r") as data:
            data_content = data.readlines()
        data_content[lineNumber] = userData[0] + ":" + userData[1] + ":" + userData[2] + ":" + userData[3] + ":" + \
                                   userData[4] + ":" + userData[5] + ":" + str(new_balance) + "\n"
        with open("data.txt", "w") as data:
            data.writelines(data_content)
        print("\n You have successfully deposit your balance!")

        f = open("report.txt", "a")
        f.write(
              userData[1] + "|Deposit RM" + str(deposit_amt) + "|" + date() + "|The current balance is now " + str(new_balance) + "\n")
        f.close()

        customer_menu(userData, lineNumber)


def customer_transfer(userData, lineNumber):
    balance = int(userData[6])
    dest_IDchecker = []
    for rec in open("data.txt").readlines():
        dest_IDchecker.append(rec.split(":")[1])
    accDest = dest_input(dest_IDchecker)
    lineDest = dest_IDchecker.index(accDest)
    DestData = [rec.split(':') for rec in open("data.txt").readlines()][lineDest]
    transfer_amt = int(input(" How much money you would like to transfer "))
    new_balance = 0
    dest_balance = int(DestData[6])
    new_dest_balance = 0
    while True:
        if balance >= transfer_amt:
            new_balance = balance - transfer_amt
            new_dest_balance = dest_balance + transfer_amt
            break
        else:
            print("\n Your balance is not enough to transfer  \n")
            transfer_amt = int(input(" How much money you would like to transfer "))

    with open("data.txt", "r") as data:
        data_content = data.readlines()
    data_content[lineNumber] = userData[0] + ":" + userData[1] + ":" + userData[2] + ":" + userData[3] + ":" + \
                               userData[4] + ":" + userData[5] + ":" + str(new_balance) + "\n"
    with open(" data.txt", "w") as data:
        data.writelines(data_content)
    print("\n You have successfully transfer your balance!")

    with open("data.txt", "r") as data:
        data_content = data.readlines()
    data_content[lineDest] = DestData[0] + ":" + DestData[1] + ":" + DestData[2] + ":" + DestData[3] + ":" + \
                             DestData[4] + ":" + DestData[5] + ":" + str(new_dest_balance) + "\n"
    with open("data.txt", "w") as data:
        data.writelines(data_content)

    f = open("report.txt", "a")
    f.write(userData[1] + "|Transfer RM" + str(
        transfer_amt) +  "|" + date() + "|The current balance is now " + str(new_balance) + "\n")
    f.write(accDest + "|have successfully receive RM" + str(transfer_amt) + "|" + date() + "|The current balance is now " + str(new_dest_balance) + "\n")
    f.close()

    customer_menu(userData, lineNumber)


main()
