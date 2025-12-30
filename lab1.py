class node:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.next=None
        self.prev=None

class doublell:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,name,id,loc):
        nd=node(name,id)
        if(self.head==None): #no list
            self.head = nd
            self.tail = nd
        else:
            if loc==0: #first node
                self.head.prev=nd
                nd.next=self.head
                self.head=nd
            else:
                temp=self.head
                i=0
                while i < loc-1 and temp!=None:
                    temp=temp.next
                    i=i+1
                if temp == self.tail or temp==None:
                    self.tail.next=nd
                    nd.prev=self.tail
                    self.tail=nd
                else:
                    nd.next=temp.next
                    temp.next.prev=nd
                    nd.prev=temp
                    temp.next=nd
    def search(self,id):
        nd = self.head
        location=0
        if self.head!=None:
            while nd.id!=id and nd!=None:
                nd=nd.next
                location=location+1
        return location

    def update(self,old_id,new_id):
        location=self.search(old_id)
        i = 0
        temp = self.head
        while i < location:
            temp = temp.next
            i = i + 1
        temp.id = new_id

    def delete(self,id):
        location=self.search(id)
        i=0
        temp=self.head
        while i < location:
            temp=temp.next
            i=i+1
        if temp==self.head:
            self.head==self.head.next
            self.head.prev=None
        elif temp == self.tail:
            self.tail=self.tail.prev
            self.tail.next=None
        else:
            temp.next.prev=temp.prev
            temp.prev.next=temp.next

    def printlist(self):
        temp=self.head
        while temp!=None:
            print("Name:",temp.name," ID:",temp.id)
            temp=temp.next

ll=doublell()
ll.insert("yasmeen",100,0)
ll.insert("ali",200,1)
ll.insert("sara",300,2)
ll.insert("mohamed",400,3)
ll.printlist()
print('After Update:')
ll.update(400,250)
ll.delete(200)
ll.printlist()