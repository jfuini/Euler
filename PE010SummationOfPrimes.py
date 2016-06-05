# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 11:43:05 2016

@author: John Fuini


PE 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import numpy as np

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if np.mod(n,i) == 0:
            return False
    return True
   
    
def next_prime(n):
    num = n
    while True:
        num = num + 1
        if is_prime(num):
            yield num
            
def prime_sum(max):
    sum = 0
    prime_generator = next_prime(1)
    while True:
        prime_num = next(prime_generator) 
        if prime_num >= max:
            break
        else:
            sum = sum + prime_num
    return sum
    
print(prime_sum(2000000))
    
    
    
    
    
    