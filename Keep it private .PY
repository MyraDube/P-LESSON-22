class myClass:
    __PrivateVar = 27;
    def __privMeth(self):
        print("I am inside class myClass")
    def hello(self):
        print("Private Variable value:", myClass.__PrivateVar)
foo = myClass()
foo.hello()
foo.__privMeth
