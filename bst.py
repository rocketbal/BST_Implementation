# An implementation of the Binary Search Tree(BST) Data Structure
# ----------------------------TreeNode class with helper functions ------------------------------- #
class TreeNode:
    def __init__(self,val,parent,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
# ----------------------------Check to see if root has left child------------------------------- #
    def hasLeftChild(self):
        return True if self.left else False
# ----------------------------Check to see if root has right child------------------------------- #
    def hasRightChild(self):
        return True if self.right else False

# ----------------------------BST class with insert, delete and traverse methods ------------------------------- #
class BST:
    def __init__(self,root=None):
        self.root=root

# ----------------------------insert method------------------------------- #
    def insert(self,val):
        if self.root is None:
            self.root = TreeNode(val,None)
        else:
            self._insert(val,self.root)
# ----------------------------insert helper method------------------------------- #
    def _insert(self,val,currentNode:TreeNode):
        if val < currentNode.val:
            if currentNode.hasLeftChild():
                self._insert(val,currentNode.left)
            else:
                currentNode.left = TreeNode(val,currentNode)
        else:
            if currentNode.hasRightChild():
                self._insert(val,currentNode.right)
            else:
                currentNode.right = TreeNode(val,currentNode)
# ----------------------------Inorder traverse method------------------------------- #
    def traverse(self):
        if self.root:
            self.traverse_inorder(self.root)
# ----------------------------Traverse helper method------------------------------- #
    def traverse_inorder(self,root):
        if root.left:
            self.traverse_inorder(root.left)
        print(root.val)

        if root.right:
            self.traverse_inorder(root.right)

# ----------------------------Find the max val------------------------------- #
    def max(self):
        if self.root:
            self.get_max(self.root)


    def get_max(self,root):
        if root.right:
            self.get_max(root.right)
        else:
            return (root.val)

# ----------------------------Find the min val------------------------------- #
    def min(self):
        if self.root:
            self.get_min(self.root)


    def get_min(self,root):
        if root.left:
            self.get_min(root.left)
        else:
            return root.val

    def get_predecessor(self,node):
        if node.right:
            node = node.right
        else:
            return node

# ----------------------------Remove method------------------------------- #
    def remove(self,data):
        if self.root:
            self.remove_node(data,self.root)

# ----------------------------Remove helper method------------------------------- #
    def remove_node(self,data,node):
        if node is None:
            return

# ----------------------Search for data in left/right subtrees------------------------------- #
        if node.val > data:
            self.remove_node(data,node.left)
        elif node.val < data:
            self.remove_node(data,node.right)

        else:
# ---------------------if the data to be deleted in a leaf node------------------------------- #
            if node.left is None and node.right is None:
                print("Deleting this leaf node: %d", node.val)

                parent = node.parent

                if parent is not None and node == parent.left:
                    parent.left = None

                if parent is not None and node == parent.right:
                    parent.right = None

                if parent is None:
                    self.root = None

                del node
# ---------------------if the data to be deleted has only right child------------------------------- #
            elif node.left is None and node.right is not None:
                print("Deleting the right child: %d", node.val)

                parent = node.parent
                if parent:
                    if parent.left == node:
                        parent.left = node.right

                    if parent.right == node:
                        parent.right = node.right

                else:
                    self.root = node.right

                node.right.parent = parent
                del node
# ---------------------if the data to be deleted has only left child------------------------------- #
            elif node.right is None and node.left is not None:
                print("Deleting the left child: %d", node.val)

                parent = node.parent
                if parent:
                    if parent.left == node:
                        parent.left = node.left

                    if parent.right == node:
                        parent.right = node.left

                else:
                    self.root = node.left

                node.left.parent = parent
                del node



            else:
# ---------------------if the data to be deleted has two children------------------------------- #
                print("Deleting node with two children: %d", node.val)
                # -------------Grab the predecessor/successor to swap with root node------------------ #
                predecessor = self.get_predecessor(node.left)
                temp = predecessor.val
                predecessor.val = node.val
                node.val = temp
                # ----------In this case, root node is now a leaf node------------------ #
                # ----------recursively delete the leaf node------------------ #
                self.remove_node(data,predecessor)





root = BST()
root.insert(10)
root.insert(5)
root.insert(15)
root.insert(4)
root.insert(20)
root.insert(1000)
root.remove(10)
root.traverse()
