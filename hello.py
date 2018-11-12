class TestClass:
    name = "Test"

    def __init__(self):
        print("TTTTTTTTTTT")
    
    def static_method():
        print("STATCI!")
    
    def get_name(self):
        print("QQQQQQQQQQQQQQQQQQ")
        return self.name

    def area(self, x, y):
        return x * y
    
class Child(TestClass):
    def __init__(self):
        super().__init__()
        print ("MY someting")

    def get_name(self):
        t = super().get_name()
        print ("blah")
        return("Child Name:" + self.name)
    
    def area(self, x ,y):
        t = super().area(x,y)
        return t/2

test = TestClass()
child = Child()
child.get_name()

#cmd = input("Input the function name>>")
#getattr(test, cmd)()
#getattr(TestClass, 'static_metho')()