import main
print("1: View Total Revenue, 2: Top Customer, 3: Top City, 4: Ordered Revenue List, 5: Top Selling Product, 6: Average Order Cost, 7: Full Report")

menu = True
while menu:
    choice = input("\nInput your choice (0 for choices, N to exit): ")
    if choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "N", "n"]:
        print("Invalid choice. Please try again.")
    elif choice == "N" or choice == "n":
        menu = False
    else:
        choice = int(choice)
        if choice == 0:
            print("1: View Total Revenue, 2: Top Customer, 3: Top City, 4: Ordered Revenue List, 5: Top Selling Product, 6: Average Order Cost, 7: Full Report")
        if choice == 1:
            print("Total revenue is", main.report["total_revenue"])
        if choice == 2:
            print("The customer that has spent the most is", main.report["top_customer"])
        if choice == 3:
            print("The city that has spent the most is", main.report["top_city"])
        if choice == 4:
            print("The list of customers from highest to lowest spending is:", main.report["ordered_revenue_dict"])
        if choice == 5:
            print("The top selling product is:", main.report["top_products"])
        if choice == 6:
            print("Average order cost is:", main.report["average_order_value"])
        if choice == 7:
            print("The full report is:", main.report)
