class mystack(list):
    """a Super Cool Class"""
    def push(self,a):
        self.append(a)

    def peek(self):
        if self.isEmpty() == False:
            return self[-1]
        return None

    def isEmpty(self):
        if len(self) == 0:
            return True
        return False
        

#hallo = mystack()

#hallo.push("ha")

#print(hallo.isEmpty())

#print(hallo.peek())

#hallo.pop()

#print(hallo.isEmpty())

