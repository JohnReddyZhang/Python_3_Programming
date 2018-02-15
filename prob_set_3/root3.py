import sys
lam = lambda x: 'FizzBuzz' if x % 15 == 0 else ('Buzz' if x % 5 == 0 else ('Fizz' if x % 3 == 0 else (x)))
for item in [lam(x) for x in range(1,int(sys.argv[1])+1)]: print(item)