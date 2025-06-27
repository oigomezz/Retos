"""Module providing a function to compute the Collatz sequence for a given number."""


def collatz(n: int) -> list[int]:
    """Function computing the Collatz sequence for a given number."""
    if n == 1:
        return [4, 2, 1]
    path = []
    next_n = n
    while next_n > 1:
        next_n = next_n//2 if next_n % 2 == 0 else 3 * next_n + 1
        path.append(next_n)
    return path


if __name__ == "__main__":
    data = {}
    with open('collatz.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            key, value = linea.split(":")
            key = int(key.strip())
            value = value.replace("[", "").replace("]", "").strip()
            data[key] = [int(x) for x in value.split(",")]

        for key, value in data.items():
            print(f"{key}: {len(value)}")
