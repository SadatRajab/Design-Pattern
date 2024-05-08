class Memento:
    def __init__(self,file,content):
        self.file=file
        self.content=content

class x :
    def __init__(self,file):
        self.file=file
        self.content=""

    def write(self,string):
        self.content+=string
    
    def save(self):
        return Memento(self.file,self.content)
    

class y:
    def save(self,writer):
        self.mem=writer.save()
    
    def undo(self,writer):
        writer.undo(self.mem)

if __name__=="__main":
    carekater=y()
    writer=x("GFG.text")
    
    writer.write("frist Data save")
    print(writer.content)

    carekater.save(writer)
    
    writer.write("Second Data Save")
    
    carekater.undo(writer)
    
    print(writer.content)