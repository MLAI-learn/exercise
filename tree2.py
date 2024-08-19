class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,i):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.get_level()<=i-1:
            for child in self.children:
                child.print_tree(i)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def locations_tree():
    root=TreeNode('Global')

    india=TreeNode('India')
    usa=TreeNode('USA')
    root.add_child(india)
    root.add_child(usa)

    gujurat=TreeNode('Gujurat')
    gujurat.add_child(TreeNode('Ahmedabad'))
    gujurat.add_child(TreeNode('Baroda'))

    karnataka=TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bengluru'))
    karnataka.add_child(TreeNode('Mysuru'))

    india.add_child(gujurat)
    india.add_child(karnataka)

    newjersy=TreeNode('New Jersey')
    newjersy.add_child(TreeNode('Princeton'))
    newjersy.add_child(TreeNode('Trenton'))

    cali=TreeNode('California')
    cali.add_child(TreeNode('San Francisco'))
    cali.add_child(TreeNode('Mountain View'))
    cali.add_child(TreeNode('Palo Alto'))

    usa.add_child(newjersy)
    usa.add_child(cali)

    return root



if __name__=='__main__':
    p=locations_tree()
    p.print_tree(3)
    p.print_tree(2)
    p.print_tree(1)