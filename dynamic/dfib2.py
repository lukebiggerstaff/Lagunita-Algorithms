import sys

def fib(n):
    back1, back2 = 1, 0
    for i in range(2, n+1):
        current = back1 + back2
        back2 = back1
        back1 = current

    return current


if __name__ == '__main__':
    result = fib(int(sys.argv[1]))
    print(result)
