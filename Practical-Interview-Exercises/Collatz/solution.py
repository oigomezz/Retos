def collatz(n):
    if n == 1:
        return [4, 2, 1]
    path = []
    next_n = n
    while next_n > 1:
        next_n = next_n//2 if next_n % 2 == 0 else 3 * next_n + 1
        path.append(next_n)
    return path


if __name__ == "__main__":
    n = int(input("Ingrese numero a verificar: "))
    print(n, ":", collatz(n))
