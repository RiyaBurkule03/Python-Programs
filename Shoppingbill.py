def calculate_electronics_gst(a, b):
    return (a + b) * 1.18


def calculate_fashion_gst(c, d):
    return (c + d) * 1.13


def calculate_food_gst(e):
    return e * 1.07


def total_bill(a, b, c, d, e):
    return (
        calculate_electronics_gst(a, b)
        + calculate_fashion_gst(c, d)
        + calculate_food_gst(e)
    )


def calculate_discounted_bill(a, b, c, d, e):
    total = total_bill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount


# Sample values supplied directly as function arguments
a, b, c, d, e = 100, 100, 100, 100, 100

total = total_bill(a, b, c, d, e)
discount = total * 0.20
final_amount = calculate_discounted_bill(a, b, c, d, e)

print(f"Total after GST = ₹{total:.2f}")
print(f"Discount = ₹{discount:.2f}")
print(f"Final payable amount = ₹{final_amount:.2f}")