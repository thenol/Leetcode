def gcd(a, b):
    """
    辗转相除法求最大公约数
    """
    m, n = max(a, b), min(a, b)
    while m % n:
        m, n = n, m % n
    return n


if __name__ == "__main__":
    print(gcd(6, 4))
