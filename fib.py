
'''
Implement an iterative version (using a loop instead of recursion) of fib 
and compare runtimes. (2 Points).

Note that in each step of the computation, you need only the values of 
the last two fibonacci numbers in the sequence to compute the next value.
'''

def fib(n):
    '''Returns the nth Fibonacci number'''
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def fibit(n):
    pass # your code

if __name__ == '__main__':
    for i in range(33):
        print(i, fib(i))
    for i in range(33):
        print(i, fibit(i))

