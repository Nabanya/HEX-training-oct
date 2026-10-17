# retail_utils.py
# 56. Functions for calculating total, discount, checking stock
def calculate_order_total(price, quantity):
    return price * quantity

def calculate_discount(amount):
    return amount * 0.10 if amount >= 50000 else amount * 0.05

def check_stock_status(stock):
    if stock > 20:
        return "High Stock"
    elif 1 <= stock <= 20:
        return "Low Stock"
    return "Out of Stock"