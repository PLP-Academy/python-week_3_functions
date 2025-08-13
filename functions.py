def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying discount
    if discount is 20% or more.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Function to safely get a float input from the user
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Prompt the user for input
original_price = get_float_input("Enter the original price: ")
discount_percentage = get_float_input("Enter the discount percentage: ")

# Call the function
final_price = calculate_discount(original_price, discount_percentage)

# Display result
print(f"Final price: Ksh{final_price:.2f}")
