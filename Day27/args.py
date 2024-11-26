
def function(*args):
    soma = 0
    for i in args:
        soma += i
    return soma

print(function(1,2,3,4,4,34,334,2,43))

def calcular(n, **kwargs):
    n += kwargs["soma"]
    print(n)
    n *= kwargs["mult"]
    print(n)
    n -= kwargs["sub"]
    print(n)
    n /= kwargs["div"]
    print(n)

calcular(5, soma=5, mult=3, sub=10, div=4)