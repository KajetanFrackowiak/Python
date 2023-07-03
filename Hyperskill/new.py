# import math
#
#
# def get_user_input(prompt):
#     """Gets user input and validates it."""
#     value = input(prompt)
#     while not value.isdigit():
#         print("Please enter a valid number.")
#         value = input(prompt)
#     return int(value)
#
#
# def calculate_annuity_payment(loan_principal, number_of_payments, loan_interest):
#     """Calculates the annuity payment."""
#     interest_rate = loan_interest / 12 / 100
#     annuity_payment = loan_principal * (interest_rate * (1 + interest_rate) ** number_of_payments) / (
#             (1 + interest_rate) ** number_of_payments - 1)
#
#     return annuity_payment
#
#
# def calculate_number_of_payments(loan_principal, annuity_payment, loan_interest):
#     """Calculates the number of payments."""
#     interest_rate = loan_interest / 12 / 100
#     number_of_payments = math.log(annuity_payment / (annuity_payment - interest_rate * loan_principal),
#                                   1 + interest_rate)
#     return number_of_payments
#
#
# def calculate_loan_principal(annuity_payment, number_of_payments, loan_interest):
#     """Calculates the loan principal."""
#     interest_rate = loan_interest / 12 / 100
#     loan_principal = annuity_payment / ((interest_rate * (1 + interest_rate) ** number_of_payments) / (
#             (1 + interest_rate) ** number_of_payments - 1))
#
#     return loan_principal


import math

calculate_type = input('''What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:\n''')

if calculate_type == "n":
    loan_principal = int(input("Enter the loan principal\n"))
    annuity_payment = float(input("Enter the monthly payment\n"))
    loan_interest = float(input("Enter the loan interest\n"))

    interest_rate = loan_interest / 12 / 100
    number_of_payments = math.ceil(math.log(annuity_payment / (annuity_payment - interest_rate * loan_principal),
                                            1 + interest_rate))

    years = number_of_payments // 12
    mouths = number_of_payments % 12
    if years == 0 and number_of_payments == 1:
        print(f"It will take {number_of_payments} month to repay this loan!")
    elif years == 0 and number_of_payments > 1:
        print(f"It will take {number_of_payments} months to repay this loan!")
    elif years == 1 and number_of_payments == 0:
        print(f"It will take {years} year to repay this loan!")
    elif years == 1 and number_of_payments == 1:
        print(f"It will take {years} year and {mouths} month to repay this loan!")
    elif years > 1 and number_of_payments == 1:
        print(f"It will take {years} years and {mouths} month to repay this loan!")
    elif years > 1 and number_of_payments > 1:
        print(f"It will take {years} years and {mouths} months to repay this loan!")

elif calculate_type == "a":
    loan_principal = int(input("Enter the loan principal\n"))
    number_of_payments = int(input("Enter the number of payments\n"))
    loan_interest = float(input("Enter the loan interest\n"))

    interest_rate = loan_interest / 12 / 100
    annuity_payment = math.ceil(loan_principal * (interest_rate * (1 + interest_rate) ** number_of_payments) / (
            (1 + interest_rate) ** number_of_payments - 1))

    print("Your monthly payment = {}".format(annuity_payment))

elif calculate_type == "p":
    annuity_payment = float(input("Enter the monthly payment\n"))
    number_of_payments = int(input("Enter the number of payments\n"))
    loan_interest = float(input("Enter the loan interest\n"))

    interest_rate = loan_interest / 12 / 100
    loan_principal = annuity_payment / ((interest_rate * (1 + interest_rate) ** number_of_payments) / (
            (1 + interest_rate) ** number_of_payments - 1))
    print("Your loan principal = {}".format(loan_principal))
