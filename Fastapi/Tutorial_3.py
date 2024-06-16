#Static type checker MyPy

class rectangle:
    def __init__(self,width:int,height:int):
        self.width=width
        self.height=height

    def area(self):
        return (self.width*self.height)

def division(a:int,b:int)->float:
    return a/b

def sayhello(name:str)->str:
    print(name.capitalize())
    return f"Hello {name}"

if __name__=="__main__":
    print(division(7,2))

    print(sayhello("joe"))

    rect = rectangle(5,4)
    print(rect.area())


