# SYMMETRIC DIFFERENCE UPDATE
class MySet:
    def __init__(self):
        self.data = []

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def symmetric_difference_update(self, other):
        yangi = []

        for item in self.data:
            if item not in other.data:
                yangi.append(item)

        for item in other.data:
            if item not in self.data:
                yangi.append(item)

        self.data = yangi

    def show(self):
        print(self.data)

s1 = MySet()
s1.data = [1, 2, 3, 4]

s2 = MySet()
s2.data = [3, 4, 5, 6]

s1.symmetric_difference_update(s2)

s1.show()   
