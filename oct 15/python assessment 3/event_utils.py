# event_utils.py
# 75

def calculate_booking_amount(ticket_price, tickets):
    return ticket_price * tickets

def calculate_discount(amount):
    return amount * 0.10 if amount >= 10000 else amount * 0.05

def check_event_capacity(registered, capacity):
    if registered > capacity:
        return "Invalid Data"
    elif registered == capacity:
        return "Full"
    return "Seats Available"