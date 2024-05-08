class system1:
    def operation1(self):
        print("Subsystem1: Ready!")

class system2:
    def operation1(self):
        print("Subsystem2: Go!")

class facade:
    def __init__(self):
        self._subsystem1 = system1()
        self._subsystem2 = system2()
    
    def operation(self):
        self._subsystem1.operation1
        self._subsystem2.operation1()