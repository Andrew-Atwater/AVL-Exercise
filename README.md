University of Maine COS 226: Jump to the Left, Step to the Right
COS 226
Jump to the Left, Step to the Right
20pts
Due: Feb 18th, 2026, 11:59pm

1 Assignment Description
For this homework, you will implement an AVL (Adelson-Velsky and Landis) tree using
Python and the visualizer framework. An AVL tree is a self-balancing binary search tree
where the heights of the two child subtrees of any node differ by at most one. When this
balance is violated, rotations are performed to restore the AVL property.
Your implementation should include all the standard BST operations (insert, search,
delete) with automatic rebalancing through rotations.

2 Required AVL Tree Methods

2.1 add
Parameters
• data: an integer that is suppose to be added to the tree in the correct spot
Return: Nothing
The add method is the starting point of the add and will kick off the recursive function
starting at the root of the tree. If duplicate data is found, do not add.

2.2 add recursive
Parameters:
• curNode: the node the add method is currently looking at.
• data: an integer that is suppose to be added to the tree in the correct spot.
Return: root of subtree after balancing.
The recursive portion of the add method. Will only be called by itself and initially called
by the ”add” method. If the curNode is ”None”, needs to return a new Node containing the
data. Will need to update height and potentially re-balance after adding.

2.3 search
Parameters
• data: an integer that the method will search for.
Return: int value representing either depth if positive or -1 if value doesn’t exist.
Search for a value in the AVL tree. return depth of node if found, or -1 if not found.
Should use the loop method to find the value to save on memory.

2.4 remove
Parameters
• data: an integer that the method will search for.
Returns: Nothing Will attempt to remove a value by kicking off the recursive function at
the root of the tree.

2.5 remove recursive
• curNode: the node the add method is currently looking at.
• data: an integer that is suppose to be added to the tree in the correct spot.
Returns: root node of the subtree after potentially balancing.
The recursive portion of the remove method. Will first need to find the node that is
searched for. If curNode is None, that means the recursive function could not find the data
to be removed (and just needs to return None as the root of the subtree).
If the data is found, check which circumstance it’s in.
• Two child: find and copy the data of the next larger node, then continue recursively
removing now looking for that new value.
• One child: return the child as the root of the subtree to take the removed node’s place.
• No child: return None as the root of the new subtree.
After the recursive remove call, update height and check if rotations are needed.

2.6 get height
Return the height of the tree (or a specific node). The height of a leaf node is 0.

2.7 get balance factor
Calculate and return the balance factor of a node (height of left subtree - height of right
subtree).

2.8 find larger
Parameters:
• curNode: the node you’re starting the search from.
Returns: the next node larger than curNode.
find larger should find the next sequential node by going right once, then left as far as it
can.

3 Rotation Methods

3.1 rotate left
Parameters:
• curNode: the root node that you’re rotating on.
Returns: The new root of the subtree.
Perform a left rotation around a given node to restore AVL balance. A left rotation is
counter-clockwise.

3.2 rotate right
Parameters:
• curNode: the root node that you’re rotating on.
Returns: The new root of the subtree.
Perform a right rotation around a given node to restore AVL balance. A right rotation
is clockwise.

4 Steps to Complete the Assignment

4.1 Visualizer Instructions
This assignment will be using the visualizer framework. See the visualizer example.py file
for an example of how to use it.

4.2 Steps
• Insert the values (in order) into the tree based on the nodes.txt file
• Create a snapshot of the tree after all values have been inserted (Should look like the
image AVLafter30insert.png)
• Delete the nodes (in order) 1, 44, 45.
• Create a snapshot of the tree after all deletions (should look like the image AVLafter45delete.png)
• Show the visualizer at the end of the program
