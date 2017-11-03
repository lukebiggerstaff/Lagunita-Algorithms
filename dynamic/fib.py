import sys

def dfib(arg):
    if arg <= 2: return 1
    else: f = dfib(arg -1) + dfib(arg-2)
    return f

if __name__ == '__main__':
    result = dfib(int(sys.argv[1]))
    print(result)
