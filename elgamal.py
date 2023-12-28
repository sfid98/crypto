import random

def findGenerator(n):
    s = set(range(1,n))
    for candidate in s:
        g = set()
        for pot in s:
            g.add((candidate**pot)%n)
        if g == s:
            print("generator",candidate)
            return candidate
    raise Exception("cannot find generator")


def encrypt(g,n,y):
    m = random.randint(1,n)
    k = random.randint(1,n)
    print("message",m)
    c1 = g ** k
    c2 = m*(y**k)
    return dict(c1 = c1, c2 = c2)

def decrypt(x,n,encMessage):
    c1 = encMessage["c1"]
    c2 = encMessage["c2"]
    dec = (c2*pow(c1**x,-1,n))%n
    print("dec",dec)

def main():
    n = 97
    g = findGenerator(n)
    x = random.randint(1,n)
    y = g ** x
    print("x", x)
    print("public key is", g,n,y)

    encMessage = encrypt(g,n,y)
    decrypt(x,n,encMessage)

if __name__ == "__main__":
    main()



