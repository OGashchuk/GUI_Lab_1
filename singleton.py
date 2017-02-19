class Singleton():
    obj = None
    b = 0
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *args, **kwargs)
        return cls.obj
    
obj1 = Singleton()
obj1.b = 10
obj2 = Singleton()
print(obj2.b)
print(obj2 is obj1)
