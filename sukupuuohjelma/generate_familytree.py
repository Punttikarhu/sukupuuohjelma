from read_family import read_family
from tree_class import Tree, Node

def generate_familytree() -> Node:
    """Builds a tree structure for the family tree

    Returns:
        root (Node): root node of the tree
    """
    family = read_family()
    root = Node(family[0][1], gender="male", generation=0)
    nodes = {family[0][0]: root}
    nodes = Tree.find_subnodes(family, root, family[0][0], nodes)
    return root

if __name__ == "__main__":       
    from anytree import RenderTree, AsciiStyle, PreOrderIter
    root = generate_familytree()
    print(RenderTree(root, style=AsciiStyle()))
    print([node.generation for node in PreOrderIter(root)])