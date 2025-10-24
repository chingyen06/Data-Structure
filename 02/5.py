def product_rec(n, m):
    if (m == 1):
        return n
    else:
        return n + product_rec(n, m-1)
    
def product_ite(n, m):
    result = 0

    for i in range(m):
        result += n

    return result

def main():
    n, m = map(int, input().split())

    print(product_rec(n, m))

    print(product_ite(n, m))


main()