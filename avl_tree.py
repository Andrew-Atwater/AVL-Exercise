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
            return cur
        
        if data < cur.data:
            cur.left = self.add(cur.left, data)
        
        elif data > cur.data:
            cur.right = self.add(cur.right, data)
            
        if cur.left == None:
            leftHeight = 0
        else:
            leftHeight = cur.left.height
        
        if cur.right == None:
            rightHeight = 0
        else:
            rightHeight = cur.right.height
            
        
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
        
        return cur
    
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
tree.add(10, tree.head)
tree.add(20, tree.head)
tree.add(30, tree.head)
tree.add(40, tree.head)
tree.add(50, tree.head)
tree.add(1, tree.head)

visualizer.add_to_stack(tree)
visualizer.visualize()