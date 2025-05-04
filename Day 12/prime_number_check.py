def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False 
        
    for i in range(2, num):
        
        if num % i == 0:
            return False
        
    return True 

number = int(input("Check this number: "))
print(f"Is {number} prime? {is_prime(number)}")