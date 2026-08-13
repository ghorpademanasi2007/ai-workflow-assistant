# Simple AI Agent using Python

def agent():
    print("Welcome to My AI Agent!")
    print("I can help you with basic tasks.")
    
    while True:
        print("\nChoose an option:")
        print("1. Greet")
        print("2. Tell the date")
        print("3. Solve a simple calculation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            print("Hello,", name + "! Nice to meet you.")

        elif choice == "2":
            from datetime import datetime
            today = datetime.now()
            print("Today's date is:", today.strftime("%d-%m-%Y"))

        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == "+":
                print("Answer:", num1 + num2)
            elif operator == "-":
                print("Answer:", num1 - num2)
            elif operator == "*":
                print("Answer:", num1 * num2)
            elif operator == "/":
                if num2 != 0:
                    print("Answer:", num1 / num2)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operator.")

        elif choice == "4":
            print("Thank you for using the AI Agent!")
            break

        else:
            print("Invalid choice. Please try again.")


agent()