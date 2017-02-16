class Iterator:
    def __init__(self, value):
        self.number = value
        self.index = len(value)

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.number[self.index]


class val:
    def __init__(self):
        self.num = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "\n"]

    def Iter(self):
        return Iterator(self.num)


if __name__ == "__main__":
    num = val()
    for vall in num.Iter():
        print(vall, end=' ')

    
  
