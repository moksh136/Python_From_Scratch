from tools import mock_interview, password_tool, time_tool, name_game, lucky_tool, health_tool
import math

def show_menu():
    print("\n===== College Fun Toolkit =====")
    print("1. Check Password Strength")
    print("2. Roast or Compliment Generator")
    print("3. Typing Speed Test")
    print("4. Lucky Number + Square Root")
    print("5. Find Your Birthday's Weekday")
    print("6. Show Current Time")
    print("7. let's have an mock interview")
    print("8. BMI Health Checker")
    print("9. Exit")

def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice (1-9): "))

        match choice:
            case 1:
                pwd = input("Enter a password to check strength: ")
                score = password_tool.calculate_strength(pwd)
                print(f"Password strength score: {score}/3")

            case 2:
                name = input("Enter your name: ")
                mode = input("Type 'r' for Roast or 'c' for Compliment: ").lower()
                match mode:
                    case "r":
                        print(name_game.get_roast(name))
                    case _:
                        print(name_game.get_compliment(name))

            case 3:
                sentence = "Python is fun when you understand functions and modules"
                wpm = time_tool.typing_speed_test(sentence)
                print(f"Your typing speed: {wpm} WPM")

            case 4:
                lucky = lucky_tool.lucky_number()
                print(f"todays lucky number is: {lucky}")
                print(f"Square root of lucky number: {round(math.sqrt(lucky), 2)}")

            case 5:
                year = int(input("Birth year: "))
                month = int(input("Birth month: "))
                day = int(input("Birth day: "))
                weekday = lucky_tool.birthday_weekday(year, month, day)
                print(f"your birthday was {weekday} ")

            case 6:
                print(f"Current time: {time_tool.get_current_time()}")

            case 7:
                print("\n--- Quick mock Time! ---")
                score = mock_interview.run_mock()
                print(f"\nyour final score: {score}/3")
                match score:
                    case 3:
                        print("you got full marks 🔥")
                    case 1 | 2:
                        print("not bad 👌")
                    case _:
                        print("Better luck next time")

            case 8:
                weight = float(input("enter your weight in kg: "))
                height = float(input("enter your height in cm: "))
                bmi = health_tool.calculate_bmi(weight, height)
                category = health_tool.bmi_category(bmi)
                tip = health_tool.health_tip(category)
                print(f"\nyour BMI: {bmi}")
                print(f"Category: {category}")
                print(f"Tip: {tip}")

            case 9:
                print("Thankyou for using this toolkit !!")
                break

            case _:
                print("invalid choice!! choose a number b/w 1 to 9")

if __name__ == "__main__":
    main()