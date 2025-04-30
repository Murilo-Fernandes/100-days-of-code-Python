def is_leap_year(year):
    """This function checks if a given year is a leap year or not."""
    if year % 4 == 0: 
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False 
        return True
    else:
        return False
    # Don't change the function name.

year = int(input("Enter a year: "))
print(f"is {year} a leap year? {is_leap_year(year)}") 