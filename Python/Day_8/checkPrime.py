def checkPrime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime
        
        
checkNum = int(input())

is_prime = checkPrime(checkNum)

if is_prime:
    print("is Prime")
else:
    print("not Prime")