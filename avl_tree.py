"""
COS226 HW2: AvL Tree
Andrew Atwater
This assignment provides logic to add and remove nodes from an AVL tree, while rebalancing and rotating as needed
"""





from binaryVisualizer import *

class AVLTree(BinaryTree):
    
    #overwrite add
    def add(self, data):
        self.head = self.addRecursive(self.head, data)
            
    def addRecursive(self, cur, data):
        
        if cur == None:
            return Node(data)

        if data < cur.data:
            cur.left = self.addRecursive(cur.left, data)

        elif data > cur.data:
            cur.right = self.addRecursive(cur.right, data)

        else:
            print(f"Data {data} already exists, cannot add")
            return cur
        
        cur.height = 1 + max(self.calcHeight(cur.left), self.calcHeight(cur.right))

        return self.rebalance(cur)
    
    def search(self, data):

        cur = self.head
        depth = 0

        while cur != None:
            if data == cur.data:
                return depth
            
            elif data < cur.data:
                cur = cur.left

            elif data > cur.data:
                cur = cur.right

            else: #dupe
                return -1
            
            depth += 1

        return -1 #fail case
    
    def remove(self, data):
        self.head = self.removeRecursive(self.head, data)

    def removeRecursive(self, cur, data):
        if cur == None:
            return None

        if data < cur.data:
            cur.left = self.removeRecursive(cur.left, data)

        elif data > cur.data:
            cur.right = self.removeRecursive(cur.right, data)

        else:
            #node found

            #no child
            if cur.left == None and cur.right == None:
                return None

            #one child
            if cur.left == None:
                return cur.right

            if cur.right == None:
                return cur.left

            #two children
            largerNode = self.findLarger(cur)
            cur.data = largerNode.data
            cur.right = self.removeRecursive(cur.right, largerNode.data)

        #update height
        cur.height = 1 + max(self.calcHeight(cur.left), self.calcHeight(cur.right))

        #rebalance
        return self.rebalance(cur)
    
    def calcBalance(self, cur):
        if cur == None:
            return 0
        return self.calcHeight(cur.left) - self.calcHeight(cur.right)
            
    def calcHeight(self, cur):
        if cur == None:
            return 0
        return cur.height
    
    def rebalance(self, cur):

        balance = self.calcBalance(cur)

        #left heavy
        if balance > 1:

            #LL
            if self.calcBalance(cur.left) >= 0:
                return self.rightRotate(cur)

            #LR
            else:
                cur.left = self.leftRotate(cur.left)
                return self.rightRotate(cur)

        #right heavy
        if balance < -1:

            #RR
            if self.calcBalance(cur.right) <= 0:
                return self.leftRotate(cur)

            #RL
            else:
                cur.right = self.rightRotate(cur.right)
                return self.leftRotate(cur)

        return cur
    
    def findLarger(self, cur):
        curlarge = cur.right
        while curlarge.left != None:
            curlarge = curlarge.left
        return curlarge
    
    def rightRotate(self, rootNode):
        newRoot = rootNode.left
        temp = newRoot.right

        newRoot.right = rootNode
        rootNode.left = temp

        #update heights
        rootNode.height = 1 + max(self.calcHeight(rootNode.left), self.calcHeight(rootNode.right))

        newRoot.height = 1 + max(self.calcHeight(newRoot.left), self.calcHeight(newRoot.right))

        return newRoot

    def leftRotate(self, rootNode):
        newRoot = rootNode.right
        temp = newRoot.left

        newRoot.left = rootNode
        rootNode.right = temp

        #update heights
        rootNode.height = 1 + max(self.calcHeight(rootNode.left), self.calcHeight(rootNode.right))

        newRoot.height = 1 + max(self.calcHeight(newRoot.left), self.calcHeight(newRoot.right))
        
        return newRoot
    
visualizer = TreeVisualizer()

tree = AVLTree()

with open("nodes.txt", "r") as file:
    for line in file:
        if line != "":
            value = int(line)
            tree.add(value)

visualizer.add_to_stack(tree)

tree.remove(1)
tree.remove(44)
tree.remove(45)

visualizer.add_to_stack(tree)

visualizer.add_to_stack(tree)
visualizer.visualize()