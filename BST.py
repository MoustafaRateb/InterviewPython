
class Node(object):
    def __init__(self, value, description=''):
        self.description = description
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value, description=''):
        # Create a new Node
        newNode = Node(value, description)
        # if root exists
        if self.root:
            # set currentNode = root
            currentNode = self.root
            # loop till insertion done
            while True:
                # if current node value > new node value
                if currentNode.value > newNode.value:
                    # if current node has empty left slot insert new node in it
                    # else update current node to be its left node
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                        break
                else:
                    # if current node value < new node value
                    # if current node has empty right slot insert new node in it
                    # else update current node to be its right node
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode
                        break
        else:
            self.root = newNode
        # if root doesn't exist set root = current node

    def lookup(self, search_value):
        """Return Node if the value
        is in the tree, return
        None otherwise."""
        # set current = root
        currentNode = self.root
        # loop until find value or reach tree leaf
        while currentNode:
            # if current = none value not exist in tree
            if search_value == currentNode.value:
                return currentNode
            # if current value = search value return current node
            if search_value < currentNode.value:
                currentNode = currentNode.left
            # if search value < current value set current = current.left
            elif search_value > currentNode.value:
                currentNode = currentNode.right
            # if search value > current value set current = current.right
        return None

    def print_tree(self, node=None):
        """Print(out all tree nodes)"""
        indent = ''
        if not node:
            node = self.root
        printer = [(indent, node)]
        # push root into stack with indentation
        # loop till stack is empty
        while printer:

            # pop first item from stack and print its value with indentation
            current = printer.pop()
            print(current[0] + str(current[1].value))
            indent = current[0] + "\t"
            # push child nodes into stack if existed with increasing indentation
            if current[1].left:
                printer.append((indent, current[1].left))
            if current[1].right:
                printer.append((indent, current[1].right))

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print(solution."""
        if start:
            traversal.append(str(start.value))
            self.preorder_print(start.left, traversal)
            self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)


# Test print_tree
# Should be 1-2-4-5-3
tree.print_tree()


tree.print_tree(tree.lookup(170))
