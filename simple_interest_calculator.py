def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: The principal amount (initial amount).
    :param rate: The interest rate per period.
    :param time: The number of periods.
    :return: The simple interest amount.
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("All inputs must be non-negative values.")

    interest = (principal * rate * time) / 100
    return interest

if __name__ == "__main__":
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the interest rate (in percentage): "))
        time = float(input("Enter the time (in years): "))

        interest = calculate_simple_interest(principal, rate, time)

        print(f"Simple Interest: {interest}")
    except ValueError:
        print("Please enter valid numeric values for the principal, rate, and time.")
