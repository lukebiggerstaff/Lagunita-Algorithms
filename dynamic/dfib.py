import sys

def fib(n):
    memo = dict()

    def fibr(num):
        if num in memo: return memo[num]
        if num <= 2: f = 1
        else: f = fibr(num -1) + fibr(num-2)
        memo[num] = f
        return f

    return fibr(n)


if __name__ == '__main__':
    result = fib(int(sys.argv[1]))
    print(result)
