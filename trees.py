# Creating a basic tree

class TreeNode:
    ''' data and children '''
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children

    def __str__(self, level=0) -> str:
        ret = ' ' * level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, tree_node):
        ''' Add a child node to the tree '''
        self.children.append(tree_node)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.add_child(cold)
tree.add_child(hot)
tea = TreeNode('Latte', [])
coffee = TreeNode('Mocha', [])
coke = TreeNode('Coke', [])
sprite = TreeNode('Sprite', [])
cold.add_child(coke)
cold.add_child(sprite)
hot.add_child(tea)
hot.add_child(coffee)
print(tree)
