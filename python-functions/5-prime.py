#!/usr/bin/env python3


def is_prime(number):
    
    if number <= 1:
        return False
    
    elif number == 2:
        return True
    
    elif number % 2 == 0:
        return False
    
    else:
    
        limit = int(number ** 0.5)
    
        for divisor in range(3, limit + 1, 2):
    
            if number % divisor == 0:
                return False
    
        return True


