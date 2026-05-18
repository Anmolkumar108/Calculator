# ====================================
# This Is A Most Advance Calculator
# =====================================
while True:
    print("\n=== Do You Want To Use Calculator And Discount Calculator And Vijaly Wheel Units And Date Of Birth Calculator And GST Calculator ===")
    choice = input("\n Enter C for Calculator, D for Discount Calculator, V for Vijaly Wheel Units, B for Date Of Birth Calculator, G for GST Calculator: ").strip().upper()

    if choice == "C":
        Print("=== Normal Calculator ===")
        num1 = int(input("Please Sir Enter First Number: "))
        num2 = int(input("Please Sir Enter Second Number: "))
        operation = input("Please Sir Enter Operation (+, -, *, /): ").strip()
        
        if operation == "+":
            result = num1 + num2
            print("The Addition of", num1, "and", num2, "is", result)
        elif operation == "-":
            result = num1 - num2
            print("The Subtraction of", num1, "and", num2, "is", result)
        elif operation == "*":
            result = num1 * num2
            print("The Multiplication of", num1, "and", num2, "is", result)
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("The Division of", num1, "and", num2, "is", result)
        else:
            print("Sorry Sir Invalid Operation")

    elif choice == "D":
        print("=== Amount Discount Calculator ===")
     price = int(input("Please Sir Enter The Price Of The Product: "))
        discount = int(input("Please Sir Enter The Discount Percentage (%): "))
        discount_amount = (price * discount) / 100
        final_price = price - discount_amount
        print("The Final Price After Discount is:", final_price)

    elif choice == "V":
        print("=== Vijaly Wheel Calculator ===")
        will = int(input("Please Sir Enter The Units Of Vijaly Wheel: "))
        if will > 100:
            print("You Have To Pay 100 Rs")
        elif will > 50:
            print("You Have To Pay 50 Rs")
        elif will > 25:
            print("You Have To Pay 25 Rs")
        elif will > 10:
            print("You Have To Pay 10 Rs")
        else:
            print("You Have To Pay 5 Rs")

    elif choice == "B":
        print("=== Check Date Of Birth  ===")
        print("Please Sir Enter Your Date Of Birth (dd mm yyyy):", end="")
        b_day, b_month, b_year = map(int, input().split())

        print("Please Sir Enter Today's Date (dd mm yyyy):", end="")
        t_day, t_month, t_year = map(int, input().split())

        if t_day < b_day:
            t_day += 30
            t_month -= 1

        if t_month < b_month:
            t_month += 12
            t_year -= 1

        r_day = t_day - b_day
        r_month = t_month - b_month
        r_year = t_year - b_year

        print("\n--- Your Age ---")
        print(f"{r_year} years, {r_month} months, {r_day} days")

# GST Calculator
    elif choice == "G":
        print("=== Gst Calculator ===")
        print("\n=== C . To Calculate GST Amount ===")
        print("\n=== R . To Remove GST Amount ===")
        choice = input("Please Sir Enter Your Choice (C or R) : ").strip().upper()
        
        if choice == "C":
            amount = float(input("Please Sir Enter The Original Amount:"))
            gst_rate = float(input("Please Sir Enter The GST Rate (%):"))
            gst_amount = (amount * gst_rate) / 100
            total_Price = amount + gst_amount
            print(f"\n--- Result ---")
            print(f"Original Amount: {amount}")
            print(f"GST Amount: ({gst_amount}%): {gst_amount}")
            print(f"Total Bill (To GST): {total_Price}")

        elif choice == 'R':
            total_price = float(input("Please Sir Enter The Total Price (Including GST): "))
            gst_rate = float(input("Please Sir Enter The GST Rate (%): "))
            gst_amount = (total_price * gst_rate) / (100 + gst_rate)
            original_amount = total_price - gst_amount
            print(f"\n--- Result ---")
            print(f"Total Price (Including GST): {total_price}")
            print(f"Original Amount: {original_amount}")
            print(f"GST Amount: ({gst_rate}%): {gst_amount}")

    else:
        print("Invalid choice. Please enter C, D, V, B, or G.")

    again = input("\nDo you want to do any other calculation? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("--- The calculator is turning off. Thank you! ---")
        break

            
