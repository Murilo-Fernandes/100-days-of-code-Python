def is_leap_year(year):
    """Calculate if a year is or not a Leap Year."""
    if year % 4 == 0:
        if year % 100 == 0: 
            if year % 400 == 0:
                return True
            return False
        elif year % 100 != 0:
            return True 
    else:
        return False
  
    
print(is_leap_year(2008))