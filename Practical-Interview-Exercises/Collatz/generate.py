"""Generates the Collatz sequence for numbers from 1 to 1000 and saves it to a file."""
data = {1: [4, 2, 1]}


def collatz(n: int) -> list[int]:
    """Function to compute the Collatz sequence for a given number."""
    if n not in data:
        path = []
        next_n = n
        next_n = next_n//2 if next_n % 2 == 0 else 3 * next_n + 1
        path.append(next_n)
        path.extend(collatz(next_n))
        data[n] = path
        return path
    else:
        return data[n]


if __name__ == "__main__":
    with open('collatz.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            key, value = linea.split(":")
            key = int(key.strip())
            value = value.replace("[", "").replace("]", "").strip()
            data[key] = [int(x) for x in value.split(",")]

    for i in range(2, 1001):
        collatz(i)

    ordenados = dict(sorted(data.items(), key=lambda item: int(item[0])))
    for key, value in ordenados.items():
        print(f"{key}: {value}")
