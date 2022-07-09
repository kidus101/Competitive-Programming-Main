class MyCircularDeque:

    def __init__(self, k: int):
        self.qeue=[]
        self.len=k
        

    def insertFront(self, value: int) -> bool:
        if(len(self.qeue)==self.len):
            return False
        else:
            self.qeue.insert(0,value)
            return True

        
        
        

    def insertLast(self, value: int) -> bool:
        if(len(self.qeue)==self.len):
            return False
        self.qeue.append(value)
        return True
        

    def deleteFront(self) -> bool:
        if(len(self.qeue)==0):
            return False
        self.qeue.pop(0)
        return True #O(1)
        

    def deleteLast(self) -> bool:
        if(len(self.qeue)==0):
            return False
        self.qeue.pop(-1)
        return True #O(1)

    def getFront(self) -> int:
        if(len(self.qeue)!=0):
            return self.qeue[0]
        return -1 #O(1)
        

    def getRear(self) -> int:
        if(len(self.qeue)!=0):
            return self.qeue[-1]
        return -1 #O(1)
     

    def isEmpty(self) -> bool:
        if(len(self.qeue)==0):
            return True
        return False #O(1)
        

    def isFull(self) -> bool:
        if(len(self.qeue)==self.len):
            return True #O(1)
