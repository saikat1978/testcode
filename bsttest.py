from dataclasses import dataclass

@dataclass
class Node:
    parent: Node
    left: Node
    right: Node
    value: int = 0

node_value: int = 0
result_node = Node()

def findInorderedLeast(node: Node) -> Node:
    if node.value > node_value and (node.value <= result_node.value):
            result_node = node

    if not node.left and not node.right:
        return node

    if node.left:
        node = findInorderedLeast(node.left)
    
    if node.right:
        node = findInorderedLeast(node.right)

    return findInorderedLeast(node.parent)



    


