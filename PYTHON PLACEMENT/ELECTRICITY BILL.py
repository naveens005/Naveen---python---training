# Inputs
units_consumed = int(input("Enter units consumed: "))
is_senior_citizen = input("Is senior citizen (True/False): ") == "True"
has_solar_panel = input("Has solar panel (True/False): ") == "True"
payment_mode = input("Payment mode (online/offline): ")

# 1. Base Bill Calculation (Slab System)
bill = 0

if units_consumed <= 100:
    bill = units_consumed * 3
elif units_consumed <= 300:
    bill = (100 * 3) + ((units_consumed - 100) * 5)
else:
    bill = (100 * 3) + (200 * 5) + ((units_consumed - 300) * 8)

# 2. Senior Citizen Discount (10%)
if is_senior_citizen:
    bill = bill - (bill * 0.10)

# 3. Solar Panel Discount
if has_solar_panel:
    if units_consumed <= 250:
        bill -= 500
    else:
        bill -= 300

# 4. Payment Mode Surcharge
if payment_mode == "offline":
    if bill < 1000:
        bill += 50
    else:
        bill += 100

# 5. Minimum Payable Rule
if bill < 200:
    bill = 200

# Final Output
print("Final Electricity Bill: ₹", bill)