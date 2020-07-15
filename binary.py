import copy
import random
import math
import matplotlib.pyplot as plt

def avg(lst):                   #function to calculate average of a list
    return sum(lst)*1.0/len(lst)


class Binary:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.val=val
    def add(self,new):      #recurvise method to add a node to the binary tree
        if self.val==None:
            self.val=new.val
            self.left=new.left
            self.right=new.right
        temp=self
        if new.val<self.val:
            if self.left==None:
                self.left=copy.deepcopy(new)
            else:
                self.left.add(new)
        if new.val>self.val:
            if self.right==None:
                self.right=copy.deepcopy(new)
            else:
                self.right.add(new)
    def height(self):       #recurvise method to find the height of a binary tree
        if self.left!=None and self.right!=None:
            return max(self.left.height(),self.right.height())+1
        if self.left==None and self.right!=None:
            return self.right.height()+1
        if self.left!=None and self.right==None:
            return self.left.height()+1
        return 0



avg_h=[]        #list to store average height of a binary tree having n nodes for each n
log_n=[]        #list to store log n to the base 2
for n in range(1,51):
    log_n.append(math.log(n,2))
    h=[]        #list to store height of binary tree having n nodes
    for j in range(100):    #generating 100 binary trees of n nodes
        b=Binary(None)
        l=[]
        i=0
        while i<n:          #adding n elements to the binary tree
            new=random.randint(1,200)
            if new in l:
                i-=1
            else:
                l.append(new)
                b.add(Binary(new))
            i+=1
        h.append(b.height())    #calculating and appending the height of binary tree
    avg_h.append(avg(h))        #calculating and appending the average height of binary tree



plt.plot(range(1,51),avg_h)     #plotting the resulted graph
plt.plot(range(1,51),log_n)     #plotting the best case of binary search tree
plt.plot(range(1,51),range(1,51))   #plotting the worst case of binary search tree
plt.text(30,29,'WORST CASE',color='red')
plt.text(30,math.log(30,2)-1.5,'BEST CASE',color='green')
plt.text(30,11,'RESULT',color='blue')
plt.axis([1,50,0,50])
plt.xlabel('NUMBER OF NODES')
plt.ylabel('AVGERAGE HEIGHT')
plt.show()
