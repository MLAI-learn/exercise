class TreeNode:
    def __init__(self, name,designation):
        self.name = name
        self.designation=designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_(self, property_name):
        if property_name == 'both':
            value = self.name + " (" + self.designation + ")"
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_(property_name)




    def add_child(self, child):
        child.parent = self
        self.children.append(child)



def build():
    root=TreeNode('Nilupul','CEO')
    gels=TreeNode('Gels','HR head')

    cinmay=TreeNode('Cinmay','CTO')
    
    
    
    vishva=TreeNode('Vishwa','Infrastructural head')
    cinmay.add_child(vishva)
    vishva.add_child(TreeNode('Dhaval','Cloud manager'))
    vishva.add_child(TreeNode('Abhijit','App manager'))
    
    cinmay.add_child(TreeNode('Aamir','Application head'))


    
    gels.add_child(TreeNode('Peter','Recruitment manager'))
    gels.add_child(TreeNode('Waqas','Policy head'))
    

    root.add_child(cinmay)
    root.add_child(gels)

    return root

    
        


if __name__=='__main__':
    p=build()
    p.print_('both')
    p.print_('name')
    p.print_('designation')
    

