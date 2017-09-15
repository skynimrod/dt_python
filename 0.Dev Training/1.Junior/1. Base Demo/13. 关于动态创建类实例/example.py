class testclass():
    name = ""
    def setname(self, strs):
        self.name = strs
        
    def show(self):
        print(self.name)


m = __import__('.', globals(), locals(), ['testclass']) 
c = getattr(m, 'testclass') 
myobject = c()

print(myobject)
