class Calculator: 
    def __init__(self,id):
        self.id=id
    
    def add(self,x,y):
        return x+y

    def getId(self):
        print("Calculator id:"+self.id)

class CoolCalculator(Calculator):
    def __init__(self,id):
        super(CoolCalculator,self).__init__(id)

    def getId(self):
        print("Cool calculator id"+self.id)

cc = CoolCalculator("CC111")
print(cc.add(1,2))
cc.getId()