print()
print("   Welcome to the eShop!")
print("-------------------------")

admin_username = "admin"
admin_password = "pass1"
customer_username = "customer"
customer_password = "pass2"
cashier_username = "cashier"
cashier_password = "pass3"

print("Login required before you can continue.")

logged_in = False
current_role = ""
attempts = 0

while attempts < 3 and logged_in == False:
    entered_username = input("Username: ").strip().lower()
    entered_password = input("Password: ").strip()

    if entered_username == admin_username and entered_password == admin_password:
        current_role = "Admin"
        logged_in = True
    elif (
        entered_username == customer_username and entered_password == customer_password
    ):
        current_role = "Customer"
        logged_in = True
    elif entered_username == cashier_username and entered_password == cashier_password:
        current_role = "Cashier"
        logged_in = True
    else:
        attempts = attempts + 1
        print("Invalid credentials.")
        if attempts < 3:
            print("Please try again.")

if logged_in == False:
    print("Access denied after 3 failed attempts.")
else:
    print("Welcome, " + current_role + "!")

    keep_running = True

    while keep_running == True:
        print()
        print("-------------------------------------------")
        print("Role:", current_role)

        if current_role == "Admin":
            print("1. Process checkout")
            print("2. View role rules")
            print("3. Logout")
            choice = input("Select an option: ")

            if choice == "1":
                subtotal_valid = False
                subtotal = 0.0

                while subtotal_valid == False:
                    subtotal_text = input("Enter subtotal amount: ").strip()
                    try:
                        subtotal = int(subtotal_text)
                        if subtotal >= 0:
                            subtotal_valid = True
                        else:
                            print("Subtotal cannot be negative.")
                    except ValueError:
                        print("Please enter a valid number.")

                coupon_code = input("Enter coupon code (or NONE): ").strip().upper()
                if coupon_code == "NONE":
                    coupon_code = ""

                location_valid = False
                location = ""

                while location_valid == False:
                    location = (
                        input("Enter location (local/out-of-country): ").strip().lower()
                    )
                    if location == "local" or location == "out-of-country":
                        location_valid = True
                    else:
                        print("Invalid location. Try again.")

                tier_discount_rate = 0.0
                if subtotal >= 500000:
                    tier_discount_rate = 0.15
                elif subtotal >= 250000:
                    tier_discount_rate = 0.10
                elif subtotal >= 100000:
                    tier_discount_rate = 0.05
                else:
                    tier_discount_rate = 0.0

                tier_discount = subtotal * tier_discount_rate
                discounted_subtotal = subtotal - tier_discount

                coupon_discount_rate = 0.0
                coupon_valid = False

                if coupon_code == "SAVE10":
                    coupon_discount_rate = 0.10
                    coupon_valid = True
                elif coupon_code == "XMAS15":
                    coupon_discount_rate = 0.15
                    coupon_valid = True
                else:
                    coupon_discount_rate = 0.0

                if coupon_code == "":
                    print("No coupon entered.")
                elif coupon_valid == True:
                    print("Coupon accepted.")
                else:
                    print("Coupon rejected.")

                coupon_discount = discounted_subtotal * coupon_discount_rate
                taxable_amount = discounted_subtotal - coupon_discount

                tax_rate = 0.0
                if location == "local":
                    tax_rate = 0.05
                elif location == "out-of-country":
                    tax_rate = 0.12
                else:
                    tax_rate = 0.15

                tax = taxable_amount * tax_rate
                final_total = taxable_amount + tax

                print()
                print(f"""------Order Summary for {current_role}------'
Subtotal:           UGX {subtotal:,.0f}
Tier discount:      -UGX {tier_discount:,.0f}
Coupon discount:     -UGX {coupon_discount:,.0f}
Taxable amount:      UGX {taxable_amount:,.0f}
Tax rate:           {tax_rate * 100:.0f}%
Tax:                 UGX {tax:,.0f}
Final total:         UGX {final_total:,.0f}
----------------------------------""")

            elif choice == "2":
                print("Admin has full access to checkout, rules, and logout.")
                print("Customer can only shop and checkout.")
                print("Cashier can only process sales and logout.")
            elif choice == "3":
                keep_running = False
                print("Logging out...")
            else:
                print("Invalid menu option.")

        elif current_role == "Customer":
            print("1. Shop and checkout")
            print("2. Logout")
            choice = input("Select an option: ").strip()

            if choice == "1":
                subtotal_valid = False
                subtotal = 0.0

                while subtotal_valid == False:
                    subtotal_text = input("Enter subtotal amount: ").strip()
                    try:
                        subtotal = int(subtotal_text)
                        if subtotal >= 0:
                            subtotal_valid = True
                        else:
                            print("Subtotal cannot be negative.")
                    except ValueError:
                        print("Please enter a valid number.")

                coupon_code = input("Enter coupon code (or NONE): ").strip().upper()
                if coupon_code == "NONE":
                    coupon_code = ""

                location_valid = False
                location = ""

                while location_valid == False:
                    location = (
                        input("Enter location (local/out-of-country): ").strip().lower()
                    )
                    if location == "local" or location == "out-of-country":
                        location_valid = True
                    else:
                        print("Invalid location. Try again.")

                tier_discount_rate = 0.0
                if subtotal >= 500000:
                    tier_discount_rate = 0.15
                elif subtotal >= 250000:
                    tier_discount_rate = 0.10
                elif subtotal >= 100000:
                    tier_discount_rate = 0.05
                else:
                    tier_discount_rate = 0.0

                tier_discount = subtotal * tier_discount_rate
                discounted_subtotal = subtotal - tier_discount

                coupon_discount_rate = 0.0
                coupon_valid = False

                if coupon_code == "SAVE10":
                    coupon_discount_rate = 0.10
                    coupon_valid = True
                elif coupon_code == "XMAS15":
                    coupon_discount_rate = 0.15
                    coupon_valid = True
                else:
                    coupon_discount_rate = 0.0

                if coupon_code == "":
                    print("No coupon entered.")
                elif coupon_valid == True:
                    print("Coupon accepted.")
                else:
                    print("Coupon rejected.")

                coupon_discount = discounted_subtotal * coupon_discount_rate
                taxable_amount = discounted_subtotal - coupon_discount

                tax_rate = 0.0
                if location == "local":
                    tax_rate = 0.05
                elif location == "out-of-country":
                    tax_rate = 0.08
                else:
                    tax_rate = 0.15

                tax = taxable_amount * tax_rate
                final_total = taxable_amount + tax

                print()

                print(f"""---Order Summary for {current_role}---
Subtotal:           UGX {subtotal:,.0f}
Tier discount:      -UGX {tier_discount:,.0f}
Coupon discount:     -UGX {coupon_discount:,.0f}
Taxable amount:      UGX {taxable_amount:,.0f}
Tax rate:           {tax_rate * 100:.0f}%
Tax:                 UGX {tax:,.0f}
Final total:         UGX {final_total:,.0f}
----------------------------------""")

            elif choice == "2":
                keep_running = False
                print("Logging out...")
            else:
                print("Invalid menu option.")

        elif current_role == "Cashier":
            print("1. Process sale")
            print("2. Logout")
            choice = input("Select an option: ").strip()

            if choice == "1":
                subtotal_valid = False
                subtotal = 0.0

                while subtotal_valid == False:
                    subtotal_text = input("Enter subtotal amount: ").strip()
                    try:
                        subtotal = int(subtotal_text)
                        if subtotal >= 0:
                            subtotal_valid = True
                        else:
                            print("Subtotal cannot be negative.")
                    except ValueError:
                        print("Please enter a valid number.")

                coupon_code = input("Enter coupon code (or NONE): ").strip().upper()
                if coupon_code == "NONE":
                    coupon_code = ""

                location_valid = False
                location = ""

                while location_valid == False:
                    location = (
                        input("Enter location (local/out-of-country): ").strip().lower()
                    )
                    if location == "local" or location == "out-of-country":
                        location_valid = True
                    else:
                        print("Invalid location. Try again.")

                tier_discount_rate = 0.0
                if subtotal >= 500000:
                    tier_discount_rate = 0.15
                elif subtotal >= 250000:
                    tier_discount_rate = 0.10
                elif subtotal >= 100000:
                    tier_discount_rate = 0.05
                else:
                    tier_discount_rate = 0.0

                tier_discount = subtotal * tier_discount_rate
                discounted_subtotal = subtotal - tier_discount

                coupon_discount_rate = 0.0
                coupon_valid = False

                if coupon_code == "SAVE10":
                    coupon_discount_rate = 0.10
                    coupon_valid = True
                elif coupon_code == "XMAS15":
                    coupon_discount_rate = 0.15
                    coupon_valid = True
                else:
                    coupon_discount_rate = 0.0

                if coupon_code == "":
                    print("No coupon entered.")
                elif coupon_valid == True:
                    print("Coupon accepted.")
                else:
                    print("Coupon rejected.")

                coupon_discount = discounted_subtotal * coupon_discount_rate
                taxable_amount = discounted_subtotal - coupon_discount

                tax_rate = 0.0
                if location == "local":
                    tax_rate = 0.05
                elif location == "out-of-country":
                    tax_rate = 0.08
                else:
                    tax_rate = 0.15

                tax = taxable_amount * tax_rate
                final_total = taxable_amount + tax

                print()
                print(f"""---Order Summary for {current_role}---
Subtotal:           UGX {subtotal:,.0f}
Tier discount:      -UGX {tier_discount:,.0f}
Coupon discount:     -UGX {coupon_discount:,.0f}
Taxable amount:      UGX {taxable_amount:,.0f}
Tax rate:           {tax_rate * 100:.0f}%
Tax:                 UGX {tax:,.0f}
Final total:         UGX {final_total:,.0f}
----------------------------------""")

            elif choice == "2":
                keep_running = False
                print("Logging out...")
            else:
                print("Invalid menu option.")
