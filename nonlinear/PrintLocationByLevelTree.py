class build_location_tree:
    def __init__(self, location , level):
        self.location = location
        self.level = level
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
        
    def print_tree(self, loc_level):
        spaces = ' ' * self.find_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.location)
        
        for child in self.children:
            if self.find_level() == loc_level:
                break
            child.print_tree(loc_level)
            
            
            
if __name__ == "__main__":
    world = build_location_tree("World", 0)
    
    asia = build_location_tree("Asia", 1)
    india = build_location_tree("India", 2)
    india.add_child(build_location_tree("Delhi", 3))
    india.add_child(build_location_tree("Mumbai", 3))
    
    china = build_location_tree("China", 2)
    china.add_child(build_location_tree("Beijing", 3))
    china.add_child(build_location_tree("Shanghai", 3))
    
    asia.add_child(india)
    asia.add_child(china)
    
    europe = build_location_tree("Europe", 1)
    germany = build_location_tree("Germany", 2)
    germany.add_child(build_location_tree("Berlin", 3))
    germany.add_child(build_location_tree("Munich", 3))
    
    uk = build_location_tree("UK", 2)
    uk.add_child(build_location_tree("London", 3))
    uk.add_child(build_location_tree("Manchester", 3))
    
    europe.add_child(germany)
    europe.add_child(uk)
    
    world.add_child(asia)
    world.add_child(europe)
    
    print("Print all locations at level 0")
    world.print_tree(0)
    
    print("\nPrint all locations at level 1")
    world.print_tree(1)
    
    print("\nPrint all locations at level 2")
    world.print_tree(2)
    
    print("\nPrint all locations at level 3")
    world.print_tree(3)