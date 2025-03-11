def gcd(a, b):
    """辗转相除法求最大公约数，假设 a > b"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """计算最小公倍数"""
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    # 示例
    a = 12
    b = 18
    print(f"{a} 和 {b} 的最小公倍数是: {lcm(a, b)}")
