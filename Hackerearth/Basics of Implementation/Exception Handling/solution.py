class MyException(Exception):
    def __init__(self, a):
        self.detail = a

    def __str__(self):
        return f"MyException[{self.detail}]"


def solve(arr):
    ans = 0

    for i in range(10):
        for j in range(i + 1, 10):
            ans += arr[i] // arr[j]

    raise MyException(ans)


def main():
    try:
        n = int(input())
        arr = [0] * n
        for i in range(10):
            arr[i] = int(input().strip())

        s = input()
        print(s[10])

        solve(arr)

    except ValueError:
        print("Format mismatch")
    except IndexError:
        print("Index is invalid")
    except ZeroDivisionError:
        print("Invalid division")
    except MyException as e:
        print(e)
    except Exception:
        print("Exception encountered")
    finally:
        print("Exception Handling Completed")


if __name__ == "__main__":
    main()
