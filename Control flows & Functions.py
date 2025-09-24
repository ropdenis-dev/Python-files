# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # ✅ Apply discount only if 20% or more
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price  # ✅ No discount applied


# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}")
