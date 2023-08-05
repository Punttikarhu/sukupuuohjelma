from anytree import Node
   
class Tree:
    @staticmethod
    def find_subnodes(family: list, root_node: Node, root_node_id: int, nodes: dict):
        for row in family:
            node_id = row[0]
            name = row[1]
            gender = row[2]
            parent_node_id = row[3]
            if root_node_id == parent_node_id:
                node = Node(name, root_node, gender=gender, generation=root_node.depth+1)
                nodes[node_id] = node
                nodes = Tree.find_subnodes(family, node, node_id, nodes)
        return nodes    
