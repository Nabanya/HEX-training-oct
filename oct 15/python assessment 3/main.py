# main.py

# 76-77
import event_utils

b_amt = event_utils.calculate_booking_amount(2500, 5)
disc = event_utils.calculate_discount(b_amt)
cap_status = event_utils.check_event_capacity(250, 300)

print("--- Section H: User-Defined Module Output ---")
print(f"77. Booking Amount: ₹{b_amt}, Discount: ₹{disc}, Capacity Status: {cap_status}")

# 78
from event_utils import calculate_booking_amount
print("78. Direct Call Booking Amount:", calculate_booking_amount(3000, 2))

# 79
import event_utils as eu
print("79. Alias Check Capacity:", eu.check_event_capacity(300, 300))
print("\n")
