
def calculate_bonus(salary, rating):
    rating = rating.lower()

    if rating == "excellent":
        bonus = salary * 0.20
    elif rating == "good":
        bonus = salary * 0.10
    elif rating == "average":
        bonus = salary * 0.05
    elif rating == "poor":
        bonus = 0
    else:
        return None

    return bonus


def display_report(name, salary, rating, bonus):
    print("\n----- Employee Report -----")
    print("Employee Name:", name)
    print("Monthly Salary:", salary)
    print("Performance Rating:", rating.capitalize())
    print("Monthly Bonus:", bonus)
    print("Annual Salary with Bonus:", salary * 12 + bonus * 12)


name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: "))
rating = input("Enter performance rating: ")

bonus = calculate_bonus(salary, rating)

if bonus is None:
    print("Invalid rating! Please enter Excellent, Good, Average, or Poor.")
else:
    display_report(name, salary, rating, bonus)
