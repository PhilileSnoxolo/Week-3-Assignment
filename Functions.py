def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or more.
    
    Parameters:
    - price (float): Original price of the item.
    - discount_percent (float): Discount percentage to be applied.
    
    Returns:
    - float: Final price after discount if discount is 20% or more.
    - float: Original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
