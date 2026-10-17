# section A

# 1
attendee_name = "Aarav Shah"
num_tickets = 4
ticket_price = 3000.0

# 2
total_amount = num_tickets * ticket_price

# 3
if total_amount >= 10000:
    discount_rate = 0.10
else:
    discount_rate = 0.05

discount_amount = total_amount * discount_rate
final_amount = total_amount - discount_amount

# 4
print(f"4. Attendee Name: {attendee_name}")
print(f"   Original Booking Amount: ₹{total_amount:.2f}")
print(f"   Discount Applied: ₹{discount_amount:.2f}")
print(f"   Final Amount Payable: ₹{final_amount:.2f}\n")

# 5-6
event_capacity = 300
registered_participants = 250

if registered_participants > event_capacity:
    capacity_status = "Invalid Data"
elif registered_participants == event_capacity:
    capacity_status = "Full"
else:
    capacity_status = "Seats Available"

print(f"6. Capacity Status: {capacity_status}\n")

# 7
print("7. Numbers 1 to 15:")
for i in range(1, 16):
    print(i, end=" ")
print("\n")

# 8
print("8. Numbers divisible by 3 (from 1-15):")
for i in range(1, 16):
    if i % 3 == 0:
        print(i, end=" ")
print("\n")

# 9
print("9. Countdown from 10 to 1:")
countdown = 10
while countdown >= 1:
    print(countdown, end=" ")
    countdown -= 1
print("\n")

# 10
print("10. Demonstration of break and continue:")
print("    - Skipping 5 using continue:", end=" ")
for i in range(1, 10):
    if i == 5:
        continue
    print(i, end=" ")
print()

print("    - Stopping at 7 using break:", end=" ")
for i in range(1, 10):
    if i == 7:
        break
    print(i, end=" ")
print("\n")

# section B
booking_amounts = [5000, 3500, 7500, 6000, 4000, 7000, 3000, 10000]

# 11
total_booking = sum(booking_amounts)
print(f"11. Total Booking Amount: ₹{total_booking}")

# 12
avg_booking = total_booking / len(booking_amounts)
print(f"12. Average Booking Amount: ₹{avg_booking:.2f}")

# 13
print(f"13. Highest Amount: ₹{max(booking_amounts)}")
print(f"    Lowest Amount: ₹{min(booking_amounts)}")

# 14
above_5000 = [amt for amt in booking_amounts if amt > 5000]
print(f"14. Amounts > 5000: {above_5000}")

# 15
sorted_desc = sorted(booking_amounts, reverse=True)
print(f"15. Amounts Sorted Descending: {sorted_desc}\n")

cities = ["Hyderabad", "Mumbai", "Pune", "Hyderabad", "Delhi", "Mumbai"]

# 16
unique_cities = set(cities)
print(f"16. Unique Cities Set: {unique_cities}")

# 17
unique_cities.add("Bangalore")

# 18
print(f"18. Count of Unique Cities: {len(unique_cities)}\n")

# 19
event_tuple = ("E101", "AI Innovation Summit", "Hyderabad", 500)

# 20
e_id, e_name, e_venue, e_capacity = event_tuple
print(f"20. Unpacked Event: ID={e_id}, Name='{e_name}', Venue='{e_venue}', Capacity={e_capacity}\n")

# 21
registration = {
    "registration_id": "R1001",
    "attendee_name": "Aarav Shah",
    "city": "Hyderabad",
    "tickets": 2,
    "status": "Pending",
    "amount": 5000
}

# 22
registration["status"] = "Confirmed"

# 23
registration["tickets"] += 1

# 24
registration["email"] = "aarav.shah@example.com"

# 25
print("25. Registration Dictionary Items:")
for k, v in registration.items():
    print(f"    {k}: {v}")
print("\n")

# section C

# 26
def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets

# 27
def get_discount_amount(amount):
    return amount * 0.10 if amount >= 10000 else amount * 0.05

# 28
def is_active_registration(status):
    return status.strip().lower() in ["confirmed", "pending"]

# 29
def total_booking_sum(amounts_list):
    return sum(amounts_list)

# 30
increase_by_10_percent = lambda amt: amt * 1.10
print(f"30. Amount 5000 increased by 10%: ₹{increase_by_10_percent(5000):.2f}")

# 31
filtered_amounts = list(filter(lambda amt: amt > 6000, booking_amounts))
print(f"31. Booking Amounts > 6000: {filtered_amounts}")

# 32
registrations_list = [
    {"id": "R1001", "name": "Aarav Shah", "city": "Hyderabad", "status": "Confirmed", "amount": 5000},
    {"id": "R1002", "name": "Simran Kaur", "city": "Mumbai", "status": "Confirmed", "amount": 3500},
    {"id": "R1003", "name": "Faiz Ahmed", "city": "Pune", "status": "Pending", "amount": 7500},
    {"id": "R1005", "name": "Mohit Kapoor", "city": "Delhi", "status": "Cancelled", "amount": 4000}
]
confirmed_regs = list(filter(lambda r: r["status"] == "Confirmed", registrations_list))
print(f"32. Confirmed Registrations: {[r['name'] for r in confirmed_regs]}")

# 33
extracted_cities = list(map(lambda r: r["city"], registrations_list))
print(f"33. Extracted Cities: {extracted_cities}")

# 34
unique_extracted_cities = list(set(map(lambda r: r["city"], registrations_list)))
print(f"34. Unique Cities: {unique_extracted_cities}")

# 35
sorted_regs = sorted(registrations_list, key=lambda r: r["amount"])
print("35. Registrations Sorted by Amount:")
for r in sorted_regs:
    print(f"    {r['name']} - ₹{r['amount']}")
print("\n")

# section D

# 36-38
class Event:
    def __init__(self, event_id, event_name, capacity, ticket_price):
        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price

    def display_event(self):
        print(f"Event [{self.event_id}] {self.event_name} | Capacity: {self.capacity} | Price: ₹{self.ticket_price}")

    def calculate_revenue(self, tickets_sold):
        return tickets_sold * self.ticket_price

# 39
e1 = Event("E101", "AI Innovation Summit", 500, 2500)
e2 = Event("E102", "Leadership Forum", 350, 3500)

# 40-42
class OnlineEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, platform):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.platform = platform

    def display_event(self):
        print(f"[ONLINE] Event [{self.event_id}] {self.event_name} | Platform: {self.platform} | Price: ₹{self.ticket_price}")

# 43-44
class PhysicalEvent(Event):
    def __init__(self, event_id, event_name, capacity, ticket_price, venue):
        super().__init__(event_id, event_name, capacity, ticket_price)
        self.venue = venue

    def display_event(self):
        print(f"[PHYSICAL] Event [{self.event_id}] {self.event_name} | Venue: {self.venue} | Price: ₹{self.ticket_price}")

# 45-46
online_e = OnlineEvent("E103", "Data Bootcamp", 200, 3000, "Zoom")
physical_e = PhysicalEvent("E104", "Startup Connect", 300, 4000, "Delhi Expo Center")

event_catalog = [e1, online_e, physical_e]

print("46. Polymorphism Demonstration:")
for event_obj in event_catalog:
    event_obj.display_event()
print("\n")

