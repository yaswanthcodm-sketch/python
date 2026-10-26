days = ["Monday", "Tuesday", "Wednesday"]
prepared = [100, 120, 90]
served = [92, 105, 85]
acceptable_limit = 10
total_waste = 0

print("--- Food Waste Report ---")
for i in range(len(days)):
    if prepared[i] <= 0 or served[i] < 0 or served[i] > prepared[i]:
        print(days[i] + ": Invalid meal counts.")
    else:
        leftovers = prepared[i] - served[i]
        waste_percent = leftovers / prepared[i] * 100
        total_waste += leftovers
        print(days[i] + ":")
        print("  Prepared:", prepared[i])
        print("  Served:", served[i])
        print("  Leftovers:", leftovers)
        print("  Waste percentage:", round(waste_percent, 2), "%")
        if waste_percent > acceptable_limit:
            print("  Warning: waste is above 10%.")

print("Total leftover meals:", total_waste)
