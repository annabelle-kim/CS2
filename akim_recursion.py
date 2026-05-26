def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def summation(n):
    if n ==1:
        return 1
    else:
        return n+summation(n-1)

def exponential(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * exponential(base,exponent-1)
    
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def sum_digits(n):
    if n==0:
        return 0
    else:
        return (n % 10) + sum_digits(n//10)
    
def product_digits(n):
    if n==0:
        return 0
    elif n<10:
        return n
    else:
        return (n % 10)*product_digits(n//10)

def whole_prod(n1,n2):
    if n1 == 0:
        return 0
    elif n2 == 0:
        return 0
    else:
        return n1+whole_prod(n1,n2-1)
    
def sum_range(start, end):
    if start>end:
        return 0
    else:
        return start + sum_range(start+1, end)

def reverse_digits(n):
    if n < 10:
        return n
    return str(n%10) + str(reverse_digits(n//10))

def gcd(num1, num2):
    if num2 ==0:
        return num1
    else:
        return gcd(num2 , num1%num2)
    

def main():
    fac_value = factorial(5)
    print(fac_value)
    sum_value = summation(5)
    print(sum_value)
    exp_value = exponential(2,5)
    print(exp_value)
    fib_value = fibonacci(9)
    print(fib_value)
    sumdig_value = sum_digits(52)
    print(sumdig_value)
    prodig_value = product_digits(34)
    print(prodig_value)
    whole_val = whole_prod(5,4)
    print(whole_val)
    sum_range_val = sum_range(1,7)
    print(sum_range_val)
    reverse_val = reverse_digits(54)
    print(reverse_val)
    gcd_val = gcd(15,20)
    print (gcd_val)

main()