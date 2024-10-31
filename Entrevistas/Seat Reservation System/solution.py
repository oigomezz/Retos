class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(n, 0, -1))

    def reserve(self) -> int:
        return self.seats.pop()

    def unreserve(self, seat_number: int) -> None:
        left = 0
        right = len(self.seats)
        while left < right:
            middle = left + (right-left)//2
            if self.seats[middle] < seat_number:
                right = middle
            else:
                left = middle + 1

        # In the worst case, it will have a time complexity of O(N)
        self.seats.insert(left, seat_number)
