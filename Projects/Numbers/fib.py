'''**Fibonacci Sequence** -
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number. 
'''

#!/usr/bin/env python

def fib(N):
    if N == 1:
        return [1, 0]
    else:
        terms = fib(N - 1)
        terms = [terms[0] + terms[1], terms[0]]
        return terms


def main():
    print "Enter a positive integer."
    s = raw_input("Which term in the Fibonacci sequence you want to see? ")
    N = int(s)
    print fib(N)[1]


if __name__ == "__main__":
    main()