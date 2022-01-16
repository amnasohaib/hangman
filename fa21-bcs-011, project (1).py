# Project of Pharmacy Management System which shows billing, finding products in the shop, employee salary
# and increase/decrease in sale percent
# by fa21-bcs-011, Amna Sohaib

print(format("**", ">15s"), "PHARMACY MANAGEMENT SYSTEM", "**")
print(format("WELCOME", ">33s"))


def billing():
    sum = 0
    count = 0
    product = input("Enter Product name(0 to quit):")
    while product != '0':
        count = count + 1
        price = eval(input("Enter price of the product:"))
        product = input("Enter Product name(0 to quit):")
        sum = sum + price

    else:
        print("---------------------------")
        print(format("BILL", ">15s"))
        print(format("Number of Products:","21s"), count)
        print(format("Total Bill:", "20s"), sum)
        print("---------------------------")
    return sum


def product():
    product = str("1.Paracetamol, 2.Injections, 3.Bandages")
    print("Select Product Type:", product)
    product_type = eval(input("Enter number"))
    if product_type == 1:
        print("Your product is in Aisle 1.")
    elif product_type == 2:
        print("Your product is in Aisle 2.")
    elif product_type == 3:
        print("Your product is in Aisle 3.")
    else:
        print("-- UNAVAILABLE DATA --")


def salary():
    name = str(input("Enter your name:"))
    post_str = ['1.manager', '2.cashier', '3.helper']
    print(post_str)
    monthly_salary = 1
    post = eval(input("Choose your designated post:"))
    days = int(input("Enter number of days worked:"))
    if post == 1:
        monthly_salary = days * 1000
    elif post == 2:
        monthly_salary = days * 500
    elif post == 3:
        monthly_salary = days * 200
    else:
        print("--INVALID DATA--")
    print("\n|||||||||||||||||||||||||||||||||||\n")
    print(format("--", ">9s"), "Employee Salary --")
    print(format("EMPLOYEE NAME:", ">22s"), name)
    print(format("This Month's Salary:", ">23s"), monthly_salary)
    print("\n|||||||||||||||||||||||||||||||||||\n")


def sale_percent():
    last_income = eval(input("Enter last month's income:"))
    new_income = eval(input("Enter this month's income:"))
    sales_percent = ((new_income - last_income) / last_income) * 100
    print("****************************************")
    print("----------------------------------------")
    print(format("LAST MONTH'S INCOME:", ">27s"), last_income)
    print(format("THIS MONTH'S INCOME:", ">27s"), new_income)
    print("\nTHIS MONTH'S SALE PURCHASE=", round(sales_percent, 3), "%")
    print("----------------------------------------")
    print("****************************************")


def main():
    options = ["1. Billing", "2. Locating Product", "3. Employee Salary", "4. Sale Percent of this Month"]
    print("==========================================================")
    print("\n", options[0], "\n", options[1], "\n", options[2], "\n", options[3])
    x = input("Choose your desired option:")
    if x == '1':
        billing()
    elif x == '2':
        product()
    elif x == '3':
        salary()
    elif x == '4':
        sale_percent()
    else:
        print("Invalid Data.")


print("\n==========================================================")
while input("\nWould You Like To Look at Our Options? (y/n):") == "y":
    main()
print("\n****************************************")
print("----------------------------------------")
print(format("Thank you For Visiting", ">30s"))
print(format("Have a good day!", ">27s"))
print("----------------------------------------")
print("****************************************")
