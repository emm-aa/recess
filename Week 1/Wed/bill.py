print("\nWelcome to the BILL SPLITTER\n")

while True:
    try:
        bill_amount = int(input("Enter the total bill amount: "))
        number_of_people = int(input("Enter the number of people splitting bill: "))
        tip_percentage = int(input("Enter tip percentage (10%/20%/30% or custom): "))
        break
    except ValueError:
        print("Invalid input. Please enter digits only.\n")


tip_amount = (tip_percentage * bill_amount) / 100
total_bill = bill_amount + tip_amount
bill_per_person = total_bill / number_of_people

print(f"""\n\t***RECEIPT***
Tip Amount\t= ({tip_percentage} * {bill_amount:,}) / 100
\t\t= {tip_amount:,.0f}

Total Bill\t= {bill_amount:,} + {tip_amount:,.0f}
\t\t= {total_bill:,.0f}

Amount per person = {total_bill:,.0f} / {number_of_people}
\t\t= {bill_per_person:,.0f}

    THANKS FOR THE SUPPORT
\t*************""")
