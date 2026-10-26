units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid input: units cannot be negative.")
else:
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50
    if units > 200:
        surcharge = energy_charge * 0.05
    else:
        surcharge = 0

    total = energy_charge + fixed_charge + surcharge
    print("\n--- Electricity Bill ---")
    print("Units consumed:", units)
    print("Energy charge: Rs.", round(energy_charge, 2))
    print("Fixed charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Total bill: Rs.", round(total, 2))
