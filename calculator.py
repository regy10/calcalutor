#This program will calculate the total amount of charge of the food include tips and sales tax and display the grand total

def calculate_total_cost(meal_cost, tip_percentage, tax_percentage):
    # Calculate tip and tax amounts
    tip_amount = meal_cost * (tip_percentage / 100)
    tax_amount = meal_cost * (tax_percentage / 100)

    # Calculate total cost
    total_cost = meal_cost + tip_amount + tax_amount

    return total_cost, tip_amount, tax_amount


def display_receipt(meal_cost, tip_percentage, tax_percentage):
    total_cost, tip_amount, tax_amount = calculate_total_cost(meal_cost, tip_percentage, tax_percentage)

    # Display receipt
    print("Meal Cost: ${:.2f}".format(meal_cost))
    print("Tip ({}%): ${:.2f}".format(tip_percentage, tip_amount))
    print("Tax ({}%): ${:.2f}".format(tax_percentage, tax_amount))
    print("---------------------")
    print("Total Cost: ${:.2f}".format(total_cost))


# summary of your transaction.
meal_cost = float(input("Enter the cost of the meal: $"))
tip_percentage = float(input("Enter the tip percentage: "))
tax_percentage = float(input("Enter the sales tax percentage: "))

display_receipt(meal_cost, tip_percentage, tax_percentage)
