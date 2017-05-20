'''
**Collatz Conjecture** - 

Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process: 
If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1. 
'''

#!/usr/bin/env python

def collatz(num, count = 0):
    if num <= 1:
        return count
    if num % 2 == 0:
        return collatz(num/2, count + 1)
    else:
        return collatz(num*3 + 1, count + 1)


def main():
print collatz(2) #1
print collatz(3) #7
print collatz(4) #2
print collatz(5) #5
print collatz(6) #8

main()