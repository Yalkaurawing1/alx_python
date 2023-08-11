#!/usr/bin/env python3

def fibonacci_sequence(n):
    
    if not isinstance(n, int) or n < 0:
        return []
    
    fib_list = []
    
    a = 0
    b = 1
    
    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b
    
    return fib_list


