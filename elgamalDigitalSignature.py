import math
import random
from decimal import Decimal
import time
import gmpy2
def findGenerator(n):
    group = set(range(1,n))
    for candidate in group:
        s = set()
        for pot in group:
            s.add(gmpy2.powmod(candidate,pot,n))
        if group == s:
            print("Generator",candidate)
            return candidate
    raise Exception("No generator found")

def generateK(p):
    k = random.randint(1,p-2)
    while 1 != math.gcd(k,p-1):
        k = random.randint(1,p-2)
    print("k",k)
    return k

def main():
    ms1 = time.time()
    
    p = 662029 
    alpha = findGenerator(p)
    a = random.randint(1,p - 2) 
    beta = gmpy2.powmod(alpha, a, p)

    k = generateK(p)
    gamma = pow(alpha,k)
    x = random.randint(1,p)

    delta = ((x - a*gamma)*gmpy2.powmod(k,-1,p-1)%(p-1))
    print("delta",delta)

    betaGamma = gmpy2.powmod(beta, gamma, p)
    gammaDelta = gmpy2.powmod(gamma, delta, p)

    print("betaGamma",betaGamma)
    print("gammaDelta",gammaDelta)

    v1 = (betaGamma * gammaDelta)%p
    v2 = pow(alpha, x, p)

    print("v1",v1)
    print("v2",v2)

    ms2 = time.time()

    print("time taken",ms2 - ms1)
if __name__ == "__main__":
    main()
