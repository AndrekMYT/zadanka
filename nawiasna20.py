import sys


n = int(sys.stdin.readline())
if n == 1:
    print('()')
    exit()
if n %2 == 0:
    x = '('*n
    y = ')' *n
    print(f'{x}{y}')
else:
    nmod = n//2
    x = '('*nmod
    y = ')' *nmod
    print(f'{x}{y}{x}{y}')