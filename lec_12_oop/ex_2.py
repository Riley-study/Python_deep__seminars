class Iter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop):
            return chr(i)
        raise StopIteration


chars = Iter(65, 91) # вызывает на печать бесконечное ААААААААА, так как кажый раз при вызове некст
# передается один и тот же диапазон. Чтобы не было зыцикливания нужен цикл while
for c in chars:
    print(c)
