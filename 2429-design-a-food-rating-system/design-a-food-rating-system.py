import heapq

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f = {}
        self.c = {}
        for x, y, z in zip(foods, cuisines, ratings):
            self.f[x] = [y, z]
            if y not in self.c:
                self.c[y] = []
            heapq.heappush(self.c[y], (-z, x))

    def changeRating(self, food: str, new: int) -> None:
        y, _ = self.f[food]
        self.f[food][1] = new
        heapq.heappush(self.c[y], (-new, food))

    def highestRated(self, y: str) -> str:
        h = self.c[y]
        while h:
            r, x = h[0]
            if -r == self.f[x][1]:
                return x
            heapq.heappop(h)
