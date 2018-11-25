class mystack(list):
    """a Super Cool Class"""
    def push(self,a):
        self.append(a)

    def peek(self):
        return self[-1]

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

