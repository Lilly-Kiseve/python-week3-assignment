def calculate_discount(price, discount_percent):
    """Calculate the final price after applying if it is 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price # No discount applied


# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))


# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after discount (if applicable): ${final_price:.2f}")
