#Function to figure out the final price after discount
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

print("Welcome to Kevin's Discount Calculator ")
print("Let's see how much you can save today!\n")

# Ask the shopper for details
try:
    original_price = float(input("What's the original price of the item? Ksh "))
    discount_percent = float(input("What's the discount percentage? "))

    # Get the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Lets Show results
    if discount_percent >= 20:
        print(f"Congrats! You got a discount. Your final price is: Ksh {final_price:.2f}")
    else:
        print(f"No discount applied. Your price stays at: Ksh {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
