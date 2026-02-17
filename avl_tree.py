from binaryVisualizer import *

class AVLTree(BinaryTree):
    
    #overwrite add
    def add(self, data, cur):
        if self.head != None:
            self.head = Node(data)
            return
        
        if cur == None:
            #bottom of tree(end)
            return Node(data)
        
        #cur is a node if we get past the if statements
        if cur.data == data:
            print(f"Data {data} already exists, cannot be added")
            return
        
        if data < cur.data:
            cur.left = self.addRecursive(cur.left, data)
        
        elif data > cur.data:
            cur.right = self.addRecursive(cur.right, data)
            
    def addRecursive(cur, data):
        if data < cur.data:
            cur.left.addRecursive(cur.left, data)
        
        elif data > cur.data:
            cur.right.addRecursive(cur.right, data)
            
        balance = cur.calcBalance()
        
        if balance > 1:
            #left imbalance
            leftBalance = cur.left.calcBalance()
            if cur.left.calcBalance == -1:
                cur.left.leftRotate()
                cur = cur.rightRotate()
                
        elif balance < -1:
            #right imbalance
            rightBalance = cur.right.calcBalance()
            if cur.right.calcBalance == 1:
                cur.right.rightRotate()
                cur = cur.leftRotate()
    
    def calcBalance(cur):
        pass
            
    def calcHeight(cur):
        pass
    
    def findLarger(cur):
        pass
    
    def rightRotate(rootNode):
        newRoot = rootNode.left
        rootNode.left = newRoot.right
        newRoot.right = rootNode
        return newRoot
    
    def leftRotate(rootNode):
        newRoot = rootNode.right
        rootNode.right = newRoot.left
        newRoot.left = rootNode
        return newRoot
    
visualizer = TreeVisualizer()

tree = AVLTree()

visualizer.add_to_stack(tree)
visualizer.visualize()