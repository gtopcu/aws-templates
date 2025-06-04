
class Node:
    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

node_1 = Node(1, None, None)
node_3 = Node(3, None, None)
node_2 = Node(2, node_1, node_3)
node_7 = Node(7, None, None)
node_4 = Node(4, node_2, node_7)

node_15 = Node(15, None, None)
node_16 = Node(16, node_15, None)
node_11 = Node(11, None, node_16)

node_8 = Node(8, node_4, node_11)

# def print_sorted_tree(node: Node):
#     left_child = node.left_child
#     bottom_child = None
#     while left_child is not None:
#         print("Node:", left_child.value)
#         if left_child.left_child is not None:
#             left_child = left_child.left_child
#         else:
#             bottom_child = left_child
#             break
#     print(bottom_child.value)

def get_child(node: Node):
    if node.left_child is not None:
        get_child(node.left_child)
    print(node.value)

    if node.right_child is not None:
        get_child(node.right_child)

# get_child(node_8)

# def check_exists(node: Node, value):
#     # print(node.value)
#     if node.value == value:
#         print("Found! ", value)
#         return True
#     elif value < node.value and node.left_child is not None:
#         return check_exists(node.left_child, value)
#     elif value > node.value and node.right_child is not None:
#         return check_exists(node.right_child, value)
    
#     print("Not found!", value)
#     return False


def insert_node(node: Node, value):
    # print(node.value)
    if node.value == value:
        return

    if value < node.value:
        if node.left_child is None:
            node.left_child = Node(value, None, None)
            print("Inserted left")
            return
        else:
            print("Left find", value)
            insert_node(node.left_child, value)
    else:
        if node.right_child is None:
            node.right_child = Node(value, None, None)
            print("Inserted right")
            return 
        else:
            print("Right find", value)
            insert_node(node.right_child, value)

insert_node(node_8, 6)
get_child(node_8)