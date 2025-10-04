class build_management_tree:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.parent = None
        self.children = []
    
    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)
    
    def find_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        
    def print_tree(self, property_name):
        spaces = ' ' * self.find_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if property_name == "name":
            print(prefix + self.name)
        elif property_name == "designation":
            print(prefix + self.designation)
        else:
            print(prefix + f"{self.name} ({self.designation})")
        
        for child in self.children:
            child.print_tree(property_name)
            
            
if __name__ == "__main__":
    ceo = build_management_tree("Nilupul", "CEO")
    
    cto = build_management_tree("Chinmay", "CTO")
    infra_head = build_management_tree("Vishwa", "Infrastructure Head")
    infra_head.add_child(build_management_tree("Dhaval", "Cloud Manager"))
    infra_head.add_child(build_management_tree("Abhijit", "App Manager"))
    
    cto.add_child(infra_head)
    cto.add_child(build_management_tree("Aamir", "Application Head"))
    
    hr_head = build_management_tree("Gels", "HR Head")
    hr_head.add_child(build_management_tree("Peter", "Recruitment Manager"))
    hr_head.add_child(build_management_tree("Waqas", "Policy Manager"))
    
    ceo.add_child(cto)
    ceo.add_child(hr_head)
    
    print("Print only names:")
    ceo.print_tree("name")
    
    print("\nPrint only designation:")
    ceo.print_tree("designation")
    
    print("\nPrint both name and designation:")
    ceo.print_tree("both")