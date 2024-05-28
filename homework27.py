class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.start = self.start
        self.end = self.end
        return self

    def __next__(self):
        while self.start < self.end:
            self.start += 1
            if self.start % 2 == 0:
                return self.start


    # def __next__(self):
    #     self.start += 1
    #     if self.start % 2 == 0:
    #         if self.start > self.end:
    #             raise StopIteration()
    #         return self.start


en = EvenNumbers(10, 25)
for i in en:
    if i is None:
        break
    print(i)
